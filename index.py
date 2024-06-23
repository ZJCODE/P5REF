import streamlit as st

# Set page config
st.set_page_config(page_title='P5 Reference',
                   page_icon='🎨', 
                   layout='wide',
                   initial_sidebar_state='collapsed')

from streamlit_navigation_bar import st_navbar
from references import references
from footer import footer

styles = {
    "nav": {
        "background-color": "white",
        "justify-content": "left",
        "font-size": "20px",
        "padding": "5px",
    },
    "span": {
        "padding": "75px",
        "color": "#FF671D",
    },
}


page_select = st_navbar(    
                 pages=["P5 参考手册"],
                 styles = styles,
                 options={"use_padding": False,"show_menu": False,"show_sidebar": False}
                 )

references()

footer()