import streamlit as st
import extra_streamlit_components as stx
import time
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(layout="wide") 

st.header("Reflecting on your learning progress")

with st.form("my_form"):
      st.write("To understand your progress, please fill in the following information:")
      st.caption("Milestone 1 - Project initiation")
      st.write("Team formation")
      st.selectbox("Stage", options=["No team found", "Found a team", "Agree on way of working", "Storming time", "Performing time"], placeholder="Select an option", index=None)
      st.write("Project specification")
      st.checkbox("Read project specification")
      st.checkbox("Chat with the customer")
      st.checkbox("Understand what need to do")
      st.checkbox("Understand what should not do")
      st.checkbox("Describe the functional requirements")
      st.checkbox("Describe the non-functional requirements")
      st.write("Project tool configuration") 
      st.checkbox("Set up a project repository - Github, Dropbox, etc")
      st.checkbox("Set up communication tool - Team, Messenger, Slack, etc")
      st.checkbox("Set up a project management board - Trello, Monday, etc")
      st.checkbox("Set up a software development environment - Visual Studio, Sublime, etc")
      st.checkbox("Set up a document editor tool - Word 365, Google Doc, etc")
      st.checkbox("Learn to use LearnIX")
      st.write("Scope planning")
      st.selectbox("Stage", options=["Nothing done", "Read about WBS", "Understand WBS", "Create a WBS", "Get the WBS validated"], placeholder="Select an option", index=None)
      st.write("Time planning")
      st.selectbox("Stage", options=["Nothing done", "Read about Gantt Chart", "Understand Gantt Chart", "Create a Gantt Chart", "Get the Gantt Chart validated"], placeholder="Select an option", index=None)
      st.caption("Milestone 2 - Project execution")
      st.write("Prototyping")
      st.write("Agile development")
      st.write("Risk management")
      st.write("Communication management")
      st.caption("Milestone 3 - Project closing")
      st.write("Testing")
      st.write("Report")
      st.write("Deployment")
      st.form_submit_button("Save form")

st.header("Summary of your learning progress")

st.write("Here we summarize your learning progress!")
st.write("Team: It looks like you have established your team! Do you get more meeting with other team members? Have you considered using a team contract to improve commitment within the team?")
st.write("Customer: Here is the summary of your conversation with the customer so far. Make sure the request from the customers correctly understood!")
st.write("Knowledge module: At this time, you should have completed module 2 with creating WBS for your project. Are you not sure if it is not correct? Send an email to the lecturer for feedback: anguatusn.no")
st.write("Process: Do you define how you and teammates will work together? We suggest to follow Scrum method. Let start the first Srpint. More information, read Module 4")
st.write("Product: It is still early to work with the website now. However, you might want to look at websites about HTML, CSS to learn about web development!")
st.write("Report: It is early to work with the report now. Obligagory Assignment 1 is the closet formal milestone.")
