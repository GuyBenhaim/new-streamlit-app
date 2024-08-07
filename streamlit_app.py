import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title('Streamlit Demo App with Charts')

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [23, 45, 56, 78, 89]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
st.write('### Sample Data', df)

# Bar chart using Streamlit's built-in function
st.write('### Bar Chart')
st.bar_chart(df.set_index('Category'))

# Line chart using Streamlit's built-in function
st.write('### Line Chart')
st.line_chart(df.set_index('Category'))

# Area chart using Streamlit's built-in function
st.write('### Area Chart')
st.area_chart(df.set_index('Category'))

# Matplotlib chart
st.write('### Matplotlib Chart')
fig, ax = plt.subplots()
ax.bar(df['Category'], df['Values'], color='skyblue')
ax.set_xlabel('Category')
ax.set_ylabel('Values')
ax.set_title('Bar Chart using Matplotlib')
st.pyplot(fig)

# Adding user input
st.write('### User Input Example')
category = st.selectbox('Select Category', df['Category'])
value = st.slider('Select Value', 0, 100, 50)

# Display selected values
st.write(f'Selected Category: {category}')
st.write(f'Selected Value: {value}')

# Update DataFrame based on user input
df.loc[df['Category'] == category, 'Values'] = value

# Display updated DataFrame
st.write('### Updated Data', df)

# Updated Matplotlib chart
fig, ax = plt.subplots()
ax.bar(df['Category'], df['Values'], color='lightcoral')
ax.set_xlabel('Category')
ax.set_ylabel('Values')
ax.set_title('Updated Bar Chart using Matplotlib')
st.pyplot(fig)
