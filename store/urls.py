from django.urls import path , include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('properties', views.PropertyViewSet)

urlpatterns = [
    path('' , include(router.urls)),
    path('cart/' , views.UserCartView.as_view())
]
