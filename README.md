# Personal Finance Tracker

A simple command-line application for tracking personal income, expenses, and budgets, built in Python.

## Features

- **Track Income** — Record income by category (e.g., salary, investments) with support for multiple entries per category.
- **Track Expenses** — Record expenses by category (e.g., food, rent, utilities) with support for multiple entries per category.
- **Set Budgets** — Define a budget amount for any category.
- **Financial Reports** — Generate a summary showing total income, total expenses, budget vs. actual spending (with variance), and overall balance.
- **View Summary** — Quickly review all recorded income, expenses, and budgets.
- **Input Validation** — Guards against negative or non-numeric amounts.

## Requirements

- Python 3.6+

No external dependencies are required — the project only uses Python's standard library (`datetime`, `calendar`).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```
2. Run the script directly (no additional setup needed):
   ```bash
   python finance_tracker2.py
   ```

## Usage

When you run the script, you'll be presented with a menu:

```
--- Personal Finance Tracker ---
1. Add Income
2. Add Expense
3. Set Budget
4. Generate Financial Report
5. View Summary
6. Exit
```

Enter the number corresponding to the action you'd like to take, then follow the prompts.

### Example Workflow

1. **Add Income** — Enter a category (e.g., `salary`) and an amount (e.g., `5000`).
2. **Add Expense** — Enter a category (e.g., `rent`) and an amount (e.g., `1500`).
3. **Set Budget** — Enter a category (e.g., `rent`) and a budget amount (e.g., `1600`).
4. **Generate Financial Report** — View totals, budget variance per category, and your overall balance.
5. **View Summary** — See a raw breakdown of all recorded income, expenses, and budgets.
6. **Exit** — Close the application.

## Project Structure

```
.
├── finance_tracker2.py   # Main application logic
└── README.md              # Project documentation
```

## How It Works

The app is built around a single `FinanceTracker` class that stores data in memory during a session:

- `self.income` — a dictionary mapping category names to a list of income amounts.
- `self.expenses` — a dictionary mapping category names to a list of expense amounts.
- `self.budget` — a dictionary mapping category names to a single budget amount.

> **Note:** Data is not persisted between sessions — all records are lost when the program exits. This makes it a great starting point for adding file-based or database storage as a future enhancement.

## Potential Enhancements

- Persist data to a file (CSV/JSON) or database so records survive between sessions.
- Add date tracking for income and expense entries.
- Add the ability to edit or delete individual entries.
- Export financial reports to a file (CSV/PDF).
- Add monthly/yearly filtering and trend analysis.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or file an issue.

## License

This project is available under the MIT License. Feel free to use and modify it for your own purposes.
