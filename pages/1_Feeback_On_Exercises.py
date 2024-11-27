import streamlit as st
import os
#from decouple import config
import openai
import streamlit as st
#from streamlit_chat import message
from email.policy import default
from pymongo import MongoClient
from pymongo.server_api import ServerApi
st.set_page_config(layout = "wide", page_title="StartupGPT")
#import app_components as components 
#import chatbot_utils as cu


openai.api_key = st.secrets["OPENAI_KEY"]
cathy_line =''
jim_line = ''
starting_line = "Let's roleplay. Act as a project owner who will convert three lab rooms at USN Bø campus into a co-working space named USNStart at Bø campus, the main building. The coworking space is in a planning phase and will be open by the end of the year. You will get 3 rooms in an area of 500 square meters together. It will include: Open Workspace: This is the heart of a coworking space, featuring flexible seating arrangements with communal desks, tables, and chairs. It's suitable for individual work, informal meetings, and collaborative projects. There is space for 60 individual working here. Private offices: Small, fully-furnished offices that can accommodate individuals or small teams, offering more privacy and a dedicated workspace. The total capacity is 6 private offices. Meeting rooms: Various-sized meeting rooms equipped with projectors and whiteboards for presentations, client meetings, or team discussions. There are 5 meeting rooms in total. Lounge Area: Comfortable seating areas, often with sofas and coffee tables, providing a relaxed atmosphere for informal meetings or relaxation. Kitchen and Dining Area: A well-equipped kitchen or kitchenette with facilities for preparing meals and dining. It also offers complimentary coffee, tea, and snacks. Printing and Scanning area: Equipment for printing, scanning, and photocopying documents. Game room: A recreational space with games like billiards, ping-pong, or video games, encouraging breaks and social interaction. There are also plenty of parking places. As of today, the tenants are Revisorteam, YourCompanion, GreenEnergy, and VismaAI, who sit in private offices. We want to attract students who want to work and become entrepreneurs. We also want to attract individuals who work in groups—larger companies centrally in our cities, who live in the region and/or want to move to the region, and in that way, take their work home and then be able to sit in a co-working building, where they meet other like-minded people and not alone in a home office. There are available offers for seating in the coworking space: Day Pass: Day passes allow members to access the coworking space for a single day. This costs 699 NOK per day. Monthly Membership: Monthly memberships grant unlimited access to the coworking space for a fixed monthly fee. This costs 6000 NOK per month. Student membership: the membership for students. This costs 9000 NOK per semester (6 months). Annual Fixed Desk: members may have their own desk within the enclosed office space, which offers more privacy and can accommodate small teams. This costs 50,000 NOK per year. Private Office Desk: In private offices, members may have their own desk within the enclosed office space, which offers more privacy and can accommodate small teams. This costs 20,000 NOK per month per office. I would like to create a landing page to increase our visibility and attract customers to us. We want to have: Clear and Engaging Headline: Start with a clear, attention-grabbing headline that communicates the core value of your coworking space. Compelling Visuals: Use high-quality images or videos of the coworking space, showcasing the interior, workstations, communal areas, and facilities. You come up with your own ideas about the interior design of the space. Membership Plans and Pricing: Display your membership options, pricing, and any special offers or discounts prominently. Include a call-to-action (CTA) button to encourage visitors to explore plans. Amenities and Facilities: List the key amenities and facilities available in your coworking space, such as high-speed internet, meeting rooms, coffee lounge, and more. Highlight what makes your space unique. Location Information: Clearly state your coworking space's location, including the address, a map, and information about nearby public transportation or parking options. Testimonials and Reviews: Include positive testimonials or reviews from current members. Real feedback can build trust and credibility. Contact Information: Provide multiple contact options, including an email address, phone number, and a contact form. Make it easy for potential members to get in touch. About Us Section: Share a brief overview of your coworking space's history, mission, and values. Highlight what makes your community unique. Responsive Design: Ensure that the landing page is responsive and mobile-friendly, so it displays correctly on all devices and screen sizes. Privacy and Security: Include a section about data privacy and security to reassure potential members that their information will be protected. Floor plan: showing the proposed floor plan and images of interior designs. Booking: allow people with day passes or monthly memberships to book available desks in the open workspace for the current month. A floor map should be displayed, and desk selection should be interactive and visual on the map. A member can only choose to book one desk for one day at a time. A confirmation should be displayed after the reservation is done. Project Brief: USNStart Coworking Space Website. The primary objective of this project is to create a dynamic and engaging website for USNStart Coworking Space, located at the Bø campus of the University of South-Eastern Norway (USN). The website should serve as an informative, user-friendly, and visually appealing platform to attract potential members, provide information about our coworking space, and facilitate desk booking for members. The website should implement all requirements described above. The scope of the project encompasses the design, development, and launch of the USNStart Coworking Space website. This includes, but is not limited to: Development of a responsive website accessible on desktop, tablet, and mobile devices. Design and layout of the website, considering the provided interior design concepts and floor plan. Creation of pages and content that convey key information about the coworking space, membership plans, and existing tenants. Inclusion of images, videos, and visuals to showcase the interior and amenities. Integration of privacy and security measures to protect user data. Coordination with project stakeholders for feedback and review. We are very flexible with design ideas. For website design inspiration see: https://meshcommunity.com/hubs/digs/ https://www.wework.com/l/coworking-space/oslo https://www.spacesworks.com/nb/oslo-nb/kvadraturen/ We are also flexible with the floor map ideas. For inspiration, see: https://pin.it/3sLJ0EQ https://pin.it/43gdiRI https://workdesign.com/wp-content/uploads/2012/11/Coworking-Concept-Floor-Plan-720x405.jpg The desk reservation function is in a very early stage. We want your proposal, both about the process of booking and the user experience of the booking process. We do not have any brand design yet. You are all free to design the logo, color palette, typography, and icons. Technically, we want prototypes to be made with Figma. The prototypes should be interactive with multiple screens. The final website should be implemented using HTML, CSS, and JavaScript. Any supporting tool to generate the code is allowed, for instance, siter.io, or chatgpt. The website can be static, without the backend. Implementation of the backend part is a plus. In the end, the website should be hosted and published (just for the purpose of this course). It is NOT allowed to use any Content Management Systems (WordPress, Webflow, etc.). The code should be written or generated from scratch. We can ignore other aspects of web publication, such as Web analytics, SEO, and interoperability. In order to test the landing page, I would like to run a usability test with some students on campus for the landing page and the booking function. The project will start from the second week of January 2024 and end at the end of April 2024. The success of the USNStart Coworking Space website project can be evaluated based on various criteria. Success in this context can be measured in terms of meeting project objectives, delivering value to the target audience, and achieving the desired outcomes. Here are the criteria of success for this project: Alignment with Project Objectives: The website effectively aligns with the project objectives as defined in the project brief, including creating an engaging online presence for the coworking space and facilitating desk bookings. Fulfillment of all user stories: all stated user stories should be documented, analyzed, prototyped, implemented, and tested. Quality of the visual elements: the visual elements should be comparable to the given examples. Quality and scope of codebase: the codebase should be at a reasonable size for a team of four developers working in a month. Usability test: The website should meet or exceed the expectations of its target audience, in this case, to test with students. Demonstration of Agile team: the team should work and follow Agile practices. Teamwork: the extent that teams frequently meet, and team maturity demonstrated via the evolution of the type of team issues over time. Quality of document: the project report should be written clearly with a reasonable reading flow, logical organization of sections, avoidance of jargon, and use of language appropriate for the target audience. Proper format a document with page numbers, captions for tables, figures, explanations for abbreviations, high resolution for included figures, and a reference section. Students may need to ask questions, seek clarifications, or provide progress updates during the development process. Communication should be done via email. Each email should have a title - PRO1000 - Group number - Main points to communicate. Emails should be sent to angu@usn.no. Please use this persona to provide feedback and guidance to students to collect requirements, clarify student concerns, answer their questions, and guide them to develop and evaluate the landing page. Now wait for students' questions. Try to be as detailed as possible. If the questions from students are not clear enough to give them a detailed answer, then ask them to clarify or give more details in their questions. For each question, try to define and explain a concept or term if the student introduces them in their questions. Try to answer questions in paragraphs; if using bullet."

def get_response(jim_line):
    output =  "dummy"
    return output 
                                                                                                                                                                                                                 
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["General", "Module 1", "Module 2", "Module 3", "Module 4", "Module 5", "Module 6", "Module 7", "Module 8"])

with tab1:
    col01, col02 = st.columns([1, 2])
    with col01:
        st.video("pages/intro.mp4")
    with col02:
        st.write("This is Anh. I will help to answer any of your question regarding to the course, project, assignments and so on.")
        st.write("Examples: How are the teams formed, and can we request to be in a team with specific classmates? How is the final grade distributed across the presentation, project report, prototype, and teamwork?")
    with st.form("my_form"):
        jim_line = st.text_area("Write your question here","", height=70)
        submitted = st.form_submit_button("Submit")

with tab2:
    st.image("https://miro.medium.com/v2/resize:fit:720/format:webp/1*fiEXMWcFg328ztjZEWYlpg.jpeg", width=400)
    col1, col2, col3, col4 = st.columns(4)
    with col1: 
        st.button("Characterizing a software project",key="ex1",use_container_width=True) 
    with col2:
        st.button("Stakeholder analysis",key="ex2",use_container_width=True) 
    with col3: 
        st.button("Project management areas",key="ex3",use_container_width=True) 
    with col4: 
        st.button("SWOT analysis",key="ex4",use_container_width=True) 
    with st.expander("Submit your exercise here"):
        with st.form("my_form1"):
            jim_email= st.text_input("Email to receive feedback", "12345678@std.usn")
            jim_line = st.text_area("Write your exercise here","", height=200)
            submitted = st.form_submit_button("Submit")
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
