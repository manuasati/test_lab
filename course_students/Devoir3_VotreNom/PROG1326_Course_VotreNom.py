import PROG1326_Student_VotreNom

def validate_cuorse_name(course_name):
	return len(course_name) > 5

class Course(object):
	def __init__(self, name):
		self.name = name
		self.students_list = []

	def add_students(self, student):
		self.students_list.append(student)

	def return_course_average(self):
		return sum([float(student.grade) for student in self.students_list])/len(self.students_list)		

	def return_student_average(self, student_name):
		for student in self.students_list:
			if student.name == student_name.strip():
				return student
		return None

	def return_all_students(self):
		return self.students_list

	def __str__(self):
		return "<Course:%s - %s>" %(self.name, len(self.students_list))

print ("Devoir 3 par Anthony Ilunga")
print ("Utilisation de classe et module. Script pour calculer la moyenne d'un cours.\n")

while (True):
	course_name = input ("Quel est le nom du cours? ")
	if validate_cuorse_name(course_name):
		course = Course(name=course_name)
		break
	print ("Nom invalide. ", end="")

while(True):
	order = "\n-------------------------------------\n"
	order += "1 - Inscrire des étudiants au cours\n"
	order += "2 - Afficher la moyenne du cours\n"
	order += "3 - Afficher la moyenne d'un étudiant(e)\n"
	order += "4 - Afficher tous les étudiant(e)s\n"
	order += "5 - Recommencez pour un nouveau cours\n"
	order += "6 - Sortir\n"
	order += "Veuillez choisir une commande: "
	order = input (order)

	if order == "1":
		while (True):
			while (True):
				student_name = input ("Quel est le nom de l'étudiant(e)? ")
				if PROG1326_Student_VotreNom.validate_student_name(student_name):
					break
				print ("Nom invalide. ", end="")

			while (True):
				student_grade = input ("Quelle est sa moyenne? ")
				if PROG1326_Student_VotreNom.validate_student_grade(student_grade):
					break
			student = PROG1326_Student_VotreNom.Student(student_name, student_grade)
			course.add_students(student)
			add_more_student = input ("Voulez-vous entrer un autre étudiant(e)? (o ou n) ")
			if add_more_student != 'o':
				break

	elif order == "2":
		if course.return_all_students():
			print("La moyenne du cours %s est de : %s" %(course.name, course.return_course_average()))
		else:
			print ("Il n’y a pas d’étudiant(e) dans le cours!")

	elif order == "3":
		if course.return_all_students():
			student_name = input ("Entez le nom de l'étudiant(e): ")
			student = course.return_student_average(student_name)
			if student:
				print ("La moyenne de cet étudiant(e) est de : %s" %student.grade)
			else:
				print ("L'étudiant(e) n'est pas inscrit à ce cours.") 
		else:
			print ("Il n’y a pas d’étudiant(e) dans le cours!")

	elif order == "4":
		students = course.return_all_students()
		if students:
			print ("Voici la liste d'étudiant(e)s du cours %s " %course.name)
			for student in students:
				print ("%s %.1f" %(student.name, student.grade))
		else:
			print ("Il n’y a pas d’étudiant(e) dans le cours!")
	elif order == "5":
		while (True):
			course_name = input ("Quel est le nom du cours? ")
			if validate_cuorse_name(course_name):
				course = Course(name=course_name)
				break
			print ("Nom invalide.", end="")

	elif order == "6":
			break	
	else:
		print("Commande Invalide.")

input("Press Enter key to exit.")