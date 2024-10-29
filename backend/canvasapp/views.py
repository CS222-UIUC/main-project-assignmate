from django.http import JsonResponse
from canvasapi import Canvas
from canvasapi.exceptions import CanvasException
from collections import defaultdict

API_URL = "https://canvas.illinois.edu/"
API_KEY = "[replace with actual API KEY]"

# Initialize the Canvas object
CANVAS = Canvas(API_URL, API_KEY)
USER = CANVAS.get_user('self')

def get_courses():
    valid_courses = []
    courses = USER.get_courses()
    for course in courses:
        if not hasattr(course, 'id'):
            print("A course in the list is missing an ID and will be skipped.")
            continue

        try:
            c = CANVAS.get_course(course.id)
            valid_courses.append(c)
        except CanvasException:
            pass
    return valid_courses

def get_assignments(course_id):
    assignments = defaultdict(list)
    try:
        course = CANVAS.get_course(course_id)
        work = course.get_assignments()
        for w in work:
            assignments[course.name].append(w.name)
    except CanvasException:
        print(f"Could not retrieve assignments for course ID {course_id}.")
    return assignments

def courses_view(request):
    courses = get_courses()
    course_list = [{"id": course.id, "name": course.name} for course in courses]
    return JsonResponse(course_list, safe=False)

def assignments_view(request, course_id):
    assignments = get_assignments(course_id)
    return JsonResponse(assignments, safe=False)

# Create your views here.
