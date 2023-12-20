Django Blog Project
Welcome to my Django Blog project! This project aims to provide a comprehensive blogging platform built using Python and the Django framework.

Overview
This blog project allows users to manage various elements of a blog, including posts, menu links, tags, and categories through an intuitive admin interface. The key features include:

Admin Dashboard: Easily manage blog elements via the admin panel, including post titles, menu links, and more.
Tag and Category System: Utilizes a many-to-many relationship to organize content efficiently, enhancing user navigation and enabling precise searches through the search bar.
Search Functionality: The search bar enables users to find posts by title, category, and tags, ensuring quick and accurate content discovery.
Additional Classes: Includes PostAttachment and Pages classes to complement blog functions, such as post publication status and image resizing.
Getting Started
To set up this project locally, follow these steps:

Clone this repository.
Install the required dependencies using pip install -r requirements.txt.
Run migrations with python manage.py migrate to set up the database.
Create a superuser account using python manage.py createsuperuser to access the admin panel.
Start the development server with python manage.py runserver.
Usage
Once the server is running, access the admin panel (/admin) to manage posts, categories, tags, and other blog elements.

Contributing
Contributions are welcome! If you have suggestions, improvements, or feature ideas, please feel free to open an issue or create a pull request.

Technologies Used
Python
Django
HTML
CSS
