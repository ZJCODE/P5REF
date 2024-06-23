import streamlit as st

def footer():
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #ffffff; /* White background */
            text-align: center;
            padding: 10px 0;
            color: #888888; /* Black text */
            font-size: 14px; /* Font size */
        }
        .footer a {
            text-decoration: none; /* Remove underline from links */
            color: #888888; /* Set link color */
        }
        </style>
        <div class="footer">
            &copy; 2024 Made by <a href="https://www.zjun.life/">ZJun</a>
        </div>
        """,
        unsafe_allow_html=True
    )