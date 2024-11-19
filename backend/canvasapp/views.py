from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from canvasapi import Canvas
from canvasapi.exceptions import CanvasException
from collections import defaultdict
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = "https://canvas.illinois.edu/"
API_KEY = os.environ["CANVAS_API_KEY"]

# Initialize the Canvas object
CANVAS = Canvas(API_URL, API_KEY)
USER = CANVAS.get_user('self')


def get_courses():
    valid_courses = []
    courses = USER.get_courses()
    for course in courses:
        if not hasattr(course, 'id'):
            continue
        try:
            c = CANVAS.get_course(course.id)
            valid_courses.append(c)
        except CanvasException:
            pass
    return valid_courses


def get_all_assignments():
    all_assignments = defaultdict(list)
    valid_courses = get_courses()
    for course in valid_courses:
        name = course.name
        try:
            work = course.get_assignments(bucket="ungraded")
            for w in work:
                assignment_data = {
                    "name": w.name,
                    "due_date": w.due_at,  # Due date of the assignment
                    "points": w.points_possible  # Points the assignment is worth
                }
                all_assignments[name].append(assignment_data)
        except CanvasException:
            pass
    return all_assignments


def get_assignments_by_course(course_id):
    assignments = []
    try:
        course = CANVAS.get_course(course_id)
        work = course.get_assignments()
        for w in work:
            assignment_data = {
                "name": w.name,
                "due_date": w.due_at,  # Due date of the assignment
                "points": w.points_possible  # Points the assignment is worth
            }
            assignments.append(assignment_data)
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
        course_list = [{"id": course.id, "name": course.name} for course in courses]
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
        return Response(
            {
                "name": assignment.name,
                "description": assignment.description,
                "due_date": assignment.due_at,
                "points": assignment.points_possible
            },
            status=status.HTTP_200_OK
        )
