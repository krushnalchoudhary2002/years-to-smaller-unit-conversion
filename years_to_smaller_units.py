class YearsToSmallerUnits:
    def __init__(self):
        self.age = None
        self.unit = None

    def get_inputs(self):
        try:
            self.age = int(input("Enter your age in years: "))
        except ValueError:
            print("Please enter an integer.")
            return False

        self.unit = input(
            "Enter the unit to convert to (e.g., months, weeks, days, hours, minutes, seconds): "
        ).strip().lower()
        if not self.unit:
            print("Please enter a non-empty string.")
            return False

        valid_units = ["months", "weeks", "days", "hours", "minutes", "seconds"]
        if self.unit not in valid_units:
            print(f"Invalid unit. Please select from {', '.join(valid_units)}.")
            return False

        return True

    def calculate_duration(self):
        if self.unit == "months":
            return self.age * 12
        elif self.unit == "weeks":
            return self.age * 52.143
        elif self.unit == "days":
            return self.age * 365.25
        elif self.unit == "hours":
            return self.age * 365.25 * 24
        elif self.unit == "minutes":
            return self.age * 365.25 * 24 * 60
        elif self.unit == "seconds":
            return self.age * 365.25 * 24 * 60 * 60
        else:
            return None 

    def display_result(self):
        result = self.calculate_duration()
        if result is not None:
            print(
                f"\nThe person has lived for approximately {result:,.2f} {self.unit}."
            )
        else:
            print("Please check your inputs.")


if __name__ == "__main__":
    converter = YearsToSmallerUnits()
    if converter.get_inputs():
        converter.display_result()
