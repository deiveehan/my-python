import yagmail

sender="sammit54321@gmail.com"
receiver= "deiveehan@gmail.com"
subject = "Test meail from python app"
content = """
Testing email from python app by the user
testing 
hi..
"""

yag = yagmail.SMTP(user=sender, password="yourgmailapppassword")
yag.send(to=receiver, subject=subject, contents=content)

print("Email sent !")