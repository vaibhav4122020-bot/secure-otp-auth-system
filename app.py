import streamlit as st
from auth import register_user,login_user,generate_otp
from email_service import send_otp

st.title("Secure OTP Authentication System")

menu = ["Login","Register","Forgot Password"]
choice = st.sidebar.selectbox("Menu",menu)

if choice=="Register":
    st.subheader("Create Account")
    email = st.text_input("Email")
    password = st.text_input("Password",type="password")

    if st.button("Register"):
        register_user(email,password)
        st.success("Account created successfully")

elif choice=="Login":
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password",type="password")

    if st.button("Login"):
        user = login_user(email,password)
        if user:
            st.success("Login Successful")
        else:
            st.error("Invalid Credentials")

elif choice=="Forgot Password":
    st.subheader("Reset Password")
    email = st.text_input("Enter Email")

    if st.button("Send OTP"):
        otp = generate_otp()
        send_otp(email,otp)
        st.session_state["otp"] = otp
        st.success("OTP sent to email")

    otp_input = st.text_input("Enter OTP")

    if st.button("Verify OTP"):
        if otp_input == st.session_state.get("otp"):
            st.success("OTP Verified")
        else:
            st.error("Wrong OTP")
