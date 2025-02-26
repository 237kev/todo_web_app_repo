import streamlit as st
import functions

st.title('My todo Webapp')
st.subheader('This is my todo webapp')
st.write('This app should increase you productivity')

todos = functions.get_todos(functions.TODO_FILES_PATH)


for todo in todos:
    st.checkbox(todo)