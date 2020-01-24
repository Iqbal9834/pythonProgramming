from django.urls import path,include
from . import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('developer', views.Developerview)
router.register('address',views.Addressview)
router.register('project',views.Projectview)
router.register('block',views.Blockview)
router.register('floor',views.Floorplanview)
router.register('people',views.Peopleview)
urlpatterns = [
    path('',include(router.urls))
]