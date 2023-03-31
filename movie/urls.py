from django.urls import path
from movie import views

urlpatterns = [
    path('<int:movie_id>', views.details, name='details')
]
