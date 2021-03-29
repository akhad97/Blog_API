from django.urls import path, include
from rest_framework import routers
from. import views


router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'contacts', views.ContactViewSet)
router.register(r'menus', views.MenuViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]