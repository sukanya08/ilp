from rest_framework.test import APITestCase, APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework import status
import json
import base64
from django.urls import reverse
from django.contrib.auth import get_user_model
from tests import IlpTestCase
# Create your tests here.
from .views import Admin1sBoundary
from boundary.models import Boundary, BoundaryType
from common.models import Status, InstitutionType

class BoundaryApiTests(IlpTestCase):

    '''setupTestData is invoked in the parent class which sets up fixtures just once for all the tests.
    So this test case should essentially be just reads/fetches. If we require a pristine DB each time for
    writes, please write another class '''
    def setUp(self):
        #setup a test user
        self.user = get_user_model().objects.create_user('admin', 'admin@klp.org.in', 'admin')
        self.view = Admin1sBoundary.as_view()
        self.factory = APIRequestFactory()
        # country, created = BoundaryType.objects.get_or_create(char_id="C", name="Country")
        # state, created = BoundaryType.objects.get_or_create(char_id="ST", name="State")
        # school_district, created = BoundaryType.objects.get_or_create(char_id="SD", name="School District")
        # preschool_district, created = BoundaryType.objects.get_or_create(char_id="PD", name="Preschool District")


        # active_status, created = Status.objects.get_or_create(char_id="AC", name="Active")

        # preschool_type, created = InstitutionType.objects.get_or_create(char_id="pre",name="Preschool")
        # primary_type, created = InstitutionType.objects.get_or_create(char_id="primary", name="Primary School")

        # boundary_india, created = Boundary.objects.get_or_create(id=1,name="India", boundary_type=country, dise_slug="India",status=active_status)
        # boundary_karnataka, created = Boundary.objects.get_or_create(id=2,parent=boundary_india,name="Karnataka", boundary_type=state, dise_slug="Karnataka",status=active_status)
        # Boundary.objects.get_or_create(id=3, parent=boundary_karnataka, name="Test District",boundary_type=school_district, type=preschool_type, dise_slug="Test District", status=active_status)
    

    def test_list_noauth(self):
        url = '/api/v1/ka/boundary/admin1s'
        print("=======================================================")
        print("Test unauthorized access of URL - ",url)
        request = self.factory.get(url)
        response = self.view(request)
        self.assertEqual(response.status_code,403)
        response.render()
        data = json.loads(response.content)
        print("Response is: ", data)
        print("End test ===============================================")
       
    def test_list_admin1s_boundaries(self):
        url = '/api/v1/ka/boundary/admin1s'
        print("=======================================================")
        print("Test listing all admin1s boundaries - ", url)
        request = self.factory.get(url)
        force_authenticate(request,user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response.render()
        data = json.loads(response.content)
        self.assertIsNotNone(data)
        self.assertNotEqual(data['count'],0)
        self.assertEqual(data['count'],38)
        print("Response is : ", data)
        print("End test ===============================================")

    def test_admin1s_preschool_districts(self):
        url = '/api/v1/ka/boundary/admin1s?school_type=pre'
        print("=======================================================")
        print("Testing listing admin1s boundaries filter by school type ", url)
        request=self.factory.get(url)
        force_authenticate(request,user=self.user)
        response = self.view(request, type='pre')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response.render()
        data = json.loads(response.content)
        self.assertEqual(data['count'],4)
        print("Response is : ", data)
        print("End test ===============================================")
    
    def test_admin1s_primaryschool_districts(self):
        url = '/api/v1/ka/boundary/admin1s?school_type=primary'
        print("=======================================================")
        print("Testing listing primary school admin1s boundaries ", url)
        request=self.factory.get(url)
        force_authenticate(request,user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response.render()
        data = json.loads(response.content)
        print("Response is : ", data)
        print("End test ===============================================")
    
    def test_admin2s_boundaries(self):
        url = '/api/v1/ka/boundary/admin2s'
        print("=======================================================")
        print("Testing list all admin2s boundaries ", url)
        request=self.factory.get(url)
        force_authenticate(request,user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response.render()
        data = json.loads(response.content)
        print("Response is : ", data)
        print("End test ===============================================")

    def test_admin2s_preschool_districts(self):
        url = '/api/v1/ka/boundary/admin2s?school_type=pre'
        print("=======================================================")
        print("Testing listing admin2s preschool boundaries ", url)
        request=self.factory.get(url)
        force_authenticate(request,user=self.user)
        response = self.view(request, type='pre')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response.render()
        data = json.loads(response.content)
        print("Response is : ", data)
        print("End test ===============================================")
    
    def test_admin2s_primaryschool_districts(self):
        url = '/api/v1/ka/boundary/admin2s?school_type=primary'
        print("=======================================================")
        print("Testing listing primary school admin2s boundaries ", url)
        request=self.factory.get(url)
        force_authenticate(request,user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response.render()
        data = json.loads(response.content)
        print("Response is : ", data)
        print("End test ===============================================")

    def test_admin3s_boundaries(self):
        url = '/api/v1/ka/boundary/admin3s'
        print("=======================================================")
        print("Testing list all admin3s boundaries ", url)
        request=self.factory.get(url)
        force_authenticate(request,user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response.render()
        data = json.loads(response.content)
        print("Response is : ", data)
        print("End test ===============================================")

    def test_admin3s_preschool_districts(self):
        url = '/api/v1/ka/boundary/admin3s?school_type=pre'
        print("=======================================================")
        print("Testing listing admin3s preschool boundaries ", url)
        request=self.factory.get(url)
        force_authenticate(request,user=self.user)
        response = self.view(request, type='pre')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response.render()
        data = json.loads(response.content)
        print("Response is : ", data)
        print("End test ===============================================")
    
    def test_admin3s_primaryschool_districts(self):
        url = '/api/v1/ka/boundary/admin3s?school_type=primary'
        print("=======================================================")
        print("Testing listing primary school admin3s boundaries ", url)
        request=self.factory.get(url)
        force_authenticate(request,user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response.render()
        data = json.loads(response.content)
        print("Response is : ", data)
        print("End test ===============================================")