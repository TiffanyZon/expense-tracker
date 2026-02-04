import pandas as pd
import plotly.express as px

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
    return df


def load_expenses(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return pd.DataFrame(columns=EXPENSE_COLUMNS)


def add_expense_to_df(df, expense):
    return pd.concat([df, pd.DataFrame([expense])], ignore_index=True)


def sum_expenses_by_category(df):
    return df.groupby("category")["amount"].sum()


def create_pie_fig(df):
    return px.pie(
        df,
        values="amount",
        names="category",
        title=None,
        height=400,
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
