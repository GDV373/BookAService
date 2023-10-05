# BookAService

BookAService is a website designed for business and customers to register. While Business can share there available services and customers can book services that they need.

Unregistered users can view the index, about and contact pages to learn about the service. Users can sign up for the site from the registration form, and instantly be able to book or create there services.

Registered businesses can approve or cancel orders sent in the dashboard. Settings can be changed if need be and they can also add or remove services as needed.

Registered customers can book orders and also add special notes. Settings can be changed if need be. They also have to register their car details while logged in so the businesses can also confirm that they can work on that vehicle
It up to the business to call the customer to approve his booking and change the status of the job.


The live site can be found here: [BookAService](https://bookaservice-32a4c779d8fe.herokuapp.com/)

# Table of Contents
- [User Experience]()
- [Features]()
  - [General]()
  - [VetProfiles]()
  - [Records]()
- [Design]()
- [Technologies Used]()
- [Testing](TESTING.md)
- [Deployment]()
- [Credits]()

# User Experience

### User Stories

The user stories used as part of the planning for the website have been consolidated here.

- As an unregistered user I can view the website home, about and contact pages
- As an unregistered user I can register to be either as a business or a customer
- As a customer user I can change my settings of my account and delete it while logged in
- As a customer user I can register,remove and change details of any car while logged in
- As a customer user I can book from the dashboard page with any registered business while logged in
- As a customer user I can view the status in the dashboard of all bookings while logged in
- As a customer user I can log out of the account any time while logged in
- As a business user I can change my settings of my account and delete it while logged in
- As a business user I can change my services, update or delete them while logged in
- As a business user I can view all requests from the dashboard and change the actons as needed it while logged in
- As a business user I can view all completed requests from the dashboard while logged in
- As a business user I can log out of the account any time while logged in


# Features
## General
### Navigation Bar

<details>
<summary>Navbar</summary>

![Navbar]()
</details>

The navigation bar is featured across all pages.

For unregistered or logged-out users of the site, the navbar displays links to "Log in / Register", "About" and "Contact", with the "Log in / Register" link opening a new page when clicked on, listing the options of registration or login.There is also social media links, adress of website owner, opening hours and contact number.

For registered users of the site, the respective tabs show with the options needed to operate there account

The navbar is a free to use bootstrap5 from [themewagon.com](https://themewagon.com/themes/free-html5-bootstrap-5-business-website-template-carserv/)

### Footer

<details>
<summary>Footer</summary>

![Footer]()
</details>

The footer is featured across all pages.

The footer features a standard address information with social media links next to the opening hours. Then there are the services showing a few service what can be found and a newsletter that is currently on comming soon. At the bottom there are copyrights tags on the left and on the right there are the Home button FAQ`s and a button to go to the top of the page quickly.

### Home Page

<details>
<summary>Home Page Unregistered</summary>

![Home Page](readme-docs/images/HomePageNotLoggedIn.jpg)
</details>

<details>
<summary>Home Page Logged In as customer</summary>

![Home Page](readme-docs/images/HomePageLoggedInAsCustomer.jpg)
</details>

<details>
<summary>Home Page Logged In as business</summary>

![Home Page](readme-docs/images/HomePageLoggedInAsBusiness.jpg)
</details>

The Home page has three states depending on the user.

For all users, the home page displays a spinning services ad, "Log in / Register" in the top right section. While scrolling you can see the company’s achievements, then some of the company’s workers and finally a few reviews from users.

For logged in accounts the top nav bar will display new tabs to use the websites function. These will change with what type of user you are logged in as. User only have one login page the back end will automatically assign the correct tabs to that user to view.


### About Page

<details>
<summary>About Page</summary>

![About Page]()
</details>

The about page is available for users who are not registered or who are not logged in through a link in the navbar. 

The primary purpose is to act as marketing for the site for users who are learning about the site. The first section features a paragraph of text describing the site and it's worth to the user, and a list of "Benefits". The second section features more in depth descriptions about the benefits of the site and explains how the site's features meet those benefits.

On larger screens, the about page is displayed in rows with the contents displayed as alternating columns of text and promotional material. On smaller screens, page is displayed as alternating rows of text and promotional material. 

### Contact Page

<details>
<summary>Contact Page</summary>

![Contact Page]()
</details>

The contact page is available to all users through a link in the navbar for users who are not logged in or a link in the footer for those who are It features a simple form that requires the name, email and message from the user. It sends the message to the site owner and provides the user with feedback by displaying "Message sent."

## Vet Profiles

### Registration Page

<details>
<summary>Registration Page</summary>

![Registration]()
</details>

The registration page is accessible through a "Sign Up" link in the navbar or "Register" CTA button on the index page for users who are not logged in. The page features a simple form that requires the users "Email", "First Name", "Last Name", "Password" and "Confirm Password". 

If the user attempts to register while leaving any of the fields blank, they are prompted to fill in the missing field. If the user attempts to register with an email that is already registered, they are given a message that the email is already in use. If the user attempts to register without the passwords matching, they are given a message that the password fields don't match. 

When the user registers, they are logged in and redirected to the index page where they are informed their account is awaiting approval.

### Login Page

<details>
<summary>Login Page</summary>

![Login]()
</details>

The login page is accessible through a "Sign In" link in the navbar or "Login" CTA button on the index page for users who are not logged in. The page features a simple form that requires the user's "Email" and "Password". If the user attempts to submit an empty field, they are prompted to fill in the required field. If the user's credentials are invalid, they are given a message that their login is invalid.

When the user logs in, they are redirected to their profile if their account is active. If their account is not active, the user is redirected to the index page informing them that their account is awaiting approval.

### Profile

<details>
<summary>Profile</summary>

![Profile]()
</details>

The user profile page is available for users who are registered and whose account has been set to active by the admin. Each user can only view their own profile. The profile page features two sections.

The first section includes the heading "Profile for {user name}", where the user's first and last name are present to provide feedback to the user that they are viewing their own profile. Below the heading, the user's details are displayed: "Name", "Surname" and "Email Address". Below this, an "Edit Profile" button allows the user to edit their details. On large screens, "Go To:" with links to "Animal Records" and "Available Drugs" is displayed on the right of the screen next to the user's details. On smaller screens, the links are present below the "Edit Profile" button.

The second section features the user's "Prescription History" which displays the list of their prescriptions. Below the "Prescription History" heading, there is a line of text that explains to the user the restrictions on editing and deleting prescriptions. Below this, the prescriptions are presented in a table ordered by date, starting with the most recent. 

On larger screens, the table includes the details "Animal", "Dose", "Drug", "Date" and "View". On smaller screens, the details on the table include "Animal", "Date" and "View". "Animal" is the animal's full name, "Dose" is the dosage of the drug that was administered, "Drug" is the drug's name, "Date" is the date the prescription was created and "View" is a link to the full details of the prescription. The details provided in the table are intended to provide just enough context so that user can find previous prescriptions. They can then click "View" to review the prescription in more details.

### Edit Profile

<details>
<summary>Edit Profile</summary>

![Edit Profile]()
</details>

The edit profile button on the user's profile navigates to the "Edit Profile" form which is prepopulated with the current user's details. The user is able to change their email, name and surname through this form. All fields are required and the user is prompted to fill an empty field if they attempt to submit the form with empty fields. 

The user is able to change their email, but only to another email which is not currently registered on the site. They will receive a message that the email is already in use if they attempt to do so and the form will reset to their
current details.


# Design

The concept for PetRx was a professional site for veterinarians to prescribe medication for their patients. As such, the aim of the design was a clean, easy to use site where information was clearly displayed and easy to understand.


## CRUD Functionality

While trying to stay as true to life as possible, regular registered users have the ability to create, view, edit and delete prescriptions for animals. In real life, these types of records are protected and, once administered, a vet would not be allowed to alter or delete an existing prescription as it is an important part of an animal's medical history. As a middle ground, it was decided to provide users the ability to edit and delete prescriptions within a 24 hour window to provide CRUD functionality while maintaining an air of realism. As mentioned in "Future Features", this is something to be addressed in future iterations.


## Colour
![Colour Palette]()

A blue colour palette was used for this project based on the association of the colour with healthcare. The main background colour is a white with a hint of blue to give a clean appearance. The main font colour is almost black to aid readability. A secondary font colour of dark blue was used for text in the header and footer to keep with the style. Buttons and links are styled in lighter shades of blue to stand out and indicate interactivity.


## Typography

Fira Sans and Rubik were imported from Google Fonts. They were chosen for their readability and similarity, to create easily legible content that is pleasant to read without being distracting.


## Wireframes

Wireframes were created in Balsamiq. They were used for initial planning of template layouts.

<details>
<summary>Index Wireframe</summary>

![Index Wireframe](readme-docs/wireframe/index-wf.webp)
</details>

<details>
<summary>About Wireframe</summary>

![About Wireframe](readme-docs/wireframe/about-wf.webp)
</details>

<details>
<summary>Contact Wireframe</summary>

![Contact Wireframe](readme-docs/wireframe/contact-wf.webp)
</details>

<details>
<summary>Register Wireframe</summary>

![Register Wireframe](readme-docs/wireframe/register-wf.webp)
</details>

<details>
<summary>Login Wireframe</summary>

![Login Wireframe](readme-docs/wireframe/signin-wf.webp)
</details>

<details>
<summary>Vet Profile Wireframe</summary>

![Vet Profile Wireframe](readme-docs/wireframe/user-profile-wf.webp)
</details>

<details>
<summary>Records Wireframe</summary>

![Records Wireframe](readme-docs/wireframe/records-wf.webp)
</details>

<details>
<summary>Animal Record Wireframe</summary>

![Animal Record Wireframe](readme-docs/wireframe/animal-profile-wf.webp)
</details>

<details>
<summary>Prescribe Wireframe</summary>

![Prescribe Wireframe](readme-docs/wireframe/prescribe-wf.webp)
</details>


## Agile Methodology

[GitHub Projects Page](https://github.com/users/SJECollins/projects/3/views/1)

GitHub Projects was used in part for the planning of this website to create and track User Stories as they were implemented and fulfilled. One week was spent on project planning, including the first mentor meeting where we planned the project timeline. The initial "sprint" took three weeks, culminating in the second mentor meeting where we reviewed the project and discussed fixes and improvements. Then another roughly three weeks on implementing further features, testing, fixes, documentation, and the final mentor meeting for the project.


## Entity Relationship Diagram

The below Entity Relationship Diagram was created on [diagrams.net](https://www.diagrams.net/). It illustrates the relationships between the 5 models present in the project: Vet, Record, Category, Drug and Prescription.

<details>
<summary>ERD</summary>

![ERD](readme-docs/petrx-erd.webp)
</details>


# Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5): mark-up language.
- [CSS3](https://en.wikipedia.org/wiki/CSS): styling.
- [JavaScript](https://www.javascript.com/): programming language.
- [Python 3](https://www.python.org/): programming language.
- [Django 3.2](https://www.djangoproject.com/)
  - [Django Crispy Forms](https://pypi.org/project/django-crispy-forms/): for forms.
  - [Crispy Bootstrap5](https://pypi.org/project/crispy-bootstrap5/): bootstrap5 template pack for crispy forms.
  - [Django Forms Dynamic](https://github.com/dabapps/django-forms-dynamic): for the dynamic form using HTMX.
  - [Django Widget Tweaks](https://pypi.org/project/django-widget-tweaks/): for the dynamic form.
  - [Coverage](https://github.com/nedbat/coveragepy/tree/6.5.0): for measuring code coverage of Python tests.
- [HTMX](https://htmx.org/): UI.
- [Bootstrap](https://getbootstrap.com/): styling.
- [Cloudinary](https://cloudinary.com/): store static and media files.
- [GIT](https://git-scm.com/): for version control.
- [GitHub](https://github.com/): for host repository.
- [Gitpod](https://www.gitpod.io/): online IDE.
- [Heroku](https://)
- [Google Fonts](https://fonts.google.com/): to import fonts.
- [Font Awesome](https://fontawesome.com/): to import icons.
- [Balsamiq](https://balsamiq.com/): to create wireframes.
- [Diagrams.net](https://www.diagrams.net/): for Entity Relationship Diagram.
- [GIMP](https://www.gimp.org/): to edit images and create colour palette.
- [Inkscape](https://inkscape.org/): to create the logo.

# Testing

Testing for the site can be found at the below link:

[Link to TESTING.md](TESTING.md)


# Deployment
## Steps to deploy site using Heroku:
- Assuming gunicorn, dj_database_url, psycopg2 and dj3-cloudinary-storage have been installed
- On the Heroku dashboard, select "New" and click "Create new app"
  - Create a unique app name - this will be added to allowed hosts in the project settings
  - Select your region
  - Click "Create app"
- Go to the Resources tab:
  - Search for "postgres" in the add-ons search bar and select "Heroku Postgres"
  - Click "Submit Order Form"
- Go to the settings tab:
  - Scroll down to the config vars section and select "Reveal Config Vars"
  - DATABASE_URL will be set after adding Heroku Postgres - this will be copied to the project
  - Add a new config var for SECRET_KEY - create your own or use a django secret key generator
  - Add a new config var for CLOUDINARY_URL - copy the "API Environment variable" from your cloudinary dashboard, remove "CLOUDINARY_URL="
  - Add a new config var for DISABLE_COLLECTSTATIC, with the value 1 - this will be removed before deployment
- In your project, for your environment variables:
  - Create a new env.py file in the top level directory
  - In env.py:
    - Import os
    - Add 'os.environ["DATABASE_URL"] = "Paste the DATABASE_URL from the Heroku app here"'
    - Add 'os.environ["SECRET_KEY"] = "Paste your new secret key here"'
    - Add 'os.environ["CLOUDINARY_URL"] = "Paste your CLOUDINARY_URL as in the Heroku app here"'
  ```
  import os

  os.environ['DATABASE_URL'] = 'postgres://exampledatabaseurl'
  os.environ['SECRET_KEY'] = 'examplesecretkey'
  os.environ['CLOUDINARY_URL'] = 'cloudinary://examplecloudinaryurl'
  ```
  - If not already present, create a .gitignore file and add env.py to it

- In your project, in settings.py:
  - Import os
  - Import dj_database_url
  - if os.path.isfile('env.py'):
	import env
  ```
  import os
  import dj_database_url
  if os.path.isfile('env.py'):
      import env
  ```
  - Replace the insecure secret key with "SECRET_KEY = os.environ.get('SECRET_KEY')"
  ```
  SECRET_KEY = os.environ.get('SECRET_KEY')
  ```
  - Link new database by commenting out old DATABASES section and adding:
	DATABASES = {
			'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
			}
  ```
  DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
  ```
  - Add Heroku to the allowed hosts: "ALLOWED_HOSTS = ['the_app_name_from_heroku.herokuapp.com']
  ```
  ALLOWED_HOSTS = ['example-heroku-app-name.herokuapp.com', 'localhost']
  ```
  - Add 'cloudinary_storage' (above 'django.contrib.staticfiles') and 'cloudinary' (below) to INSTALLED_APPS
  ```
  ...
  'cloudinary_storage',
  'django.contrib.staticfiles',
  'cloudinary',
  ...
  ```
  - Setup Cloudinary to store static and media files
  ```
    STATIC_URL = '/static/'
	STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
	STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
	STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

	MEDIA_URL = '/media/'
	DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
  ```
  - Run 'python3 manage.py collectstatic' to collect static files
- In your project:
  - Create a Procfile in the top level directory and add 'web: gunicorn project_name.wsgi' to tell 
  ```
  web: gunicorn project_name.wsgi
  ```
  - Create a requirements file with 'pip3 freeze --local > requirements.txt' for Heroku to install required packages
  ```
  pip3 freeze --local > requirements.txt
  ```
  - Make migrations with 'python3 manage.py migrate'
  ```
  python3 manage.py migrate
  ```
  - Commit and push to GitHub
- Prior to final deployment:
  - Set DEBUG = False in project settings.py
  - Remove DISABLE_COLLECTSTATIC config var from Heroku
- Go to the Deploy tab:
  - Select GitHub and confirm connection to GitHub account
  - Search for the repository and click "Connect"
  - Scroll down to the deploy options
  - Select automatic deploys if you would like automatic deployment with each new push to the GitHub repository
  - In manual deploy, select which branch to deploy and click "Deploy Branch"
  - Heroku will start building the app
- The link to the app can be found at the top of the page by clicking "Open app"

The live site can be found here: [PetRx](https://ci-pp4-petrx.herokuapp.com/)


## Steps to clone site:
- In the GitHub repository, click the "Code" button.
- Select "HTTPS" and copy the URL.
- Open Git Bash and navigate to the repository where you would like to locate the cloned repository.
- Type "git clone" followed by the copied URL.
- Press enter to create the clone.
- Install required packages with the command "pip3 install -r requirements.txt"

# Credits
## Code
- The code for the custom user model allowing registering with email based on tutorial by [Coding With Mitch](https://www.youtube.com/watch?v=eCeRC7E8Z7Y&ab_channel=CodingWithMitch)
- The code for testing custom user models is based on this tutorial by [Michael Herman on testdriven.io](https://testdriven.io/blog/django-custom-user-model/)
- The code for pagination is from the [Official Django Documentation](https://docs.djangoproject.com/en/4.1/topics/pagination/)
- The code for search is based on this tutorial by [Codemy.com](https://www.youtube.com/watch?v=AGtae4L5BbI&ab_channel=Codemy.com)
- The code for chained dropdown in the prescription form is from this tutorial by [BugBytes](https://www.youtube.com/watch?v=uU1uLYaNr9U&ab_channel=BugBytes)
- The code for using htmx to display prescription lists and modals is based on this tutorial by [Benoit Blanchon](https://www.youtube.com/watch?v=3dyQigrEj8A&ab_channel=BenoitBlanchon)
- The code for custom error handlers is based on this tutorial by [Cryce Truly](https://www.youtube.com/watch?v=3SKjPppM_DU&ab_channel=CryceTruly)

## Media
- The logo was created in Inkscape
- Icons are from [Font Awesome](https://fontawesome.com)
- The  fonts are imported from [Google Fonts](https://fonts.google.com)

- Images from [Pexels](https://pexels.com):
  - [Black cat](https://www.pexels.com/photo/black-cat-holding-persons-arm-1049764/) by Ruca Souza
  - [Cat paw](https://www.pexels.com/photo/orange-cat-foot-on-laptop-keyboard-1440387/) by Александар Цветановић
- Images from [Unsplash](https://unsplash.com):
  - [Collie at desktop](https://unsplash.com/photos/zWOQD6fFCBs) by Pavel Herceg
  - [Safe cat](https://unsplash.com/photos/A7nK49HCqSI) by Aleksandar Cvetanovic
  - [Pom at tablet](https://unsplash.com/photos/gySMaocSdqs) by Cookie the Pom

## Acknowledgement
I'd like to thank my mentor, Brian Macharia, for providing very good advice, tips and feedback, as well as excellent resources that aided greatly in organising and implementing this project.