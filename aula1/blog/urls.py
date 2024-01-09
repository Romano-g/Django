from django.urls import path
from blog.views import blog, exemplo


urlpatterns = [
    path('', blog),
    path('exemplo/', exemplo)
]
