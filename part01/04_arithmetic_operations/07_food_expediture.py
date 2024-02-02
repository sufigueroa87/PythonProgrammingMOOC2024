# Please write a program which estimates a user's typical food expenditure.
#
# The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.
#
# Based on this information the program calculates the user's typical food expenditure both weekly and daily.
#
# The program should function as follows:
# How many times a week do you eat at the student cafeteria? 4
# The price of a typical student lunch? 2.5
# How much money do you spend on groceries in a week? 28.5
#
# Average food expenditure:
# Daily: 5.5 euros
# Weekly: 38.5 euros

vecesComenCafeteria = int(input("How many times a week do you eat at the student cafeteria? "))
precioComerCafeteria = float(input("The price of a typical student lunch? "))
dineroCompra = float(input("How much money do you spend on groceries in a week? "))

dineroCafeteriaSemanal = float(vecesComenCafeteria * precioComerCafeteria)
dineroGastadoComidaSemana = float(dineroCafeteriaSemanal + dineroCompra)

print("Average food expenditure: ")
print(f"Daily: {dineroGastadoComidaSemana / 7} euros")
print(f"Weekly: {dineroGastadoComidaSemana} euros")