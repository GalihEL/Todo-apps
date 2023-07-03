import streamlit as st
import func
todos = func.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    func.write_todos(todos)
st.title("Todo App")
st.subheader("An app for your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos) 
        del st.session_state[todo]
        st.experimental_rerun()
st.text_input(label="", placeholder="Type your to do here.",
              key="new_todo", on_change=add_todo)
