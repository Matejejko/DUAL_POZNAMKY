from datetime import datetime
while True:
    text = input('davaj: ')
    if text == 'time':
        # Current date and time
        current_datetime = datetime.now()
        print("Current date and time:", current_datetime)

        # Current year
        year = current_datetime.year
        print("Current year:", year)

        # Month of year
        month = current_datetime.month
        print("Month of year:", month)

        # Week number of the year
        week_number = current_datetime.strftime("%U")
        print("Week number of the year:", week_number)

        # Weekday of the week
        weekday = current_datetime.strftime("%A")
        print("Weekday of the week:", weekday)

        # Day of year
        day_of_year = current_datetime.strftime("%j")
        print("Day of year:", day_of_year)

        # Day of the month
        day_of_month = current_datetime.day
        print("Day of the month:", day_of_month)

        # Day of week
        day_of_week = current_datetime.weekday()  # Monday is 0 and Sunday is 6
        print("Day of week:", day_of_week)
    else:
        print(text)