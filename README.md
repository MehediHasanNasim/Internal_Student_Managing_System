# Internal School Management System

## About the Project
This project is an Internal School Management System developed using Django. It provides a multi-user platform with three user types: admin, teacher, and student. Each user has role-based access control, with robust authentication and email verification. Students can view their profiles and updates, including monthly attendance, required fees, and notices, which are managed by the administration.


![12121212](https://github.com/MehediHasanNasim/Internal_Student_Managing_System/assets/75909031/db963714-7715-4cae-908e-bbce685e1eb1)


### Features
- **Multi-user Platform:** Admin, teacher, and student roles with specific permissions.
- **Role-based Access Control:** Different functionalities available based on user roles.
- **Email Verification:** Ensures users are authenticated through email verification.
- **Personalized Profiles:** Students can view their own profiles, info and updates. 
- **Administrative Updates:** Admins can update student information such as attendance, fees, and notices.

## Tools and Technologies
- **Languages:** Python, HTML, CSS
- **Framework:** Django
- **Database:** SQL Database

## Setup Instructions
Follow these steps to set up the project on your local machine.

### Prerequisites
- Python 3.x
- Django 3.x
- A SQL database (e.g., SQLite, PostgreSQL)
- Git

### Installation
1. **Clone the repository:**
    ```sh
    git clone https://github.com/MehediHasanNasim/Internal_Student_Managing_System.git
    cd Internal_Student_Managing_System
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

6. **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:8000/`.


## Configuration
### Email Verification
To set up email verification, configure the email settings in `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'



### Frontend View

