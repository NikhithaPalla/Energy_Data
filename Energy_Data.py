import streamlit as st 
import pandas as pd
import altair as alt 
import numpy as np

st.title("Energy Data")
energy_data = pd.read_csv('Energy data 1990 - 2020.csv')
st.write(energy_data)


# create dropdowns for user selection
selected_Y_axis = st.sidebar.selectbox('Select y-axis:', energy_data.select_dtypes(include=np.number).columns.tolist())
selected_country = st.sidebar.selectbox('Select a country:', energy_data['country'].unique())


# Filter data based on dropdown selections
filtered_energy = energy_data[(energy_data['country'] == selected_country)]


# Create Bar chart
bar_chart = alt.Chart(energy_data).mark_bar().encode(
    alt.X('Year:N'),
    alt.Y(selected_Y_axis)
).interactive()
    
# Show chart
st.altair_chart(bar_chart.transform_filter(
    (alt.datum.country == selected_country)
), use_container_width=True)

