from applications import people, salary
from datetime import date
import dirty_main


if __name__ == '__main__':
    print(5*'-', 'main.py output', 5*'-')
    print(date.today())
    people.get_employees()
    salary.calculate_salary()
    print((len(' main.py output ')+10)*'-')

    dirty_main.run()