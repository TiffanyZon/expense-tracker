import streamlit as st
from datetime import date
import pandas as pd
import numpy as np
import csv

st.title("Expense Tracker")
st.write("Register your expenses and get and overview of your spendings")

st.header("Add a new expense")
with st.form(key="expense_form"):
    amount = st.number_input("Amount (SEK)", min_value=0.0, format="%.2f")
    category = st.selectbox(
        "Category", ["Food", "Transport", "Housing", "Entertainment", "Other"]
    )
    expense_date = st.date_input("Select a date", value=date(2026, 1, 29))
    comment = st.text_input("Comment (optional)")
    submitted = st.form_submit_button(label="Save Expense")

    if submitted:
        st.balloons()
        new_expense = {
            "amount": amount,
            "category": category,
            "date": expense_date,
            "comment": comment,
        }

        try:
            df = pd.read_csv("expenses.csv")
            df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)
        except FileNotFoundError:
            df = pd.DataFrame([new_expense])

        df.to_csv("expenses.csv", index=False)

        st.success("Expense saved!")
        st.dataframe(df)
