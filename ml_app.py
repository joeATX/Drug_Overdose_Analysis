import streamlit as st
# Load EDA packages
import pandas as pd


@st.cache_data
def load_data(df):
    return pd.read_pickle(df) 


# Load the data from the pickle file (or CSV file)
df = load_data('data/drug_overdose_data.pkl')

desc_template = """

#### Drug Overdose Stats Overview

This dataset provides insights into drug overdose death rates across various categories in the United States.

#### Dataset Summary
- **Number of Rows:** 22
- **Number of Columns:** 8
- **Number of Integer Data Types:** 6
- **Number of Object Data Types:** 2
- **Missing/Null Values:** 0
- **Data Range:** 1999 to 2020

#### Key Statistics
- **Death Rate by Any Opioid:** 8.23 deaths per 100,000 people
  - Approximately 8.23 individuals are dying due to any opioids per 100,000 people.
- **Average Overdose Death Rates:**
  - **Cocaine:** 2.35 deaths per 100,000 people
  - **Heroin:** 2.08 deaths per 100,000 people
  - **Synthetic Opioids:** 3.14 deaths per 100,000 people
  - **Prescription Opioids:** 3.8 deaths per 100,000 people

#### Geographic Coverage
- **Entity/Code Column:** Contains data for 1 country: United States | USA
  - This indicates the dataset includes data only from the United States.

#### Proportions of Deaths
- **Any Opioid:** 42%
- **Cocaine:** 12%
- **Heroin:** 10.6%
- **Synthetic Opioids:** 16%
- **Prescription Opioids:** 19.4%

#### Insights
- The death rate from **Any Opioid** is the highest compared to Cocaine, Heroin, Synthetic Opioids, and Prescription Opioids.
- Among Heroin, Cocaine, Synthetic Opioids, and Prescription Opioids, **Prescription Opioids** have the highest death rate.

#### Additional Information
- For detailed data and processing information, you can refer to the [original data source](https://www.example.com).
- **Source:** Data processed from the original dataset provided by Kaggle.

**Dataset Source:** Kaggle
- [Kaggle Dataset](https://www.kaggle.com/datasets/willianoliveiragibin/drug-overdose-death?select=drug-overdose-death-rates+new.csv)
"""


def run_ml_app():
    st.subheader("Machine Learning")
    # Display the description template
    st.markdown(desc_template, unsafe_allow_html=True)