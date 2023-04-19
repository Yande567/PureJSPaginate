from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

# Import Views
from .views import employeeList

urlpatterns = [
    path("employees/", employeeList, name="employee-list"),
]

urlpatterns += staticfiles_urlpatterns()