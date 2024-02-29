from django.contrib import admin
from modapp.models import Student, Module, Academic, StudentModuleAcademic, StudentModuleEnrollment


# Register your models here.

admin.site.register(Student)
admin.site.register(StudentModuleAcademic)
admin.site.register(StudentModuleEnrollment)
admin.site.register(Module)
admin.site.register(Academic)

