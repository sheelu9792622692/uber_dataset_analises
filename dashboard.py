import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Uber data analysis dashboard")
df = pd.read_csv(r"c:\Users\micro\AppData\Local\Temp\f60f3fb6-9241-422d-b57d-eada42d01bee_archive.zip.bee\ncr_ride_bookings.csv")
df

# . Bar Chart – Booking Status Distribution
st.header("Booking Status Distribution")
booking_status_counts = df['Booking Status'].value_counts() 
fig1 = px.bar(x=booking_status_counts.index, y=booking_status_counts.values, 
              labels={'x': 'Booking Status', 'y': 'Count'}, 
              title='Distribution of Booking Status')
st.plotly_chart(fig1)

# Bar Chart – Bookings by Vehicle Type
st.header("Bookings by Vehicle Type")
vehicle_type_counts = df['Vehicle Type'].value_counts()
fig2 = px.bar(x=vehicle_type_counts.index, y=vehicle_type_counts.values, 
              labels={'x': 'Vehicle Type', 'y': 'Count'}, 
              title='Number of Bookings by Vehicle Type')
st.plotly_chart(fig2)

# Stacked Bar Chart – Vehicle Type vs Booking Status
st.header("Vehicle Type vs Booking Status")
vehicle_status_counts = df.groupby(['Vehicle Type', 'Booking Status']).size().unstack(fill_value=0)
fig4 = vehicle_status_counts.plot(kind='bar', stacked=True, figsize=(10,6
))
plt.title('Vehicle Type vs Booking Status')
plt.xlabel('VehiclLie Type')
plt.ylabel('Number of Bookings')
st.pyplot(fig4.figure)

#Bar Chart – Average Ride Distance by Vehicle Type
st.header("Average Ride Distance by Vehicle Type")
avg_distance = df.groupby('Vehicle Type')['Ride Distance'].mean()
fig6 = px.bar(x=avg_distance.index, y=avg_distance.values, 
              labels={'x': 'Vehicle Type', 'y': 'Average Ride Distance (km)'}, 
              title='Average Ride Distance by Vehicle Type')
st.plotly_chart(fig6)

# Pie Chart – Payment Method Share
st.header("Payment Method Share")
payment_method_counts = df['Payment Method'].value_counts()
fig7 = px.pie(names=payment_method_counts.index, values=payment_method_counts.values, 
              title='Share of Payment Methods')
st.plotly_chart(fig7)

# Bar Chart – Driver Cancellation Reasons
st.header("Driver Cancellation Reasons")
driver_cancellation_reasons = df[df['Booking Status'] == 'Cancelled by Driver']['Driver Cancellation Reason'].value_counts()
fig9 = px.bar(x=driver_cancellation_reasons.index, y=driver_cancellation_reasons.values, 
                labels={'x': 'Driver Cancellation Reason', 'y': 'Count'}, 
                title='Driver Cancellation Reasons')    
st.plotly_chart(fig9)

# Heatmap – Correlation of Key Metrics
st.header("Correlation of Key Metrics")
key_metrics = df[['Ride Distance', 'Fare Amount', 'Tip Amount', 'Total Amount']]
correlation_matrix = key_metrics.corr()
fig10, ax = plt.subplots(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
plt.title('Correlation Matrix of Key Metrics')
st.pyplot(fig10)

