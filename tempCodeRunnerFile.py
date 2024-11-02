import streamlit as st

pg = st.navigation([st.Page("main.py"), st.Page("uber_pickups.py")])
pg.run()