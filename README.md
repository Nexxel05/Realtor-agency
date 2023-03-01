# Realtor agency project

Django project for management of realtors and advertisements

## Check it out!

[Realtor agency project deployed to Render](https://realtor-agency.onrender.com/)

Login Credentials:

User: admin

Password: 1qazcde3

## Installation

Python3 must be already installed

```shell
git clone https://github.com/Nexxel05/Realtor-agency.git
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
Create .env file in root ditectory and store there your SECRET_KEY like shown in .env_sample 
```
python manage.py migrate
python manage.py runserver
```

## Features

* Authentication functionality for Realtor/User
* Management of advertisements directly from the website
* Powerful admin panel for advanced management