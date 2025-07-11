import streamlit as st
import requests 

# live currency converter
def currency_converter():
    st.title("Live Currency Converter")
    
    # Input for amount
    amount = st.number_input("Enter amount in USD:", min_value=0.0, step=0.01)
    
    # Fetching exchange rates
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
     
    data = response.json()
    
    # Display available currencies
    currencies = list(data['rates'].keys())
    selected_currency = st.selectbox("Select currency to convert to:", currencies)
    
    # Conversion logic
    if st.button("Convert"):
        rate = data['rates'][selected_currency]
        converted_amount = amount * rate
        st.success(f"{amount} USD is equal to {converted_amount:.2f} {selected_currency}")

currency_converter()