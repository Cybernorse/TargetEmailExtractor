import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import time 

class emailer_code:
  def __init__(self):
    self.emails=[]
    with open("market_email.csv",'r',encoding='utf-8') as ema:
      ema.readline()
      for i in ema:
        self.emails.append(i)
    self.count=0
    self.end=694

  def emailer(self):
    try:
      me = "waqarsdma@gmail.com"
      # you = ["bigpenguincave@gmail.com","waqarsher66@gmail.com"]
      if self.count<=self.end:
        for reciever in self.emails[self.count:self.end]:
          print(reciever)
          msg = MIMEMultipart('alternative')
          msg['Subject'] = "Link"
          msg['From'] = me
          msg['To'] = reciever

          text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
          html = """\
          <html>
            <head></head>
            <body>
              <p>Please like this page regardless of whether you want to see our content or not, thank you..<br>
                https://www.facebook.com/Market-Hive-107660687800620
              </p>
            </body>
          </html>
          """

          part1 = MIMEText(text, 'plain')
          part2 = MIMEText(html, 'html')

          msg.attach(part1)
          msg.attach(part2)

          mail = smtplib.SMTP('smtp.gmail.com', 587)

          mail.ehlo()

          mail.starttls()

          mail.login('waqarsdma@gmail.com', 'eminuses-es')
          mail.sendmail(me, reciever, msg.as_string())
          mail.quit()

          time.sleep(5)
          self.count+=1
      else:
        print("Email sending complete")
    except:
      self.count+=1
      self.emailer()


if __name__=='__main__':
  obj=emailer_code()
  obj.emailer()
