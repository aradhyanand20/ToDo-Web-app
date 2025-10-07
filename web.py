import streamlit as st
import functions
todo_web = functions.get_todos()
def add_todos():
    todo = st.session_state["newtodo"] + "\n"
    todo_web.append(todo)
    functions.write_todos(todo_web)

st.title("TODO APP")
st.subheader("Enter your tasks below")
st.write("Aim is to increase productivity")

for index,todo in enumerate(todo_web):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_web.pop(index)
        functions.write_todos(todo_web)
        del st.session_state[todo]
        st.rerun()
st.text_input(label="", placeholder="Enter your task",
              on_change=add_todos, key='newtodo')

