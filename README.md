# Automation Moodle Bot

This application is a automation bot to change the configurations of Moodle topics and activites. 
It will navigate between the topics set the opening date and deadline, and it will navigate between the activites (question and tasks) and set the configurations.

**This applcation is used to a specific kind of Moodle and the login is configurated to be with USP emails @USP. If you are not part of EducaSP (or VemPraUSP), you have to change the way of login and maybe the access between pages.**

## Stack

- Python 3.8.3
- Selenium 3.141.0

There is a requirements.txt with the libraries. This file contains all requirements to execute the project. You will only need Python and Pip to use. To install the libraries:

```
pip install -r requirements.txt
```

You aslo need a `geckodriver` in the root of the repository. To download: https://github.com/mozilla/geckodriver/releases.

## Enviroment Variables
You need two variables to execute:
- MOODLE_EMAIL: The Moodle Email
- MOODLE_PASSWORD: The Moodle Password
