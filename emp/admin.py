from django.contrib import admin
from .models import Emp, Testimonial, Feedback

# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('name', 'phone','working', 'emp_id','email')
    list_editable=('phone', 'working')
    search_fields=('name', 'phone')
    list_filter=('name','working')

admin.site.register(Emp, EmpAdmin)
admin.site.register(Testimonial)
admin.site.register(Feedback)