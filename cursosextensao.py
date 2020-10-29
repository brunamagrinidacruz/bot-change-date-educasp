from dotenv import load_dotenv
load_dotenv()
from os import getenv

# https://selenium-python.readthedocs.io/waits.html
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SECONDS = 30 # Seconds to wait between change of page
SECONDS_VALIDATION = 8 # Seconds to wait when have a validation

configureDate = False

# Change the topic openning date
def topic_change(firefox, classText, open_day, open_month, INITIAL_YEAR, INITIAL_HOUR, INITIAL_MINUTE):

        if getenv("MODE") == "DEBUG":
            print("    Mostrando botão de ~Editar~")
        # Set the div with the options of 'Editar' to visible
        divEditOptions = firefox.find_element_by_xpath("//li[contains(@aria-label, '" + classText + "')]//div[@role='menu']")
        firefox.execute_script("arguments[0].classList.add('show')", divEditOptions)

        if getenv("MODE") == "DEBUG":
            print("    Clicando no botão ~Editar tópico~")
        # Button of 'Editar tópico'
        buttonEditTopic = firefox.find_element_by_xpath("//li[contains(@aria-label, '" + classText + "')]//span[contains(text(), 'Editar tópico')]")
        buttonEditTopic.click()

        #################### Configure the restrictions ####################

        if getenv("MODE") == "DEBUG":
            print("    Fazendo aparecer ~Restringir acesso~")
        # Set the div with the options of 'Restringir acesso' to visible
        divResctrictOptions1 = WebDriverWait(firefox, SECONDS).until(EC.presence_of_element_located((By.XPATH, "//fieldset[@id='id_availabilityconditions']//div[contains(@id, 'yui')]"))) # firefox.find_element_by_xpath("//fieldset[@id='id_availabilityconditions']//div[contains(@id, 'yui')]")
        firefox.execute_script("arguments[0].style.display='block'", divResctrictOptions1)
        divResctrictOptions2 = firefox.find_element_by_xpath("//fieldset[@id='id_availabilityconditions']//div[@aria-live='polite']")
        firefox.execute_script("arguments[0].style.display='block'", divResctrictOptions2)

        if getenv("MODE") == "DEBUG":
            print("    Verificando se já possui restrições")
        # Verify if already has restrictions associate
        divExistResctrictAlready = firefox.find_element_by_xpath("//div[@class='availability-none']")
        thereIsRestrictions = divExistResctrictAlready.get_attribute("aria-hidden")

        # If should apply a open date and close date. If configureDate = false, the bot will disable all date configurations
        if(configureDate):
            def setting_date():
                #################### Selecting the date ####################
                if getenv("MODE") == "DEBUG":
                    print("    Selecionando a data de abertura")

                optionDay = firefox.find_element_by_xpath("//select[@name='x[day]']/option[text()='" + open_day + "']")
                optionDay.click()
                optionMonth = firefox.find_element_by_xpath("//select[@name='x[month]']/option[text()='" + open_month + "']")
                optionMonth.click()
                optionYear = firefox.find_element_by_xpath("//select[@name='x[year]']/option[text()='" + INITIAL_YEAR + "']")
                optionYear.click()
                optionHour = firefox.find_element_by_xpath("//select[@name='x[hour]']/option[text()='" + INITIAL_HOUR + "']")
                optionHour.click()
                optionMinute = firefox.find_element_by_xpath("//select[@name='x[minute]']/option[text()='" + INITIAL_MINUTE + "']")
                optionMinute.click()

            # If the classe already has a restrict associeated, should replace
            if(thereIsRestrictions == None): # It doesn't have any restriction attached 
                if getenv("MODE") == "DEBUG":
                    print("    Não há restrições associadas. Adicionando restrição")

                buttonNewRestriction = firefox.find_element_by_xpath("//button[contains(text(), 'Adicionar restrição')]")
                buttonNewRestriction.click()

                buttonDateRestriction = firefox.find_element_by_xpath("//button[contains(text(), 'Data')]")
                buttonDateRestriction.click()

                setting_date()
            else:
                setting_date()

        else: # If should desative the open and close date
            # If the classe already has a restrict associeated, should delete
            if(thereIsRestrictions == None): # It doesn't have any restriction attached 
                if getenv("MODE") == "DEBUG":
                    print("    Não há restrições associadas. Continuando...")
            else:
                buttonDeleteRestriction = firefox.find_element_by_xpath("//a[contains(@title, 'Excluir')]")
                buttonDeleteRestriction.click()
                if getenv("MODE") == "DEBUG":
                    print("    Deletando restrição.")

        if getenv("MODE") == "DEBUG":
            print("    Salvando e voltando ao curso")
            buttonSaveDate = firefox.find_element_by_xpath("//input[@value='Salvar mudanças']")
            buttonSaveDate.click()
            
def activity_change(firefox, classText, open_day, open_month, INITIAL_YEAR, INITIAL_HOUR, INITIAL_MINUTE, FINAL_DAY, FINAL_MONTH, FINAL_YEAR):
    
    # Set the div with the options of 'Editar' of activity to visible
    if getenv("MODE") == "DEBUG":
        print("    Tornando visivel o menu de ~Editar~")
    WebDriverWait(firefox, SECONDS).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@aria-label, '" + classText + "')]//div[@role='menu']")))
    divEditOptions = firefox.find_elements_by_xpath("//li[contains(@aria-label, '" + classText + "')]//div[@role='menu']")[3]
    firefox.execute_script("arguments[0].classList.add('show')", divEditOptions)

    if getenv("MODE") == "DEBUG":
        print("    Clicando na atividade")
    # Click in activity
    buttonActivity = firefox.find_element_by_xpath("//li[contains(@aria-label, '" + classText + "')]//span[contains(text(), 'Atividade')]")
    buttonActivity.click()

    if getenv("MODE") == "DEBUG":
        print("    Abrindo menu para editar atividade")
    # Open of menu
    WebDriverWait(firefox, SECONDS).until(EC.presence_of_element_located((By.XPATH, "//div[@role='menu']")))
    divEditOptionsInsideAcitivity = firefox.find_elements_by_xpath("//div[@role='menu']")[2]
    firefox.execute_script("arguments[0].classList.add('show')", divEditOptionsInsideAcitivity)

    if getenv("MODE") == "DEBUG":
        print("    Clicando em ~Editar configurações~")
    # Configuration page of activity
    buttonEditConfig = firefox.find_element_by_xpath("//a[contains(text(), 'Editar configurações')]")
    buttonEditConfig.click()

    try: # Activity (close questions)
        # Set the durations configurations visible
        divDuration = WebDriverWait(firefox, SECONDS_VALIDATION).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Duração')]/ancestor::legend/following-sibling::div"))) # firefox.find_element_by_xpath("//a[contains(text(), 'Duração')]/ancestor::legend/following-sibling::div")
        firefox.execute_script("arguments[0].style.display='block'", divDuration)

        if getenv("MODE") == "DEBUG":
            print("    É questão fechada")

        # If should apply a open date and close date. If configureDate = false, the bot will disable all date configurations
        if(configureDate):
            if getenv("MODE") == "DEBUG":
                print("    Habilitando data de abertura")
            # Enable opening date
            checkboxTimeOpen = firefox.find_element_by_id("id_timeopen_enabled")
            if not(checkboxTimeOpen.is_selected()):
                checkboxTimeOpen.click()

            if getenv("MODE") == "DEBUG":
                print("    Habilitando data de fechamento")
            # Enable deadline
            checkboxTimeClosed = firefox.find_element_by_id("id_timeclose_enabled")
            if not(checkboxTimeClosed.is_selected()):
                checkboxTimeClosed.click()

            if getenv("MODE") == "DEBUG":
                print("    Selecionando a data inicial")
            #################### Selecting the initial date ####################
            optionInitialDay = firefox.find_element_by_xpath("//select[@id='id_timeopen_day']/option[text()='" + open_day + "']")
            optionInitialDay.click()
            optionInitialMonth = firefox.find_element_by_xpath("//select[@id='id_timeopen_month']/option[text()='" + open_month + "']")
            optionInitialMonth.click()
            optionInitialYear = firefox.find_element_by_xpath("//select[@id='id_timeopen_year']/option[text()='" + INITIAL_YEAR + "']")
            optionInitialYear.click()
            optionInitialHour = firefox.find_element_by_xpath("//select[@id='id_timeopen_hour']/option[text()='" + INITIAL_HOUR + "']")
            optionInitialHour.click()
            optionInitialMinute = firefox.find_element_by_xpath("//select[@id='id_timeopen_minute']/option[text()='" + INITIAL_MINUTE + "']")
            optionInitialMinute.click()

            if getenv("MODE") == "DEBUG":
                print("    Selecionando a data final")
            #################### Selecting the deadline ####################
            optionFinalDay = firefox.find_element_by_xpath("//select[@id='id_timeclose_day']/option[text()='" + FINAL_DAY + "']")
            optionFinalDay.click()
            optionFinalMonth = firefox.find_element_by_xpath("//select[@id='id_timeclose_month']/option[text()='" + FINAL_MONTH + "']")
            optionFinalMonth.click()
            optionFinalYear = firefox.find_element_by_xpath("//select[@id='id_timeclose_year']/option[text()='" + FINAL_YEAR + "']")
            optionFinalYear.click()
            optionFinalHour = firefox.find_element_by_xpath("//select[@id='id_timeclose_hour']/option[text()='" + "23" + "']")
            optionFinalHour.click()
            optionFinalMinute = firefox.find_element_by_xpath("//select[@id='id_timeclose_minute']/option[text()='" + "59" + "']")
            optionFinalMinute.click()
        
        else:
            if getenv("MODE") == "DEBUG":
                print("    Desabilitando data de abertura")
            # Disable opening date
            checkboxTimeOpen = firefox.find_element_by_id("id_timeopen_enabled")
            if checkboxTimeOpen.is_selected():
                checkboxTimeOpen.click()

            if getenv("MODE") == "DEBUG":
                print("    Desabilitando data de fechamento")
            # Disable deadline
            checkboxTimeClosed = firefox.find_element_by_id("id_timeclose_enabled")
            if checkboxTimeClosed.is_selected():
                checkboxTimeClosed.click()
        
    except: # Questions (open questions)
        if getenv("MODE") == "DEBUG":
            print("    É questão aberta")

        if getenv("MODE") == "DEBUG":
            print("    Habilitando menu de ~Disponibilidade~")
         # Set the avabality configurations visible
        divDuration = WebDriverWait(firefox, SECONDS).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Disponibilidade')]/ancestor::legend/following-sibling::div"))) # firefox.find_element_by_xpath("//a[contains(text(), 'Disponibilidade')]/ancestor::legend/following-sibling::div")
        firefox.execute_script("arguments[0].style.display='block'", divDuration)

        # If should apply a open date and close date. If configureDate = false, the bot will disable all date configurations
        if(configureDate):
            if getenv("MODE") == "DEBUG":
                print("    Habilitando data de abertura")
            # Enable opening date
            checkboxTimeOpen = firefox.find_element_by_id("id_allowsubmissionsfromdate_enabled")
            if not(checkboxTimeOpen.is_selected()):
                checkboxTimeOpen.click()

            if getenv("MODE") == "DEBUG":
                print("    Habilitando data de fechamento")
            # Enable deadline
            checkboxTimeClosed = firefox.find_element_by_id("id_duedate_enabled")
            if not(checkboxTimeClosed.is_selected()):
                checkboxTimeClosed.click()

            if getenv("MODE") == "DEBUG":
                print("    Desabilitando data final")
            # Disable the date of final deadline
            checkboxTimeClosed = firefox.find_element_by_id("id_cutoffdate_enabled")
            if checkboxTimeClosed.is_selected():
                checkboxTimeClosed.click()

            if getenv("MODE") == "DEBUG":
                print("    Desabilitando notificação")
            # Disable notification
            checkboxTimeClosed = firefox.find_element_by_id("id_gradingduedate_enabled")
            if checkboxTimeClosed.is_selected():
                checkboxTimeClosed.click()

            if getenv("MODE") == "DEBUG":
                print("    Selecionando a data inicial")
            #################### Selecting the initial date ####################
            optionInitialDay = firefox.find_element_by_xpath("//select[@id='id_allowsubmissionsfromdate_day']/option[text()='" + open_day + "']")
            optionInitialDay.click()
            optionInitialMonth = firefox.find_element_by_xpath("//select[@id='id_allowsubmissionsfromdate_month']/option[text()='" + open_month + "']")
            optionInitialMonth.click()
            optionInitialYear = firefox.find_element_by_xpath("//select[@id='id_allowsubmissionsfromdate_year']/option[text()='" + INITIAL_YEAR + "']")
            optionInitialYear.click()
            optionInitialHour = firefox.find_element_by_xpath("//select[@id='id_allowsubmissionsfromdate_hour']/option[text()='" + INITIAL_HOUR + "']")
            optionInitialHour.click()
            optionInitialMinute = firefox.find_element_by_xpath("//select[@id='id_allowsubmissionsfromdate_minute']/option[text()='" + INITIAL_MINUTE + "']")
            optionInitialMinute.click()

            if getenv("MODE") == "DEBUG":
                print("    Selecionando a data final")
            #################### Selecting the deadline ####################
            optionFinalDay = firefox.find_element_by_xpath("//select[@id='id_duedate_day']/option[text()='" + FINAL_DAY + "']")
            optionFinalDay.click()
            optionFinalMonth = firefox.find_element_by_xpath("//select[@id='id_duedate_month']/option[text()='" + FINAL_MONTH + "']")
            optionFinalMonth.click()
            optionFinalYear = firefox.find_element_by_xpath("//select[@id='id_duedate_year']/option[text()='" + FINAL_YEAR + "']")
            optionFinalYear.click()
            optionFinalHour = firefox.find_element_by_xpath("//select[@id='id_duedate_hour']/option[text()='" + "23" + "']")
            optionFinalHour.click()
            optionFinalMinute = firefox.find_element_by_xpath("//select[@id='id_duedate_minute']/option[text()='" + "59" + "']")
            optionFinalMinute.click()

        else:
            if getenv("MODE") == "DEBUG":
                print("    Desabilitando data de abertura")
            # Disable opening date
            checkboxTimeOpen = firefox.find_element_by_id("id_allowsubmissionsfromdate_enabled")
            if checkboxTimeOpen.is_selected():
                checkboxTimeOpen.click()

            if getenv("MODE") == "DEBUG":
                print("    Desabilitando data de fechamento")
            # Disable deadline
            checkboxTimeClosed = firefox.find_element_by_id("id_duedate_enabled")
            if checkboxTimeClosed.is_selected():
                checkboxTimeClosed.click()

            if getenv("MODE") == "DEBUG":
                print("    Desabilitando data final")
            # Disable the date of final deadline
            checkboxTimeClosed = firefox.find_element_by_id("id_cutoffdate_enabled")
            if checkboxTimeClosed.is_selected():
                checkboxTimeClosed.click()

    if getenv("MODE") == "DEBUG":
        print("    Salvando e voltando ao curso")
    buttonSaveDate = firefox.find_element_by_xpath("//input[@value='Salvar e voltar ao curso']")
    buttonSaveDate.click()

def execute(firefox, course_id, INITIAL_DAY, INITIAL_MONTH, AMOUNT_DAYS_OF_MONTH, SECOND_MONTH, INITIAL_YEAR, INITIAL_HOUR, INITIAL_MINUTE, FINAL_DAY, FINAL_MONTH, FINAL_YEAR):
    firefox.get("https://cursosextensao.usp.br/")

    if getenv("MODE") == "DEBUG":
            print(" Acessando o curso")
    # Accessing a course
    buttonCourse = WebDriverWait(firefox, SECONDS).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@onclick, '" + str(course_id) + "')]"))) # firefox.find_element_by_xpath("//button[contains(@onclick, '" + str(course_id) + "')]")
    buttonCourse.click()

    try:
        if getenv("MODE") == "DEBUG":
            print("    Ativando edição")
        # Enable edition
        buttonEnableEdition = WebDriverWait(firefox, SECONDS_VALIDATION).until(EC.presence_of_element_located((By.XPATH, "//input[@value='Ativar edição']"))) # firefox.find_element_by_xpath("//input[@value='Ativar edição']")
        buttonEnableEdition.click()
    except: # Okay if the edit is enable
        if getenv("MODE") == "DEBUG":
            print("    A edição já está habilitada")
        pass

    week = -1 # Represents the week of the classes (topics). It will be used to generate the right day (add 7 days for week)
    isBetweenTwoMonths = False # Represents if the days of classes will be split in two differents months
    for classNumber in range(16): # Interact between the 16 classes
        #################### Generating the class ####################

        classText = "Aula "
        if classNumber < 9:
            classText += "0" + str(classNumber + 1) 
        else:
            classText += str(classNumber + 1) 

        #################### Calcute the date ####################

        if classNumber%4 == 0: # We are in classes: 0, 4, 8 or 12. This classes are the begging of a new week
            week += 1

        # Define the date
        open_day = ""
        open_month = INITIAL_MONTH

        day = int(INITIAL_DAY) + (week*7) # The day. This value is bigger than 31

        # If the day calculated is equal or bigger than the amonunt of days of the month, it indicates that the classes will happen between two months
        if not(isBetweenTwoMonths) and day >= AMOUNT_DAYS_OF_MONTH:
            isBetweenTwoMonths = True 

        # If the INITIAL_DAY 22 and the AMOUNT_DAYS_OF_MONTH = 29
        # The day in week = 0 will be 22: 22 != 29 (day != AMOUNT_DAYS_OF_MONTH) so open day will be 22 % 29 = 22 (day % AMOUNT_DAYS_OF_MONTH)
        # The day in week = 1 will be 29: 29 == 29 (day == AMOUNT_DAYS_OF_MONTH) so open day will be 29
        # The day in week = 2 will be 36: 36 != 29 (day != AMOUNT_DAYS_OF_MONTH) so open day will be 36 % 29 = 7 (day % AMOUNT_DAYS_OF_MONTH)
        # The day in week = 3 will be 43: 43 != 29 (day != AMOUNT_DAYS_OF_MONTH) so open day will be 43 % 29 = 14 (day % AMOUNT_DAYS_OF_MONTH)
        if day == AMOUNT_DAYS_OF_MONTH:
            open_day = str(day)
        else:
            if(isBetweenTwoMonths): # Select next month
                open_month = SECOND_MONTH
            open_day = str(day % AMOUNT_DAYS_OF_MONTH)
        
        if getenv("MODE") == "DEBUG":
            print("  " + classText)
            print("    Dia de abertura: " + open_day + "/" + open_month + "/" + INITIAL_YEAR)
            print("    Hora de abertura: " + INITIAL_HOUR + ":" + INITIAL_MINUTE)
            print("    Dia de fechamento: " + FINAL_DAY + "/" + FINAL_MONTH + "/" + FINAL_YEAR)
            
        if getenv("MODE") == "DEBUG":
            print("   Arrumando tópico")
        topic_change(firefox, classText, open_day, open_month, INITIAL_YEAR, INITIAL_HOUR, INITIAL_MINUTE)

        if getenv("MODE") == "DEBUG":
            print("   Arrumando atividade")
        activity_change(firefox, classText, open_day, open_month, INITIAL_YEAR, INITIAL_HOUR, INITIAL_MINUTE, FINAL_DAY, FINAL_MONTH, FINAL_YEAR)