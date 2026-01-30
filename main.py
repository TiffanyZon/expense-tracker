import streamlit as st
from datetime import date
import pandas as pd
import numpy as np
import plotly.express as px

tab1, tab2 = st.tabs(["Add expense", "Overview"])

df = None

with tab1:
    st.title("Expense Tracker")
    st.write("Register your expenses and get and overview of your spendings")

    st.header("Add a new expense")
    with st.form(key="expense_form"):
        amount = st.number_input("Amount (SEK)", min_value=0.0, format="%.2f")
        category = st.selectbox(
            "Category",
            [
                "Food",
                "Transport",
                "Housing",
                "Entertainment",
                "Subscription",
                "Student Loan",
                "Other",
            ],
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
            st.success("Expense Saved! 💸")

with tab2:
    st.header("Overview")

    if df is None:
        try:
            df = pd.read_csv("expenses.csv")
        except FileNotFoundError:
            df = pd.DataFrame()
    if not df.empty:
        with st.expander("Expenses Preview"):
            st.dataframe(df)
        col1, col2 = st.columns([1, 1])
        with col1:
            st.subheader("Spending by Category (Pie)")
            fig = px.pie(
                df,
                values="amount",
                names="category",
                title=None,
                height=400,
                color_discrete_sequence=px.colors.qualitative.Set2,
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Spending by Category (Bar)")
            summary = df.groupby("category")["amount"].sum()
            st.bar_chart(summary, use_container_width=True)

    else:
        st.info("No expenses recorded yet.")
