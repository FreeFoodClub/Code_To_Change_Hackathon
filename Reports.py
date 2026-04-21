import csv
import streamlit as st

name = input("user's name: ")

def save_reports(area, issue, severity, user_comment):
    with open("Data.csv", "a", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([area, issue, severity, user_comment])


def post_report(username):
    st.write("---Welcome to Calgary's Issue Reporting Page---")
    st.write(f"Hello {username}!")
    add_area = st.selectbox("Which part of the city did you find the issue in?: ",
        ("Northwest","Northeast","Southwest","Southeast")
        )
    add_issue = st.selectbox(
        "Which issue do you want to report?: ",
        ("Potholes","Slippery Road","C-Train Elevator Down")
        )
    add_severity = st.selectbox(
        "How severe is the issue from the scale of 1-5? (1 being lowest/5 being most severe)",
        ("1","2","3","4","5","6","7","8","9","10")
        )
    add_comment = st.selectbox("Do you want to add an additional comment?: ",
                               ("Yes","No")
                               )
    comment = ""
    if add_comment == "Yes":
        comment = st.text_input("Add Your Comment:")
    if st.button("Submit Report"):
        save_reports(add_area, add_issue, add_severity, comment)
    

def main():
    post_report(name)

main()
