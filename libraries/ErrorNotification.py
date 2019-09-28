import smtplib

class ErrorNotification:

	smtp = 'smtp.gmail.com'
	port = 587
	sender = 'suportetecnico.globo@gmail.com'
	password = 'K63,}<7tSt7CAwYk'
	recipient = 'caio_warwar@yahoo.com.br'

	def __init__(self):
		self.server = smtplib.SMTP(self.smtp, self.port)
		self.server.ehlo()
		self.server.starttls()
		self.server.login(self.sender, self.password)

	def send_notification(self, route):
		msg = 'Um erro ocorreu!\n'
		msg += str(route)
		self.server.sendmail(self.sender, self.recipient, msg)
		self.server.quit()
