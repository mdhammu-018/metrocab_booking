import streamlit as st
import random

st.title("Friendship Calculator")

n1 = st.text_input("Your Name")
n2 = st.text_input("Your Friend Name")

if st.button("Check %"):
    if n1 and n2:
        s = random.randint(90, 100)
        st.success(f"{n1} ❤️ {n2}\n\nFriendship score: {s}%")
        st.balloons()
    else:
        st.warning("Please enter both names.")