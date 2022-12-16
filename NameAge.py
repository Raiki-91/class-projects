from datetime import date

def year_from_date():
    now = date.today()  # current date and time
    year = now.strftime("%Y")  # year from current date time
    return int(year)
def how_old():

    return age


name = str(input("What is your name? "))
age = int(input("How old are you?"))
year= year_from_date() - age
print('Hello', name + "!", 'You were born in', str(year) + '.')
