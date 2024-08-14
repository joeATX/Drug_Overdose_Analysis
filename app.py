import streamlit as st
import pandas as pd
# Import our mini apps
from eda_app import run_eda_app
# Import our mini apps
from ml_app import run_ml_app


@st.cache_data
def load_data(df):
    return pd.read_pickle(df)


df = load_data('data/drug_overdose_data.pkl')

desc_temp = """
#### Drug Overdose Stats App
This dataset contains the most current drug overdose data.

#### About the Dataset
This dataset provides the annual number of deaths in the United States from drug overdoses per 100,000 people. Overdoses can result from the intentional excessive use of substances or from poisoning due to altered or mixed substances, where the user is unaware of the drug’s potency.

The data is sourced from:
- **US Centers for Disease Control and Prevention WONDER**
- **Data published by US Centers for Disease Control and Prevention WONDER**
- **Retrieved from** [US Centers for Disease Control and Prevention WONDER](https://www.drugabuse.gov/related-topics/trends-statistics/overdose-death-rates)

#### Data Processing
At Our World in Data, all data and visualizations rely on information from original data providers. The preparation process involves:
- Standardizing country names and world region definitions
- Converting units
- Calculating derived indicators (e.g., per capita measures)
- Adding or adapting metadata

For a detailed description of our data pipeline and the code used, please read about our [data pipeline](https://ourworldindata.org/data-pipeline).

#### How to Cite This Data
In-line citation for limited space:
- **Any opioids Deaths per 100,000 people attributed to any opioids.**

**Source:** US Centers for Disease Control and Prevention WONDER – processed by Our World in Data.

**Dataset Source:** Kaggle

#### Datasource
- [Kaggle Dataset](https://www.kaggle.com/datasets/willianoliveiragibin/drug-overdose-death?select=drug-overdose-death-rates+new.csv)

#### App Content
- EDA Section: Exploratory Data Analysis
- ML Section: ML Predictor App
"""


def main():
    st.title("Drug Overdose Death Rate")
    menu = ["Home", "EDA", "ML", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write(desc_temp)
    elif choice == "EDA":
        run_eda_app()
    elif choice == "ML":
        run_ml_app()

        
if __name__ == '__main__':
    main()