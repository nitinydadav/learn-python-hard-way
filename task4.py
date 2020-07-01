import smtplib

sender_email = "yadnitin89@gmail.com"
rec_email = "nitin.yad005@gmail.com"
password = input(str("enter your password "))
message = "hello you are has been hacked "

server = smtplib.SMTP_SSL("smtp.gmail.com",587)
server.starttls()
server.login(sender_email, password)
print("login success")
server.sendmail(sender_email, rec_email,message)
print("email has been sent ", rec_email)