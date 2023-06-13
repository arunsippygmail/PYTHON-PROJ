import streamlit as st

st.set_page_config(layout="wide")

col1,col2=st.columns(2)


with col1:
    st.image("images/photo.png",width=400)
with col2:
    st.title("Arun Sippy")
    st.title('A title with _italicssss_ [alphbets] :blue[colors] and emojis :sunglasses:')

    Content=""" Hi I am arunsippy
                _I live in INdia_. TO explore new things is my Hobby"""
    st.info(Content)
st.write("U can find some Apps for ur selves below")