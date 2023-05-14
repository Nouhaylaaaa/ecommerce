from django.urls import path
from .views import create_user,connexion,logoutUser
from boutique.views import home1,AboutUs,Contact
urlpatterns = [
    path('create/',create_user,name='create'),
    path('connexion/', connexion,name='connexion'),
    path('home1/', home1 , name='home1'),
    path('logout', logoutUser,name='logout'),
    path('AboutUs/', AboutUs , name='AboutUs'),
    path('ContactPage/', Contact, name='ContactPage'),


]