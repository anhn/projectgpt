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
 
with tab1:
    col01, col02 = st.columns([1, 2])
    with col01:
        st.video("pages/game.mp4")
    with col02:
        st.write("Q&A about the course!")
    #with st.form("my_form"):
        #jim_line = st.text_area("Write your question here","", height=70)
        #submitted = st.form_submit_button("Submit")
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4o"        
    if "messages" not in st.session_state:
        st.session_state.messages = []        
    for message in st.session_state.messages:
         if message["role"] in ["user", "assistant"]:
             with st.chat_message(message["role"]):
                st.markdown(message["content"])        
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "system", "content": get_course_description("description")})
        st.session_state.messages.append({"role": "system", "content": get_course_description("report_guideline")})
        st.session_state.messages.append({"role": "system", "content": get_course_description("project")})
        st.session_state.messages.append({"role": "system", "content": "Jeg har sykdom som migrene, og derfor kunne jeg ikke så mye komme på universitet. I forrige semester fortalte jeg om meg selv til deg. Jeg tar 2 busser for å komme til skolen. Det tar nesten 5 timer å gå og komme. Jeg skrevet mitt situasjon til student veileder som heter Hege. Hvis jeg er frisk, vil jeg gjøre en innsats for å delta på undervisning. Hvis det er mulig, kan du hjelpe meg å finne gruppe"})
        st.session_state.messages.append({"role": "assistant", "content": "This course is mainly group work, so I suggest you to come to the class at least for group arrangement. I can not just simply put you in a group. There needs some agreements among everyone in the group about how you will work and what to achieve in the end."})
        st.session_state.messages.append({"role": "system", "content": " jeg og gruppen lurer på når felles møte med kunden skal være? "})
        st.session_state.messages.append({"role": "assistant", "content": "We will have a schedule for each group to meet the customer, and will announce in canvas"})
        st.session_state.messages.append({"role": "system", "content": "And what do you think is a fair number when it comes to sprints, is it okay with 6 since were doing this project in around 12 weeks? One sprint over 2 weeks each time?"})
        st.session_state.messages.append({"role": "assistant", "content": "Two-week sprints are a standard duration in Agile. For student projects with many other duties, you can think of three-week sprints. You should plan for three months working in this project, so maybe a practical number of sprints are between three and five"})
        st.session_state.messages.append({"role": "system", "content": "Vi har en presentasjon på fredag. Jeg lurer på om den vil være foran hele gruppen?"})
        st.session_state.messages.append({"role": "assistant", "content": "Ja, alle gruppemedlemmer bør delta på presentasjonen. Hvordan dere velger å presentere – om én person tar ledelsen eller dere fordeler det – er opp til dere som gruppe. Lykke til! 😊"})
        st.session_state.messages.append({"role": "system", "content": "Unfortunately I have got the flu, so I can't attend the lecture on Friday."})
        st.session_state.messages.append({"role": "assistant", "content": "Thank you for letting me know—focus on resting and recovering, and feel free to reach out if you need any materials or assistance"})
        st.session_state.messages.append({"role": "system", "content": "jeg lurer på om hva betyr akkurat å skrive om problemstilling i Report, er det du mener å skrive om problemstilling i prosjekt eller?"})
        st.session_state.messages.append({"role": "assistant", "content": "Du kan problemet kundene har, og det er derfor de trenger å lage dette prosjektet. Du kan også angi mål eller mål for prosjektet, og forventningene til kundene."})
        st.session_state.messages.append({"role": "system", "content": "Lurte bare på om det er greit at vi er en gruppe på 5 stk? Vi har vært i gruppe tidligere og vil prøve å unngå å splittes."})
        st.session_state.messages.append({"role": "assistant", "content": "Hei Det er greit. Kan du skrive navnet till alle gruppe medlemer og sende via epost?"})
        st.session_state.messages.append({"role": "system", "content": "In Module 2 Exercise 3- It it enough short simple answers (A few sentences) or should write something more detailed?"})
        st.session_state.messages.append({"role": "assistant", "content": "Module 2 Exercise 3: a short answer is enough so long it can explain for your argument, decisions or analysis"})
        st.session_state.messages.append({"role": "system", "content": "Hei jeg ble kastet ut fra gruppa kan jeg få nye grupe vær så snill"})
        st.session_state.messages.append({"role": "assistant", "content": "Hei, jeg forstår situasjonen. Jeg skal undersøke hva som har skjedd og finne en løsning. Jeg vil enten hjelpe deg med å bli reintegrert i gruppa eller plassere deg i en ny gruppe. Jeg tar kontakt snart!"})
        st.session_state.messages.append({"role": "system", "content": "Is it okie one group member submit the assignment ?"})
        st.session_state.messages.append({"role": "assistant", "content": "Yes, you are working under a Group setting in Canvas and one member will delivery for the whole group."})
        st.session_state.messages.append({"role": "system", "content": "Hva er hovedmålet med PRO1000?"})
        st.session_state.messages.append({"role": "assistant", "content": "Hovedmålet med PRO1000 er å gi studentene praktisk erfaring med prosjektarbeid. Studentene arbeider i grupper for å planlegge, designe og utvikle en funksjonell nettside, samtidig som de lærer prosjektstyring og samarbeid."})
        st.session_state.messages.append({"role": "system", "content": "Hvilke ferdigheter vektlegges i dette faget?"})
        st.session_state.messages.append({"role": "assistant", "content": "Faget fokuserer på prosjektplanlegging, teamarbeid, webutvikling, dokumentasjon og presentasjonsferdigheter."})
        st.session_state.messages.append({"role": "system", "content": "Hvordan blir gruppeprestasjonen evaluert?"})
        st.session_state.messages.append({"role": "assistant", "content": "Gruppeprestasjonen vurderes basert på det endelige prosjektplanlegging, teamarbeid, prosjektleveransen, og finale dokumenter"})
        st.session_state.messages.append({"role": "system", "content": "Skal prosjektet være på norsk eller engelsk?"})
        st.session_state.messages.append({"role": "assistant", "content": "Prosjektet og rapporten bør som hovedregel være på norsk, med mindre annet er avtalt med faglærer."})
        st.session_state.messages.append({"role": "system", "content": "Hvordan bør vi fordele tiden for dette prosjektet?"})
        st.session_state.messages.append({"role": "assistant", "content": "For dette prosjektet bør de første ukene brukes til å bli kjent med prosjektet, definere mål og forventninger, samt gjøre nødvendig research. Deretter kan dere bruke tid på prosjektplanlegging, inkludert å etablere en backlog og definere roller og ansvar i gruppen. Når dette er på plass, kan dere gå over til implementeringsfasen, organisert i Scrum-sprinter. En typisk tilnærming kan være å bruke én til to uker på oppstart og planlegging, og deretter jobbe i sprintsykluser på to uker for å utvikle, teste og levere funksjonalitet. Husk å ha sprint reviews og retrospektiver for å evaluere fremdriften og justere planene underveis"})
        st.session_state.messages.append({"role": "system", "content": "Kan vi spørre studentassistenten om hjelp?"})
        st.session_state.messages.append({"role": "assistant", "content": "Ja, studentassistenter er tilgjengelige i labtimene eller via e-post for veiledning og støtte. Du kan bruke AI assistent her for spøsmåler om emne, prosjekt, oppgaver, etc"})
        st.session_state.messages.append({"role": "system", "content": "Hvordan fordeles vurderingen mellom individuell og gruppeinnsats?"})
        st.session_state.messages.append({"role": "assistant", "content": "Gruppens leveranser teller hovedsakelig for vurderingen, men individuell innsats kan være en faktor gjennom peer-review og deltakelse i presentasjonen."})
        st.session_state.messages.append({"role": "system", "content": "Hva hvis et gruppemedlem ikke bidrar?"})
        st.session_state.messages.append({"role": "assistant", "content": "Dokumenter problemet og diskuter det med faglærer eller studentassistent for å håndtere det på en passende måte."})     
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            user_messages = [
               {"role": m["role"], "content": m["content"]}
               for m in st.session_state.messages
               #if m["role"] == "user"   Include only user messages
            ]
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=user_messages,
                stream=True,
            )
            response = st.write_stream(stream)
            #response2 = client.audio.speech.create(
            #    model="tts-1",
            #    voice="nova",
            #    input=response
            #)
            #response2.write_to_file("output1.mp3")
            #with open("output1.mp3", "rb") as audio_file:
            #    st.audio(audio_file, format='audio/mp3')
        st.session_state.messages.append({"role": "assistant", "content": response})


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
        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = "gpt-4o"        
        if "messages" not in st.session_state:
            st.session_state.messages = []        
        for message in st.session_state.messages:
             if message["role"] in ["user", "assistant"]:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])        
        if prompt_tab2 := st.text_area("What is up?"):
             st.session_state.messages.append({"role": "system", "content": get_course_description("project")})
             if em1 == "Exercise2":
                  st.session_state.messages.append({"role": "system", "content": "Act as a lecturer in a software project management course. Students are asked to list all potential stakeholders. Classify them based on their interest, influence, and impact on the project. Anticipate any potential conflicts of interest in term of website functionalities among them."})
                  st.session_state.messages.append({"role": "system", "content": "Evaluation criteria is the completeness and correctness of identified stakeholders, reasonable arguments for their interest, influence and impact, and. Create a rubric for yourself with five levels: Excellent (5)	Proficient (4)	Satisfactory (3)	Needs Improvement (2)	Unsatisfactory (1). Write feedback with the template as follows: First of all, write one sentence to introduce the feedback purpose and, the connection of doing this exercise to the course learning objective. Secondly, in the next paragraph write a brief evaluation using the rubric. Give the assessment out of the full scale. Thirdly , in the next paragraph, briefly summarize the strengths and weaknesses of the answer. Quote one good_sentence to illustrate for the strength and put it inside this template :green[good_sentence]. Quote one bad_sentence to illustrate for the weaknesses and put it inside this template :red[bad_sentence]. Fourthly, a headline Action points and then followed bullet points at most three actionable points to improve the student answer. Finally, write a simple but curious and interesting question in the end to motivate the student to engage in discussing the given feedback. Write all in good Norwegian."})
             st.session_state.messages.append({"role": "user", "content": prompt_tab2})
             with st.chat_message("user"):
                  st.markdown(prompt_tab2)
             with st.chat_message("assistant"):
                  user_messages = [
                      {"role": m["role"], "content": m["content"]}
                      for m in st.session_state.messages
                  ]
                  user_messages_string = " ".join([m["content"] for m in user_messages])
                  print(num_tokens_from_string(user_messages_string, "gpt-4o"))
                  if(num_tokens_from_string(user_messages_string, "gpt-4o")<2000):
                      stream = client.chat.completions.create(
                          model=st.session_state["openai_model"],
                          messages=user_messages,
                          stream=True,
                      )
                      response = st.write_stream(stream)
                      st.session_state.messages.append({"role": "assistant", "content": response})
                  else:
                      st.markdown(f"The input you entered is too long. The total words you have now is **{num_tokens_from_string(prompt_tab2, "gpt-4o")}**. The total number of tokens used is **{num_tokens_from_string(user_messages_string, "gpt-4o")}** Keep the input less than 2000 words!")
        #with st.form("my_form1"):
        #    jim_email= st.text_input("Email to receive feedback", "12345678@std.usn")
        #    jim_line = st.text_area("Write your exercise here","", height=200)
        #    submitted = st.form_submit_button("Submit")
with tab3:
    st.image("https://cdn-cnhfh.nitrocdn.com/jsHsUxJJAapjeJICfnGvtaAAOHZlckTe/assets/images/optimized/rev-dfbdbb8/e360-media.s3.amazonaws.com/2024/07/07160602/2290114_ProjectScopeManagementPMA-ControlScopeProcessPMP_070524.jpg", width=400)
    col5, col6, col7, col8 = st.columns(4)
    with col5: 
        st.button("Github project setting",key="ex5",use_container_width=True) 
    with col6:
        st.button("Project Layout",key="ex6",use_container_width=True) 
    with col7: 
        st.button("Project success criteria",key="ex7",use_container_width=True) 
    with col8: 
        st.button("Requirement Gathering and Analysis",key="ex8",use_container_width=True) 
    col9, col10 = st.columns(2)
    with col9: 
        st.button("Work Breakdown Structure (WBS)",key="ex9",use_container_width=True) 
    with col10:
        st.button("Scope validation",key="ex10",use_container_width=True) 
    with st.expander("Submit your exercise here"):
        with st.form("my_form2"):
            jim_email= st.text_input("Email to receive feedback", "12345678@std.usn")
            jim_line = st.text_area("Write your exercise here","", height=200)
            submitted = st.form_submit_button("Submit")
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
