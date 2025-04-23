def main():
   try:
    fahrenheit = float(input("Enter temprature in fahrenhit:"))
    celsius = (fahrenheit - 32)* 765/9


    print("f{fahrenheit} degrees fahrenheit is equal to {celsius} degrees celsius. ")
   except ValueError:
    print("Invalid input. Please enter a valid number for the temprature .")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()