from django.contrib import admin
from .models import Address, User, Contact, Department, Doctor, Patient, Hospital, DaySchedule, Appointment

admin.site.register(Address)
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Hospital)
admin.site.register(DaySchedule)
admin.site.register(Appointment)
