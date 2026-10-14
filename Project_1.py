# ======= Expense Tracker =======

import json
from tabulate import tabulate
import math
from datetime import datetime

# ===========================================================

def load_expense():  # Function to load previous expenses.

    try:
        with open("Expenses.json", "r") as f:
            data =  json.load(f)

            if not isinstance(data, list):
                print("Invalid expense data format")
                return None

            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Invalid JSON file")
        return None

# =============================================================

def save_expense(): #Function to save new expenses.

    with open("Expenses.json", "w") as f:
        json.dump(total_expenses, f, indent=4)

# ============================================================

def add_expense():  # Function which help user to add expenses.
    
    S_no = len(total_expenses) + 1

    categories = ["travel","shopping","food","other"]

    while True:
        date = input("Enter date (YYYY-MM-DD):")
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid Date format")

    while True:
        category = input("Enter expense category (Food / Travel / Shopping / other):").strip().lower()
        if category in categories:
            break
        else:
            print("Invalid Category")

    description = input("Enter expense description:")

    try:
        amount = float(input("Enter expense amount:"))
        if not math.isfinite(amount) or amount <= 0:
            raise ValueError("Amount must be positive")
    except ValueError:
        print("Invalid Amount")
    else:
        single_expense = {
            "S_No": S_no,
            "Date": parsed_date.isoformat(),
            "Category": category,
            "Description": description,
            "Amount": amount,
        }

        total_expenses.append(single_expense)
        return True

    save_expense()
    
# =====================================================================

def expense_summary():  # Function which help user to view expenses summary.
    headers = ["S_No","Date","Category","Description","Amount"]
    data = []
    
    if total_expenses == []:
        print("No expenses found")
    else:
        for i in total_expenses:
            item = (
                i["S_No"],
                i.get("Date", "N/A"),
                i["Category"],
                i["Description"],
                i["Amount"]
                )
            data.append(item)
        print(tabulate(data,headers=headers,tablefmt="fancygrid"))

# =====================================================================

def delete_expense(): # Function which help user to delete expenses.
    while True:
        try:
            choice = int(input("Enter S.no which you want to delete:"))
            break
        except ValueError:
            print("Invalid Choice")

    for i in total_expenses:
        if i["S_No"] == choice:
            total_expenses.pop(choice-1)

            for index, expense in enumerate(total_expenses, start=1):
                expense["S_No"] = index
            print("Deleted!")
            break
    else:
        print("S.No not found")

    save_expense()

#=====================================================================

def Search_expenses(): # Function which help user to search expenses by category,date or amount.
    while True:
        print("\n1. Search by category")
        print("2. Search by date")
        print("3. Search by amount")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice:"))
        except ValueError:
            print("Invalid Choice")
            continue

        if choice == 1:
            search = input("Search Category:").strip().lower()
            headers = ["S_No","Date","Category","Description","Amount"]
            data = []

            for i in total_expenses:
                if i["Category"] == search:
                    item = (i["S_No"],
                            i.get("Date", "N/A"),
                            i["Category"],
                            i["Description"],
                            i["Amount"]
                            )
                    data.append(item)

            if data:
                print(tabulate(data,headers=headers , tablefmt="fancygrid"))
            else:
                print("Category not found")

            continue

        elif choice == 2:
            search = input("Search date (YYYY-MM-DD):").strip()
            try:
                datetime.strptime(search, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid Date format")
                continue

            headers = ["S_No","Date","Category","Description","Amount"]
            data = []

            for i in total_expenses:
                if i.get("Date") == search:
                    item = (i["S_No"],
                            i.get("Date", "N/A"),
                            i["Category"],
                            i["Description"],
                            i["Amount"]
                            )
                    data.append(item)

            if data:
                print(tabulate(data,headers=headers , tablefmt="fancygrid"))
            else:
                print("No Expenses found for this date")

            continue
        
        elif choice == 3:
            try:
                search = float(input("Search Amount:"))
                if not math.isfinite(search) or search <= 0:
                    raise ValueError
            except ValueError:
                print("Invalid Amount")
                continue

            headers = ["S_No","Date","Category","Description","Amount"]
            data = []

            for i in total_expenses:
                if i["Amount"] <= search:
                    item = (i["S_No"],
                            i.get("Date", "N/A"),
                            i["Category"],
                            i["Description"],
                            i["Amount"]
                            )
                    data.append(item)

            if data:
                print(tabulate(data,headers=headers , tablefmt="fancygrid"))
            else:
                print("No expenses found within this amount")

            continue

        elif choice == 4:
            break

        else:
            print("Invalid Choice")

# ==================================================================

def show_total():  # Function which help user to show total expenses.
    travel = 0
    food = 0
    shopping = 0
    other = 0

    for i in total_expenses:
        if i["Category"] == "travel":
            travel += i["Amount"]
        elif i["Category"] == "food":
            food += i["Amount"]
        elif i["Category"] == "shopping":
            shopping += i["Amount"]
        elif i["Category"] == "other":
            other += i["Amount"]

    total = travel + food + shopping + other
    print("\nTravelling Expenses:",travel)
    print("Food Expenses:",food)
    print("Shopping Expenses:",shopping)
    print("Other Expenses:",other)
    print("Total Expenses:",total)

# ================================================================
        
def main():  # Main Function
    global total_expenses

    total_expenses = load_expense()

    if total_expenses is None:
        print("Program stopped to protect your data.")
        return

    while True:
        print("\n1. Add Expenses")
        print("2. Expenses Summary")
        print("3. Delete expenses")
        print("4. Search Expenses")
        print("5. Show total expenses")
        print("6. Exit")

        try:
            option = int(input("Choose any one:"))
        except ValueError:
            print("Invalid Choice")
            continue

        if option == 1:
            add_expense()

        elif option == 2:
            expense_summary()

        elif option == 3:
            delete_expense()

        elif option == 4:
            Search_expenses()

        elif option == 5:
            show_total()

        elif option == 6:
            break

        else:
            print("Option not found")

# ===========================================================

main()