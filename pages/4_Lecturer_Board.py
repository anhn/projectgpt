import streamlit as st
import pandas as pd

feedback1 = "Students are divided into teams of six to eight students. Teams are formed by randomly assigning students; the members generally do not know each other beforehand. This is a typical situation in a real life setting, especially when working as a consultant. The students are free to choose the methods that best fit their projects. In some cases, the development approaches are enforced by customers due to existing working processes they have adopted in their organizations. Each team decides by themselves about their management and leadership mechanisms. In most of the cases, students organize themselves using a flat organizational structure within the team. Decision making is often done collectively and the reasons for important decisions are documented in the final reports. There are several lectures at the beginning of the course teaching topics such as project management, team dynamics, Scrum, architecture, and testing."
feedback2 = "Students typical engage in three phases of their projects, which are planning, execution and closing (refer to Figure 1). In the planning phase, the students get to know their team members, customers, and their project requirements. The students need to decide roles and areas of responsibility for each member. They also make a preliminary project plan and set up the working environment. In the execution phase, the student teams typically carry out sprints with frequent deliveries to their customers. Each project covers fundamental SE activities, i.e., requirement elicitation, architecture level design, coding, and testing. Students also write a project report that reflects their team’s progress. In the closing phase, the project results are submitted in a report; they are also demonstrated and presented to the customer and course staff (e.g., course instructor, supervising teaching assistant)."
feedback3 = "The course deliverables for each team include (1) an end of term demonstration of the software, (2) a presentation, and (3) a final project report. The course project work is evaluated on the basis of the quality of the project reports, the functioning prototype of the system, the presentation delivered at the end of the course, and the team dynamics. Customers consider their experience working with the team, the value of the software developed, and the delivered report in their evaluations. Supervisors, who are typically teaching assistants in the course, evaluate their teams’ performance and learning based on their observations throughout the course. The faculty member responsible for the course involves both the customer and the supervisor in an evaluation meeting to determine the final marks for students. In the evaluation scheme, a team with a poorly functioning application does not necessarily receive a low grade. Student teams that have difficult projects with poor functionality, but express quick learning curves and effective teamwork can achieve a good grade."

df = pd.DataFrame({
    "UserId": [1, 2, 3],
    "Exercise": ["a", "b", "c"],
    "Feedback": [feedback1,feedback2,feedback3],
    "FeedbackSent": [True,False,True]
})

edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
st.button('Click me', on_click=click_button)

def click_button():
    edited_df.to_csv("data.csv", index=False)

