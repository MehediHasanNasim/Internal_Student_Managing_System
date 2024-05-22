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

## Setup Instructions to Run
Follow these steps to set up the project on your local machine.

### Prerequisites (Install)
- Python 3.x
- Django 3.x
- A SQL database (e.g., SQLite, PostgreSQL)
- Git

### Run
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
```

## Project Flow and Frontend View

### About section
![Screenshot 2024-05-22 012530](https://github.com/MehediHasanNasim/Internal_Student_Managing_System/assets/75909031/5af494c5-33a5-4d7e-b395-2ec3f448758a)

### Location Link
![Screenshot 2024-05-22 012600](https://github.com/MehediHasanNasim/Internal_Student_Managing_System/assets/75909031/b9df5c03-c07a-4152-b23b-de3c85428e4d)

### Signup
![Screenshot 2024-05-22 013255](https://github.com/MehediHasanNasim/Internal_Student_Managing_System/assets/75909031/25e7e0d8-64f3-400a-b6d4-a6e7280fc654)

### User Profile
![Screenshot 2024-05-22 012835](https://github.com/MehediHasanNasim/Internal_Student_Managing_System/assets/75909031/4d6b34a9-9e98-4dea-a950-1a6775006bb5)

### Admin Dashboard of Student List
![Screenshot 2024-05-22 012923](https://github.com/MehediHasanNasim/Internal_Student_Managing_System/assets/75909031/963c226d-c920-413a-89d9-eb9e882b33f2)

### Student Info
![Screenshot 2024-05-22 012950](https://github.com/MehediHasanNasim/Internal_Student_Managing_System/assets/75909031/ae2236b4-d7ba-4621-bc98-ba9218f9f9ff)

### Edit or Update Student info page
![Screenshot 2024-05-22 013058](https://github.com/MehediHasanNasim/Internal_Student_Managing_System/assets/75909031/04e4b6ba-5c71-4f83-abf0-04c938f9015e)

### Student Form
![Screenshot 2024-05-22 013206](https://github.com/MehediHasanNasim/Internal_Student_Managing_System/assets/75909031/2f0c1574-7eb2-4d93-8a53-6d39ed39992a)



