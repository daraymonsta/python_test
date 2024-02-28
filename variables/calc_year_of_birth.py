import datetime

def calculate_hours_between_years(start_year, end_year):
    # Create datetime objects for the start of the start year and the start of the end year + 1
    start_date = datetime.datetime(start_year, 1, 1)
    end_date = datetime.datetime(end_year - 1, 1, 1)  # +1 to include the end year in the calculation

    # Calculate the difference between the two dates
    difference = end_date - start_date

    # Convert the difference to hours
    hours = difference.total_seconds() / 3600  # 3600 seconds in an hour

    return hours


name_str = input("What is your name? ")
age_int = int(input("What is your age? "))
had_birthday_this_year_str = input("Have you already had your birthday this year? ('yes' or 'no') ")
current_year_int = datetime.date.today().year
if had_birthday_this_year_str == 'yes':
    year_born_int = current_year_int - age_int
else:
    # if 'no', take off an extra year
    year_born_int = current_year_int - age_int - 1

print(f"OMG, {name_str} are {age_int} years old so you were born in {year_born_int}!")
hours_lived_float = age_int * 365.25 * 24
print(f"You have lived for approximately {hours_lived_float} hours.")
hours_lived_more_accurate = calculate_hours_between_years(year_born_int, current_year_int)
print(f"Total hours worked out by the 'time' library: {hours_lived_more_accurate}")
diff_between_calc_hours_methods = (hours_lived_more_accurate - hours_lived_float) / 24
print(f"Hours difference between the manual and time library methods: {diff_between_calc_hours_methods}")