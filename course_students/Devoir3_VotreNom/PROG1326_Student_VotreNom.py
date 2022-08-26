
def validate_student_name(student_name):
	student_name = student_name.replace(" ","")
	return len(student_name) > 0 and student_name.isalpha()

def validate_student_grade(student_grade):
	try:
		student_grade = float(student_grade)
		if 100 < student_grade or student_grade < 0:
			return False
		else:
			return True
	except:
		print("Average invalid.", end="")
		return False
	return True

class Student(object):
	def __init__(self, name, grade):
		self.name = name
		self.grade = grade

	def __str__(self):
		return "<Student:%s>" %self.name
