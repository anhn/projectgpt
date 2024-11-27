import streamlit as st
import pandas as pd

chart_data1 = pd.DataFrame(np.random.randn(10, 10), columns=["Group1", "Group2", "Group3", "Group4", "Group5", "Group6", "Group7", "Group8", "Group9", "Group10"])
st.title("Teamwork")
st.line_chart(chart_data1)

chart_data2 = pd.DataFrame(np.random.randn(10, 10), columns=["Group1", "Group2", "Group3", "Group4", "Group5", "Group6", "Group7", "Group8", "Group9", "Group10"])
st.title("Software development processes")
st.line_chart(chart_data2)

chart_data3 = pd.DataFrame(np.random.randn(10, 10), columns=["Group1", "Group2", "Group3", "Group4", "Group5", "Group6", "Group7", "Group8", "Group9", "Group10"])
st.title("Project Management")
st.line_chart(chart_data3)

chart_data4 = pd.DataFrame(np.random.randn(10, 10), columns=["Group1", "Group2", "Group3", "Group4", "Group5", "Group6", "Group7", "Group8", "Group9", "Group10"])
st.title("Product")
st.line_chart(chart_data4)
