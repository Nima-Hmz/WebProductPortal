from django.urls import path
from .views import IndexView, AboutUsView

app_name = 'home'

urlpatterns = [

	path('', IndexView.as_view(), name='index'),
	path('aboutus/', AboutUsView.as_view(), name='aboutus')


]