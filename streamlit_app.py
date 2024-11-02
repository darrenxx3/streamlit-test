import streamlit as st

pg = st.navigation([st.Page("pages/main.py"), st.Page("pages/uber_pickups.py")])
pg.run()