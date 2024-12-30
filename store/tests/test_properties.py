from rest_framework.test import APIClient
from rest_framework import status
import pytest
from django.conf import settings

class TestPropertyPermissions:
    @pytest.fixture(autouse=True)

    def test_create_user_is_not_admin(self):
        #arrange
        
        #act
        client = APIClient()
        response = client.post('/store/properties/', {"external_id" : "apartment_"} )
        #assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_user_is_not_admin(self):
        client = APIClient()
         # Arrange
        client.login(username="bilal", password="123")

        # Create a property to delete
        property_data = {"title": "Property to Delete", "city": "Rotterdam", "rent": 1000}
        create_response = self.client.post("/store/properties/", property_data, format="json")
        assert create_response.status_code == 201  # Ensure property was created

        property_id = create_response.data['id']
        
        #act
        response = client.delete('/store/properties/', )
        #assert
