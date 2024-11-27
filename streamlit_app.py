# streamlit_app.py - Streamlit Frontend
import streamlit as st
import requests

def main():
    """
    Streamlit application for interacting with the addition API
    """
    # Set page title and configuration
    st.set_page_config(page_title="Number Addition App", page_icon=":calculator:")
    
    # Title and description
    st.title("Number Addition App")
    st.write("Enter two numbers to get their sum via API")
    
    # Input fields for numbers
    col1, col2 = st.columns(2)
    
    with col1:
        a = st.number_input("Enter first number", value=0, step=1)
    
    with col2:
        b = st.number_input("Enter second number", value=0, step=1)
    
    # Button to trigger API call
    if st.button("Add Numbers"):
        try:
            # Make API call
            response = requests.get(
                "http://localhost:8000/content", 
                params={"a": a, "b": b}
            )
            
            # Check if request was successful
            if response.status_code == 200:
                result = response.json()['result']
                st.success(f"The sum of {a} and {b} is: {result}")
            else:
                st.error("Failed to get result from API")
        
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to API: {e}")

if __name__ == "__main__":
    main()