def calculate_day_of_week(year, month, day):
    """
    Calculate the day of the week using Zeller's Congruence algorithm.
    
    Returns:
        0 = Saturday, 1 = Sunday, 2 = Monday, ..., 6 = Friday
    """
    if month < 3:
        month += 12
        year -= 1
    
    century = year // 100
    year_of_century = year % 100
    
    # Zeller's Congruence formula
    day_of_week = (day + (13 * (month + 1) // 5) + year_of_century + 
                  (year_of_century // 4) + (century // 4) + (5 * century)) % 7
    
    return day_of_week

def get_day_name(day_num):
    """Convert day number to day name"""
    days = ["Saturday", "Sunday", "Monday", "Tuesday", 
            "Wednesday", "Thursday", "Friday"]
    return days[day_num]

def main():
    print("Day of the Week Calculator")
    print("--------------------------")
    
    try:
        year = int(input("Enter year (e.g., 2023): "))
        month = int(input("Enter month (1-12): "))
        day = int(input("Enter day (1-31): "))
        
        if month < 1 or month > 12:
            print("Invalid month. Please enter a value between 1 and 12.")
            return
        if day < 1 or day > 31:
            print("Invalid day. Please enter a value between 1 and 31.")
            return
        
        day_num = calculate_day_of_week(year, month, day)
        day_name = get_day_name(day_num)
        
        print(f"\nThe day of the week for {month}/{day}/{year} is {day_name}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()