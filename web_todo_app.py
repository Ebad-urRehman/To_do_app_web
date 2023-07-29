import streamlit as st
import function
# as upload webpage on web server it is important to note that our web server is capable of handling many users
todos = function.get_file_todos()
def add_todo():
    todo =st.session_state["new_todo"]+'\n'
    # above session state is dictionary in which the key "newtodo" is when user imported
    todos.append(todo)
    function.write_file_todos(todos)
st.title("The Todo App")
st.subheader("This is a Todo App")
st.write("This app can increase your efficiency and productivity")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_file_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
        # del st.session_state[todo]
st.text_input(label="", placeholder="Enter a todo:",
              on_change=add_todo, key="new_todo")
