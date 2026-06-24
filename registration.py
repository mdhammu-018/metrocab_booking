import streamlit as st
st.title("Registration Page")
name=st.text_input("Enter Full Name:")
email=st.text_input("Enter Email:")
mobile=st.text_input("Enter Mobile Number:")
course=st.selectbox("Select Course:",["Python","Java","C++","Data Science"])
if st.button("Registration"):
    if not name or not email or not mobile:
        st.warning("Please fill all the fields")
    else:
        st.success("Registration done!")
        st.balloons()
