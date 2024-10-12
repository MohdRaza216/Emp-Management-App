from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.emp_record, name="emp_record"),
    path('add-emp/', views.add_emp, name="add_emp"),
    path('delete-emp/<str:emp_id>', views.delete_emp, name="delete_emp"),
    path('update-emp/<str:emp_id>', views.update_emp, name="update_emp"),
    path('do-update-emp/<str:emp_id>', views.do_update_emp, name="do_update_emp"),
    path('testimonials/', views.testimonial, name="testimonials"),
    path('feedback/', views.feedback, name="feedback"),
] 
