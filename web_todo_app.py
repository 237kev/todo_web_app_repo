import streamlit as st
import functions

todos = functions.get_todos(functions.TODO_FILES_PATH)

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.set_todos(functions.TODO_FILES_PATH, todos)



st.title('My todo Webapp')
st.subheader('This is my todo webapp')
st.write('This app should increase you productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.set_todos(functions.TODO_FILES_PATH, todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='New todo', placeholder='enter a new todo item ...',
              on_change=add_todo, key='new_todo')