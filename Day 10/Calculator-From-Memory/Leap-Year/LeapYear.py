def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
year = int(input("Which year do you want to check? "))
is_leap = is_leap_year(year)
if is_leap:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
