import streamlit as st

st.title("Hello World, I'm Darren")
st.subheader("This is streamlit testing")
st.header("Testing")
st.text("Streamlit text")
st.markdown("**Bold Text**")
st.markdown("[Anime](https://www.9animetv.to)")
st.markdown("---")
st.markdown("`This is code block`")
json= {"a": "1,2,3"}
st.json(json)

code ="""
print("hello world")
def funct():
    return 0;"""
st.code(code, language="python")