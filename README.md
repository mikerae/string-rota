![Am I Responsive](#)

# Orchestra String Rota
Code Institute Milestone Project 4
Written in python, developed on GitPod and Git Hub and deployed via Heroku.
## You can view a live version [here](#)
## How to use

## Contents
+ [UXD](#uxd)
    + [Strategy](#strategy)
    + [Scope](#scope)
    + [Structure](#structure)
    + [Skeleton](#skeleton)
    + [Surface](#surface)
+ [Schemas](#model-schema)
+ [Technologies Used](#technologies-used)
+ [Resources](#resources)
+ [Development](#development)
+ [Bugs and Fixes](#bugs-and-fixes)
+ [Known Issues](#known-issues)
+ [Deployment](#deployment)
+ [Acknowledgments](#acknowledgments)
## UXD
### Strategy
[Back to Top](#contents)
- Agile design process
- 3Cs: 
    - Card
        - User Story Template
    - Conversation
        - Tasks
    - Confirmation
        - Acceptance Criterea
- Predicted Project Effort
    - Ideal Time
        - Elapsed time
    - Story Points
        - Bench Mark Task: 1 story point
        - Allocated task: x story points
    - Methods of allocation of Story Points
        - Modified Fibonacci: 1, 3, 5, 8, 13, 20, 40
        - Doubling Score: 1, 2, 4, 8, 16, 32, 64
- Backlog
    - GitHub Milestones as Backlog
- Sprints
    - GitHub Milestones as Sprints (Iterations)
        - Timeboxing 1 - 2 weeks
- Prioritisation of Issues
    Moscow labeling
    - Must have: < 60% of total story points in iteration
    - Should have: the rest
    - Could have: 20% of total story points in iteration
    - Won't have
- Information Radiators
    - GitHub Projects as Kanban Boards 
        - Boards were created for the following:
            - Set Up
            - Sprint 1: to prepare for mid-project  Mentor session
            - Sprint 2: to prepare for final Mentor session
            - Sprint 3: to complete and submit project for assesment
### User Stories
- 3Cs: 
    - Card
        - User Story Template
    - Conversation
        - Tasks
    - Confirmation
        Acceptance Criterea



#### XX

#### XX

### Scope
#### Minimum Viable Product
[Back to Top](#contents)
#### Features
- Original code meets CI assessment criteria
- Complete code presents a working version of the game connect 4
- All external resources are clearly credited
#### Future Development
[Back to Top](#contents)

Future versions of the game can include:

### Structure
[Back to Top](#contents)
#### Flow Chart
![flow chart](/assets/images/flow-chart.png)


### Skeleton
[Back to Top](#contents)

#### XX

##### Features
T
### Surface
[Back to Top](#contents)

#### XX

### Model Schema
[Back to Top](#contents)

## Technologies Used
[Back to Top](#contents)

### Languages

The development environment used was GitPod
### Virtual Environment
- A virtual environment was used to ensure compatibility in deployment. A template containing all standard project requirements was prepared by the Code Institute.
- The environment was updated with additional requirements by downloading them into the environment via the terminal, and the requirements.txt file was updated using the following code:
```
pip3 freeze > requirements.txt
```
### Git
Git was used for version control
### GitHub
GitHub was used for external project storage and display
### Libraries
The following libraries were used:
#### psycopg2-2.9.5
#### Django-4.1.3

#### Python Libraries
The following internal python libraries were used:
- 
## Resources
[Back to Top](#contents)

The following resources were used:
+ Code Institute Training Material
+ Walkthroughs
    + CI ....

+ Python Documentation
+ Stack Overflow: https://stackoverflow.com/
+ Wikapedia: https://en.wikipedia.org/wiki/Main_Page
## Development
[Back to Top](#contents)

### Setting Up Development Environment
A gitHub repository was created using a required Code Institute template. This template created a virtual environment within the GitPod workspace which contained requirements for the Milestone 4 project.
#### Local Set Up
The following libraries were installed in the gitPPod workspace:
- psycopg2-2.9.5
``` gitpod /workspace/string-rota (main) $ pip3 install psycopg2 ```
- dj_database_url-1.0.0 ``` gitpod /workspace/string-rota (main) $ pip3 install dj_database_url ```

- Django-4.1.3 gunicorn-20.1.0 
``` gitpod /workspace/string-rota (main) $ pip3 install django gunicorn ```
- dj3_cloudinary_storage-0.0.6
``` gitpod /workspace/string-rota (main) $ pip3 install dj3-cloudinary-storage ```
pip

The details of the currently installed libraries were stored in the file requirements.txt so that Heroku can load them on ddeployment:
```
pip3 freeze --local > requirements.txt
```
This stored the following requirements:
```
asgiref==3.5.2
backports.zoneinfo==0.2.1
cloudinary==1.30.0
dj-database-url==1.0.0
dj3-cloudinary-storage==0.0.6
Django==4.1.3
gunicorn==20.1.0
psycopg2==2.9.5
sqlparse==0.4.3
```

A Django project was created:
``` gitpod /workspace/string-rota (main) $ django-admin startproject django_string_rota . ```

The Django install was tested by running the server:
``` gitpod /workspace/string-rota (main) $ python3 manage.py runserver ```

A browser window was opened using the port : http://127.0.0.1:8000/
and the default Django landing page was diplayed, demonstrating a succesful install.

The string_rota app was created in Django using: ``` gitpod /workspace/string-rota (main) $ python3 manage.py startapp string_rota ```

The string_rota app was added to the list of installed apps in the settings.py file
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'string_rota',
]
```

A number of the lines in the settings.py file were raising a linting error because they were too long for standard use in a terminal. Since these settings were not going to be visible in a terminal, the errors were supresssed by adding the following to the end of the long line:
```
  # noqa E501
```

The changes to the Django database were migrated, using the following command:
```
gitpod /workspace/string-rota (main) $ python3 manage.py migrate
```
#### Create app on Heroku
The app "string-rota" was created on Heroku by:
- Logging into Heroku
- Clicking on New
    - Click "Create new app"
- Giving the app a unique name.
    - "string-rota" was accepted as unique
- The region was chosen as:
    - Europe
- The app was created:
    - Click "Create app"

#### Create database on ElephantSQL
The database "string-rota" was created on ElephantSQL by:
- Logging into ElephantSQL
- Click on "Create New Instance"
- The plan was named "string-rota"
- The plan type was " Tiny Turtle (Free)
- CLick on "Select Region"
- "EU-West-1 (Ireland)" was selected by default
- Click on "Review"
- Click on "Create Instance"

#### Store database environment variables in env.py
- create a file "env.py" at the top directory in the workspace, at the same level as requirements.txt
- ensure that "env.py" is added to .gitignore so that it's sensetive contents are not pushed to github.
- In env.py
    - Import the os library
    - Add the DATABASE URL to the environment

        ``` 
        import os
        os.environ["DATABASE_URL"] = "<copiedURL>"
        ```
    where "copiedURL" is replaced by the copied elephantSQL "string-rota" URL

    - Add a secret key to the environment
        ```
        os.environ["SECRET_KEY"] = "my_super^secret@key"
        ```
#### Modify settings.py
- The following code was added to the settings.py file below PATH import:
```
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env
```
- Replace the insecure Django SECRET_KEY with the env.py SECRET_KEY
```
SECRET_KEY = os.environ.get('SECRET_KEY')
```
- Comment out the default database url variable (which would have conected Django to the internal db.sqlite3 database) and add a link to the env.py database url (the ElephantSQL remote database)
```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```
#### Migrate changes to django database
```
gitpod /workspace/string-rota (main) $ python3 manage.py migrate
```
#### Test conection with remote ElephantSQL database
- In the dashborad for ElephantSQL (logged in)
    - select "string-rota" instance
    - on the left menu
        - selcet BROWSER
        - select 'Table queries'
            - observe the dropdown is populated. This means that tables have been created by django in this database, and that the connection between django and the database is made.
#### Add Environment Varriables to Heroku
- In 'string-rota'
    - Click on 'Reveal Config Vars'
    - Add the follwing KEYS and their corresponding VALUES (without "")from env.py:
        - DATABASE_URL
        - SECRET_KEY
        - PORT 8000
#### Add Cloudinary Environment Varriable
- In created Cloudinary Account
    - Copy 
- In env.py
    - add environment variable:
    ```
    os.environ["CLOUDINARY_URL"] = "copied_url"
    ```
- In Heroku Config Vars
    - Add CLOUDINARY_URL: copied_url
#### Add Temporary Config Var to Heroku
There are no static files yet, and without the following variable set, the build will fail on Heroku.
Once static files are introduced into the project, this variable can be removed.
- DISABLE_COLLECTSATIC: 
#### Update Installed Apps and media/ static files in settings.py
- add 'cloudinary_storage' above 'django.contrib.staticfiles'
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary'
    'string_rota',
]
```
- below STATIC_URL = '/static/'  add the following:
```
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'  # noqa E501
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STRORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```
#### Add a Templates Directory in settings.py
- under BASE_DIR = Path(__file__).resolve().parent.parent add the following:
```
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
```
- in TEMPATES give 'DIRS' the value 'TEMPLATES'
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
#### Add Heroku Host Name in Settings.py
- in ALLOWED_HOSTS add the heroku app name
```
ALLOWED_HOSTS = ['string-rota.herokuapp.com', 'localhost']
```
#### Create 3 directories in the top level director, next to manage.py
- 'media'
- 'static'
- 'templates'
#### Create a Procfile
This tells Heroku that thew app will be displayed using the gunicorn webserver
- Create 'Procfile' at the top level, next to manage.py
```
web: gunicorn django_string_rota.wsgi
```
#### Push to GitHub and connect repository to Heroku
- Push to git hub
- In Heroku, string-rota:
    - Click on 'Deploy"
    - Select GitHub Connect to Github
    - Select the string-rota repository
    - choose auomatic deployment






### XX

### Full development of Minimum Viable Product
The Minimum Viable Product as defined in stage one of the development scope above was developed and deployed before progressing to stage two and beyond.


## Testing
[Back to Top](#contents)

### Automatic Testing
### Manual Testing
Table
#### Human Testing

### Incremental Function Testing
As each function and logic code was added and adapted, the code was tested to ensure its functionality was as expected.

### Python PEP8CI 
Python code
The code was tested using PEP8CI online http:# and passed without issue.
![#](#)

### JavaScript

### HTML

### CSS


###  pycodestyle Python Linter

### VSC Debugger
Extensive use of the built in debugger was used to test the more complex aspects of the code. Breakpoints were used to stop the code at particular points so that the values of particular variables could be examined.


### PEP8

## Bugs and Fixes
[Back to Top](#contents)


## Known Issues
[Back to Top](#contents)


## Deployment
[Back to Top](#contents)

### Initial Development Deployment
The project was deployed to Heroku in the intitial stages of development in order to resolve early and fundamental deployment issues.

#### !!!!! Review and update all of the following!!!!!

The project was deployed to the Heroku platform using the following steps:
- Delete unused resources/libraries
- Add \n to input line
- pip3 freeze > requirements.txt
- commit & push to gitHub
- make Heroku account
- create new app (in Heroku)
- in dashboard : open settings
- in settings : open config vars
    - add config vars
        - creds.json to config vars (these are environment variables, not exposed to the public). Key: “CREDS”, Value: the contents of creds.json
        -  key: “PORT”, Value : “8000”
    - Add build packs:
        - Heroku/python
        - Heroic/nodejs
- in deploy
    - choose deployment method
        - GitHub
        - connect to GitHub
        - Authorise Heroic to access your gitHub
        - search for and connect to repository name
        - choose a deployment method (Enable Automatic Deploys)
        - master/main branch
        - click view to open a web page with the deployment in a browser

#### Freeze requirements
Before deployment, the imported libraries were frozen into the requirement.txt file so that they could be available in the deployed virtual environment. The following code was used:
```
pip3 freeze > requirements.txt
```
This is the contents of the project requirements.txt file:
```
xx

```
### Final Deployement
The following additional steps were taken before final deployment
- Django debug mode was set to FALSE
- The GitHub Repository was made public
The project was deployed to the Heroku platform using the following steps:
- Delete unused resources/libraries
- Add \n to input line
- pip3 freeze > requirements.txt
- commit & push to gitHub
- make Heroku account
- create new app (in Heroku)
- in dashboard : open settings
- in settings : open config vars
    - add config vars
        - creds.json to config vars (these are environment variables, not exposed to the public). Key: “CREDS”, Value: the contents of creds.json
        -  key: “PORT”, Value : “8000”
    - Add build packs:
        - Heroku/python
        - Heroic/nodejs
- in deploy
    - choose deployment method
        - GitHub
        - connect to GitHub
        - Authorise Heroic to access your gitHub
        - search for and connect to repository name
        - choose a deployment method (Enable Automatic Deploys)
        - master/main branch
        - click view to open a web page with the deployment in a browser


## Acknowledgments
[Back to Top](#contents)

Grateful acknowledgment is given to the following
- Mentor: Martina Terlevic for her amazing guidance and encouragement
- Code Institute: for training materials, training environment and specific code