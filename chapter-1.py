import streamlit as st

st.title("Hello, Streamlit!")
st.subheader("This is a simple Streamlit app.")
st.text("You can use this app to display text, images, and more.")
st.write("Streamlit makes it easy to create web apps for data science and machine learning projects.")

# selectbox for user input
cars = st.selectbox(
    'Choose an Car:',
    ['select', 'BMW', 'Mercedes', 'Audi', 'Toyota', 'Honda']
)
st.write(f"You selected: {cars}")
st.success("You have successfully selected a car!")