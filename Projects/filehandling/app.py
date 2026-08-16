from pathlib import Path
import streamlit as st

# Import file handling functions from the main script
from main import createfile, readfile, updatefile, deletefile

st.set_page_config(page_title="File Manager", page_icon="📁", layout="wide")

st.title("📁 Simple File Manager")
st.caption("Create, read, update, rename, and delete files using a clean UI.")

# -------------------------
# Helper for clean messages
# -------------------------
def safe_call(func, *args, **kwargs):
    try:
        func(*args, **kwargs)
        return True
    except Exception as err:
        st.error(f"Error: {err}")
        return False

# -------------------------
# App Layout
# -------------------------
tab1, tab2, tab3, tab4 = st.tabs(["Create", "Read", "Update", "Delete"])

with tab1:
    st.subheader("Create a file")
    file_name = st.text_input("File name", placeholder="example.txt")
    file_content = st.text_area("File content", height=150)

    if st.button("Create File"):
        if not file_name:
            st.warning("Please enter a file name.")
        else:
            # Use the existing function logic
            try:
                path = Path(file_name)
                if path.exists():
                    choice = st.radio("File already exists. Do you want to overwrite it?", ["No", "Yes"])
                    if choice == "No":
                        st.info("File creation cancelled.")
                    else:
                        with open(path, "w", encoding="utf-8") as fs:
                            fs.write(file_content)
                        st.success("File created/updated successfully!!")
                else:
                    with open(path, "w", encoding="utf-8") as fs:
                        fs.write(file_content)
                    st.success("File created successfully!!")
            except Exception as err:
                st.error(f"Error occurred as {err}")

with tab2:
    st.subheader("Read a file")
    read_name = st.text_input("File to read", key="read_file_name", placeholder="example.txt")

    if st.button("Read File"):
        if not read_name:
            st.warning("Please enter a file name.")
        else:
            path = Path(read_name)
            if not path.exists():
                st.error("File not found.")
            else:
                try:
                    with open(path, "r", encoding="utf-8") as file:
                        content = file.read()
                    if not content:
                        st.info("The file is empty.")
                    else:
                        st.success("File loaded successfully!")
                        st.code(content, language="text")
                except Exception as err:
                    st.error(f"Error occurred as {err}")

with tab3:
    st.subheader("Update a file")
    update_name = st.text_input("File name", key="update_file_name", placeholder="example.txt")
    update_option = st.selectbox("Choose an update option", ["Overwrite the file", "Append content", "Rename the file"])
    update_content = st.text_area("Content", height=150, key="update_content")
    new_name = st.text_input("New file name", key="new_file_name", placeholder="new_name.txt")

    if st.button("Update File"):
        if not update_name:
            st.warning("Please enter a file name.")
        else:
            path = Path(update_name)
            if not path.exists():
                st.error("File not found.")
            else:
                try:
                    if update_option == "Overwrite the file":
                        with open(path, "w", encoding="utf-8") as file:
                            file.write(update_content)
                        st.success("File overwritten successfully!!")

                    elif update_option == "Append content":
                        with open(path, "a", encoding="utf-8") as file:
                            file.write(update_content)
                        st.success("Content appended successfully!!")

                    elif update_option == "Rename the file":
                        if not new_name:
                            st.warning("Please enter a new file name.")
                        else:
                            new_path = Path(new_name)
                            if new_path.exists():
                                st.error("New file name already exists. Choose a different one.")
                            else:
                                path.rename(new_path)
                                st.success(f"File renamed successfully to {new_path}")
                except Exception as err:
                    st.error(f"Error occurred as {err}")

with tab4:
    st.subheader("Delete a file")
    delete_name = st.text_input("File to delete", key="delete_file_name", placeholder="example.txt")

    if st.button("Delete File"):
        if not delete_name:
            st.warning("Please enter a file name.")
        else:
            path = Path(delete_name)
            if not path.exists():
                st.error("File not found.")
            else:
                confirm = st.checkbox("I confirm I want to delete this file")
                if confirm:
                    try:
                        path.unlink()
                        st.success("File deleted successfully!!")
                    except Exception as err:
                        st.error(f"Error occurred as {err}")
                else:
                    st.info("Delete operation cancelled.")
