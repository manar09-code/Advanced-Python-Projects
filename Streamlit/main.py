#streamlit: an open-source Python library that makes it easy to create and share beautiful custom web apps for machine learning and data science.
import streamlit as st
st.write('Hello World')
#adding a text input and return
st.text_input('Favorite Movie?')
#using input elements
#Streamlit supports Markdown formatting by default
# this capture the return value into x
x = st.text_input('Favorite Movie?')
st.write(f"Your favorite movie is: {x}")
#creating a button
is_clicked = st.button("Click Me")
import streamlit as st
st.write("## This is a H2 Title!")
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
multi = '''If you end a line with two spaces,
a soft return is used for the next line.
Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
#working with data
import pandas as pd
data = pd.read_csv("movies.csv")
# This shows the data in a nice table
st.write(data)  # display the data inside the app
#showing data in a graph
import numpy as np
# Some random generated data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.bar_chart(chart_data)
st.line_chart(chart_data)
#Loan Repayments App
#Streamlit is generally used in building simpler apps that are interactive and heavily focused on working with data or machine learning.
# Loan Repayments Calculator
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

st.title("Mortgage Repayments Calculator")

st.write("### Input Data")
col1, col2 = st.columns(2)  # Display elements in 2 column using the column component
# Set a default value or minimum/maximum value
home_value = col1.number_input("Home Value", min_value=0, value=500000)
deposit = col1.number_input("Deposit", min_value=0, value=100000)
interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=5.5)
loan_term = col2.number_input("Loan Term (in years)", min_value=1, value=30)
# Calculate the repayments.
loan_amount = home_value - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12
monthly_payment = (
    loan_amount
    * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
    / ((1 + monthly_interest_rate) ** number_of_payments - 1)
)
# Display the repayments.
total_payments = monthly_payment * number_of_payments
total_interest = total_payments - loan_amount
st.write("### Repayments")
col1, col2, col3 = st.columns(3)    # Create 3 columns
col1.metric(label="Monthly Repayments", value=f"${monthly_payment:,.2f}")
col2.metric(label="Total Repayments", value=f"${total_payments:,.0f}")
col3.metric(label="Total Interest", value=f"${total_interest:,.0f}")
# Create a data-frame with the payment schedule.
schedule = []
remaining_balance = loan_amount
for i in range(1, number_of_payments + 1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    year = math.ceil(i / 12)  # Calculate the year into the loan
    schedule.append(
        [
            i,
            monthly_payment,
            principal_payment,
            interest_payment,
            remaining_balance,
            year,
        ]
    )
df = pd.DataFrame(
    schedule,
    columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"],
)
# Display the data-frame as a chart.
st.write("### Payment Schedule")
payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()
st.line_chart(payments_df)
#Deploying to Streamlit Cloud
#To deploy streamlit app, you can use Streamlit Cloud to deploy for free and it will be publicly visible.
#First, make sure that your app is published to Github because that’s where Streamlit is going to read the source code and then deploy it from.
#Make sure to put the dependencies in requirements.txt file. You can use the following command to create it (you have to be in a virtual environment):
#pip freeze > requirements.txt
#Then go back to your local version of the app, and click the Deploy button in the top corner. And choose to deploy to Streamlit Community Cloud for free. Then click Deploy.

