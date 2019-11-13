
import os
import smtplib
import imghdr
from email.message import EmailMessage

# https://myaccount.google.com/lesssecureapps
# https://accounts.google.com/DisplayUnlockCaptcha

class SendEmail(object):

	def __init__(self, subject, body,
				 from_address, password,
				 to_address, attachments=None):

		self.from_address = from_address
		self.password = password
		if not isinstance(to_address, str):
			to_address = ", ".join(to_address)
		self.msg = EmailMessage()
		self.msg['Subject'] = subject
		self.msg['From'] = from_address
		self.msg['To'] = to_address
		self.msg.set_content(body)
		self.add_attachments(attachments)

	def attach_image(self, image_file):
		with open(image_file, 'rb') as f:
			file_data = f.read()
			file_type = imghdr.what(f.name)
			file_name = f.name
		self.msg.add_attachment(
			file_data, maintype='image', subtype=file_type, filename=file_name)

	def add_attachments(self, attachments):
		if not attachments:
			return
		for attachment in attachments:
			if os.path.basename(attachment).rsplit('.', 1)[1] in \
					['jpg', 'jpeg', 'png']:
				self.attach_image(attachment)

	def send_email(self):
		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
			smtp.login(self.from_address, self.password)
			smtp.send_message(self.msg)


# if __name__ == "__main__":
# 	se = SendEmail()
# 	se.send_email()


# Debug - with localhost
# python3 -m smtpd -c DebuggingServer -n localhost:1025
# with smtplib.SMTP('localhost', 1025) as smtp:
# 	subject = "Grab dinner this weekend?"
# 	body = "How about dinner 6pm this Saturday?"

# 	msg = f"Subject: {subject}\n\n{body}"
# 	smtp.sendmail(EMAIL_ADDRESS, 'abhishek.korra19@gmail.com', msg)
