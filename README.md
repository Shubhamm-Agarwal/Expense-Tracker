# 💰 Expense Tracker V2

A command-line Expense Tracker built using **Python** that allows users to record, manage, and analyze their daily expenses.

The project uses **JSON file storage** to save expense records and displays them in a formatted table.

## 🚀 Features

- **Add Expenses:** Record expenses with a category, description, and amount.
- **Expenses Summary:** Display all recorded expenses in a formatted table.
- **Category-wise total:** Calculate expenses for Food, Travel, Shopping, and Other.
- **Delete Expenses:** Delete expense which ever user wanted to.
- **JSON Storage:** Save expenses locally and load them when the program restarts.
- **Input Validation:** Reject invalid categories, negative amounts, zero values, and non-finite numbers.
- **Error Handling:** Handle invalid inputs and corrupted JSON files.

## 🛠️ Technologies Used

- Python
- JSON
- Tabulate Library
- Git & GitHub

## 📁 Project Structure

```text
Expense-Tracker/
├── Project_1.py
├── Expenses.json
├── README.md
├── requirements.txt
└── .gitignore
```

## ⚙️ Installation & Usage

**1. Clone the repository**

```bash
git clone https://github.com/Shubhamm-Agarwal/Expense-Tracker.git
```

**2. Navigate to the project folder**

```bash
cd Expense-Tracker
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
python Project_1.py
```

## 💻 Application Menu

```text
1. Add Expenses
2. Expenses Summary
3. Show total expenses
4. Delete Expenses
5. Exit
```

## 📊 Example Expense Summary

```text
Travelling Expenses: 100.0
Food Expenses: 250.0
Shopping Expenses: 500.0
Other Expenses: 0
Total Expenses: 850.0
```

## 🔮 Future Improvements

- Edit and delete existing expenses
- Search expenses by category
- Add dates to expense records
- Generate monthly expense reports
- Integrate a SQL database
- Build a graphical or web-based interface

## 👨‍💻 Author

**Shubham Agarwal**

GitHub: [Shubhamm-Agarwal](https://github.com/Shubhamm-Agarwal)

---

*Built as a Python learning project to practice functions, dictionaries, file handling, JSON, exception handling, and modular programming.*
