# News Flow Hub Django App

Welcome to News Flow Hub (https://news-flow-hub.onrender.com/), a Django application that empowers users to explore a curated selection of news articles across various topics. The project incorporates three main models: Topic, Redactor, and Newspaper.

Data for access to service:
```shell
Login: admin.user
Password: 1qazcde3
```

## Features:
🔹 Topic Model: Represents diverse news categories, providing a broad spectrum of subjects for readers.

🔹 Redactor Model (Customized User Model): Extends the default user model to include specific information about redactors, empowering them to contribute articles with details such as years of experience.

🔹 Newspaper Model: Forms the core content structure, including title, article content, publication date, associated topic, and contributing redactors. This model serves as the foundation for news articles available on the platform.

## Requirements:
Ensure you have the following dependencies installed:
```shell
Django~=4.2.5
flake8==5.0.4
flake8-quotes==3.3.1
flake8-variables-names==0.0.5
pep8-naming==0.13.2
django-debug-toolbar==3.2.4
django-crispy-forms==1.14.0
```
## Usage:

Clone the repository:
```shell
https://github.com/grungezz/news_flow_hub.git
```

Change your working directory to the project folder:
```shell
cd news_flow_hub
```

Create and activate a virtual environment (if not done automatically by your IDE):
```shell
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
```
Install the project's Python dependencies using pip with the requirements file:
```shell
pip install -r requirements.txt
```
Apply database migrations to set up the database:
```shell
python manage.py makemigrations
python manage.py migrate
```
Load initial data if needed (from "test_data.json" in this case):
```shell
python manage.py loaddata test_data.json
```

Start the development server:
```shell
python manage.py runserver
```

Visit the app in your browser.


## Create Redactor:
The project provides a user-friendly form for creating redactors. To access, navigate to the registration page after signing up.

## Contributing:
Feel free to contribute to the project by submitting bug reports, feature requests, or pull requests. Your input is highly valued.