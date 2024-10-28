# Django Inventory Management System

This project is a comprehensive inventory management system built with the Django framework. This application enables users to efficiently manage stock, monitor inventory levels in real time, and generate detailed reports for better decision-making.

It is worth remembering that this project is not yet finished.

### Features

- **Product Management**: Easily add, edit, or delete product details, ensuring up-to-date information across the inventory.
- **Stock Tracking**: Monitor stock levels in real-time, with automated alerts for low inventory to support timely restocking.
- **Reporting**: Generate and export comprehensive reports on sales, inventory levels, and other key metrics to support data-driven decisions.

### Installation

To get this project running on your local machine, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/LuisHb211/Django-Management-System.git
```
2. Navigate to the project directory:
```bash
cd Django-Management-System
```
3.  Create the virtual environment:
```bash
python -m venv venv
```
4. Activate the virtual environment:
```bash
.\venv\Scripts\activate 
```
5.  Install the requirements:
```bash
pip install -r requirements.txt 
```
6. Create the database:
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

### Django Secret Key

To use the application, you’ll need a Django SECRET_KEY. Generate one by running the following script in the terminal:
```bash
python generate_secret_key.py
```
Once generated, open settings.py and paste the key in the SECRET_KEY variable.

### Usage

Start the server:
```bash
  python manage.py runserver
```
To use the application, navigate to `http://localhost:8000` in your web browser after starting the server.


## 🛠️ Built with

* [Visual Studo Code](https://code.visualstudio.com/)  
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Git](https://git-scm.com/) 
* [Bootstrap](https://getbootstrap.com/)

### Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Submit a pull request.
