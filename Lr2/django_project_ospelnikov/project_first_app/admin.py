from django.contrib import admin

from project_first_app.models import Owner, DrivingLicence, Own, Car, User

# Register your models here.
admin.site.register(Owner)
admin.site.register(DrivingLicence)
admin.site.register(Own)
admin.site.register(Car)
admin.site.register(User)