from django.urls import path
from .views import register_user,login_user,logout_user,MashulotlarSerializerView,MashulotlarIDSerializerView,AuthUserRegistrationView


urlpatterns = [
	path('signup/',register_user,name='signup'),
	path('login/',login_user,name='login'),
	path('logout/',logout_user,name='logout'),


	#RESTAPI uchun
	path('',MashulotlarSerializerView.as_view()),
	path('<int:pk>/',MashulotlarIDSerializerView.as_view()),
	path('register/',AuthUserRegistrationView.as_view()),
	]