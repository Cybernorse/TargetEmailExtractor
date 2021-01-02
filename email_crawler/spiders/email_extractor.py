import scrapy
from scrapy.spiders import CrawlSpider,Request
from googlesearch import search
import re
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# search the specific keywords from google search engine python module 
# and keep on getting the links and keep on extracting the emails from each website url


class email_extractor(CrawlSpider):
    name='email_ex'
    # allowed_domain=['']

    def __init__(self,keyloc=None,*args, **kwargs):
        super(email_extractor, self).__init__(*args, **kwargs)
        self.email_list=[]
        self.args=keyloc.split('|')
        print(self.args)
        self.query=f" '{self.args[0]} {self.args[1]}'.gmail.com "

    def start_requests(self):
        for results in search(self.query, num=10, stop=None, pause=2): 
            yield SeleniumRequest(
                url=results,
                callback=self.parse,
                wait_until= EC.presence_of_element_located((By.TAG_NAME,"html")),
                dont_filter=True
                )
    
    def parse(self,response):
        EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        emails=re.finditer(EMAIL_REGEX, str(response.text))
        for email in emails:
            self.email_list.append(email.group())
            
        for email in set(self.email_list):
            yield{
                "emails":email
            }

        self.email_list.clear()
