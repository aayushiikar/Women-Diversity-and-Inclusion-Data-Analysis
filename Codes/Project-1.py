import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Function to load and preprocess the first dataset
def load_dataset1():
    df1 = pd.read_excel(r"C:\Users\aayus\Downloads\NFHS_5_Factsheets_Data.xls")
    # Preprocess or filter the data as needed
    return df1

# Function to load and preprocess the second dataset
def load_dataset2():
    df2 = pd.read_excel(r"C:\Users\aayus\Downloads\NFHS_5_India_Districts_Factsheet_Data.xls")
    # Preprocess or filter the data as needed
    return df2

# Function for the first page
# Function for the first page
def page1(df):
    st.title("Page 1: EDA on Women's Menstrual Hygiene and Domestic Violence faced at home and during pregnancy")

    # Display entire dataset or provide options for exploration
    if st.checkbox("Show Raw Data"):
        st.write(df)

    # Columns of interest for the percentage distribution plots
    columns_of_interest = ['Women age 15-24 years who use hygienic methods of protection during their menstrual period26 (%)',
                            'Ever-married women age 18-49 years who have ever experienced spousal violence27 (%)',
                            'Ever-married women age 18-49 years who have experienced physical violence during any pregnancy (%)']

    # Unique states in the DataFrame
    unique_states = df['States/UTs'].unique()

    # Sidebar selection for state and column
    selected_state_percentage = st.sidebar.selectbox('Select State', unique_states)
    selected_column_percentage = st.sidebar.selectbox('Select Column', columns_of_interest)

    # Filter rows for the selected state
    state_rows_percentage = df[df['States/UTs'] == selected_state_percentage]

    # Convert column values to numeric
    state_values_percentage = pd.to_numeric(state_rows_percentage[selected_column_percentage], errors='coerce')

    # Calculate percentages for the selected state
    state_percentages = state_values_percentage / state_values_percentage.sum() * 100

    # Create percentage plot for the selected state and column
    fig_percentage, ax_percentage = plt.subplots(figsize=(16, 9))  # Increase the size of the plot
    fig_percentage.subplots_adjust(top=0.8)  # Add space between title and plot
    ax_percentage.bar(state_rows_percentage['Area'], state_percentages, color=['blue', 'orange', 'green'], alpha=0.7)
    title_text_percentage = f'Percentage Distribution of\n{selected_column_percentage} in {selected_state_percentage}'
    ax_percentage.set_title(title_text_percentage, fontsize=24, color='#2c3e50') # Increase font size of the title and set text color
    ax_percentage.set_xlabel('Area', fontsize=24)
    ax_percentage.set_ylabel('Percentage', fontsize=8)

    # Display the percentage plot in Streamlit app
    st.pyplot(fig_percentage)
    st.markdown("<br>", unsafe_allow_html=True)
    # Create a box plot for the selected column
    fig_box, ax_box = plt.subplots(figsize=(16, 9))  # Increase the size of the plot
    fig_box.subplots_adjust(top=0.8)  # Add space between title and plot
    sns.boxplot(x='Area', y=selected_column_percentage, data=state_rows_percentage, palette='viridis', width=0.7)
    title_text_box = f"Box Plot for {selected_column_percentage} in {selected_state_percentage}"
    ax_box.set_title(title_text_box, fontsize=24, color='#2c3e50')  # Increase font size of the title and set text color
    ax_box.set_xlabel('Area', fontsize=24)  # Increase font size of x-axis label
    ax_box.set_ylabel(selected_column_percentage, fontsize=14)  # Increase font size of y-axis label

    # Display the box plot in Streamlit app
    st.pyplot(fig_box)

# Function for the second page
def page2(df):
    st.title("Page 2: NFHS-5 Data Overview Underage Marriage of girls District-State Wise Data Taken")
    if st.checkbox("Show Raw Data"):
        st.write(df)

    # Display selected columns
    columns_to_keep = ['District Names', 'State/UT', 'Women age 20-24 years married before age 18 years (%)']
    st.write("Selected Columns:", columns_to_keep)

    # Display DataFrame
    st.write("DataFrame Preview:")
    st.dataframe(df[columns_to_keep])

    # Set the style for seaborn
    sns.set(style="whitegrid")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    # State-wise comparison for 'Women age 20-24 years married before age 18 years (%)'
    plt.figure(figsize=(24, 16))
    sns.barplot(x='Women age 20-24 years married before age 18 years (%)', y='State/UT', data=df, palette='viridis')
    plt.title('State-wise Comparison of Women Age 20-24 Years Married Before Age 18',fontsize=50)
    plt.xlabel('Percentage',fontsize=30)
    plt.ylabel('State/UT',fontsize=30)

    # Display the plot
    st.pyplot(plt)

def main():
    st.markdown(
        """
        <style>
            .big-font {
                font-size: 36px !important;
                color: white;
                background-color: #3498db;
                padding: 10px;
                border-radius: 10px;
                margin-bottom: 20px;
            }
            .sub-header {
                font-size: 24px;
                color: #2c3e50;
                margin-bottom: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sidebar selection for page
    selected_page = st.sidebar.radio("Select Page", ["Page 1", "Page 2"])

    if selected_page == "Page 1":
        df1 = load_dataset1()
        page1(df1)

    elif selected_page == "Page 2":
        df2 = load_dataset2()
        page2(df2)

if __name__ == "__main__":
    main()
