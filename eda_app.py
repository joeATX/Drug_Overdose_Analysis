import streamlit as st

# Load Data Visualization pakage(s)
import matplotlib.pyplot as plt

# Load EDA packages
import pandas as pd


@st.cache_data
def load_data(df):
    return pd.read_pickle(df) 


# Load the data from the pickle file (or CSV file)
df = load_data('data/drug_overdose_data.pkl')


def run_eda_app():
    st.subheader("Exploratory Data Analysis")
    submenu = st.sidebar.selectbox("Submenu", ["Descriptive", "Plots"])
    if submenu == "Descriptive":
        st.dataframe(df)

        with st.expander("Data Types"):
            st.dataframe(df.dtypes)

        with st.expander("Data Summary"):
            st.dataframe(df.describe())

        with st.expander("Data Distribution"):
            st.dataframe(df['year'].value_counts()),
            st.dataframe(df['any_opioid'].value_counts())

    elif submenu == "Plots":
        st.subheader("Plots for Our Data")
        # Layout Bar Plot
        col1, col2 = st.columns([4, 4], gap="large")

        with col1:
            with st.bar_chart(df):
                drug_df = df
                plt.close('all')
                fig, ax = plt.subplots(figsize=(18, 10))

                bar_width = 0.15
                years = drug_df["year"]
                indices = range(len(years))

                # Plot each category with an offset to avoid overlap
                ax.bar([i - 2 * bar_width for i in indices],
                       df['any_opioid'],
                       bar_width,
                       label='Any opioid',
                       color='tab:red'
                       )
                ax.bar([i - bar_width for i in indices],
                       df['cocaine'],
                       bar_width,
                       label='Cocaine',
                       color='tab:blue'
                       )
                ax.bar(indices, df['heroin'],
                       bar_width,
                       label='Heroin',
                       color='tab:green'
                       )
                ax.bar([i + bar_width for i in indices],
                       df['synthetic_opioid'],
                       bar_width,
                       label='Synthetic opioids',
                       color='tab:purple'
                       )
                ax.bar([i + 2 * bar_width for i in indices],
                       df['prescription_opioid'],
                       bar_width,
                       label='Prescription Opioids',
                       color='tab:orange'
                       )

                # Setting labels and title
                ax.set_ylabel('Death Rates per 100,000')
                ax.set_xlabel('Year')
                ax.set_title(
                    'Trend of Drug Overdose Death Rates over the Years'
                    )
                ax.set_xticks(indices)
                ax.set_xticklabels(years)
                ax.legend(title='Drug Category')

                # Adjust layout and rotate x-ticks
                plt.xticks(rotation=45)
                plt.tight_layout()
                # Display the custom plot in Streamlit
                st.pyplot(fig)

            # Add an expandable summary below the bar graph
            with st.expander("Summary of Findings"):
                st.markdown("""
                - **Any opioid** has the highest death rates per 100,000 across the years.
                - **Cocaine** shows some fluctuations but has seen notable increases.
                - **Heroin** rates peaked around the mid-decade.
                - **Synthetic opioids** have seen a sharp rise in recent years.
                - **Prescription opioids** remain a significant issue but with lower rates compared to synthetic opioids.
                """)

            with st.line_chart(df):
                drug_df = df
                # Prepare data for the line chart
                line_data = df.set_index('year')
                # Display the line chart in Streamlit
                st.line_chart(line_data)

            # Display the line chart with a summary below in an expander
            with st.expander("Line Graph and Summary"):
                # Add a summary below the line graph
                st.markdown("""
                ### Summary of Trends
                - **Any opioid** has consistently high death rates compared to other categories.
                - **Cocaine** shows fluctuations but generally increases over the years.
                - **Heroin** has significant peaks, especially in the mid-decade.
                - **Synthetic opioids** exhibit a dramatic rise, particularly in recent years.
                - **Prescription opioids** remain a concern but with less volatility compared to synthetic opioids.
                """)

        any_opioid = df['any_opioid'].mean()
        cocaine = df['cocaine'].mean()
        heroin = df['heroin'].mean()
        synthetic_opioid = df['synthetic_opioid'].mean()
        prescription_opioid = df['prescription_opioid'].mean()

        data = [any_opioid,
                cocaine, heroin,
                synthetic_opioid,
                prescription_opioid
                ]
        labels = ['Any Opioid',
                  'Cocaine',
                  'Heroin',
                  'Synthetic Opioid',
                  'Prescription Opioid'
                  ]
        colors = ['#FF9999',
                  '#66B2FF',
                  '#99FF99',
                  '#FFCC99',
                  '#FFD700'
                  ]
                
        with col2:
            # Plot the pie chart
            fig, ax = plt.subplots(figsize=(20, 10))
            wedges, texts, autotexts = ax.pie(data,
                                              labels=labels,
                                              colors=colors,
                                              autopct='%1.1f%%',
                                              startangle=140
                                              )

            # Customize fonts for labels and percentages
            for text in texts:
                text.set_fontsize(28)  # Set the font size for labels
                text.set_fontweight('bold')  # Set the font weight for labels

            for autotext in autotexts:
                autotext.set_fontsize(28)  
                autotext.set_fontweight('bold')
        
            ax.set_title('Average Drug Overdose Death Rates Distribution',
                         fontsize=30,
                         fontweight='bold'
                         )

            # Adjust layout to ensure everything fits
            plt.tight_layout()

            # Display the pie chart in Streamlit
            st.pyplot(fig)

            st.subheader("Histogram of Data")
    
            # Create a histogram using Matplotlib
            plt.figure(figsize=(20, 10))
            
            # Plot histogram for each column
            for col in df.columns[2:]:  # Adjust indexing based on your columns
                plt.hist(df[col], bins=20, alpha=0.5, label=col)
    
            plt.title('Histogram of Data', fontsize=18)
            plt.xlabel('Values', fontsize=18)
            plt.ylabel('Frequency', fontsize=18)
            plt.legend(fontsize=18)

            # Set x-ticks to display all labels
            plt.xticks(rotation=45, fontsize=14)

            # Adjust layout to ensure everything fits
            plt.tight_layout()
            
            # Display the plot in Streamlit
            st.pyplot(plt.gcf())  # Use plt.gcf() to get the current figure

            

        