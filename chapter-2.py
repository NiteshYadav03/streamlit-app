import streamlit as st

st.title("Welcome to Chapter 2 of Streamlit!")

if st.button("Click Me!"):
    st.write("You clicked the button!")

# add checkbox for user input
if st.checkbox("Show/Hide"):
    st.write("Checkbox is checked!")
else:
    st.write("Checkbox is unchecked!")


# radio button for user input
options = st.radio(
    'Select an option:',
    ['Option 1', 'Option 2', 'Option 3']
)
st.write(f"You selected: {options}")
st.info("You have successfully selected an option!")

# slider for numerical input
number = st.slider("Select a number:", 0, 100, 50)
st.write(f"You selected the number: {number}")
 
# take inputs
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25)
st.write(f"Hello {name}, you are {age} years old!")

float_value = st.text_input("Enter a float value:")
if float_value:
    try:
        float_value = float(float_value)
        st.write(f"You entered the float value: {float_value}")
    except ValueError:
        st.error("Please enter a valid float value.")

# dob input
dob = st.date_input("Select your date of birth:")