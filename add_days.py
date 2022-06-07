def days_till_the_next_month(month: int, day: int) -> int:
    long = (1,3,5,6,8,10,12)
    day_in_month = 0
    
    if month in long:
        days_in_month = 31
    else:
        days_in_month = 30 if month != 2 else 28
        
    return days_in_month - day 

# For the sake of simplicity I omit the case of a leap year in all other 
# meanings I treat a date as a date of Gregorian calendar
def add(date: str, number_of_days: int) -> int:
    date_int = [int(x) for x in date.split(".")]
    date_dict = {"day": date_int[0], "month": date_int[1], "year": date_int[2]}
    
    years_to_add = number_of_days // 365
    if years_to_add:
        date_dict["year"] += years_to_add
        number_of_days = number_of_days % 365
    
    while number_of_days:
        till_next = days_till_the_next_month(date_dict["month"], date_dict["day"])
        if number_of_days > till_next:
            date_dict["month"] += 1
            date_dict["day"] = 1
            number_of_days -= till_next
        elif number_of_days == till_next:
            date_dict["month"] += 1
            date_dict["day"] = 1
            number_of_days = 0
        else:
            date_dict["day"] += number_of_days
            number_of_days = 0
            
    return date_dict
            
if __name__ == "__main__":
    print(add("10.01.2008", 10))
    print(add("29.06.2020", 8))
