from django.urls import path
from .views import CoursesView, AssignmentsView, AssignmentsByCourseView, AssignmentByIdView

urlpatterns = [
    path('api/courses/', CoursesView.as_view(), name='courses'),
    path('api/assignments/', AssignmentsView.as_view(), name='all_assignments'),
    path('api/courses/<int:course_id>/assignments/', AssignmentsByCourseView.as_view(), name='assignments'),
    path('api/courses/<int:course_id>/assignments/<int:assignment_id>/', AssignmentByIdView.as_view(), name='assignment'),
]
