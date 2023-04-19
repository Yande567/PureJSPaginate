from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

# Import Views
from .views import EmployeeList

urlpatterns = [
    path("employees/", EmployeeList.as_view(), name="employee-list"),
]

urlpatterns += staticfiles_urlpatterns()
