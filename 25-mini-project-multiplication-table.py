def multiplication_table(table, stop):
    print(f"Multiplication table {table}")
    
    for factor in range(1, stop + 1):
        print(f"{table} x {factor} = {table * factor}")

terminate = False
while not terminate:
    print("Welcome to multiplication table creator")
    # user inputs
    user_table = int(input("Pick a table (in figure):\n"))
    stop_point = int(input("Where do you want your to table to end?\n"))

    multiplication_table(user_table, stop_point)
    user_terminate = input("Do you want to terminate the program now? yes/no\n").lower()
    if user_terminate == "yes":
        terminate = True
        