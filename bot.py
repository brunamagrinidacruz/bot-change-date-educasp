from dotenv import load_dotenv
load_dotenv()
from os import getenv

from selenium import webdriver
from time import sleep
from cursosextensao import execute
from datecourse import next_month, amount_of_days

# 1765
COURSES_ID = [1797, 1798, 1799,  1800, 1801, 1802, 1803, 1804, 1805, 1880] # The id of the courses that will have the date changed

INITIAL_DAY = "03" # Day of initial opening of classes
INITIAL_MONTH = "agosto" # Month of initial opening of classes
INITIAL_YEAR = "2020" # Year of initialopening of classes. The year must be equal to all 16 classes
INITIAL_HOUR = "08" # Hour of initial opening of classes (with two decimal places)
INITIAL_MINUTE = "00" # Minute of initial opening of classes (with two decimal places)
FINAL_DAY = "7" # Day of deadline of activitys
FINAL_MONTH = "setembro" # Month of deadline of activitys
FINAL_YEAR = "2020" # Year of deadline of activitys

AMOUNT_DAYS_OF_MONTH = amount_of_days(INITIAL_MONTH) # The amount of days during the INITIAL_MONTH
SECOND_MONTH = next_month(INITIAL_MONTH) # If the classes will happen during two differents month, this is the second month

firefox = webdriver.Firefox(executable_path="./geckodriver")
firefox.get("https://cursosextensao.usp.br/auth/shibboleth")

inputName = firefox.find_element_by_id("username")
inputName.send_keys(getenv("MOODLE_EMAIL"))
inputPassword = firefox.find_element_by_id("password")
inputPassword.send_keys(getenv("MOODLE_PASSWORD"))

buttonLogin = firefox.find_element_by_name("_eventId_proceed")
buttonLogin.click()

sleep(5) # Waiting the login ok

print("O robô irá iniciar.")
print("Data de abertura do curso: " + INITIAL_DAY+" de "+INITIAL_MONTH+" de "+INITIAL_YEAR)
print("Data de fechamento do curso: " + FINAL_DAY+" de "+FINAL_MONTH+" de "+FINAL_YEAR)
print("Bruna Magrini.")
print("---------------------------------------------------------")
for course_id in COURSES_ID:
    print("Executando o curso: " + str(course_id))
    execute(firefox, course_id, INITIAL_DAY, INITIAL_MONTH, AMOUNT_DAYS_OF_MONTH, SECOND_MONTH, INITIAL_YEAR, INITIAL_HOUR, INITIAL_MINUTE, FINAL_DAY, FINAL_MONTH, FINAL_YEAR)



