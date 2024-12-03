# Project Overview

This project is a web application built using Django, designed to manage various functionalities such as email handling, web scraping, and integration with external services like Canvas. The application is structured into multiple apps, each responsible for a specific feature.

## Project Structure

- **app1**: Handles user authentication and custom email validation.
- **canvasapp**: Integrates with Canvas to fetch courses and assignments.
- **email_handler**: Manages email sending functionalities.
- **scraper**: Contains web scraping utilities to gather data from external sources.


## Prerequisites

- Python 3.x
- Django
- Other dependencies listed in `requirements.txt`

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd backend
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up the database:
    ```sh
    python manage.py migrate
    ```

4. Configure environment variables in the `.env` file located in the `backend` directory. Ensure the following variables are set:
    ```properties
    GOOGLE_CLIENT_ID=<your-google-client-id>
    GOOGLE_CLIENT_SECRET=<your-google-client-secret>
    CANVAS_API_KEY=<your-canvas-api-key>
    ```

## Running the Application

To run the application, navigate to the `backend` directory and execute the following command:

```sh
python manage.py runserver
```

# Project Features and Documentation

## Features

### 1. **User Authentication**
- Implements custom email validation restricted to `@illinois.edu` domain.
- Includes login and signup functionalities for secure access.

### 2. **Canvas Integration**
- Fetches courses and assignments directly from Canvas.
- Provides API endpoints for seamless access to course and assignment data.

### 3. **Email Handling**
- Sends test emails using Django's email backend.
- Includes functionality for scheduled email sending.

### 4. **Web Scraping**
- Scrapes data from external websites using Selenium.
- Offers API endpoints to retrieve scraped data.

---

## License

This project uses the MIT License.