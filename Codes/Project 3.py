import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have already read the data from an Excel file
# Replace this with your actual data reading logic
df = pd.read_csv(r"C:\Users\aayus\Downloads\WPRUsual.csv")

# Sidebar title
st.title("Population Comparison App")

# Display raw data if checkbox is selected
if st.checkbox("Show Raw Data"):
    st.write("Raw Data:")
    st.write(df)

# EDA Section 1: Comparing Rural Male and Rural Female Populations
st.subheader("Comparison of Rural Male and Female Populations")
fig_1, ax_1 = plt.subplots(figsize=(12, 8))
sns.barplot(data=df[['State/UT', 'Rural Male', 'Rural Female']], x='State/UT', y='Rural Male', color='skyblue', label='Rural Male')
sns.barplot(data=df[['State/UT', 'Rural Male', 'Rural Female']], x='State/UT', y='Rural Female', color='orange', label='Rural Female')
ax_1.set_xlabel('State/UT')
ax_1.set_ylabel('Population')
ax_1.set_title('Comparison of Rural Male and Female Populations')
ax_1.set_xticklabels(ax_1.get_xticklabels(), rotation=45, ha='right')  # Adjust rotation for better visibility
ax_1.legend()
st.pyplot(fig_1)

# EDA Section 2: Comparing Urban Male and Urban Female Populations
st.subheader("Comparison of Urban Male and Female Populations")
fig_2, ax_2 = plt.subplots(figsize=(12, 8))
sns.barplot(data=df[['State/UT', 'Urban Male', 'Urban Female']], x='State/UT', y='Urban Male', color='green', label='Urban Male')
sns.barplot(data=df[['State/UT', 'Urban Male', 'Urban Female']], x='State/UT', y='Urban Female', color='blue', label='Urban Female')
ax_2.set_xlabel('State/UT')
ax_2.set_ylabel('Population')
ax_2.set_title('Comparison of Urban Male and Female Populations')
ax_2.set_xticklabels(ax_2.get_xticklabels(), rotation=45, ha='right')  # Adjust rotation for better visibility
ax_2.legend()
st.pyplot(fig_2)

# Calculate the sums for each category
df['Male_Total'] = df['Rural Male + Urban Male']
df['Female_Total'] = df['Rural Female + Urban Female']

# EDA Section: Stacked Bar Chart
st.subheader("Comparison of Male and Female Totals")
fig, ax = plt.subplots(figsize=(12, 8))
male_bars = ax.bar(df['State/UT'], df['Male_Total'], label='Male', color='yellow')
female_bars = ax.bar(df['State/UT'], df['Female_Total'], bottom=df['Male_Total'], label='Female', color='red')

ax.set_xlabel('State/UT')
ax.set_ylabel('Population')
ax.set_title('Comparison of Male and Female Totals')

# Adding legend
ax.legend()

# Rotate x-axis labels for better readability
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

# Display the chart in Streamlit
st.pyplot(fig)
