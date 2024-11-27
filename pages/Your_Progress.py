import streamlit as st
import extra_streamlit_components as stx
import time
from streamlit_extras.switch_page_button import switch_page
from datetime import date, timedelta

st.set_page_config(layout="wide") 
st.header("Summary of your team progress")

today = date.today()
st.write("Here we summarize your learning progress up to ", today)

my_assignment = st.progress(20, text="You have completed 5/ 25 exercises in this course")
my_milestones = st.progress(33, text="You have completed 1/ 3 obligatory milestones in this course")
my_meeting = st.progress(33, text="You have completed 1/ 10 obligatory meetings in this course")
my_agile = st.progress(33, text="You have completed 5/ 10 suggested Agile practices in this course")
my_product = st.progress(10, text="You have completed 2/ 20 requirements in this course")
