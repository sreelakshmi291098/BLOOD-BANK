from django.contrib import admin

# Register your models here.
from app22.models import Donor,Reg_user,Request,feedback

admin.site.register(Donor)
admin.site.register(Reg_user)
admin.site.register(Request)
admin.site.register(feedback)