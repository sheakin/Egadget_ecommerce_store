Egadget E-commerce Store
Egadget E-commerce Store is a Python-based web application built with Django, enabling users to browse electronic gadgets, manage their shopping carts, place orders, and receive email notifications.

Features
User Authentication: Users can create accounts, log in, and log out securely.
Product Catalog: Browse and search for electronic gadgets with detailed descriptions.
Shopping Cart: Add and remove items, adjust quantities, and view total prices.
Order Management: Place new orders, cancel existing orders, and view order history.
Email Notifications: Receive email confirmations and notifications for order updates.
Technologies Used
Python
Django
HTML/CSS
Bootstrap
SQLite (or your database of choice)
SMTP (for email notifications)
Installation
To run Egadget E-commerce Store locally, follow these steps:

Clone the repository:

bash
Copy code
git clone git@github.com:sheakin/Egadget_ecommerce_store.git
cd Egadget_ecommerce_store
Set up a virtual environment:

bash
Copy code
python -m venv env
source env/bin/activate  # Activate virtual environment
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply database migrations:

bash
Copy code
python manage.py migrate
Create a superuser (admin account):

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Access the application:
Open a web browser and go to http://localhost:8000/

Usage
Admin Interface: Manage products, users, and orders via the Django admin interface at http://localhost:8000/admin/
User Interface: Browse products, add items to the cart, place orders, and manage account settings.
Contributing
Contributions are welcome! If you'd like to contribute to Egadget E-commerce Store, please follow these steps:

Fork the repository and create a new branch (git checkout -b feature-or-fix)
Make your changes and commit them (git commit -am 'Add feature')
Push to the branch (git push origin feature-or-fix)
Create a new Pull Request
License
This project is licensed under the MIT License - see the LICENSE file for details.

