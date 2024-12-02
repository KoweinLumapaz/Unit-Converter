import csv
import cowsay

#Files for Length
LengthMultiply_File = "LMultiply.csv"
LengthDivide_File = "LDivide.csv"

#Files for Weight
WeightMultiply_File = "WMultiply.csv"
WeightDivide_File = "WDivide.csv"

#Read csv file
def read_conversions(file_name):
    conversions = {}
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = (row['From'], row['To'])
            conversions[key] = float(row['Convert'])
    return conversions

def main():

    Lmultiply_conversions = read_conversions(LengthMultiply_File)
    Ldivide_conversions = read_conversions(LengthDivide_File)

    Wmultiply_conversions = read_conversions(WeightMultiply_File)
    Wdivide_conversions = read_conversions(WeightDivide_File)

    print("\n    === Unit Converter ===")
    print("   _______________________")
    print("   |     1. Length       |")
    print("   |     2. Weight       |")
    print("   |     3. Temperature  |")
    print("   |     4. Exit         |")
    print("   _______________________")

    #USer will select a category
    respo = input("\nPlease select what category: ").strip()

    #If length is picked. Select available units in metric system
    if respo =="1" or respo =="Length" or respo == "length":
        print("\n | Available units of Length (Metric System):| ")
        print("         _______________________")
        print("         | 1. Millimeters (mm) |")
        print("         | 2. Centimeters (cm) |")
        print("         | 3. Meters (m)       |")
        print("         | 4. Kilometers (km)  |")
        print("         _______________________")

        print("\nNote: Enter the symbol of units (ex: mm).")
        from_unit = input("\nEnter the unit to convert from: ").strip()
        to_unit = input("Enter the unit to convert to: ").strip()

    # Check if the "From" and "To" unit is in LMultiply_unit.csv file
        #if units combination is from multiply_unit.csv file

        if (from_unit, to_unit) in Lmultiply_conversions:
            str_value = str(input(f"Enter the value of {from_unit}: "))
            if not str_value:
                print("\n** No Value, Please try again **")
                return main()
            else:
                if str_value.isalpha():
                    print("\n** Invalid input, please try again! **")
                    return main()
                else:
                    value = float(str_value)
                    if value <= 0:
                        print("\n** Invalid input, please try again! **")
                        return main()
                    else:
                        result = multiply_units(value, from_unit, to_unit, Lmultiply_conversions)
                        #Print result
                        print(f"\n== {value} {from_unit} is equal to {result} {to_unit} ==\n")
                        try_again()

        #if units combination is from LDivide_units.csv file
        elif (from_unit, to_unit) in Ldivide_conversions:
            str_value = str(input(f"Enter the value of {from_unit}: "))
            if not str_value:
                print("\n** No Value, Please try again **")
                return main()
            else:
                if str_value.isalpha():
                    print("\n** Invalid input, please try again! **")
                    return main()
                else:
                    value = float(str_value)
                    if value <= 0:
                        print("\n** Invalid input, please try again! **")
                        return main()
                    else:
                        result = divide_units(value, from_unit, to_unit, Ldivide_conversions)
                        #Print Result
                        print(f"\n== {value} {from_unit} is equal to {result} {to_unit} ==\n")
                        try_again()

        #if there is no units combination from the 2 csv file
        else:
            print("\n** Conversion is not Available. **")
            return main()

    #If Weight is picked.
    elif respo =="2" or respo =="Weight" or respo == "weight":
        print("\n | Available units of Weight (Metric System): | ")
        print("         _______________________")
        print("         | 1. Milligrams (mg)  |")
        print("         | 2. Grams (g)        |")
        print("         | 3. Kilograms (kg)   |")
        print("         | 4. Metric Ton (t)   |")
        print("         _______________________")

        print("\nNote: Enter the symbol of units (ex: mg).")
        from_unit = input("\nEnter the unit to convert from: ").strip()
        to_unit = input("Enter the unit to convert to: ").strip()

        if (from_unit, to_unit) in Wmultiply_conversions:
            str_value = str(input(f"Enter the value of {from_unit}: "))
            if not str_value:
                print("\n** No Value, Please try again **")
                return main()
            else:
                if str_value.isalpha():
                    print("\n** Invalid input, please try again! **")
                    return main()
                else:
                    value = float(str_value)
                    if value <= 0:
                        print("\n** Invalid input, please try again! **")
                        return main()
                    else:
                        result = multiply_units(value, from_unit, to_unit, Wmultiply_conversions)
                        #Print result
                        print(f"\n== {value} {from_unit} is equal to {result} {to_unit} ==\n")
                        try_again()

        #if units combination is from LDivide_units.csv file
        elif (from_unit, to_unit) in Wdivide_conversions:
            str_value = str(input(f"Enter the value of {from_unit}: "))
            if not str_value:
                print("\n** No Value, Please try again **")
                return main()
            else:
                if str_value.isalpha():
                    print("\n** Invalid input, please try again! **")
                    return main()
                else:
                    value = float(str_value)
                    if value <= 0:
                        print("\n** Invalid input, please try again! **")
                        return main()
                    else:
                        result = divide_units(value, from_unit, to_unit, Wdivide_conversions)
                        #Print Result
                        print(f"\n== {value} {from_unit} is equal to {result} {to_unit} ==\n")
                        try_again()

        #if there is no units combination from the 2 csv file
        else:
            print("\n** Conversion is not Available! **")
            return main()

    #Exit.
    elif respo =="3" or respo =="Temperature" or respo == "temperature":
        print("\n | Available units of Temperature: | ")
        print("         _______________________")
        print("         | 1. Celsius (C)      |")
        print("         | 2. Fahrenheit (F)   |")
        print("         | 3. Kelvin (K)       |")
        print("         _______________________")

        print("\nNote: Enter the symbol of units (C/F/K).")
        from_temp = input("\nEnter the unit to convert from: ").strip()
        to_temp = input("Enter the unit to convert to: ").strip()

        #Celsius To Fahrenheit
        if from_temp=='C' and to_temp=='F':
            str_value = str(input(f"Enter the value of Celsius: "))
            if not str_value:
                print("\n** No Value, Please try again. **")
                return main()
            else:
                if str_value.isalpha():
                    print("\n** Invalid input, please try again! **")
                    return main()
                else:
                    value = float(str_value)
                    if value < -273.15:
                        print("\n** Not possible, -273.15 °C is the lowest possible temperature **")
                        return main()
                    else:
                        result = (value * 9/5) + 32
                        print(f"\n== {value} °C is equal to {result:.4f} °F ==\n")
                        try_again()

        #Celcius to Kelvin
        elif from_temp == 'C' and to_temp == 'K':
            str_value = str(input(f"Enter the value of Celsius: "))
            if not str_value:
                print("\n** No Value, Please try again. **")
                return main()
            else:
                if str_value.isalpha():
                    print("\n** Invalid input, please try again! **")
                    return main()
                else:
                    value = float(str_value)
                    if value < -273.15:
                        print("\n** Not possible, -273.15 °C is the lowest possible temperature **")
                        return main()
                    else:
                        result = value + 273.15
                        print(f"\n== {value} °C is equal to {result:.4f} K ==\n")
                        try_again()

        #Fahrenheit to Celsius
        elif from_temp == 'F' and to_temp == 'C':
            str_value = str(input(f"Enter the value of Fahrenheit: "))
            if not str_value:
                print("\n** No Value, Please try again. **")
                return main()
            else:
                if str_value.isalpha():
                    print("\n** Invalid input, please try again! **")
                    return main()
                else:
                    value = float(str_value)
                    if value < -459.67:
                        print("\n** Not possible, -459.67 °F is the lowest possible temperature **")
                        return main()
                    else:
                        result = (value - 32) * 5/9
                        print(f"\n== {value} °F is equal to {result:.4f} °C ==\n")
                        try_again()

        #Fahrenheit to Kelvin
        elif from_temp == 'F' and to_temp == 'K':
            str_value = str(input(f"Enter the value of Fahrenheit: "))
            if not str_value:
                print("\n** No Value, Please try again. **")
                return main()
            else:
                if str_value.isalpha():
                    print("\n** Invalid input, please try again! **")
                    return main()
                else:
                    value = float(str_value)
                    if value < -459.67:
                        print("\n** Not possible, -459.67 °F is the lowest possible temperature **")
                        return main()
                    else:
                        result = (( value - 32) * 5/9) + 273.15
                        print(f"\n== {value} °F is equal to {result:.4f} K ==\n")
                        try_again()

        #Kelvin to Celsius
        elif from_temp == 'K' and to_temp == 'C':
            str_value = str(input(f"Enter the value of Kelvin: "))
            if not str_value:
                print("\n** No Value, Please try again. **")
                return main()
            else:
                if str_value.isalpha():
                    print("\n** Invalid input, please try again! **")
                    return main()
                else:
                    value = float(str_value)
                    if value < 0:
                        print("\n** Not possible, 0 K is the lowest possible temperature **")
                        return main()
                    else:
                        result = value - 273.15
                        print(f"\n== {value} K is equal to {result:.4f} °C ==\n")
                        try_again()


        #Kelvin to Fahrenheit
        elif from_temp == 'K' and to_temp == 'F':
            str_value = str(input(f"Enter the value of Kelvin: "))
            if not str_value:
                print("\n** No Value, Please try again. **")
                return main()
            else:
                if str_value.isalpha():
                    print("\n** Invalid input, please try again! **")
                    return main()
                else:
                    value = float(str_value)
                    if value < 0:
                        print("\n** Not possible, 0 K is the lowest possible temperature **")
                        return main()
                    else:
                        result = ((value - 273.15) * 9/5) +32
                        print(f"\n== {value} K is equal to {result:.4f} °F ==\n")
                        try_again()

        else:
            print("\n** Conversion is not Available! **")
            return main()



    elif respo =="4" or respo =="Exit" or respo == "exit":
        cowsay.tux("Thank you for using Unit Converter!")
        return

    elif not respo:
        print("\n** No input, Please select category. **")
        return main()

    else:
        print("\n** Invalid input, please try again. **")
        return main()


#Function for multiply units
def multiply_units(value, from_unit, to_unit, conversions):
    key = (from_unit, to_unit)
    if key in conversions:
        return value * conversions[key]
    else:
        print("** Conversion not Available **")
        return main()
    
#Function for divide units
def divide_units(value, from_unit, to_unit, conversions):
    key = (from_unit, to_unit)
    if key in conversions:
        return value / conversions[key]
    else:
        print("** Conversion not Available **")
        return main()

def try_again():
    tryRespo = input("Do you want to try again? (yes/no) ").strip()
    if tryRespo == "yes" or tryRespo == "Yes" or tryRespo == 'y':
        return main()
    elif not tryRespo:
        print("\n** No input, please answer the question. **")
        return try_again()
    else:
        cowsay.tux("Thank you for using Unit Converter!")
        return

if __name__ == "__main__":
    main()