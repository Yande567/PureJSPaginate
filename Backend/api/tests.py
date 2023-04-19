from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeListTests(APITestCase):

    def test_list_employees(self):
        # Create some test employees
        employee1 = Employee.objects.create(first_name='John', last_name='Smith', position='Software Engineer',
                                            dob='1990-01-01', age=30, start_date='2019-01-01', office='New York')
        employee2 = Employee.objects.create(first_name='Jane', last_name='Doe', position='Marketing Manager',
                                            dob='1995-01-01', age=25, start_date='2019-01-01', office='London')

        # Retrieve the employee list using the API
        url = reverse('employee-list')
        response = self.client.get(url)

        # Verify the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = EmployeeSerializer([employee1, employee2], many=True).data
        self.assertEqual(response.data, expected_data)
