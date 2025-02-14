import streamlit as st
import requests
from read_webp import convert_webp


url = 'https://api.nasa.gov/planetary/apod?api_key=YJhjhLUJNuTI7NIerE0nddxKwrAqgC2MYFTWy770'

response = requests.get(url)
content = response.json()

col1, col2 = st.columns(2)
with col1:
    st.title('Lost in Time & Thought')
with col2:
    st.write('01012003')

time = convert_webp('images/time.webp')
st.image(time,width=500)
st.write("We don't know tomorrow because we can't accurately remember yesterday.")

study_tomorrow = convert_webp('images/todayStudy1.webp')
st.image(study_tomorrow, width=500)
st.write("Even if we make every effort to study today in order to remember it tomorrow, it remains impossible to truly "
         "know tomorrow. This is because we experience today through the lens of our emotions, which cloud our "
         "minds—causing us to interpret, calculate, and decide based on how we feel in the moment.")

cursed_love = convert_webp('images/cursedLove.webp')
st.image(cursed_love, width=500)
st.write("This is why I despise anything that stirs my emotions. I try my best to avoid them—especially YOU. I can’t "
         "seem to control myself; I crave more of you, even though I know it’s destructive. Yet, no matter how hard I "
         "try, I just can’t stop wanting you")

destructive_path = convert_webp('images/destructive_path.webp')
st.image(destructive_path, width=500)
st.write("This road leads to destruction—I know it, yet I can't stop walking. It’s like a game of chess; I’ve played out "
         "every possible move in my mind, and they all lead to the same end—my destruction.")

destructive_growth = convert_webp('images/destructive_growth.webp')
st.image(destructive_growth, width=500)
st.write("Maybe destruction is necessary for growth. Maybe that’s the mindset that keeps me walking this road—or maybe, "
         "I’m just addicted to you… to destruction")

growth_illusion = convert_webp('images/growth_illusion.webp')
st.image(growth_illusion, width=500)
st.write("Which means I do know tomorrow—I just choose to ignore the destruction caused by yesterday’s decisions. "
         "Because, in the end, we are pleasure-seeking beings… chasing the pleasure of you and the illusion of growth")