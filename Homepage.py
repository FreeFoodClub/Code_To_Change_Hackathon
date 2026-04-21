import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(
    page_title="SafeWalk Calgary",
    page_icon="🏙️",
)

st.title("Welcome to SafeWalk")
st.sidebar.success("Select a page above.")

st.write("### 🗺️ Live Safety Alerts Around Calgary")

# Try to read reports
try:
    df = pd.read_csv("Data.csv", header=None, names=["Area", "Issue", "Comment", "Severity"])
except FileNotFoundError:
    st.warning("No reports yet! Go to 'Report Issue' to submit one.")
    st.stop()

area_coords = {
    "Northwest": [51.100, -114.150],
    "Northeast": [51.100, -113.950],
    "Southwest": [50.950, -114.150],
    "Southeast": [50.950, -113.950],
}

df["lat"] = df["Area"].map(lambda a: area_coords.get(a, [51.05, -114.05])[0])
df["lon"] = df["Area"].map(lambda a: area_coords.get(a, [51.05, -114.05])[1])

df["popup"] = df["Issue"] + " (Severity: " + df["Severity"].astype(str) + ")"

# Show the reports
st.dataframe(df[["Area", "Issue", "Severity", "Comment"]])

# Title for map
st.write("### 🧭 Map of Reported Issues")

# Define initial map view
view_state = pdk.ViewState(
    latitude=51.05,
    longitude=-114.05,
    zoom=10,
    pitch=0,
)

# Create layer for issue pins
layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position='[lon, lat]',
    get_color='[255, 0, 0, 160]',  # Red semi-transparent pins
    get_radius=200,
    pickable=True,
)

# Define tooltip for hover info
tooltip = {
    "html": "<b>Area:</b> {Area}<br/>"
            "<b>Issue:</b> {Issue}<br/>"
            "<b>Severity:</b> {Severity}<br/>"
            "<b>Comment:</b> {Comment}",
    "style": {"backgroundColor": "white", "color": "black"}
}

# Use a public, free map style that doesn’t need a token
st.pydeck_chart(pdk.Deck(
    map_style="https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json",
    initial_view_state=view_state,
    layers=[layer],
    tooltip=tooltip
))
