import streamlit as st
import pandas as pd
 
st.selectbox("Class", options=["PRO1000 Bø", "PRO1000 Net", "PRO1000 Gol"], placeholder="Select an option", index=None)

df = pd.DataFrame({
    "UserId": [1, 2, 3],
    "TeamStage": ["Found a team","Found a team","Found a team"],
    "ProjectSpecification": ["Understand  what need to do","Understand  what need to do"","Understand  what need to do"],
    "ProjectRepositorySetup": [True,False,True],
    "CommunicationToolSetup": [True,False,True],
    "ProjectManagementBoardSetup": [True,False,True],
    "IDESetup": [True,False,True],
    "CollaborativeDocumentSetup": [True,False,True],
    "LearnIXPractice": [True,False,True],
    "WBS": ["UnderstandWBS","CreateAWBS","ValidateAWBS"],
    "GanttChart": ["Understand GanttChart","Create a GanttChart","Validate a Gantt Chart"],
    "RiskScore": [True,False,True],
    "RiskCountermeasurement": [True,False,True],
    "RoleDefined": [True,False,True],
    "CommunicationManagement": [True,False,True],
    "LowFidelityPrototyping": [True,False,True],
    "HighFidelityPrototyping": [True,False,True],
    "UXDesignLaws": [True,False,True],
    "WCAG": [True,False,True],
    "UserStories": [True,False,True],
    "ProductBacklog": [True,False,True],
    "SprintBacklog": [True,False,True],
    "BurndownChart": [True,False,True],
    "KanbanBoard": [True,False,True],
    "SprintPlanning": [True,False,True],
    "DefinitionOfDone": [True,False,True],
    "SprintReview": [True,False,True],
    "SprintRetrospective": [True,False,True],
    "UMLDiagrams": [True,False,True],
    "TechnologyStack": [True,False,True],
    "ArchitecturalDesign": [True,False,True],
    "FrontEndDevelopment": [True,False,True],
    "BackEndDevelopment": [True,False,True],
    "Database": [True,False,True],
    "NoCodeDevelopment": [True,False,True],
    "TestPlan": [True,False,True],
    "TestExecution": [True,False,True],
    "UsabilityTestPlan": [True,False,True],
    "UsabilityTestExecution": [True,False,True],
    "Deployment": [True,False,True],
    "PresentationSlide": [True,False,True]
})
edited_df = st.data_editor(df)

def click_button():
    edited_df.to_csv("data.csv", index=False)

st.button('Send feedback', on_click=click_button)
