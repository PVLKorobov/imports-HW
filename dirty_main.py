from applications.people import *
from applications.salary import *
from datetime import date

def run():
    print(5*'-', 'dirty_main.py output', 5*'-')
    print(date.today())
    get_employees()
    calculate_salary()
    print((len(' dirty_main.py output ')+10)*'-')