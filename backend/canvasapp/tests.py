import pytest
from django.urls import reverse
from unittest.mock import patch
from canvasapi.exceptions import CanvasException


@pytest.mark.django_db
class TestCanvasDataViews:

    @patch('canvasdata.views.get_courses')
    def test_courses_view(self, mock_get_courses, client):
        # Mock the return value of get_courses
        mock_get_courses.return_value = [
            type('Course', (object,), {'id': 1, 'name': 'Course 1'}),
            type('Course', (object,), {'id': 2, 'name': 'Course 2'})
        ]

        response = client.get(reverse('courses'))
        assert response.status_code == 200
        assert response.json() == [
            {'id': 1, 'name': 'Course 1'},
            {'id': 2, 'name': 'Course 2'}
        ]

    @patch('canvasdata.views.get_assignments')
    def test_assignments_view(self, mock_get_assignments, client):
        # Mock the return value of get_assignments
        mock_get_assignments.return_value = {
            'Course 1': ['Assignment 1', 'Assignment 2'],
            'Course 2': ['Assignment 3']
        }

        response = client.get(reverse('assignments', kwargs={'course_id': 1}))
        assert response.status_code == 200
        assert response.json() == {
            'Course 1': ['Assignment 1', 'Assignment 2'],
            'Course 2': ['Assignment 3']
        }

    @patch('canvasdata.views.get_assignments')
    def test_assignments_view_invalid_course(self, mock_get_assignments, client):
        # Simulate a CanvasException being raised
        mock_get_assignments.side_effect = CanvasException

        response = client.get(
            reverse('assignments', kwargs={'course_id': 999}))
        assert response.status_code == 500
