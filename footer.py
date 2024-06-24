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
            color: #FF671D",; /* Set link color */
        }
        </style>
        <div class="footer">
            &copy; Play at <a href="https://artplay.streamlit.app/">ArtPlay</a>
        </div>
        """,
        unsafe_allow_html=True
    )