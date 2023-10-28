# ShopIT

This project is a CRUD API for an E-Commerce website's product management. It's built using Python, Django, Django Rest Framework, and MySQL. You can use this API to create, read, update, and delete product listings.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [API Endpoints](#api-endpoints)
- [Database](#database)
- [Dockerization (Optional)](#dockerization-optional)
- [API Documentation](#api-documentation)
- [Fixtures for Base Data (Optional)](#fixtures-for-base-data-optional)
- [Caching (Optional)](#caching-optional)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before running this project, ensure you have the following installed:

- Python
- Django
- Django Rest Framework
- MySQL (with appropriate database setup)
- Git

### Installation

1. Clone the repository:

  ```bash
   git clone https://github.com/gouravSahu3212/ShopIT.git
   cd ShopIT

   virtualenv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   pip install -r requirements.txt


   python manage.py makemigrations
   python manage.py migrate

   python manage.py runserver
  ```

## USAGE

### API Endpoints

1. '/swagger'