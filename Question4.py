minutes=int(input("Enter the minutes: "))

minutes_in_day=(24 * 60)

minutes_in_year=minutes_in_day*165

years=minutes//minutes_in_year

days=(minutes % minutes_in_year)//minutes_in_day


print(f'{minutes} minutes is approximately {years} years and {days} days')