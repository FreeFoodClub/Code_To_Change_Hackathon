import streamlit as st
import csv

st.title("Report Issue")

class User:
    
    def __init__(self, name):
        self.name = name
        if "score" not in st.session_state:
            st.session_state["score"] = 0

    def save_score(self):
        st.session_state["score"] += 1
        with open('scores.txt', 'w') as file:
            file.write(f"{self.name}: {st.session_state['score']}\n")
        st.write(f"{self.name}'s current score: {st.session_state['score']}")
        with open('scores.txt', 'r') as file:
            self.info = file.read()
            self.upload_score(self.info)

    def upload_score(self, information):
        with open('global_scores.txt', 'a') as file:
            file.write(f'{information}\n')


def save_reports(area, issue, user_comment, severity, users_name):
    with open("Data.csv", "a", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([area, issue, user_comment, severity])
    st.write("Successfully submitted!")
    users_name.save_score()


def post_report(username):
    st.write("---Welcome to Calgary's Issue Reporting Page---")
    user_obj = User(username)
    st.write(f"Hello There!")
    add_area = st.selectbox("Which part of the city did you find the issue in?: ",
        ("Northwest","Northeast","Southwest","Southeast", "Downtown")
        )
    add_issue = st.selectbox(
        "Which issue do you want to report?: ",
        ("Potholes","Slippery Road","Accessibility")
        )
    comment = st.text_input("Describe the Issue:")

    add_severity = st.slider(
        "How severe is the issue from the scale of 1-10? (1 being lowest/10 being most severe)",1,10,5)
    
    if st.button("Submit Report"):
        save_reports(add_area, add_issue, comment, add_severity, user_obj)

def main():
    user = st.text_input("Please type in your Username:")
    post_report(user)

main()
