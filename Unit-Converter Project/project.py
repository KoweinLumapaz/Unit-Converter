import csv

multiply_File = "multiply_unit.csv"
divide_File = "divide_unit.csv"

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
    

    multiply_conversions = read_conversions(multiply_File)
    divide_conversions = read_conversions(divide_File)

    print("\n=== Weight and Length Unit Converter ===\n")
    print("1. Length")
    print("2. Weigth")
    print("3. Exit")

    #USer will select a category
    respo = input("\nPlease select what category you want to convert: ")

    #If length is picked. Select available units in metric system
    if respo =="1" or respo =="Length" or respo == "length":
        print("\nAvailable units Length (Metric System):")
        print("1. Millimeters (mm)")
        print("2. Centimeters (cm)")
        print("3. Meters (m)")
        print("4. Kilometers (km)")

        print("Note: Enter the symbol of units (ex: mm).")
        from_unit = input("\nEnter the unit to convert from: ").strip()
        to_unit = input("Enter the unit to convert to: ").strip()
        

    # Check if the "From" and "To" unit is in multiply_unit.csv file
        #if units combination is from multiply_unit.csv file
        if (from_unit, to_unit) in multiply_conversions:
            value = float(input("Enter the value to convert: "))
            result = multiply_units(value, from_unit, to_unit, multiply_conversions)
            #Print result
            print(f"\n== {value} {from_unit} is equal to {result} {to_unit} ==\n")
            

        #if units combination is from divide_units.csv file
        elif (from_unit, to_unit) in divide_conversions:
            value = float(input("Enter the value to convert: "))
            result = divide_units(value, from_unit, to_unit, divide_conversions)
            #Print Result
            print(f"\n== {value} {from_unit} is equal to {result} {to_unit} ==\n")            

        #if there is no units combination from the 2 csv file
        else:
            print("Not Available")

    #If Weight is picked.
    elif respo =="2" or respo =="Weight" or respo == "weight":
        print("Weight")    

    #Exit.
    elif respo =="3" or respo =="Exit" or respo == "exit":
        print("Thank you for using Unit Converter")
        breakpoint
    
    else:
        print("invalid input, please try again.")
        return main()


#Function for multiply units
def multiply_units(value, from_unit, to_unit, conversions):
    key = (from_unit, to_unit)
    if key in conversions:
        return value * conversions[key]
    else:
        return None 
    
#Function for divide units
def divide_units(value, from_unit, to_unit, conversions):
    key = (from_unit, to_unit)
    if key in conversions:
        return value / conversions[key]
    else:
        return None


if __name__ == "__main__":
    main()