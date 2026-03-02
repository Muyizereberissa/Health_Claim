from django.contrib import admin
from .models import Member, Provider, Procedure, Diagnosis, Claim

# Register your models here.

admin.site.register(Member)
admin.site.register(Provider)
admin.site.register(Procedure)
admin.site.register(Diagnosis)
admin.site.register(Claim)