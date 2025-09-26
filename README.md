# django-quiz-app
It is django based quiz app for multiple choice questions.

This is an online quiz organizing website project, developed using Python's web framework Django.<br>
For front-end designing I have used Twitter's front-end library Bootstrap4.


### Snaps of project 
  Login:
  ![alt text](https://github.com/sswapnil2/django-quiz-app/blob/master/screenshots/login.png "login page")
  <br>
  
  quiz:
  ![alt text](https://github.com/sswapnil2/django-quiz-app/blob/master/screenshots/quiz_page.png  "quiz page")
  <br>
  
  results:
  ![alt text](https://github.com/sswapnil2/django-quiz-app/blob/master/screenshots/results.png "results")
  <br>


### Features of the quiz:

- All questions are multiple choice question.
- Each question is displayed only once per user.
- Questions are displayed randomly for every user.
- If the user by-mistake presses refresh or go back to the previous page, there will be a new question for the user and the
  question he/she was on will be marked as attempted.
- A message will be displayed after every attempted question whether the answer was correct or incorrect.

### Leaderboard features:

- Leaderboard is a shorted list according to the score obtained by the users.
- If two users are having same score, the user who has signed up earlier will have good ranking than the one who joined late.




## Getting started with development

Dependencies:

- Python 3.11.6
- Django 5.0.3
- Ubuntu 17.04 or later or Linux Mint 18.2 or later


# Instructions 

1) ### Installing dependencies 
  It will install all required dependies in the project.<br>
  `pip install -r requirements.txt`
  
2) ### Migrations 
  To run migrations. <br>
  `python manage.py makemigrations`<br>
  `python manage.py migrate`
  
3) ### Create superuser
  To create super user run. <br>
  `python manage.py createsuperuser` <br>
  After running this command it will ask for username, password.
  You can access admin panel from `localhost:8000/admin/`

4) ### Running locally
  To run at localhost. It will run on port 8000 by default.<br>
  `python manage.py runserver` 
 
5) ### Reference
  I have refernced this quizz app from [tomwalker's](https://github.com/tomwalker) original repo. 
  Reference link to the quiz app repo is [here](https://github.com/tomwalker/django_quiz)
  
