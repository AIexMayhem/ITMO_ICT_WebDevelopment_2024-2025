from django.contrib import admin

from student_desc.models import ReadyTask, User, Homework, Mark, Subject

admin.site.register(User)
admin.site.register(Homework)
admin.site.register(ReadyTask)
admin.site.register(Mark)
admin.site.register(Subject)
