current_name = ""
current_vacation_dates = ""

def setup_profile(name, vacation_dates):
    global current_name, current_vacation_dates
    current_name = name
    current_vacation_dates = vacation_dates

def print_application_for_leave():
    print(f"Заявление на отпуск в период {current_vacation_dates}. {current_name}")

def print_holiday_money_claim(amount):
    print(f"Прошу выплатить {amount} отпускных денег. {current_name}")

def print_attorney_letter(to_whom):
    print(f"На время отпуска в период {current_vacation_dates} моим заместителем назначается {to_whom}. {current_name}")

setup_profile("Иван Петров", "1 июня – 20 июня")
print_application_for_leave()
print_application_for_leave()
print_holiday_money_claim("15 тысяч пиастров")
print_attorney_letter("Василий Васильев")

setup_profile("Мария Иванова", "5 июля – 20 июля")
print_application_for_leave()
print_holiday_money_claim("20 тысяч пиастров")
print_attorney_letter("Игорь Александров")