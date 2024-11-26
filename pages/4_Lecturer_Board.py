import streamlit as st
import pandas as pd

lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ultrices ante nec justo varius, vitae gravida mi suscipit. Nullam vehicula facilisis semper. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed euismod nisl quis tellus lobortis, vitae blandit orci congue. Phasellus ullamcorper lacinia dolor, non suscipit dui dictum vel. Donec ac magna eget augue cursus finibus. Sed lacinia, justo eu tincidunt vestibulum, felis quam auctor nibh, nec ullamcorper augue elit vel elit."


df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": ["a", "b", "c"],
    "C": [lorem_ipsum, lorem_ipsum, lorem_ipsum],
    "D": [True,False,True]
})

true_html = '<input type="checkbox" checked disabled="true">'
false_html = '<input type="checkbox" disabled="true">'

df['D'] = df['D'].apply(lambda b: true_html if b else false_html)

st.markdown(df.to_html(escape=False), unsafe_allow_html=True)
