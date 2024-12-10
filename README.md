# AssignMate

# Group Members
- Ryan Lee (rdlee4): Backend Development - Canvas/PrairieLearn integration, database, and integration w/ frontend
- Vijay Daita (vijayd2): Frontend Development - page design, integration w/ backend
- Annapoorna Narayan (an77): Backend Development - OAuth, Login, other misc. features
- Juno Kim (jkim826): Devops/Frontend - Dev Container, GitHub Actions, Test Cases

# Technical Architecture
Backend:
- Programming Language: Python
- Web Server: Django
- Database: SQLite
- Webscraping: Selenium WebDriver
- Canvas API Access: CanvasAPI

Frontend:
- Markup Language: HTML
- UI Framework: VueifyJS

# Project Overview

This project is a comprehensive web application developed using Django, aimed at streamlining various functionalities such as email management, web scraping, and seamless integration with external services like Canvas. The application is meticulously organized into multiple apps, each dedicated to a specific feature, promoting modularity and simplifying maintenance. By leveraging Django's robust framework, the project ensures scalability, security, and ease of development, making it an ideal solution for managing complex workflows and integrations.
## Features

- **Web Scraping**: Utilizes Selenium to extract data from various websites, enabling data collection and analysis.
- **Canvas Integration**: Seamlessly connects with Canvas LMS to manage courses, assignments, and grades, enhancing the educational experience.
- **User Authentication**: Implements secure user authentication using OAuth2, providing a safe and user-friendly login experience.

## Requirements

- Python 3.x
- Django
- Docker (for containerized setup)
- Other dependencies listed in `requirements.txt`

## Build Instructions

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd backend
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

### Step-by-Step

1. Set up the database:
    ```sh
    python manage.py migrate
    ```

2. Configure environment variables in the `.env` file located in the `backend` directory. Ensure the following variables are set:
    ```properties
    GOOGLE_CLIENT_ID=<your-google-client-id>
    GOOGLE_CLIENT_SECRET=<your-google-client-secret>
    CANVAS_API_KEY=<your-canvas-api-key>
    ```

3. Run the application:
    ```sh
    python manage.py runserver
    ```

### Dockerized Version

1. Build the Docker image:
    ```sh
    docker build -t project-image .
    ```

2. Run the Docker container:
    ```sh
    docker run -d -p 8000:8000 --env-file .env project-image
    ```

## Configuration Details

- Environment variables are configured in the `.env` file located in the `backend` directory.
- Ensure the following variables are set:
    ```properties
    GOOGLE_CLIENT_ID=<your-google-client-id>
    GOOGLE_CLIENT_SECRET=<your-google-client-secret>
    CANVAS_API_KEY=<your-canvas-api-key>
    ```

## Links to Important Services

- [Django Documentation](https://docs.djangoproject.com/)
- [Canvas API Documentation](https://canvas.instructure.com/doc/api/)
- [Selenium Documentation](https://www.selenium.dev/documentation/)

---

## License

This project uses the MIT License.
