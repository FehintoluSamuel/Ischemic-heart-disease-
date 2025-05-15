import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Ischemic Heart Disease Dashboard", layout="wide")

# Title
st.title("Ischemic Heart Disease Statistics Dashboard")

# Load datasets
df1 = pd.read_csv(r'analysis/cleaned_data_df1.csv')
df2 = pd.read_csv(r'\analysis\\rough_data\\cleaned_data_df2.csv')
df3 = pd.read_csv(r'\analysis\\cleaned_data_df3.csv')
df4 = pd.read_csv(r'\analysis\\rough_data\\cleaned_data_df4.csv')

# Plot 1 - Bar chart of deaths per year
df1_agg = df1.groupby('Year')['No. of deaths'].sum().reset_index()
fig_df1_A = px.bar(df1_agg, x='Year', y='No. of deaths', title='Number of Deaths Due to Ischemic Heart Disease')

# Plot 2 - Line chart with bounds
df1_agg_B = df1.groupby('Year')[['No. of deaths', 'Upper bound', 'Lower Bound']].sum().reset_index()
fig_df1_B = px.line(df1_agg_B, x='Year', y=['No. of deaths', 'Upper bound', 'Lower Bound'])
fig_df1_B.update_layout(title='Death Trends in Nigeria with Bounds', xaxis_title='Year', yaxis_title='No. of Deaths')

# Plot 3 - Health expenditure
fig_df4 = px.bar(df4, x='Year', y='Health expenditure per capita (US$)', title='Yearly Health expenditure per capita (US$)')

# Plot 4 - Pie chart of deaths by gender
df1_C_agg = df1.groupby('sex')['No. of deaths'].sum().reset_index()
colors = ['#7A288A', '#6c5ce7']
fig_df1_C = px.pie(df1_C_agg, values='No. of deaths', names='sex', color_discrete_sequence=colors)
fig_df1_C.update_traces(title='Total No. of Deaths by Gender')

# Plot 5 - Top 10 age groups
age_top_10 = df1.groupby('Age')['No. of deaths'].sum().sort_values(ascending=False).head(10)
fig_df1_D = px.bar(age_top_10, title='Top 10 Age Brackets with Highest Number of deaths')
fig_df1_D.update_layout(xaxis_title='Age', yaxis_title='No. of Deaths')

# Plot 6 - Top 10 causes of death
fig_df2 = px.bar(df2, x='Deaths per 100,000', y='Death_cause',
                 labels={'Death_cause': 'Death Causes', 'Deaths per 100,000': 'Deaths per 100,000 people'})
fig_df2.update_layout(yaxis=dict(autorange='reversed'), title='Top 10 Causes of Death in Nigeria 2021')

# Plot 7 - People per doctor
fig_df3 = px.bar(df3, x='Year', y='People per doctor', title='Number of Patients Per Physician For Each Year')

# --- Layout ---
# First row: fig_df1_A, fig_df1_B, fig_df4
col1, col2, col3 = st.columns(3)
col1.plotly_chart(fig_df1_A, use_container_width=True)
col2.plotly_chart(fig_df1_B, use_container_width=True)
col3.plotly_chart(fig_df4, use_container_width=True)

# Second row: fig_df1_C, fig_df1_D, fig_df2
col4, col5, col6 = st.columns(3)
col4.plotly_chart(fig_df1_C, use_container_width=True)
col5.plotly_chart(fig_df1_D, use_container_width=True)
col6.plotly_chart(fig_df2, use_container_width=True)

# Optional: Add third row if you want to display fig_df3
# st.subheader("Healthcare Resources")
# st.plotly_chart(fig_df3, use_container_width=True)
