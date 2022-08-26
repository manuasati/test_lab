
class User(object):
	""" Defined user object.
		create user object passing params - name and password  
		Args:
			name (str, mandatory): user name, to be provide during the user creation
			password (str, mandatory): user name, to be provide during the user creation
			#TODO: username / password validation like min/max character length to be applied
	"""
	def __init__(self, name, password):
		self.name = name
		self.password = password

	def check_password(self, password):
		return self.password == password

	def __str__(self):
		return "<User obj:%s>" %self.name
