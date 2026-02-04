from logic import save_expense
import pandas as pd


def test_expense(tmp_path):
    amount = 10
    category = "Food"
    date = "2026-01-19"
    comment = "Lunch"
    filename = tmp_path / "expenses.csv"

    df = save_expense(amount, category, date, comment, filename)

    assert len(df) == 1

    row = df.iloc[0]

    assert row["amount"] == amount
    assert row["category"] == category
    assert row["date"] == date
    assert row["comment"] == comment
