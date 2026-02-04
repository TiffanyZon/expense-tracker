import pandas as pd

EXPENSE_COLUMNS = ["amount", "category", "date", "comment"]


def save_expense(amount, category, date, comment, filename):
    new_expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "comment": comment,
    }

    df = load_expenses(filename)
    df = add_expense_to_df(df, new_expense)
    df.to_csv(filename, index=False)


def load_expenses(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return pd.DataFrame(columns=EXPENSE_COLUMNS)


def add_expense_to_df(df, expense):
    return pd.concat([df, pd.DataFrame([expense])], ignore_index=True)
