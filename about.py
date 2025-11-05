import streamlit as st
st.title("📖About This Project")
st.markdown("""
                This Project analyzes Uber trip data to uncover ride trends,peak hours,and pickup hotspots.

                **Dataset deatails:**
                - pickup_datetime: Date & time of pickup
                - dropoff_datetime: Date & time of dropoff
                - pickup_location: Pickup location
                - dropoff_location: Dropoff location
                - fare_amount: Trip Cost
                
                **Analysis Performed:**
                - Exploratory Data Analysis (EDA) 
                - Hourly & Daily trends
                - Location Heatmaps
                - Interactive filters for insights
            
                **Technologies Used:**
                - *Python* (Pandas, Numpy)
                - *Matplotlib* & *Seaborn* ,*Plotly* for Data Visualization
                - *Streamlit* for interactive visulalizations
            
                ** Data Set:**
                - Data Source[Uber Dataset]
                 (Kaggle)(https://www.kaggle.com/dataset)

                """)
    