from helpers import celcius_to_kelvin, celcius_to_fahrenheit

if __name__ == '__main__':

    while True:

        try:
            celcius_temperature = input("Enter the temperature in Celcius\n(enter 'q' to leave): ")
            if celcius_temperature.lower() != "q":
                print(f"Temperature in Kelvin(K) = {celcius_to_kelvin(float(celcius_temperature))}")
                print(f"Temperature in Fahrenheit = {celcius_to_fahrenheit(float(celcius_temperature))}")
            else:
                print("See you later!")
                break
        except ValueError:
            print("\nThis digit is invalid. \nPlease insert a number or 'q'")
