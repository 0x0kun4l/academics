from django.urls import path
from .views import home_page_view, faculty_page_view, student_page_view, event_page_view

urlpatterns = [
    path('', home_page_view, name='home'),
    path('faculty/', faculty_page_view, name='faculty'),
    path('student/', student_page_view, name='student'),
    path('event/', event_page_view, name='event'),
]