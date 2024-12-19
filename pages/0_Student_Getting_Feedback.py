import streamlit as st
from openai import OpenAI
import os
#from decouple import config
import openai
import streamlit as st
import tiktoken
import sys
sys.path.append("/PRO1000")
import chatbot_utils
#from streamlit_chat import message
from email.policy import default
from pymongo import MongoClient
from pymongo.server_api import ServerApi
st.set_page_config(layout = "wide", page_title="StartupGPT")
#import app_components as components 
#import chatbot_utils as cu

client = OpenAI(api_key=st.secrets["OPENAI_KEY"])
 
cathy_line =''
jim_line = ''
starting_line = ''
def get_response(jim_line):
    output =  "dummy"
    return output 
                                                                                                                                                                                                                 
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["General", "Module 1", "Module 2", "Module 3", "Module 4", "Module 5", "Module 6", "Module 7", "Module 8"])


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def get_course_description(type):
    pathname = f"PRO1000/{type}.txt"    
    try:
        with open(pathname, "r") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"Error: File '{pathname}' not found."
    except Exception as e:
        return f"Error: {e}"

def clear_cache():
    for key in st.session_state.keys():
        del st.session_state[key]
    if "messages" not in st.session_state:
        st.session_state.messages = []

with tab1:
   

with tab2:
    st.image("https://miro.medium.com/v2/resize:fit:720/format:webp/1*fiEXMWcFg328ztjZEWYlpg.jpeg", width=400)
    em1 = st.radio(
        "Choose the exercise to practice",
        ["Exercise1", "Exercise2", "Exercise3", "Exercise4"],
        captions=[
            "Characterizing a software project.",
            "Stakeholder analysis.",
            "Project management areas.",
            "SWOT Analysis.",
        ],
    ) 
    with st.expander("Submit your exercise here"):
        #if "openai_model" not in st.session_state:
        #    st.session_state["openai_model"] = "gpt-4o"        
        if "messages" not in st.session_state:
            st.session_state.messages = []        
        #for message in st.session_state.messages:
        #     if message["role"] in ["user", "assistant"]:
        #        with st.chat_message(message["role"]):
        #            st.markdown(message["content"])        
        if prompt_tab2 := st.text_area("What is up?"):
             if em1 == "Exercise1":
             #     clear_cache()
             #     st.session_state.messages.append({"role": "system", "content": get_course_description("project")})
             #     st.session_state.messages.append({"role": "system", "content": "Act as a lecturer in a software project management course. Students are asked to elaborate attributes of the given project regarding: A project has a unique purpose, A project is temporary, A project is developed using progressive elaboration, A project requires resources, often from various areas, A project should have a primary customer and A project involves uncertainty. Evaluation criteria is the completeness and correctness of identified attributes for the given project, logical and quality of the arguments. Create a rubric for yourself with five levels: Excellent (5)	Proficient (4)	Satisfactory (3)	Needs Improvement (2)	Unsatisfactory (1). Write feedback with the template as follows: First of all, write one sentence to introduce the feedback purpose and, the connection of doing this exercise to the course learning objective. Secondly, in the next paragraph write a brief evaluation using the rubric. Give the assessment out of the full scale. Thirdly , in the next paragraph, briefly summarize the strengths and weaknesses of the answer. Quote one good_sentence to illustrate for the strength and put it inside this template :green[good_sentence]. Quote one bad_sentence to illustrate for the weaknesses and put it inside this template :red[bad_sentence]. Fourthly, a headline Action points and then followed bullet points at most three actionable points to improve the student answer. Finally, write a simple but curious and interesting question in the end to motivate the student to engage in discussing the given feedback. Write all in good Norwegian."})
             #if em1 == "Exercise2":
                  #clear_cache()
                  #st.session_state.messages.append({"role": "system", "content": get_course_description("project")})
                  #st.session_state.messages.append({"role": "system", "content": "Act as a lecturer in a software project management course. Students are asked to list all potential stakeholders. Classify them based on their interest, influence, and impact on the project. Anticipate any potential conflicts of interest in term of website functionalities among them. Evaluation criteria is the completeness and correctness of identified stakeholders, reasonable arguments for their interest, influence and impact, and. Create a rubric for yourself with five levels: Excellent (5)	Proficient (4)	Satisfactory (3)	Needs Improvement (2)	Unsatisfactory (1). Write feedback with the template as follows: First of all, write one sentence to introduce the feedback purpose and, the connection of doing this exercise to the course learning objective. Secondly, in the next paragraph write a brief evaluation using the rubric. Give the assessment out of the full scale. Thirdly , in the next paragraph, briefly summarize the strengths and weaknesses of the answer. Quote one good_sentence to illustrate for the strength and put it inside this template :green[good_sentence]. Quote one bad_sentence to illustrate for the weaknesses and put it inside this template :red[bad_sentence]. Fourthly, a headline Action points and then followed bullet points at most three actionable points to improve the student answer. Finally, write a simple but curious and interesting question in the end to motivate the student to engage in discussing the given feedback. Write all in good Norwegian."})
             #if em1 == "Exercise3":
             #     clear_cache()
             #     st.session_state.messages.append({"role": "system", "content": "Act as a lecturer in a software project management course. Students are asked to answer What is the role of a project manager ? What aspects will you need to plan if you are responsible for implementing this project? Give a brief explaination. The answer is Project managers must not only strive to meet specific scope, time, cost, and quality goals of projects, they must also facilitate the entire process to meet the needs and expectations of the people involved in or affected by project activities. Among the areas in Project Management Body of Knowledge, for a student project the relevant areas are: scope management, schedule management, quality management, risk management, communication management and resource management. Evaluation criteria is the completeness and correctness of project manager's role, the relevanced of identified management area for the student project. Create a rubric for yourself with five levels: Excellent (5)	Proficient (4)	Satisfactory (3)	Needs Improvement (2)	Unsatisfactory (1). Write feedback with the template as follows: First of all, write one sentence to introduce the feedback purpose and, the connection of doing this exercise to the course learning objective. Secondly, in the next paragraph write a brief evaluation using the rubric. Give the assessment out of the full scale. Thirdly , in the next paragraph, briefly summarize the strengths and weaknesses of the answer. Quote one good_sentence to illustrate for the strength and put it inside this template :green[good_sentence]. Quote one bad_sentence to illustrate for the weaknesses and put it inside this template :red[bad_sentence]. Fourthly, a headline Action points and then followed bullet points at most three actionable points to improve the student answer. Finally, write a simple but curious and interesting question in the end to motivate the student to engage in discussing the given feedback. Write all in good Norwegian."})
             #if em1 == "Exercise4":
             #     clear_cache()
             #     st.session_state.messages.append({"role": "system", "content": "Act as a lecturer in a software project management course. Students are asked to team's Strengths, Weaknesses, Opportunities, and Threats. It's an excellent way for team members to understand their collective capabilities and areas that need improvement. This exercise fosters open communication and strategic planning. Evaluation criteria is the completeness and relevance of the given content regarding ability of a first year student taking courses in a full time bachelor program. Create a rubric for yourself with five levels: Excellent (5)	Proficient (4)	Satisfactory (3)	Needs Improvement (2)	Unsatisfactory (1). Write feedback with the template as follows: First of all, write one sentence to introduce the feedback purpose and, the connection of doing this exercise to the course learning objective. Secondly, in the next paragraph write a brief evaluation using the rubric. Give the assessment out of the full scale. Be easy here so if students answer all the four SWOT points the should get at least from 3/5. Thirdly , in the next paragraph, briefly summarize the strengths and weaknesses of the answer. Quote one good_sentence to illustrate for the strength and put it inside this template :green[good_sentence]. Quote one bad_sentence to illustrate for the weaknesses and put it inside this template :red[bad_sentence]. Fourthly, a headline Action points and then followed bullet points at most three actionable points to improve the student answer. Finally, write a simple but curious and interesting question in the end to motivate the student to engage in discussing the given feedback. Write all in good Norwegian."})
             #st.session_state.messages.append({"role": "user", "content": prompt_tab2})
             #with st.chat_message("user"):
                  st.markdown(prompt_tab2)
             #with st.chat_message("assistant"):
             #     user_messages = [
             #        {"role": m["role"], "content": m["content"]}
             #         for m in st.session_state.messages
             #     ]
             #     user_messages_string = " ".join([m["content"] for m in user_messages])
             #     if(num_tokens_from_string(user_messages_string, "gpt-4o")<2000):
                  st.markdown(f"The total number of tokens used is **{num_tokens_from_string(get_course_description("exercise4"), "gpt-4o")}**.")
                  stream = client.chat.completions.create(
                      model="gpt-4o",
                      messages=
                          [
                            {
                              "role": "system",
                              "content": [{ "type": "text", "text": get_course_description("exercise4") }]
                            },
                            {
                              "role": "user",
                              "content": [{ "type": "text", "text": prompt_tab2 }]
                            }
                          ],
                      stream=True,
                      temperature=0.4
                  )
                  response = st.write_stream(stream)
                 #     st.session_state.messages.append({"role": "assistant", "content": response})
                 # else:
                 #     st.markdown(f"The input you entered is too long. The total words you have now is **{num_tokens_from_string(user_messages_string, "gpt-4o")}**. The total number of tokens used is **{user_messages_string}**. Keep the input less than 2000 words!")
        #with st.form("my_form1"):
        #    jim_email= st.text_input("Email to receive feedback", "12345678@std.usn")
        #    jim_line = st.text_area("Write your exercise here","", height=200)
        #    submitted = st.form_submit_button("Submit")
with tab3:
    st.image("https://cdn-cnhfh.nitrocdn.com/jsHsUxJJAapjeJICfnGvtaAAOHZlckTe/assets/images/optimized/rev-dfbdbb8/e360-media.s3.amazonaws.com/2024/07/07160602/2290114_ProjectScopeManagementPMA-ControlScopeProcessPMP_070524.jpg", width=400)
    em2 = st.radio(
        "Choose the exercise to practice",
        ["Exercise1", "Exercise2", "Exercise3", "Exercise4"],
        captions=[
            "Characterizing a software project.",
            "Stakeholder analysis.",
            "Project management areas.",
            "SWOT Analysis.",
        ],
    ) 
    with st.expander("Submit your exercise here"):
        if "messages" not in st.session_state:
            st.session_state.messages = []        
        if prompt_tab3 := st.text_area("What is up?"):
             #if em2 == "Exercise5":
             #if em2 == "Exercise6":
             #if em2 == "Exercise7":
             if em2 == "Exercise8":
                  st.markdown(prompt_tab3)
                  st.markdown(f"The total number of tokens used is **{num_tokens_from_string(get_course_description("exercise5"), "gpt-4o")}**.")
                  stream = client.chat.completions.create(
                      model="gpt-4o",
                      messages=
                          [
                            {
                              "role": "system",
                              "content": [{ "type": "text", "text": get_course_description("exercise5") }]
                            },
                            {
                              "role": "user",
                              "content": [{ "type": "text", "text": prompt_tab3 }]
                            }
                          ],
                      stream=True,
                      temperature=0.4
                  )
                  response = st.write_stream(stream)
with tab4:
    st.image("https://images.squarespace-cdn.com/content/v1/56acc1138a65e2a286012c54/1587053683921-RPMQIPHXBQFOIZOXRTGD/time-management-1966396_1920.jpg", width=400)
    col11, col12, col13 = st.columns(3)
    with col11: 
        st.button("Network Diagram and Critical Path Analysis",key="ex11",use_container_width=True) 
    with col12:
        st.button("Gantt Chart",key="ex12",use_container_width=True) 
    with col13: 
        st.button("Time control",key="ex13",use_container_width=True) 
    with st.expander("Submit your exercise here"):
        with st.form("my_form3"):
            jim_email= st.text_input("Email to receive feedback", "12345678@std.usn")
            jim_line = st.text_area("Write your exercise here","", height=200)
            submitted = st.form_submit_button("Submit")
with tab5:
    st.image("https://cortouchmedia.com.ng/wp-content/uploads/2023/05/prototyping.png", width=400)
    col14, col15 = st.columns(2)
    with col14: 
        st.button("Low Fidelity Prototype",key="ex14",use_container_width=True) 
    with col15:
        st.button("Prototying with Figma",key="ex15",use_container_width=True) 
    with st.expander("Submit your exercise here"):
        with st.form("my_form4"):
            jim_email= st.text_input("Email to receive feedback", "12345678@std.usn")
            jim_line = st.text_area("Write your exercise here","", height=200)
            submitted = st.form_submit_button("Submit")

with tab6:
    st.image("https://scrumorg-website-prod.s3.amazonaws.com/drupal/inline-images/2023-09/scrum-framework-9.29.23.png", width=400)
    col16, col17 = st.columns(2)
    with col16: 
        st.button("Scrum Project Management",key="ex16",use_container_width=True) 
    with col17:
        st.button("Sprint execution and report",key="ex17",use_container_width=True) 
    with st.expander("Submit your exercise here"):
        with st.form("my_form5"):
            jim_email= st.text_input("Email to receive feedback", "12345678@std.usn")
            jim_line = st.text_area("Write your exercise here","", height=200)
            submitted = st.form_submit_button("Submit")
with tab7:
    st.image("https://www.intuition.com/wp-content/uploads/2023/07/Risk-Management-Process.png", width=400)
    col18, col19 = st.columns(2)
    with col18: 
        st.button("Risk Management Table",key="ex18",use_container_width=True) 
    with col19:
        st.button("Communication Management Table",key="ex19",use_container_width=True) 
    with st.expander("Submit your exercise here"):
        with st.form("my_form6"):
            jim_email= st.text_input("Email to receive feedback", "12345678@std.usn")
            jim_line = st.text_area("Write your exercise here","", height=200)
            submitted = st.form_submit_button("Submit")

with tab8:
    st.image("https://www.tatvasoft.com/outsourcing/wp-content/uploads/2022/11/difference-between-software-testing-vs-quality-assurance.jpg", width=400)
    col20, col21, col22 = st.columns(3)
    with col20: 
        st.button("Non-functional requirements",key="ex20",use_container_width=True) 
    with col21:
        st.button("Test plan",key="ex21",use_container_width=True) 
    with col22:
        st.button("Usability test",key="ex22",use_container_width=True) 
    with st.expander("Submit your exercise here"):
        with st.form("my_form7"):
            jim_email= st.text_input("Email to receive feedback", "12345678@std.usn")
            jim_line = st.text_area("Write your exercise here","", height=200)
            submitted = st.form_submit_button("Submit")

with tab9:
    st.image("https://business.adobe.com/blog/basics/media_1f189f1c2c3c424441541e86d7b8b729ad795f205.jpeg", width=400)
    col23, col24, col25 = st.columns(3)
    with col23: 
        st.button("Sprint planning meeting",key="ex23",use_container_width=True) 
    with col24:
        st.button("Sprint review meeting",key="ex24",use_container_width=True) 
    with col25:
        st.button("Retrospective meeting",key="ex25",use_container_width=True) 
    with st.expander("Submit your exercise here"):
        with st.form("my_form8"):
            jim_email= st.text_input("Email to receive feedback", "12345678@std.usn")
            jim_line = st.text_area("Write your exercise here","", height=200)
            submitted = st.form_submit_button("Submit")
