import streamlit as st
from streamlit_extras.stateful_button import button

def streamlit_ui(main_title):
    st.set_page_config(page_title='xAI Books '+main_title, page_icon="🚀", )
    st.title(main_title)  # not accepting default

    st.markdown("""
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://omnidevx.netlify.app/logo/awsLogo.png);
                background-size: 250px; /* Set the width and height of the image */
                background-repeat: no-repeat;
                padding-top: 160px;
                background-position: 35px -30px;
            }
        </style>
        """,
                unsafe_allow_html=True,
                )

    # if 'authenticated' not in st.session_state:
    #     st.session_state.authenticated = False
    #
    # if not st.session_state.authenticated:
    #     password = st.text_input("Enter password", type="password")
    #     if password == "Semantic":
    #         st.session_state.authenticated = True
    #         st.write('welcome')
    #     else:
    #         st.stop()
