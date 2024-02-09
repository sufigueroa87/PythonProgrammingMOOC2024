# Please write a program which asks the user for a year, and prints out the next leap year.
# Year: 2023
# The next leap year after 2023 is 2024
#
# Year: 2023
# The next leap year after 2023 is 2024
#
# Year: 2024
# The next leap year after 2024 is 2028

yearUser = int(input("Year: "))

year = yearUser + 1

yearLeap = False

while not yearLeap:

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                #print("That year is a leap year.")
                yearLeap = True
            else:
                #print("That year is not a leap year.")
                year = year + 1
        else:
            #print("That year is a leap year.")
            yearLeap = True
    else:
        #print("That year is not a leap year.")
        year = year + 1

print(f"The next leap year after {yearUser} is {year}")