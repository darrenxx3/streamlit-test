#importing libraries
import streamlit as st
import pandas as pd
tabel =pd.DataFrame({"Anime": ["Kanojo Okarishimasu","Naruto","Bleach","Frieren","Cyberpunk Edgerunners","Roshidere"], "Category": [11,12,13,14,15,16]})

st.title("Hello World, I'm Darren a weeb")
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

st.write("# h1")
st.metric(label="Wind Speed", value="190ms-1", delta="-1.4ms\^-1")
st.table(tabel)
st.dataframe(tabel)

#dataframe and table are not the same

#adding image
st.image("chizuru 2 edit.jpg", caption="My Waifu", width=600)

#adding audio
st.write("Different Heaven")
st.audio("Different Heaven - Far Away [NCS Release].mp3")

st.video("outro.mp4")
