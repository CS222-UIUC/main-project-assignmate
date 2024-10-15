from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.http import JsonResponse
import requests

CANVAS_API_URL = 'https://your_canvas_instance/api/v1' # Replace with actual URL once we get developer key
ACCESS_TOKEN = '[ACCESS_TOKEN]' # Replace with actual token once we get key

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

def get_all_assignments(request):
    """Get all assignments."""
    api_url = f'{CANVAS_API_URL}/assignments'
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch assignments', 'status_code': response.status_code}, status=response.status_code)


def get_assignments_by_course(request, course_id):
    """Get assignments for a specific course."""
    api_url = f'{CANVAS_API_URL}/courses/{course_id}/assignments'
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch assignments for the course', 'status_code': response.status_code}, status=response.status_code)


def get_assignment_by_id(request, assignment_id):
    """Get a specific assignment by ID."""
    api_url = f'{CANVAS_API_URL}/assignments/{assignment_id}'
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch the assignment', 'status_code': response.status_code}, status=response.status_code)

def canvas_login(request):
    # Redirect to Canvas for authorization
    canvas_auth_url = "https://canvas.instructure.com/login/oauth2/auth"
    redirect_uri = "[REDIRECT_URI]"  
    client_id = "[CLIENT_ID]" 
    response_type = "[CODE]"
    
    return redirect(f"{canvas_auth_url}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}")

def canvas_callback(request):
    # Step 2: Handle the callback and get the access token
    code = request.GET.get('code')
    token_url = "https://canvas.instructure.com/login/oauth2/token"
    client_id = "[CLIENT_ID]"  # Your Canvas client ID
    client_secret = "[CLIENT_SECRET]"  # Your Canvas client secret

    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'grant_type': '[AUTH_CODE]',
        'redirect_uri': "[REDIRECT_URI]"
    }
    
    response = requests.post(token_url, data=payload)
    
    if response.status_code == 200:
        # Handle successful response, store the access token as needed
        return JsonResponse(response.json())
    else:
        # Handle error
        return JsonResponse({'error': 'Failed to obtain access token'}, status=400)
