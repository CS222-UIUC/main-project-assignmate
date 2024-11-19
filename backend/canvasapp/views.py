from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from canvasapi import Canvas
from canvasapi.exceptions import CanvasException
from collections import defaultdict
import requests

API_URL = "https://canvas.illinois.edu/"
API_KEY = "[INSERT API TOKEN HERE]"

# Initialize the Canvas object
CANVAS = Canvas(API_URL, API_KEY)
# USER = CANVAS.get_user('self')


def get_courses():
    valid_courses = []
    try:
        # Retrieve user and courses
        USER = CANVAS.get_user('self')
        courses = USER.get_courses()

        # Iterate over courses
        for course in courses:
            if not hasattr(course, 'id'):
                continue
            try:
                c = CANVAS.get_course(course.id)
                valid_courses.append(c)
            except CanvasException:
                pass
    except requests.exceptions.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    # Return a list even if an exception occurs
    return valid_courses


def get_all_assignments():
    all_assignments = defaultdict(list)
    valid_courses = get_courses()
    for course in valid_courses:
        name = course.name
        work = course.get_assignments(bucket="ungraded")
        for w in work:
            all_assignments[name].append(w.name)
    return all_assignments


def get_assignments_by_course(course_id):
    assignments = []
    try:
        course = CANVAS.get_course(course_id)
        work = course.get_assignments()
        for w in work:
            assignments.append(w.name)
    except CanvasException:
        pass
    return assignments


def get_assignment_by_id(course_id, assignment_id):
    try:
        course = CANVAS.get_course(course_id)
        assignment = course.get_assignment(assignment_id)
        return assignment
    except CanvasException:
        return None


class CoursesView(APIView):
    def get(self, request):
        courses = get_courses()

        # Ensure courses is an iterable
        if not courses:
            return Response({"error": "No courses found or failed to fetch courses."},
                            status=status.HTTP_204_NO_CONTENT)

        # Process courses
        course_list = [{"id": course.id, "name": course.name}
                       for course in courses]
        return Response(course_list, status=status.HTTP_200_OK)


class AssignmentsView(APIView):
    def get(self, request):
        assignments = get_all_assignments()
        return Response(assignments, status=status.HTTP_200_OK)


class AssignmentsByCourseView(APIView):
    def get(self, request, course_id):
        assignments = get_assignments_by_course(course_id)
        return Response(assignments, status=status.HTTP_200_OK)


class AssignmentByIdView(APIView):
    def get(self, request, course_id, assignment_id):
        assignment = get_assignment_by_id(course_id, assignment_id)
        if assignment is None:
            return Response("Assignment not found", status=status.HTTP_404_NOT_FOUND)
        return Response({"name": assignment.name, "description": assignment.description}, status=status.HTTP_200_OK)
