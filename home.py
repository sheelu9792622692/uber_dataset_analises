import streamlit as st
import pandas as pd
import plotly.express as px

st.title("welcome to home page")
st.image(r"C:\Users\micro\Downloads\92ab8edf3c8fbcd44161a795bf1c14da.gif")
def load_data():
    df = pd.read_csv("uber_data.csv")
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    df['hour'] = df['pickup_datetime'].dt.hour
    df['day_of_week'] = df['pickup_datetime'].dt.day_name()
    return df

def show_home():
    st.title("🚖 Uber Ride Analytics Dashboard")
    st.markdown("Interactive visualization of Uber ride patterns, peak hours, and hotspot locations.")

    data = load_data()

    # --- Sidebar Filters ---
    st.sidebar.subheader("Filters")
    days = st.sidebar.multiselect("Select Days", sorted(data['day_of_week'].unique()), default=data['day_of_week'].unique())
    hours = st.sidebar.slider("Select Hours", 0, 23, (0, 23))
    
    filtered_data = data[(data['day_of_week'].isin(days)) & (data['hour'] >= hours[0]) & (data['hour'] <= hours[1])]

    # --- Key Metrics ---
    st.subheader("📊 Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rides", filtered_data.shape[0])
    col2.metric("Busiest Hour", int(filtered_data['hour'].mode()[0]))
    col3.metric("Most Popular Pickup", filtered_data['pickup_location'].mode()[0])

    # --- Trips by Hour ---
    st.subheader("Trips per Hour")
    fig_hour = px.histogram(filtered_data, x='hour', nbins=24, title="Hourly Trip Distribution", color_discrete_sequence=['#636EFA'])
    st.plotly_chart(fig_hour, use_container_width=True)

    # --- Trips by Day ---
    st.subheader("Trips by Day of Week")
    day_counts = filtered_data['day_of_week'].value_counts().sort_index()
    fig_day = px.bar(day_counts, labels={'index':'Day', 'value':'Number of Trips'}, color_discrete_sequence=['#EF553B'])
    st.plotly_chart(fig_day, use_container_width=True)

    # --- Pickup Locations Heatmap ---
    if 'latitude' in filtered_data.columns and 'longitude' in filtered_data.columns:
        st.subheader("Pickup Locations Heatmap")
        st.map(filtered_data[['latitude','longitude']].dropna())
    else:
        st.info("Add latitude & longitude columns to visualize pickups on the map.")

