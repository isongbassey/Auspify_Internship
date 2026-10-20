import csv

 

def add_expense():

    date = input("Enter date (YYYY-MM-DD): ")

    category = input("Enter category: ")

    description = input("Enter description: ")

    amount = float(input("Enter amount: "))

 

    with open("expenses.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([date, category, description, amount])

 

    print("Expense added successfully!")

 

def view_expenses():

    with open("expenses.csv", "r") as file:

        reader = csv.reader(file)

       

        next(reader, None)

 

        print("\nAll Expenses:")

        for row in reader:

            print(row)

           

def spending_summary():

    total = 0

 

    with open("expenses.csv", "r") as file:

        reader = csv.reader(file)

 

        next(reader, None)

 

        for row in reader:

            if len(row) > 3:

                total += float(row[3])

 

    print(f"\nTotal Expenses: {total}")

   

def category_summary():

    categories = {}

 

    with open("expenses.csv", "r") as file:

        reader = csv.reader(file)

 

        next(reader, None)

 

        for row in reader:

            if len(row) > 3:

                category = row[1]

                amount = float(row[3])

 

                if category in categories:

                    categories[category] += amount

                else:

                    categories[category] = amount

 

    print("\nCategory Summary:")

 

    for category, total in categories.items():

        print(category, ":", total)

       

def monthly_report():

    month = input("Enter month (YYYY-MM): ")

 

    total = 0

 

    with open("expenses.csv", "r") as file:

        reader = csv.reader(file)

 

        next(reader, None)

 

        for row in reader:

            if len(row) > 3 and row[0].startswith(month):

                total += float(row[3])

 

    print(f"\nTotal expenses for {month}: {total}")

 

def menu():

    while True:

        print("1. Add Expense")

        print("2. View Expenses")

        print("3. Spending Summary")

        print("4. Category Summary")

        print("5. Monthly Report")

        print("6. Exit")

 

        choice = input("Choose an option: ")

 

        if choice == "1":

            add_expense()

 

        elif choice == "2":

            view_expenses()

 

        elif choice == "3":

            spending_summary()

 

        elif choice == "4":

            category_summary()

 

        elif choice == "5":

            monthly_report()

 

        elif choice == "6":

            print("Goodbye!")

            break

        else:

            print("Invalid choice.")

 

menu()
