# app.py
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, classification_report
from sklearn.impute import SimpleImputer

# Page 1
def page_1():
    st.title('Higher Education Analysis')
    st.subheader('Distribution of GPI Across Different Education Levels')

    # Load your dataset
    df_higher_edu = pd.read_csv(r"C:\Users\aayus\Downloads\Higher Education.csv")
    df_higher_edu = df_higher_edu.dropna()

    plt.figure(figsize=(12, 8))
    sns.boxplot(data=df_higher_edu.iloc[:, 2:], palette='viridis')
    plt.title('Distribution of GPI Across Different Education Levels')
    plt.xlabel('Education Level')
    plt.ylabel('GPI')
    plt.xticks(rotation=45)

    # Pass the Matplotlib figure explicitly to st.pyplot()
    fig, ax = plt.subplots()
    ax = sns.boxplot(data=df_higher_edu.iloc[:, 2:], palette='viridis')
    ax.set_title('Distribution of GPI Across Different Education Levels')
    ax.set_xlabel('Education Level')
    ax.set_ylabel('GPI')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

    st.subheader('Regression Model for Level - Total')
    features_regression = ['Level - Ph.d', 'Level - M.Phil', 'Level - Post Graduate', 'Level - Under Graduate', 'Level - PG Diploma', 'Level - Diploma', 'Level - Certificate', 'Level - Integrated']

    X_regression = df_higher_edu[features_regression]
    y_regression = df_higher_edu['Level - Total']

    X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_regression, y_regression, test_size=0.2, random_state=42)

    model_reg = RandomForestRegressor()
    model_reg.fit(X_train_reg, y_train_reg)
    y_pred_reg = model_reg.predict(X_test_reg)

    mse_reg = mean_squared_error(y_test_reg, y_pred_reg)
    st.subheader('Regression Model Evaluation')
    st.write(f'Mean Squared Error: {mse_reg}')

    st.subheader('Classification Model for GPI Category')
    bins = [0, 25, 50, 75, 100]
    labels = ['0-25%', '25-50%', '50-75%', '75-100%']
    df_higher_edu['GPI_Category'] = pd.cut(df_higher_edu['Level - Total'], bins=bins, labels=labels, include_lowest=True)

    features_classification = df_higher_edu.iloc[:, 2:-3]
    X_classification = pd.get_dummies(features_classification, drop_first=True)
    y_classification = df_higher_edu['GPI_Category']

    X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(X_classification, y_classification, test_size=0.2, random_state=42)

    imputer_features_clf = SimpleImputer(strategy='mean')
    X_train_imputed_clf = imputer_features_clf.fit_transform(X_train_clf)
    X_test_imputed_clf = imputer_features_clf.transform(X_test_clf)

    imputer_target_clf = SimpleImputer(strategy='most_frequent')
    y_train_imputed_clf = imputer_target_clf.fit_transform(y_train_clf.values.reshape(-1, 1)).ravel()

    model_clf = RandomForestClassifier()
    model_clf.fit(X_train_imputed_clf, y_train_imputed_clf)
    y_pred_clf = model_clf.predict(X_test_imputed_clf)

    classification_rep_clf = classification_report(y_test_clf, y_pred_clf)
    st.subheader('Classification Model Evaluation')
    st.write('Random Forest Classifier - Classification Report:')
    st.code(classification_rep_clf)

# Page 2
def page_2():
    st.title('Dropout Rate EDA and Insights')

    # Load the dataset
    df_dropout = pd.read_csv(r"C:\Users\aayus\Downloads\Statement_SES_2011-12-DropOut (1).csv")

    # Clean the dataset (handle missing values, convert 'Year' to numerical values)
    df_dropout = df_dropout.replace('NA', pd.NA).dropna()
    df_dropout['Year'] = df_dropout['Year'].str.extract('(\d+)').astype(float)

    # Display the raw dataset
    if st.checkbox("Show Raw Data"):
        st.write(df_dropout)

    # Summary statistics
    st.subheader('Summary Statistics')
    st.write(df_dropout.describe())

    # Line plot for dropout rates over the years
    st.subheader('Line Plot: Dropout Rates Over the Years')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df_dropout[['Year', 'All Categories - Classes I-V - Boys', 'All Categories - Classes I-V - Girls']], x='Year', y='All Categories - Classes I-V - Boys', label='Boys', ax=ax)
    sns.lineplot(data=df_dropout[['Year', 'All Categories - Classes I-V - Boys', 'All Categories - Classes I-V - Girls']], x='Year', y='All Categories - Classes I-V - Girls', label='Girls', ax=ax)
    ax.set_xlabel('Year')
    ax.set_ylabel('Dropout Rate')
    ax.legend()
    st.pyplot(fig)

    # Bar plot for the latest year's dropout rates
    latest_year = df_dropout['Year'].max()
    latest_year_data = df_dropout[df_dropout['Year'] == latest_year][['All Categories - Classes I-V - Boys', 'All Categories - Classes I-V - Girls']]
    latest_year_data = latest_year_data.melt(var_name='Gender', value_name='Dropout Rate')

    st.subheader(f'Bar Plot: Dropout Rates for Boys and Girls in the Latest Year ({int(latest_year)})')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=latest_year_data, x='Gender', y='Dropout Rate', palette='viridis', ax=ax)
    ax.set_xlabel('Gender')
    ax.set_ylabel('Dropout Rate')
    st.pyplot(fig)

    # Correlation heatmap
    st.subheader('Correlation Heatmap')
    correlation_matrix = df_dropout.corr()
    fig, ax = plt.subplots(figsize=(14, 10))  # Larger size for the heatmap
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    st.pyplot(fig)

# Main Streamlit app
if __name__ == '__main__':
    # Sidebar to select page
    page = st.sidebar.selectbox("Select a Page", ["Page 1", "Page 2"])

    # Display selected page
    if page == "Page 1":
        page_1()
    elif page == "Page 2":
        page_2()
