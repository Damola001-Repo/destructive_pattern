import streamlit as st
from read_webp import convert_webp
import json

col1, col2 = st.columns(2)
with col1:
    st.title('Love; My Destructive Pattern')
with col2:
    st.write('01102003')

with open('content.json', 'r') as file:
    content = json.load(file)

for i in content:
    time = convert_webp(i['image'])
    st.image(time,width=500)
    st.write(i['content'])