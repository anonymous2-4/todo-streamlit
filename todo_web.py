import streamlit as st
import json
import os
import streamlit as st
st.write("Streamlit version:", st.__version__)


TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f)

st.title("📝 My To-Do List")
st.caption("Simple task tracker that works on desktop and mobile")

# Load existing tasks
tasks = load_tasks()

# Add new task
if "new task" not in st.session_state:
    st.session_state.new_task = ""

task = st.text_input("Enter a new task:", key="new_task")

if st.button("Add Task"):
    if task:
        tasks.append(task)
        save_tasks(tasks)
        st.session_state.new_task = ""
        st.rerun()

# Show current tasks
if tasks:
    st.subheader("Your Tasks:")
    for i, task in enumerate(tasks):
        col1, col2 = st.columns([6, 1])
        col1.write(f"{i+1}. {task}")
        if col2.button("❌", key=f"del_{i}"):
            tasks.pop(i)
            save_tasks(tasks)
            st.rerun()
else:
    st.info("No tasks yet. Add one above!")

