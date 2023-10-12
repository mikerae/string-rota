![Am I Responsive](/readme_assets/images/am-i-responsive.png)
# Orchestra String Rota
Code Institute Milestone Project 4

Written in python, developed on GitPod and Git Hub and deployed via Heroku.
## You can view a live version [here](https://string-rota.herokuapp.com/)
Please be aware that the site simulates internal management of string rotas for the RSNO. Only bona fide members of the RSNO may access the site. If you would like to access the site, please contact mikerae@me.com. Thank you for your understanding.
## Contents
+ [Project Summary](#project-summary)
+ [Design Thinking](#design-thinking)
+ [UXD](#uxd)
+ [Agile Development](#agile-development)
+ [Database Design](#database-design)
+ [Technologies Used](#technologies-used)
+ [Testing](#testing)
+ [Validation](#validation)
+ [Resources](#resources)
+ [Development](#development)
+ [Bugs and Fixes](#bugs-and-fixes)
+ [Known Issues](#known-issues)
+ [Deployment](#deployment)
+ [Acknowledgments](#acknowledgments)

## Project Summary
This app facilitates members of the string sections of the RSNO to view seating plans and related information for a set of RSNO projects. It facilitates Rota Managers of these sections to create and manage their section rotas, and facilitates members of the office to integrate this information into their own work flows.
A sample set of RSNO project data was used to simulate connection to RSNO the server.
## Design Thinking
The phases of design thinking were followed in the development of this project:
- Empathise: Short 15 minute recorded interviews were conducted with stakeholders using a questions template. The stakeholders were from the RSNO were:
    - Rota Managers from each of the 5 String Sections
    - A player from each of the 5 String Sections 
    - 2 Office managers: one who fixes guest players, and manages seating positions, and one who manages time off permissions.
- The remaining phase (Define, Ideate, Prototype and Test) were achieved through the Agile development process described below.


- The interview questions can be viewed [here](/readme_assets/images/string_rota_questions.png)
## UXD
[Back to Top](#contents)
### Strategy
User Stories generated were used to drive the UXD.
In general there were 3 broad user stories:
-  As a member of my string section (Violin 1, Violin 2, Viola, Cello, Double Bass) I  can view project seating plans and related data so that I can  know when I am required to play, and be reassured that rota decisions are reasonable.
- As a rota manager for my section (Violin 1, Violin 2, Viola, Cello, Double Bass) I can create and manage a rota and related data for each project so that I can publish this to my colleagues.
- As an member of the office, I can view and edit all rota data so that I can integrate this data into my office work flows.
### Scope
The scope of the Minimum Viable Product can be seen in the Sprints in the Github repository.
- [View an example of a sprint](/readme_assets/images/sprint-1-scope-example.png):

#### Features
- User Login Landing Page, to preserve privacy, security and to allocate appropriate permissions.
    - [View the Landing Page](/readme_assets/images/landing-page.png)
- Orchestral project are selectable:
    - [View list of orchestra projects](/readme_assets/images/projects.png)
- View project seating plans and related data by a player's section
    - [View the Section Player Rota](/readme_assets/images/sm-published.png)
- Create and manage seating plans and data for a rota manager's section. A Rota Manager for a particular section may create, edit and delete rota information.
    - [View as Rota Manager](/readme_assets/images/rm-edit-sp.png)
- Orchestral managers may view and edit all information via the admin section of the site, and in future versions will have access to all rotas. Currently, the Office Manager functionality is not properly implemented.
    - [View as Orchestra Manager](/readme_assets/images/office-manager.png  )
- When a user logs in, the information displayed to them is relevant to their particular section only. A user's section and role are displayed
    - [View User Login Details](/readme_assets/images/rm-profile.png)
- Messaging was used to provide the user with feedback on their actions
    - [View example of Messaging](/readme_assets/images/messaging.png)
- A user may login as admin with superuser permissions:
    - [View as admin](/readme_assets/images/admin.png)

#### Future Development
[Back to Top](#contents)

Future versions may include integration with live RSNO data via an api.
### Structure
[Back to Top](#contents)

A user selects a program and the rota details are displayed for that program, if they are published.
#### Boostrapmade Template: NiceAdmin
It was decided to use [Bootstrapmade](https://bootstrapmade.com/) boilerplate templates to quickly create an effective front end.
Whilst the Niceadmin template is very versatile, and of high quality in many ways, the decision to use it turned out to be problematic.
- The minimum viable product for this project has very simple requirements for the front end. The code supplied with the NiceAdmin template is full of features, with large sections of code unused for this project.
- A significant amount of the Bootstrapmade code does not pass validation (see below).
- CSS files supplied by Bootsrap made prevented Heroku from building a deployed app in debug mode (although the deployed app was only required to be in debug mode for very short periods of time for specific troubleshooting).
- Custom javascript use was inhibited by complex unknown scripts supllied by Bootstrapmade.
#### Project Structure
The MVP project structure is very simple:
- A user logs in, the the user's role (String Section Member, Rota Manager, Orchestral Manager) is recognised.
- The user selects an orchestral project to examine.
- The name of the project and the repertoire to be played is diplayed.
- The published rota for that section is displayed
- If the user is the section Rota Manager, the draft version of the section rota is displayed and full CRUD functionality is availavle, facilitating the creation and managment of a rota.
- If the user is an Orchestral Manager, all the published rotas for a particular project will (eventually) be viewable.
### Skeleton
[Back to Top](#contents)

Wireframes describing the user interface were created using Balsamic.
Boostrapmade presented an approximated solution.
- [Login Landing Page](/readme_assets/images/log-in-landing-page.png)
- [Player Dashboard](/readme_assets/images/player-dashboard.png)
- [Rota Manager Seating Plan Form](/readme_assets/images/rota-manager-seating-plan-form.png)
- [Office Project](/readme_assets/images/office-project.png)
- [Office Player Data](/readme_assets/images/ofice-player-data.png)

### Surface
[Back to Top](#contents)
The NiceAdmn Boostrap template provided a good choice of fonts, images and colours.
## Agile Development
[Back to Top](#contents)

The Agile design process was used to some for this limited project.
### Platform
The GitHub platform was used to facilitate Agile Development:
### User Stories - Github Issues
- User stories were derived from interviews with stakeholders and notated as Github [issues](https://github.com/mikerae/string-rota/issues) These user stories were refined from 'epic' to more specific user-stories.
- For some user stories, Predicted Project Effort was defined, with story points being allocated to some user stories. 
- Issues were prioritised according to Moscow principles. Github Labels were used mark user stories accordingly.
    - Must have: < 60% of total story points in iteration
    - Should have: the rest
    - Could have: 20% of total story points in iteration
    - Won't have
#### Bugs
Bugs were recorded as issues, and the progress towards resolution of these issues was tracked.
#### Tests
Tests were recorded as issues, and their results were tracked.
### Information Radiators
Information Radiators were used to monitor the progress of the project development.
- A Github [Project](https://github.com/users/mikerae/projects/9/views/1)  was used to hold all user stories for processing and allocation in a Kanban Board. User stories were allocated to the Project and their progress tracked through the following stages:
    - New Issue
    - Backlog
    - Ready
    - In Progress
    - In Review
    - Done
- Github [Milestones]((https://github.com/mikerae/string-rota/milestones)) were used to define sprint content.
### Backlog
The GitHub [Project](https://github.com/users/mikerae/projects/9/views/1) was used to hold user stories and other issues which were not allocated to the current sprint.
### Sprints - Github Milestones
- [Sprints](https://github.com/mikerae/string-rota/milestones) were defined to define development tasks needed to bring the project to Minimum Viable Product level. Other Github Milestones were used to hold user stories allocated to these sprints.
## Database Design
[Back to Top](#contents)
### Mission Statement
The purpose of the string-rota database is to facilitate the creation, management and dissemination of Orchestral String Section Rotas and related data.
### Mission Objectives
- Present Orchestral Program data for each project
- Create and view section seating plans for each project
- Maintain and present player Natural Free Day Data
- Maintain and present player Reserve status for each project
- Maintain and present player Reduced - Repertoitre status for each project
### Requirements
#### User Requirements
1. Return a list of all projects
2. Return a seating plan for a specific string section project
3. Return a list of who is Reserve for each project
4. Return a list of who is not required for Reduced Repertoire.
5. Return a player's current Natural Free Day Data in the context of their annual quota.
6. Return an historical list of Reserve Allocations for each player.
#### Rota-Manager Requirements
1. Add players to specific seating positions for each project
2. Allocate Reserve/On/Off/Not-Available Status to each player in the Rota-Manager's section for each  project.
3. Allocate Reduced-Repertoire status to particular players per project.
4. Create and edit Seating Plans and allocations in draft mode, and publish to users when ready.
#### Office Requirements
1. Return a seating plan for all sections per project
2. Return Natural Free Day Allocation and totals for each player, for each project
3. Return rolling totals for Natural Free Day Allocations and usage for each player
4. Return a list of all players with Reserve status for each project
5. Edit and update all 
#### System Requirements
1. Return Program Data
2. Return Seating Position Data for each player, project and section.
3. Store and Calculate Natural Free Day allocations and totals based on Allocation for each project.
4. Store and Return Reserve player status for each project.
### Preliminary Field List
- [View the Preliminary Field List](/readme_assets/images/preliminary-field-list.png)
### Resolution of Field and Table anomalies
In order to resolve field and table anomalies, and in order to preserve data integrity the following process was followed:
- The tables were flattened, and populated with data.
    - Any problematic fields were resolved
- The resulting fields and tables were compared with the characteristics of a sound field or table.

Very Academy produced a helpful checklist to evaluate fields and tables (https://www.youtube.com/watch?v=ycw8ZsT1ofw&t=1901s):
- [View a Field and Table Checklist](/readme_assets/images/field-and-table-checklist.png)

When attempting to flatten the project table, the resulting table produced duplicate data, further need for flattening and some calculated data:
- [View an Example of field and table problem resolution](/readme_assets/images/example-of-field-table-problem-resolution-1.png)

The products table was amended to remove duplicate data, multi-data fields and calculated fields. At this point the checklists above were mostly satisfied.

- [View Rationalisation of project table](/readme_assets/images/rationalisation-of-product-table.png)

#### Model Entity Relationship Diagram (EDR)
The entities for this project have the following relationships and attributes:
- [View String-Rota-Erd](/readme_assets/images/string-roto-erd.png)
#### Model Schemas
The Models Schemas erds for this project are:
- [View String-Rota-erd-Schema](/readme_assets/images/string-rota-erd-schema.png)
#### Model Creation
The models were created from least dependant (eg Repertoire) to most dependant.
#### Initial data input
Tables were populated starting from least dependant using utility function to import from a private google worksheet where RSNO data had been pre-cleaned manually.
Where a relationship exists between tables, both sides were populated first, then the connection was made manually in the project admin.
Whilst automating this process is understood to be possible, it is beyond the scope of this project to implement for this release.
The one case where a table was populated by script was the the Player_Project link table. Here a script was used to iterate over each player for each project.
 

## Technologies Used
[Back to Top](#contents)

### Languages
- Python
- HTML5
- CSS
- Javascript (potentially)

### Development Environment: GitPod
#### Virtual Environment
- A virtual environment was used to ensure compatibility in deployment. A template containing all standard project requirements was prepared by the Code Institute.
- The environment was updated with additional requirements by downloading them into the environment via the terminal, and the requirements.txt file was updated using the following code:
```
pip3 freeze > requirements.txt
```
### Git
Git was used for version control
### GitHub
GitHub was used for external project code storage and display
### Libraries
The following external libraries were used:
- psycopg2-2.9.5
- Django-3.2.3
- gspread google-auth
- pandas numpy pyjanitor

# Testing
[Back to Top](#contents)
### Automatic Testing
No automatic testing was used for the MVP.
Future versions will have full django unit and integration testing.
### Manual Testing
The following manual tests were made:
- [Test Log 1](/readme_assets/images/test-log-1.png)
- [Test Log 2](/readme_assets/images/test-log-2.png)
- [Test Log 3](/readme_assets/images/test-log-3.png)
- [Bug Fix #129 Testing](/readme_assets/images/testing-issue129.png)
    - [see issue #129 here](https://github.com/mikerae/string-rota/issues/129)
- [Bug Fix #130 Testing](/readme_assets/images/testing-issue130.png)
    - [see issue #130 here](https://github.com/mikerae/string-rota/issues/130)
- [Bug Fix #154 Testing](/readme_assets/images/testing-issue154.png)
    - [see issue #154 here](https://github.com/mikerae/string-rota/issues/154)
- [Bug Fix #128 Testing](/readme_assets/images/testing-issue128.png)
    - [see issue #128 here](https://github.com/mikerae/string-rota/issues/128)
- [Bug Fix #127 Testing](/readme_assets/images/testing-issue127.png)
    - [see issue #127 here](https://github.com/mikerae/string-rota/issues/127)
- [HTML Validaton #143 Testing](/readme_assets/images/testing-issue143.png)
    - [see issue #143 here](https://github.com/mikerae/string-rota/issues/143)
- [Delete Unused HTML Template #150 Testing](/readme_assets/images/testing-issue150.png)
    - [see issue #150 here](https://github.com/mikerae/string-rota/issues/150)
- [Python and JS post-validation Testing #145 #156](/readme_assets/images/testing-issue145-146.png)
    - [see issue #145 here](https://github.com/mikerae/string-rota/issues/145)
    - [see issue #146 here](https://github.com/mikerae/string-rota/issues/146)
- [Upgrade Django to 3.2.5 #147 Testing](/readme_assets/images/testing-issue147.png)
    - [see issue #147 here](https://github.com/mikerae/string-rota/issues/147)
- [Add welcome screen, links #131 Testing](/readme_assets/images/testing-issue131.png)
    - [see issue #131 here](https://github.com/mikerae/string-rota/issues/131)
- [Register #138 Testing](/readme_assets/images/testing-issue138.png)
    - [see issue #138 here](https://github.com/mikerae/string-rota/issues/138)
- [All Registered #138 Testing](/readme_assets/images/testing-issue#138%201.png)
    - [see issue #138 here](https://github.com/mikerae/string-rota/issues/138)
- [External BoostrapMade link #157 Testing](/readme_assets/images/testing-issue157.png)
    - [see issue #157 here](https://github.com/mikerae/string-rota/issues/157)
- [Display Draft/Published rota data #159 Testing](/readme_assets/images/testing-issue159.png)
    - [see issue #159 here](https://github.com/mikerae/string-rota/issues/159)
- [Change Password #166 Testing](/readme_assets/images/testing-issue166-1.png)
    - [see issue #166 here](https://github.com/mikerae/string-rota/issues/166)
- [Add Email #166 Testing](/readme_assets/images/testing-issue166-2.png)
    - [see issue #166 here](https://github.com/mikerae/string-rota/issues/166)
- [Enable Email Server #166 Testing](/readme_assets/images/testing-issue166-3.png)
    - [see issue #166 here](https://github.com/mikerae/string-rota/issues/166)
- [Update Sidebar and Welcome Screen #156 Testing](/readme_assets/images/testing-issue156-1.png)
    - [see issue #156 here](https://github.com/mikerae/string-rota/issues/156)
- [Show sections in sidebar #156 Testing](/readme_assets/images/testing-issue156-2.png)
    - [see issue #156 here](https://github.com/mikerae/string-rota/issues/156)
- [Admin/Orch Manager View Rotas #156 Testing](/readme_assets/images/testing-issue156-3.png)
    - [see issue #156 here](https://github.com/mikerae/string-rota/issues/156)
- [Admin Add Seating Position View Rotas #170 Testing](/readme_assets/images/testing-issue170-1.png)
    - [see issue #170 here](https://github.com/mikerae/string-rota/issues/170)
- [Admin Seating Position CRUD  #170 Testing](/readme_assets/images/testing-issue170-2.png)
    - [see issue #170 here](https://github.com/mikerae/string-rota/issues/170)
- [Admin Toggle Draft/Published Rotas  #170 Testing](/readme_assets/images/testing-issue170-3.png)
    - [see issue #170 here](https://github.com/mikerae/string-rota/issues/170)
- [Admin Allocate Reserve Player  #170 Testing](/readme_assets/images/testing-issue170-4.png)
    - [see issue #170 here](https://github.com/mikerae/string-rota/issues/170)
- [Admin Register Player  #172 Testing](/readme_assets/images/testing-issue172.png)
    - [see issue #172 here](https://github.com/mikerae/string-rota/issues/172)
- [Fix User Profile dropdown  #171 Testing](/readme_assets/images/testing-issue171.png)
    - [see issue #171 here](https://github.com/mikerae/string-rota/issues/171)
- [Fix CRUD Buttons for Office  #175 Testing](/readme_assets/images/testing-issue175.png)
    - [see issue #175 here](https://github.com/mikerae/string-rota/issues/175)
- [Fix Project selection for Admin and Orch Manager  #179 Testing](/readme_assets/images/testing-issue179.png)
    - [see issue #179 here](https://github.com/mikerae/string-rota/issues/179)
- [Fix Allocate Reserve Button for Admin and Rota Manager  #184 Testing](/readme_assets/images/testing-issue184.png)
    - [see issue #184 here](https://github.com/mikerae/string-rota/issues/184)
- [Update messaging  #176 Testing](/readme_assets/images/testing-issue176.png)
    - [see issue #176 here](https://github.com/mikerae/string-rota/issues/176)
#### Human Testing
No human testing was done for this MVP, but once office manager functionality, and the hiding of draft rotas is implemented, user feedback will be sort.

### Incremental Function Testing
As each feature was added, it was tested manually to ensure that it behaved as desired.
# Validation
[Back to Top](#contents)
### Python PEP8CI 
Python code
The code was tested using [PEP8CI online](https://pep8ci.herokuapp.com/)  and passed without issue.
- [CI Python Linter](/readme_assets/images/ci-python-linter.png)

#### PEP8CI Validation for Project resubmission 2
The code was tested using [PEP8CI online](https://pep8ci.herokuapp.com/) and passed without issue.
The results are shown here:
- django_string_rota/
    - [asgi](/readme_assets/images/validation/python/dsr-asgi.png)
    - [settings](/readme_assets/images/validation/python/dsr-settings.png)
    - [urls](/readme_assets/images/validation/python/sr-urls.png)
    - [manage](/readme_assets/images/validation/python/manage.png)
    - [setup](/readme_assets/images/validation/python/setup.png)
- player_info/
    - [views](/readme_assets/images/validation/python/pi-views.png)
    - [urls](/readme_assets/images/validation/python/pi-urls.png)
- string_rota/
    - [admin](/readme_assets/images/validation/python/sr-admin.png)
    - [apps](/readme_assets/images/validation/python/sr-apps.png)
    - [forms](/readme_assets/images/validation/python/sr-forms.png)
    - [models](/readme_assets/images/validation/python/sr-models.png)
    - [tests](/readme_assets/images/validation/python/sr-tests.png)
    - [urls](/readme_assets/images/validation/python/sr-urls.png)
    - [utilities](/readme_assets/images/validation/python/sr-utilities.png)
    - [views](/readme_assets/images/validation/python/sr-views.png)
- string_rota/utilities/
    - [get_orch_data](/readme_assets/images/validation/python/sr-utilities-get-orch-data.png)
    - [load_rsno_data](/readme_assets/images/validation/python/sr-utilities-load-rsno-data.png)
    - [setp_tables](/readme_assets/images/validation/python/sr-utilities-setup-tables.png)

### Pylint VSCODE linter
The pylint linter was used throughout development to ensure that problematic code was corrected as early as possible.

A number of the lines in the settings.py file were raising a linting error because they were too long for standard use in a terminal. Since these settings were not going to be visible in a terminal, the errors were suppressed by adding the following to the end of the long line:
```
  # noqa E501
```

There were several instances where the VSCode Pylint identifie that some objects had no members associated with them. These objects were, in fact, populated and accessable. This error message was disables by placing the following code at the the top of a file which generated this error.
```
# pylint: disable=no-member
```

The state of the currently deployed python code shows minor issues:
- [Pylint Output](/readme_assets/images/pylint-output.png)



### JavaScript
The project currently uses no custom javascript, mainly because it was interfering with BootstrapMade javascript and it was difficult to isolate the code without causing problems. Toasts, and very simple jquery toggle display scripts were omitted for this reason. It is intended to remove the Boostrapmade components and reinstall jquery and boostrap for future versions, allowing proper control of the code.
JSHint showed multiple javascript errors, all of which originated in BoostrapMade code. There was not time before the resubmission of this MVP to investigate and correct these issues.
- [JSHint Issues for Project resubmission 1](/readme_assets/images/jshint.png)

#### Project Resubmission 2 [JS Validation: Issue 146](https://github.com/mikerae/string-rota/issues/146)
The third party BootstrapMade templates used in this project used main.js.
JSHint identified multiple missing semi-colons, which were added to main.js.
The remaining warnings may be viewd [here](/readme_assets/images/validation/js/main.png).
These warnings were left unaddressed since they were considered beyond the scope of this project.
### HTML
The W3C NU html validator was used.
1 validation issue originating in allauth code was exposed. Input tags were closed using ```/>```.
[See the summary validator response here](/readme_assets/images/validation/html/fail/home(string-rota).png)
[See the code detail for the validator response here](/readme_assets/images/validation/html/fail/home(string-rota)-detail.png)

Otherwise the code for Project 4 resubmission passed without issue.
- [W3C HTML Validator 1](/readme_assets/images/nu-html-checker-1.png)
- [W3C HTML Validator 2](/readme_assets/images/nu-html-checker-2.png)
- [W3C HTML Validator 3](/readme_assets/images/nu-html-checker-3.png)
- [W3C HTML Validator 4](/readme_assets/images/nu-html-checker-4.png)
- [W3C HTML Validator 5](/readme_assets/images/nu-html-checker-5.png)
- [W3C HTML Validator Register](/readme_assets/images/validation/html/register.png)

However, the assesment for Project 4 resubmission 1 showed [significant html validation issues](https://github.com/mikerae/string-rota/issues/124).
It must be assumed that these issues were related to [server errors](https://github.com/mikerae/string-rota/issues/123) introduced by 'code cleaning' imediately prior to the project resubmission. 

[See issue #143 for html validation here](https://github.com/mikerae/string-rota/issues/143)

For the Project 4 second resubmission,  the ```/``` was removed.

Once this change was made, all html passed validation without issue.

### CSS
The W3C CSS Validator was used. There were multiple issues presented, all of which were caused by BootstrapMade css.
Bootstrapmade will not be used in future projects.
- [W3C CSS Validator](/readme_assets/images/wc3-css.png)

### Accessibility: Lighthouse
The Chrome Developer Tools Lighthouse was used to validate the accessibility of each page. Each page scored 100%.
- [The String-Rota Page scored 100%](/readme_assets/images/validation/lighthouse/string-rota.png)
- [The Add Seating Position Page scored 100%](/readme_assets/images/validation/lighthouse/add-sp.png)
- [The Edit Seating Position Page scored 100%](/readme_assets/images/validation/lighthouse/edit-sp.png)
- [The Reserve Player Page scored 100%](/readme_assets/images/validation/lighthouse/reserve.png)
- [The Logout Page scored 100%](/readme_assets/images/validation/lighthouse/logout.png)
- [The Landing Page scored 100%](/readme_assets/images/validation/lighthouse/index.png)
- [The Register Page scored 100%](/readme_assets/images/validation/lighthouse/register.png)
# Resources
[Back to Top](#contents)

The following resources were used:
+ Code Institute Training Material
+ Python Documentation: 
+ Django Documentation: https://docs.djangoproject.com/en/3.2/ref/
+ Stack Overflow: https://stackoverflow.com/
+ Wikapedia: https://en.wikipedia.org/wiki/Main_Page

# Development
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

The details of the currently installed libraries were stored in the file requirements.txt so that Heroku can load them on deployment:
```
pip3 freeze --local > requirements.txt
```
The current requirements used are:
```
asgiref==3.3.4
cachetools==5.2.0
cloudinary==1.25.0
cryptography==3.4.8
dj-database-url==0.5.0
dj3-cloudinary-storage==0.0.5
Django==3.2.3
django-allauth==0.44.0
django-crispy-forms==1.11.2
django-summernote==0.8.11.6
google-api-core==2.11.0
google-api-python-client==2.68.0
google-auth==2.15.0
google-auth-httplib2==0.1.0
google-auth-oauthlib==0.7.1
googleapis-common-protos==1.57.0
gspread==5.7.2
gunicorn==20.1.0
httplib2==0.21.0
lazy_loader==0.1rc2
multipledispatch==0.6.0
natsort==8.2.0
numpy==1.24.4
oauthlib==3.1.1
pandas==2.0.3
pandas-flavor==0.3.0
protobuf==4.21.10
psycopg2==2.8.6
pyasn1==0.4.8
pyasn1-modules==0.2.8
PyJWT==2.1.0
python3-openid==3.2.0
pytz==2021.1
requests-oauthlib==1.3.0
rsa==4.9
scipy==1.9.3
sqlparse==0.4.1
tabulate==0.9.0
tqdm==4.64.1
tzdata==2023.3
uritemplate==4.1.1
xarray==2022.12.0
urllib3==1.26.15
```

A Django project was created:
``` gitpod /workspace/string-rota (main) $ django-admin startproject django_string_rota . ```

The Django install was tested by running the server:
``` gitpod /workspace/string-rota (main) $ python3 manage.py runserver ```

A browser window was opened using the port : http://127.0.0.1:8000/
and the default Django landing page was displayed, demonstrating a successful install.

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

The changes to the Django database were migrated, using the following command:
```
gitpod /workspace/string-rota (main) $ python3 manage.py migrate
```
We will 
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
- Click on "Select Region"
- "EU-West-1 (Ireland)" was selected by default
- Click on "Review"
- Click on "Create Instance"

#### Store database environment variables in env.py
- create a file "env.py" at the top directory in the workspace, at the same level as requirements.txt
- ensure that "env.py" is added to .gitignore so that it's sensitive contents are not pushed to github.
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
- Comment out the default database url variable (which would have connected Django to the internal db.sqlite3 database) and add a link to the env.py database url (the ElephantSQL remote database)
```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```
#### Migrate changes to django database
```
gitpod /workspace/string-rota (main) $ python3 manage.py migrate
```
#### Test connection with remote ElephantSQL database
- In the dashboard for ElephantSQL (logged in)
    - select "string-rota" instance
    - on the left menu
        - select BROWSER
        - select 'Table queries'
            - observe the dropdown is populated. This means that tables have been created by django in this database, and that the connection between django and the database is made.
#### Add Environment Variables to Heroku
- In 'string-rota'
    - Click on 'Reveal Config Vars'
    - Add the following KEYS and their corresponding VALUES (without "")from env.py:
        - DATABASE_URL
        - SECRET_KEY
        - PORT 8000

####  data to Django db.sql and ElephantSql
##### Initial Data Loading
Initial data was imported into the project using set_up.py and associated utilities. This data was available from a spreadsheet stored in googledocs. set_up.py securely logged into the sreadsheet and retrieved the required data, then loaded the data into the models in the correct order.
#### Subsequent Data Loading
Once a credible starting data set was established, this data set was dumped into a db.json file in the fixtures dir using the following command.

```
python manage.py dumpdata --exclude auth.permission --exclude contenttypes --indent 4 > db.json
```
When the local  database needed to be reset:
- The db.sql file was deleted
- Migrations were run
- The db.json file was loaded using Loaddata

When the remote database needed to be reset:
- The database dashboard was accessed from the ElephantSql site
- The database was reset
- DEVEPLOPMENT variable was commented out in  env.py 
- Migrations were run
- The db.json file was loaded using Loaddata
#### Add Cloudinary Environment Variable
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
- DISABLE_COLLECTSATICK:1
#### Update Installed Apps and media/ static files in settings.py
The deployment platform, Heroku, is ephemeral i.e. when it is not being used, it stops running actively and any state data is lost. It is necessary, therefore, to store static files in a permanent state location. For this project, Cloudinary was used as the permanent storage location for the static files.
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
    'cloudinary',
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
- in TEMPLATES give 'DIRS' the value 'TEMPLATES'
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
#### Create 3 directories in the top level directory, next to manage.py
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

#### Build, deploy and open app on Heroku
After some trouble-shooting (see bugs and fixes) the default Django landing page was shown on the Heroku deployed site.

#### RSNO Program and Player Data
Access to live RSNO data was not within the scope of this project.
This access was assumed. To simulate live project data and current player data then following data was received from the RSNO in csv form: 
- a 4 week schedule of orchestral projects
- a list of string player names and their Annual Natural Free Day Allocation
##### Data Security
The RSNO data is private. No RSNO data is accessible via the Github repository, and the data is only accessible via the Heroku deployed app for authenticated users.
To preserve this level of privacy, a private google drive was used to store the RSNO data before importing it into the project.

These RSNO csv files were imported into a google worksheet, stored on the private google drive.
The worksheet data was accessed using the google drive and gspread APIs.

The worksheets were separated into separate sheets reflecting the structure of the project models. The data was cleaned manually. In future versions, data would be cleaned using Pandas, Numpy and Pyjanitor.

The worksheet data was imported incrementally into the database using a script run from the terminal.  Niroj in https://www.edureka.co/community/73739/django-script-access-model-objects-without-using-manage-shell, and the Django documentation provided a solution to access the project models for this purpose, since specific Django setup code was needed for stand-alone scripts.

### Development of Minimum Viable Product
The Minimum Viable Product as defined in stage one of the development scope above reduced in scope. Basic Create Read Update Delete functionality was implemented.


## Bugs and Fixes
[Back to Top](#contents)

### First Deployment Fail
```
       Failed to build backports.zoneinfo
       ERROR: Could not build wheels for backports.zoneinfo, which is required to install pyproject.toml-based projects
```
- Stack Overflow: 20BCS055_Ankur Mishira writes:
"In order to do that you need to tell heroku to switch that version and it can be done as follows :

Create runtime.txt in root directory.
python-3.8.10 <- write this in 'runtime.txt' there as to specify the version.
heroku will then install this version and you will be not getting anymore error."
- The next build failed:
```
-----> Building on the Heroku-22 stack
-----> Determining which buildpack to use for this app
-----> Python app detected
-----> Using Python version specified in runtime.txt
 !     Requested runtime 'python-3.8.10' is not available for this stack (heroku-22).
 !     For supported versions, see: https://devcenter.heroku.com/articles/python-support
 !     Push rejected, failed to compile Python app.
 !     Push failed
```
- Installed version of Python is:
```
gitpod /workspace/string-rota (main) $ python3 --version
Python 3.8.11
```
- Heroku supported versions of Python are:
python-3.11.0 on all supported stacks
python-3.10.8 on all supported stacks (recommended)
python-3.9.15 on all supported stacks
python-3.8.15 on Heroku-18 and Heroku-20 only
python-3.7.15 on Heroku-18 and Heroku-20 only
- Removed runtime.txt file, added Python buildpack to Heroku
    - Build failed with same error:
    ```
Failed to build backports.zoneinfo
       ERROR: Could not build wheels for backports.zoneinfo, which is required to install pyproject.toml-based projects
 !     Push rejected, failed to compile Python app.
 !     Push failed
    ```
It was determined that I used an incompatible version of Django.
Django was uninstalled
Then re-installed using:
```
pip3 install Django==3.2
pip3 freeze --local > requirements.txt
```
After further Heroku build fails, Code Institute Student Support reccomended re-installing all libraries using the following:
```
pip3 uninstall -r requirements.txt -y
```
The contents of requirements.txt was replaced from:
I would recommend using the versions of packages used in the walkthrough. First you can uninstall existing packages:
https://github.com/Code-Institute-Solutions/Django3blog/blob/master/12_final_deployment/requirements.txt
Then the new requirements were installed for  the packages listed in the requirements file:
pip3 install -r requirements.txt

After this, the build on Heroku succeeded , but the app did not open.
The app log showed that a comma was missing in the INSTALLED APPS.
This was corrected to:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'string_rota',
]
```
The build deployed  successfully, and the app opened with the default Django landing page.

### Static Files not found on Heroku
After initial deployment to Heroku, the admin section would not style on the Heroku site but would style on the local site.
Fix: When DEBUG=False, Heroku can collect and read the static files.
### Static Files not read when NiceAdmin templates were used.
Static files were not found on either local or Heroku sites.
The NiceAdmin templates referenced the assets folder using and absolute path.
Fix: Django was set up to reference the files using a relative path. To fix this, the following steps were taken:
- the static settings were confirmed to be correct: 
```
 STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'  # noqa E501
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
- The static files were in the top project directory ( /static/assets/... )
- The path to static files was changed: 
```  <link href="assets/css/style.css" rel="stylesheet"> ```
 was changed to ``` <link rel="stylesheet" href="{% static 'assets/css/style.css' %}"> ```, and all references to static files in the assets folder were also changed. The changes were made in the base.html file.
- The django static variable was loaded at the top of base.html:
``` {% load static %}```

### MultipleObjectsReturned Disney Project
When clicking on the Disney Project, it now throws a MultipleObjectsReturned error for get().
```
MultipleObjectsReturned at /home/recording-sessions-for-disney/
get() returned more than one Player_Project -- it returned 2!
Request Method: GET
Request URL:    http://localhost:8000/home/recording-sessions-for-disney/
Django Version: 3.2.3
Exception Type: MultipleObjectsReturned
Exception Value:    
get() returned more than one Player_Project -- it returned 2!
Exception Location: /workspace/.pip-modules/lib/python3.8/site-packages/django/db/models/query.py, line 439, in get
Python Executable:  /home/gitpod/.pyenv/versions/3.8.11/bin/python3
Python Version: 3.8.11
Python Path:    
['/workspace/string-rota',
 '/home/gitpod/.pyenv/versions/3.8.11/lib/python38.zip',
 '/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8',
 '/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/lib-dynload',
 '/workspace/.pip-modules/lib/python3.8/site-packages',
 '/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/site-packages']
Server time:    Wed, 28 Dec 2022 22:49:08 +0000
```
The other projects work fine. In Admin,  have checked:
- that all projects have unique slugs. 
- that there are no duplicate player_project records
- that there are not 2 Player_Project models

I changed the post() method in EditSeatingPosition() view to ensure that the player was defined by the seating position being edited:
```
sp_player = seating_position.player
        player_project = get_object_or_404(
            Player_Project,
            player=sp_player,
            project=project
            )
```
This issue was fixed by ensuring that PlayerProject objects were not confussed with SeatingPosition objects. Clear renaming of variables, and using utility functions to populate them helped to control the data flow.
## Known Issues
[Back to Top](#contents)

- Draft rotas are not hidden to section members and office managers.
- Office Manager cannot yet view rotas
- Jquery is not functionaly
- Toasts are not implemented.
- There is a small misalignment of the background colour in mobile view on the index.html page.


## Deployment
[Back to Top](#contents)

The project was deployed to Heroku in the initial stages of development in order to resolve early and fundamental deployment issues.
### Deployed Server: Heruko
Heroku was used to deploy the django project backend

### Cloud Database: ElephantSql
ElephantSql was used for data storage

### Cloud Static File Storage: Cloudinary
Cloudinary was used to serve static files to the Django project.
#### Deployment Process
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
### Final Deployment
The following additional steps were taken before final deployment
- The GitHub Repository was made public
- Django debug mode was set to FALSE
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

Grateful acknowledgment is given to the following:
- RSNO Interviewees:
    - Patrick Curlett
    - Ursula Heidecker-Allen
    - Robin Wilson
    - Sophie Lang
    - Claire Dunn
    - Rachel Lee
    - Margarida Castro
    - Emma Hunter
    - Matthias van de Swaagh
- RSNO Assistance:
    - Ewen McKay
    - Angela Moreland
    - Tammo Schuelke

Mentor: Martina Terlevic for her amazing guidance and encouragement
- Mentor: Dario Carrasquel for encouraging and focused support
- Particular thanks are offered to the Code Institute Tutors who patiently and most helpfully enabled me to make progress on the many occasions when I got stuck on an issue.

- Code Institute: for training materials, training environment and specific code
- Very Academy: Django ORM | Case Study 1 https://www.youtube.com/watch?v=ycw8ZsT1ofw&t=1901s
- Niroj: https://www.edureka.co/community/73739/django-script-access-model-objects-without-using-manage-shell
- Stack Overflow https://stackoverflow.com/
- Django Documentation https://docs.djangoproject.com/en/3.2/ref/models/fields/

