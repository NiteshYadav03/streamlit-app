import streamlit as st

st.title("Welcome to Chapter 3 of Streamlit!")

# make colums   
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Column 1")
    st.write("This is the first column.")
    st.button("Button in Column 1")
with col2:
        st.header("Column 2")
        st.write("This is the second column.")
        st.button("Button in Column 2")
with col3:
    st.header("Column 3")
    st.write("This is the third column.")
    st.button("Button in Column 3")

# add image
# st.image("https://www.shutterstock.com/image-photo/traveler-woman-arms-raised-triumph-260nw-2457990309.jpg",  
#          caption="Streamlit Image",
#          use_column_width=True,
#          width=10)

# sidebar for user input
st.sidebar.title("User Input")
st.sidebar.subheader("Select your preferences")
option = st.sidebar.selectbox( "Select your favorite color", ["Red", "Green", "Blue"])

with st.expander("More Options"):
    st.write("You can add more options here.")
    st.checkbox("Check me out!")
    st.radio("Choose one:", ["Option A", "Option B", "Option C"])

st.markdown("""
### Markdown Example)
You can use **Markdown** to format text in Streamlit.
- **Bold Text**
- *Italic Text*
```python
            # Python code   
def hello_world():
    print("Hello, World!")
          
           """ )