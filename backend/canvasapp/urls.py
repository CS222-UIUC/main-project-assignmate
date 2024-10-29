from django.urls import path
from .views import courses_view, assignments_view

urlpatterns = [
    path('courses/', courses_view, name='courses'),  # Endpoint to get courses
    path('assignments/<int:course_id>/', assignments_view, name='assignments'),  # Endpoint to get assignments for a specific course
]
