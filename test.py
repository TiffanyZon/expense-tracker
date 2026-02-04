from logic import save_expense, load_expenses, sum_expenses_by_category, EXPENSE_COLUMNS
import pandas as pd


def test_save_expense_creates_row(tmp_path):
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


def test_load_expenses_file_exists(tmp_path):
    filename = tmp_path / "expenses.csv"

    filename.write_text("amount,category,date,comment\n" "10,Food,2026-02-03,Lunch\n")

    df = load_expenses(filename)

    assert not df.empty
    assert len(df) == 1
    assert df.iloc[0]["amount"] == 10


def test_load_expenses_file_not_found(tmp_path):
    filename = tmp_path / "missing.csv"

    df = load_expenses(filename)

    assert df.empty
    assert list(df.columns) == EXPENSE_COLUMNS


def test_sum_expenses_by_category():
    df = pd.DataFrame(
        [
            {"amount": 10, "category": "Food"},
            {"amount": 100, "category": "Transport"},
            {"amount": 89, "category": "Food"},
        ]
    )

    summary = sum_expenses_by_category(df)

    assert summary["Food"] == 99
    assert summary["Transport"] == 100
