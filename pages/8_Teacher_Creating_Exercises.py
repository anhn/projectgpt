import streamlit as st
import extra_streamlit_components as stx
import time
from streamlit_extras.switch_page_button import switch_page
from datetime import date, timedelta


st.set_page_config(layout="wide") 

st.header("Develop the exercise here")

st.write("Course learning objectives")
st.text_input("Exercise name", "Stakeholder Analysis")
st.text_area(
    "Exercise Description",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
)
st.text_area(
    "Evaluation Criteria",
    "Criteria 1: "
    "Criteria 2: "
    "Criteria 3: "
    "...",
)
st.button("Generate an example answer")
st.text_area(
    "Example answer"
)
st.button("Generate an example feedback")
st.text_area(
    "Example feedback"
)
st.button("Save")
