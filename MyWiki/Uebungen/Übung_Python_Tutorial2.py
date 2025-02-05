from datetime import datetime


today = datetime.now()


# Aufgabe 1
def aktuelles_datum_und_uhrzeit():
    print(today.strftime("Today is %d.%m.%Y und es ist %H:%M:%S"))


aktuelles_datum_und_uhrzeit()


# Aufgabe 2
def tage_bis_jahresende(keydate):
    year = keydate.year
    end_of_year = datetime(year, 12, 31)
    return (end_of_year - keydate).days


difference_in_days = tage_bis_jahresende(today)
print(f"Remainig days until the end of the year: {difference_in_days}")


# Aufgabe 3
def tage_bis_datum(keydate):
    return (keydate - today).days


user_date_str = input("Enter a date (DD.MM.YYYY): ")

user_date = datetime.strptime(user_date_str, "%d.%m.%Y")

remaining_days = tage_bis_datum(user_date)
print(f"Remainig days from now until user input:{remaining_days} days")


# Aufgabe 4
def wochentag_berechnen(input_date):
    return input_date.strftime("%A")


user_date_str = input("Enter a date (DD.MM.YYYY): ")

user_date = datetime.strptime(user_date_str, "%d.%m.%Y")


result_weekday = wochentag_berechnen(user_date)
print(f"The weekday of the input date is {result_weekday}")


# Aufgabe 4 mit deutschen Wochentagen

user_date_str = input("Enter a date (DD.MM.YYYY): ")

user_date = datetime.strptime(user_date_str, "%d.%m.%Y")

weekdays_german = [
    "Montag",
    "Dienstag",
    "Mittwoch",
    "Donnerstag",
    "Freitag",
    "Samstag",
    "Sonntag",
]

index_of_weekday = user_date.weekday()

weekday_ger_input_date = weekdays_german[index_of_weekday]
print(f"Mein Wochentag ist: {weekday_ger_input_date}")

# Getting the day name
