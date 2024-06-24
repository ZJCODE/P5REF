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
            color: #f58025; /* Set link color */
        }
        </style>
        <div class="footer">
            可在 <a href="https://artplay.streamlit.app/">ArtPlay</a> 在线编写代码并学习使用
        </div>
        """,
        unsafe_allow_html=True
    )