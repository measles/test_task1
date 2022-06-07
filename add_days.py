def days_till_the_next_month(month: int, day: int) -> int:
    long = (1,3,5,6,8,10,12)
    if month in long:
        days_in_month = 31
    else:
        day_in_month = 30 if month != 2 else 28
        
    return day_in_month - day 

# For the sake of simplicity I omit the case of a leap year in all other 
# meanings I treat a date as a date of Gregorian calendar
def add(date: str, number_of_days: int) -> int:
    date_int = [int(x) for x in date.split(".")]
    
    years_to_add = number_of_days // 365
    if years_to_add:
        date_int[-1] += years_to_add
        number_of_days = number_of_days % 365
    
    while number_of_days:
        till_next = days_till_the_next_month(date_int[2], date_int[3])
        if number_of_days > till_next:
            date_int[2] += 1
            date_int[3] = 1
            number_of_days -= till_next
        elif number_of_days == till_next:
            date_int[2] += 1
            date_int[3] = 1
            number_of_days = 0
        else:
            date_int[3] += number_of_days
            number_of_days = 0
            
if __name__ == "__main__":
    print(add("10.01.2008", 10)
    print(add("29.06.2020". 8)
