from django.db import models

# Create your models here.
class Student(models.Model):
	full_name=models.CharField(max_length=100)
	email=models.CharField(max_length=100,unique=True)
	password=models.CharField(max_length=100,blank=True,null=True)
	username=models.CharField(max_length=200)
	interested_module=models.TextField()
	
	def __str__(self):
		return self.full_name

	# Total Enrolled modules
	def enrolled_modules(self):
		enrolled_modules=StudentModuleEnrollment.objects.filter(student=self).count()
		return enrolled_modules

class Academic(models.Model):
	full_name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100,blank=True,null=True)
	qualification=models.CharField(max_length=200)
	mobile_no=models.CharField(max_length=20)
	skills=models.TextField()
	
	class Meta:
		verbose_name_plural="1. Academics"
		
	def skill_list(self):
		skill_list=self.skills.split(',')
		return skill_list


	# Total Teacher modules
	def total_academic_modules(self):
		total_modules=Module.objects.filter(academic=self).count()
		return total_modules

	# Total Teacher Students
	def total_academic_students(self):
		total_students=StudentModuleEnrollment.objects.filter(module__academic=self).count()
		return total_students

	def __str__(self):
		return self.full_name
	
class Module(models.Model):
	# category=models.ForeignKey(CourseCategory, on_delete=models.CASCADE,related_name='category_courses')
	academic=models.ForeignKey(Academic, on_delete=models.CASCADE,related_name='academic_modules')
	title=models.CharField(max_length=150)
	description=models.TextField()
	module_views=models.BigIntegerField(default=0)

	class Meta:
		verbose_name_plural="3. Modules"

	def tech_list(self):
		tech_list=self.techs.split(',')
		return tech_list

	def total_enrolled_students(self):
		total_enrolled_students=StudentModuleEnrollment.objects.filter(module=self).count()
		return total_enrolled_students


	def __str__(self):
		return self.title

	
class StudentModuleEnrollment(models.Model):
	module=models.ForeignKey(Module,on_delete=models.CASCADE,related_name='enrolled_modules')
	student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='enrolled_student')
	moderator = models.ForeignKey(Academic,on_delete=models.CASCADE,related_name='moderator_academic', blank=True)
	enrolled_time=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural="5. Enrolled modules"

	def __str__(self):
		return f"{self.module}-{self.student}-{self.moderator}"

class StudentModuleAcademic(models.Model):
	student_module=models.ForeignKey(StudentModuleEnrollment,on_delete=models.CASCADE,related_name='studentenrolled_modules')
	academic= models.ForeignKey(Academic,on_delete=models.CASCADE,related_name='studentenrolled_academics')
	mark = models.IntegerField(default=0)
	mark_time=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural="6. Student enrolledModule"

	def __str__(self):
		return f"{self.student_module}-{self.academic}"
