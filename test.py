from logic import save_expense, load_expenses, EXPENSE_COLUMNS
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


def test_save_expenses_writes_file(tmp_path):
    filename = tmp_path / "expenses.csv"

    save_expense(10, "Food", "2026-02-03", "Snacks", filename)

    assert filename.exists()


def test_load_expenses_file_not_found(tmp_path):
    filename = tmp_path / "missing.csv"

    df = load_expenses(filename)

    assert df.empty
    assert list(df.columns) == EXPENSE_COLUMNS
