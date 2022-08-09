from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [

	path('',homePageView,name = 'home'),
	path('about/',AboutPageView.as_view(),name = 'about'),
	path('product_create/',ProductCreateView.as_view(),name='product_create'),
	path('book/',bookPageView,name = 'book'),
	path('menu/',menuPageView,name = 'menu'),
	# updateItem uchun
	path('update_item/',views.updateItem),
	# cart funsiyasi uchun 
	path('cart/', views.cart, name="cart"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

