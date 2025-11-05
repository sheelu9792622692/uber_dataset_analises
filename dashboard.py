import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


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

# line chart - daily bookings trend
st.header("Daily Bookings Trend")
df['Date'] = pd.to_datetime(df['Date'])
daily_bookings = df.groupby(df['Date'].dt.date).size()
fig10 = px.line(x=daily_bookings.index, y=daily_bookings.values, 
               labels={'x': 'Date', 'y': 'Number of Bookings'}, 
               title='Daily Bookings Trend')
st.plotly_chart(fig10)


# heatmap - booking by time of day and day of week
st.header("Bookings by Time of Day and Day of Week")
df['Hour'] = pd.to_datetime(df['Time']).dt.hour
df['DayOfWeek'] = pd.to_datetime(df['Date']).dt.day_name()
heatmap_data = df.pivot_table(index='Hour', columns='DayOfWeek', values='Booking ID', aggfunc='count').fillna(0)
fig11, ax = plt.subplots(figsize=(10,6))
sns.heatmap(heatmap_data, cmap='YlGnBu', ax=ax)
plt.title('Bookings by Time of Day and Day of Week')
st.pyplot(fig11)

#bar chart - average ride distance by vehicle type
st.header("Average Ride Distance by Vehicle Type")
avg_ride_distance = df.groupby('Vehicle Type')['Ride Distance'].mean()
fig12 = px.bar(x=avg_ride_distance.index, y=avg_ride_distance.values, 
               labels={'x': 'Vehicle Type', 'y': 'Average Ride Distance (km)'}, 
               title='Average Ride Distance by Vehicle Type')
st.plotly_chart(fig12, use_container_width=True, key="avg-ride-distance-vehicle-type")

# heatmap - correlation of key metrics
st.header("Correlation of Key Metrics")
key_metrics = df[['Ride Distance', 'Customer Rating', 'Avg CTAT', 'Booking Value', 'Avg VTAT']]
correlation_matrix = key_metrics.corr()
fig13, ax = plt.subplots(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
plt.title('Correlation of Key Metrics')
st.pyplot(fig13)

# Scatter Plot - Booking Value vs. Driver Rating
st.header("Booking Value vs. Driver Rating")
fig14 = px.scatter(df, x='Booking Value', y='Driver Ratings' \
'', 
                  labels={'x': 'Booking Value', 'y': 'Driver Rating'}, 
                  title='Booking Value vs. Driver Rating', 
                  trendline='ols')
st.plotly_chart(fig14)

# scatter plot - booking value vs customer rating
st.header("Booking Value vs. Customer Rating")
fig15 = px.scatter(df, x='Booking Value', y='Customer Rating',
                    labels={'x': 'Booking Value', 'y': 'Customer Rating'}, 
                    title='Booking Value vs. Customer Rating', 
                    trendline='ols')
st.plotly_chart(fig15)

# box plot - customer rating by vehicle type
st.header("Customer Rating by Vehicle Type")
fig16 = px.box(df, x='Vehicle Type', y='Customer Rating', 
                 labels={'x': 'Vehicle Type', 'y': 'Customer Rating'}, 
                 title='Customer Rating by Vehicle Type')
st.plotly_chart(fig16)

# box plot - driver ratings by vehicle type
st.header("Driver Ratings by Vehicle Type")
fig17 = px.box(df, x='Vehicle Type', y='Driver Ratings', 
                 labels={'x': 'Vehicle Type', 'y': 'Driver Ratings'}, 
                 title='Driver Ratings by Vehicle Type')
st.plotly_chart(fig17)

# bar chart - incomplete rides by reason
st.header("Incomplete Rides by Reason")
incomplete_rides = df[df['Booking Status'] == 'Incomplete']['Incomplete Rides Reason'].value_counts()
fig18 = px.bar(x=incomplete_rides.index, y=incomplete_rides.values,
                    labels={'x': 'Incomplete Reason', 'y': 'Count'}, 
                    title='Incomplete Rides by Reason')
st.plotly_chart(fig18)

# pie chart - cancelltion share
st.header("Cancellation Share")
cancellation_counts = df['Booking Status'].value_counts()
fig19 = px.pie(names=cancellation_counts.index, values=cancellation_counts.values, 
               title='Cancellation Share')
st.plotly_chart(fig19)

# line chart - monthly booking trend
st.header("Monthly Booking Trend")
df['Month'] = df['Date'].dt.to_period('M')
monthly_bookings = df.groupby('Month').size()
fig20 = px.line(x=monthly_bookings.index.astype(str), y=monthly_bookings.values, 
                labels={'x': 'Month', 'y': 'Number of Bookings'}, 
                title='Monthly Booking Trend')
st.plotly_chart(fig20)

