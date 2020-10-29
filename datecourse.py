from datetime import date

class Month(object):
    number = ""
    monthName = ""
    amountDays = 0
    nextMonth = ""

    def __init__(self, number, monthName, amountDays, nextMonth):
        self.number = number
        self.monthName = monthName
        self.amountDays = amountDays
        self.nextMonth = nextMonth

def ano_bissexto():
    ano = date.today().year
    if (ano%4==0 and ano%100!=0) or (ano%400==0):
        return True
    else:
        return False

MONTHS = [
    Month("01", "janeiro", 31, "fevereiro"),
    Month("02", "fevereiro", 29, "março") if ano_bissexto() else Month("02", "fevereiro", 28, "março"),
    Month("03", "março", 31, "abril"),
    Month("04", "abril", 30, "maio"),
    Month("05", "maio", 31, "junho"),
    Month("06", "junho", 30, "julho"),
    Month("07", "julho", 31, "agosto"),
    Month("08", "agosto", 31, "setembro"),
    Month("09", "setembro", 30, "outubro"),
    Month("10", "outubro", 31, "novembro"),
    Month("11", "novembro", 30, "dezembro"),
    Month("12", "dezembro", 31, "janeiro"),
]

def next_month(monthName):
    for month in MONTHS:
        if month.monthName == monthName:
            return month.nextMonth
    raise ValueError('Mês inválido.')

def amount_of_days(monthName):
    for month in MONTHS:
        if month.monthName == monthName:
            return month.amountDays
    raise ValueError('Mês inválido.')