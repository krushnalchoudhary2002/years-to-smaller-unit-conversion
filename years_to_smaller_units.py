age = 75  

# Function to calculate life duration
def calculate_duration(age):
    # Years
    years = age
    months = years * 12
    weeks = years * 52.143
    days = years * 365.25
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    return {
        "Years": years,
        "Months": months,
        "Weeks": weeks,
        "Days": days,
        "Hours": hours,
        "Minutes": minutes,
        "Seconds": seconds
    }

duration = calculate_duration(age)

print("\nDuration of life:")
for unit, value in duration.items():
    print(f"{unit}: {value:,.2f}")
# Function to calculate life duration in different time units
def calculate_duration(age):
    months = age * 12  
    weeks = age * 52.143  
    days = age * 365.25  
    hours = days * 24  
    minutes = hours * 60  
    seconds = minutes * 60  

    return {
        "Months": months,
        "Weeks": weeks,
        "Days": days,
        "Hours": hours,
        "Minutes": minutes,
        "Seconds": seconds
    }

age = 75  

duration = calculate_duration(age)

print(f"Age: {age} years\n")
print("Duration of life in different time units:")
for unit, value in duration.items():
    print(f"{unit}: {value:,.2f}")
def calculate_duration(age, unit):
    if unit == "months":
        return age * 12  
    elif unit == "weeks":
        return age * 52.143  
    elif unit == "days":
        return age * 365.25  
    elif unit == "hours":
        return age * 365.25 * 24  
    elif unit == "minutes":
        return age * 365.25 * 24 * 60  
    elif unit == "seconds":
        return age * 365.25 * 24 * 60 * 60  
    else:
        return None  # Invalid selection

age = 75
unit = "months"  

result = calculate_duration(age, unit)

print(f"\nThe person lived for approximately {result:,.2f} {unit}.")

















