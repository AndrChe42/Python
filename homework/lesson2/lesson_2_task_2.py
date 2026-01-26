def is_year_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


input_str = input("Введите год: ")
if not input_str.isdigit():
    print("Введено не число!")
else:
    year = int(input_str)
    result = is_year_leap(year)
    print(f"год {year}: {result}")
