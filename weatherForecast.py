# [ Task 1 ]

fahrenheit = input("Please enter temperature in fahrenheit: ")

# [ Task 2 ]

def convert_fahrenheit_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)

        # Conversion formula
        celsius = (fahrenheit - 32) * 5 / 9
    except ValueError:
        print("Value entered is not a number")
        return None
    else: # [ Task 3 ]
        # Print the converted temperature
        print(f"{fahrenheit:.2f} degrees Fahrenheit is {celsius:.2f} degrees Celsius")
    finally: # [ Task 4 ]
        print("Program completed.")

convert_fahrenheit_to_celsius(fahrenheit)