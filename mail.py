import subprocess
import smtplib
from email.mime.text import MIMEText
threshold = 80
partition = "/"
def report_via_email():
 msg = MIMEText("Magento EC2 instance thershold reached 80% Please check now")
 msg["Subject"] = "IMP:Low disk space warning"
 msg["From"] = "automail@gmail.com"
 msg["To"] = "org@gmail.com"
 #with smtplib.SMTP("smtp.gmail.com", 587) as server:
 server=smtplib.SMTP("smtp.gmail.com", 587)
 server.ehlo()
 server.starttls()
 server.login("automail@gmail.com","hmazzssgbnnysfeb")
 server.sendmail("automail@gmail.com","org@gmail.com",msg.as_string())
def check_once():
 df = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE)
 for line in df.stdout:
  splitline = line.decode().split()
  if splitline[5] == partition:
   if int(splitline[4][:-1]) > threshold:
    report_via_email()
check_once()

