import streamlit as st

st.set_page_config(
    page_title="Calculator",
    page_icon=""
)

st.title(" My Calculator")
st.write("Simple Calculator using Python")

# Take input
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Select operation
operation = st.selectbox(
    "Choose operation",
    [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (*)",
        "Division (/)",
        "Remainder (%)"
    ]
)

# Calculate
if st.button("Calculate"):

    if operation == "Addition (+)":
        result = num1 + num2
        st.success(f"Result: {result}")

    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.success(f"Result: {result}")

    elif operation == "Multiplication (*)":
        result = num1 * num2
        st.success(f"Result: {result}")

    elif operation == "Division (/)":
        if num2 == 0:
            st.error("Cannot divide by zero!")
        else:
            result = num1 / num2
            st.success(f"Result: {result}")

    elif operation == "Remainder (%)":
        if num2 == 0:
            st.error("Cannot find remainder with zero!")
        else:
            result = num1 % num2
            st.success(f"Remainder: {result}")