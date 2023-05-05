# Django To-Do List App

This project is a simple To-Do list application built using Django. It allows users to create, update, and delete to-do lists and items within those lists.

## Project Overview

The main components include setting up a Django project, designing a data model, using Django's built-in object-relational mapping tool, creating templates and views, and connecting them through the URL dispatcher.

## Features

- User can create, edit, and delete to-do lists
- User can add, edit, and delete items within the to-do lists
- Item due dates are displayed for better task management

## How to Run the Project Locally

To run this project locally on another machine, follow these steps:

1. Clone the repository to your local machine using SSH: git clone git@github.com:your_username/your_repository.git

2. Change into the project directory: cd your_repository

3. Create and activate a virtual environment: python3 -m venv venv source venv/bin/activate

4. Install the required packages from the `requirements.txt` file: pip install -r requirements.txt

5. Apply migrations to create the database schema: python manage.py migrate

6. Run the Django development server: python manage.py runserver

7. Open your web browser and navigate to `http://127.0.0.1:8000/` to interact with the app.
