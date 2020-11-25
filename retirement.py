from datetime import date


# Ask the user for a birth year and month
# displays the age (with additional months) for obtaining full SSA benefits
# displays the year and month for obtaining full SSA benefits

retirement_dic = {
    1937: "65",
    1938: "65 and 2 months",
    1939: "65 and 4 months",
    1940: "65 and 6 months",
    1941: "65 and 8 months",
    1942: "65 and 10 months",
    1943: "66",
    1955: "66 and 2 months",
    1956: "66 and 4 months",
    1957: "66 and 6 months",
    1958: "66 and 8 months",
    1959: "66 and 10 months",
    1960: "67"
}


# Verify input values
def get_year_input(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print('Please enter a valid number')
            continue
        if value == 1:
            exit()
        if value < 1900 and value > 2020:
            print('Please enter a year between 1900 and 2020')
            continue
        else:
            break
    return value


def get_month_input(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print('Please enter a valid number')
            continue
        if value < 1 and value > 12:
            print('Please enter a valid month')
            continue
        else:
            break
    return value


def calculate_retirement_age(year):
    if year <= 1937:
        return retirement_dic[1937]
    elif year >= 1943 and year <= 1954:
        return retirement_dic[1943]
    elif year >= 1960:
        return retirement_dic[1960]
    else:
        return retirement_dic[year]


def calculate_retirement_month(year, month):
    today = date.today()

    age = today.year - year - ((today.month) < month)

    retirement_age = calculate_retirement_age(year).split(" ")

    if len(retirement_age) > 1:
        person_age = int(retirement_age[0])
        person_month = int(retirement_age[2])
    else:
        person_age = int(retirement_age[0])
        person_month = month + 1

    retirement_year = str(((age - person_age) - today.year) * -1)

    retirement_month = date(1990, person_month -1, 1).strftime('%B')

    message = 'This will be in ' + retirement_month + ' of ' + retirement_year

    return message


def main():
    print("Welcome to the Social Security Retirement Age Calculator\n")

    year = get_year_input('Enter the year of birth or 1 to exit: ')
    month = get_month_input('Enter the month of birth: ')

    retirement_age = calculate_retirement_age(year)
    print('Your full retirement age is ' + retirement_age)

    retirement_month = calculate_retirement_month(year, month)
    print(retirement_month)


main()
