# Web Series Management Backend (Django + MySQL)

This repository contains the backend for the Web Series Management System developed for the PDS course project.  
It uses Django, Django REST Framework, a custom User model, and MySQL as the database.

This README provides complete setup instructions for any new developer working on this project.

---

# Clone the Repository
```bash

git clone https://github.com/RajShivangi/PDS.git
cd PDS
```

# Install Dependencies
```bash
pip3 install -r requirements.txt
```

# MySQL Setup (User + Database)

```bash
mysql -u root -p
```
```sql
CREATE USER 'django'@'localhost' IDENTIFIED BY 'DjangoPass123!';
GRANT ALL PRIVILEGES ON *.* TO 'django'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

CREATE DATABASE news_db;

```
# Run Migrations
* Generate migration files:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
# Models are successfully created and the migration file should appear in folder core

# Run the server
python3 manage.py runserver
```
The backend will run at:

* http://127.0.0.1:8000/

# The Rest Apis available :
* http://127.0.0.1:8000/api/series/
* http://127.0.0.1:8000/api/episodes/
* http://127.0.0.1:8000/api/dubbing/
* http://127.0.0.1:8000/api/schedule/








