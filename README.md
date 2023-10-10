# News Flow Hub Django App

Welcome to News Flow Hub (https://news-flow-hub.onrender.com/), a Django application that empowers users to explore a curated selection of news articles across various topics. The project incorporates three main models: Topic, Redactor, and Newspaper.

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
Clone the repository.
Run the development server: 
```shell
python manage.py runserver.
```
Visit the app in your browser.


## Create Redactor:
The project provides a user-friendly form for creating redactors. To access, navigate to the registration page after signing up.

## Contributing:
Feel free to contribute to the project by submitting bug reports, feature requests, or pull requests. Your input is highly valued.