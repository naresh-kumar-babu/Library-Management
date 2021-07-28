# Library-Management System  
[![Django CI](https://github.com/TechieNK/Library-Management/actions/workflows/django.yml/badge.svg)](https://github.com/TechieNK/Library-Management/actions/workflows/django.yml)

## Functions
------
### Admin

<ul>
  <li>Create Admin account and Login.</li>
  <li>Can Add, View, Book</li>
  <li>Can Issue Book to registered student.</li>
  <li>Can view Issued book with date of issue and date of expiry.</li>
  <li>Can View Students that are registered into system.</li>
 </ul>
 
 ------
 
 ### Student
 
 <ul>
  <li>Create account and Login.</li>
  <li>Can view their issued book only with expiry date and fine</li>
 </ul>
 
## Installation Instructions
The portal is primarily a django based application, and to set it up we require to have 
python environment with django and other project dependencies installed. Though one can
work with the project without an virtual environment,  it is recommended to use one so 
as to avoid conflicts with other projects.

0. Make sure that you have `Python 3`, `python-3-devel`, `gcc`, `virtualenv`, and `pip` installed.     
1. Clone the repository

    ```bash
        $ git clone https://github.com/TechieNK/Library-Management.git
        $ cd Library-Management
    ```  
2. Create a python 3 virtualenv, activate the environment and Install the project dependencies.

    ```bash
        $ virtualenv -p python3
        $ source bin/activate
        $ pip3 install -r requirements.txt
    ```   

You have now successfully set up the project on your environment. 

---

### After Setting Up
From now when you start your work, run ``source bin/activate`` inside the project repository and you can work with the django application as usual - 

* `python3 manage.py migrate` - set up database
* `python3 manage.py createsuperuser` - create admin user
* `python3 manage.py runserver`  - run the project locally

*Make sure you pull new changes from remote regularly.* 
