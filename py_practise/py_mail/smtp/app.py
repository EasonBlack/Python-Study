import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'eason@163.com'
receivers = 'eason@163.com'

mail_host="smtp.163.com"  #设置服务器
mail_user="eason@163.com"   #用户名
mail_pass="xxxxxx" 

message = MIMEText('Python SMTP Test', 'plain', 'utf-8')
message['From'] = Header("From Test",'utf-8')
message['To'] =  Header("To Test", 'utf-8')

subject = 'Python SMTP Test'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 587)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers,  message.as_string())
    print("success")
except smtplib.SMTPException as err:
    print("error: {0}".format(err))
