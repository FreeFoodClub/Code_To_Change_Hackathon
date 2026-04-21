import streamlit as st
import pandas as pd
from operator import itemgetter
import os

st.title("🏆 SafeWalk Leaderboard")

# Read data from global_scores.txt
users_and_scores = {}

if os.path.exists("global_scores.txt"):
    with open("global_scores.txt", "r") as file: 
        for line in file:
            line = line.strip()
            if not line:
                continue
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                try:
                    value = int(value.strip())
                    users_and_scores[key] = value
                except ValueError:
                    continue  # skip if value is not an integer

    # Sort users by score descending
    sorted_users = sorted(users_and_scores.items(), key=itemgetter(1), reverse=True)
    top_five_users = sorted_users[:10]

    # Create DataFrame for display
    df = pd.DataFrame(top_five_users, columns=['Username', 'Score'])
    df.index += 1  # Rank starting from 1
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Rank'}, inplace=True)

    # Display leaderboard in Streamlit
    st.subheader("Top 10 Contributors")
    st.table(df)
else:
    st.info("No scores yet! Be the first to submit a report.")
