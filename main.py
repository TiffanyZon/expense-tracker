import streamlit as st
from datetime import date
import pandas as pd
import plotly.express as px
from logic import save_expense, load_expenses, sum_expenses_by_category, create_pie_fig

FILENAME = "expenses.csv"
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
            new_expense = save_expense(
                amount, category, expense_date, comment, FILENAME
            )
            st.success("Expense Saved! 💸")

with tab2:
    st.header("Overview")

    if df is None:
        df = load_expenses(FILENAME)
    if not df.empty:
        with st.expander("Expenses Preview"):
            st.dataframe(df)
        col1, col2 = st.columns([1, 1])
        with col1:
            st.subheader("Spending by Category (Pie)")
            fig = create_pie_fig(df)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Spending by Category (Bar)")
            summary = sum_expenses_by_category(df)
            st.bar_chart(summary, use_container_width=True)

    else:
        st.info("No expenses recorded yet.")
