from django.urls import path
from rest_framework import permissions 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
	openapi.Info(
		title = "Blog API",
		description = 'API Loyiha',
		default_version = 'v1',
		terms_of_service = '',
		contact = openapi.Contact(email = "shuhratvahobov15@gmail.com"),
		license = openapi.License(name="Hozircha litsenziya yo'q"),
		

	),
	public = True,
	permission_classes = (permissions.AllowAny,),	
)


urlpatterns = [
	path('swagger/',schema_view.with_ui(
		'swagger',cache_timeout = 0), name = 'schema-swagger-ui'),
	path('redoc/',schema_view.with_ui(
		'redoc',cache_timeout = 0),name = 'schema-redoc'),
	]