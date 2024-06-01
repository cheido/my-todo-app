import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_to_add = st.session_state["new_todo"] + "\n"
    todos.append(todo_to_add)
    functions.write_todos(todos)


st.title('My Todo App')
st.subheader('This will increase your productivity')
st.write("Enter a todo item below:")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter a todo here...",
              on_change=add_todo, key='new_todo')

