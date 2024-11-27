import streamlit as st
import extra_streamlit_components as stx
import time
from streamlit_extras.switch_page_button import switch_page
from datetime import date, timedelta

st.set_page_config(layout="wide") 
st.header("Summary of your team progress")

today = date.today()
st.write("Here we summarize your learning progress up to ", today)

my_coursetime = st.progress(20, text="You have completed 3/ 15 study weeks of this course")
my_assignment = st.progress(20, text="You have completed 5/ 25 exercises in this course")
my_milestones = st.progress(33, text="You have completed 1/ 3 obligatory milestones in this course")
my_meeting = st.progress(33, text="You have completed 1/ 10 obligatory meetings in this course")
my_agile = st.progress(33, text="You have completed 5/ 10 suggested Agile practices in this course")
my_product = st.progress(10, text="You have completed 2/ 20 requirements in this course")

st.write("Here is our feedback on your progress")

st.write("Team: It looks like you have established your team! Do you get more meeting with other team members? Have you considered using a team contract to improve commitment within the team?")
st.write("Customer: Here is the summary of your conversation with the customer so far. Make sure the request from the customers correctly understood!")
st.write("Knowledge module: At this time, you should have completed module 2 with creating WBS for your project. Are you not sure if it is not correct? Send an email to the lecturer for feedback: anguatusn.no")
st.write("Process: Do you define how you and teammates will work together? We suggest to follow Scrum method. Let start the first Srpint. More information, read Module 4")
st.write("Product: It is still early to work with the website now. However, you might want to look at websites about HTML, CSS to learn about web development!")
st.write("Report: It is early to work with the report now. Obligagory Assignment 1 is the closet formal milestone.")
