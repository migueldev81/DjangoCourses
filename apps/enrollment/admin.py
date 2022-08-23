from django.contrib import admin

# Register your models here.
from apps.enrollment.models import Enrollment

admin.site.register(Enrollment)