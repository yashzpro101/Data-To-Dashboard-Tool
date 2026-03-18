"""
main.py
Author: [Jitansu]
Role: Interface Lead

Description:
The main Streamlit application that ties together the data processing 
and visualization modules for our team's scholarship portfolio project.
"""
import streamlit as st
import pandas as pd

# Importing the team's modules
import data_handler as dh # Role 1's file
import visuals as vs      # Subhakanta's file (Role 2)

# Set the page to be wide for better chart viewing
st.set_page_config(page_title="Interactive Data Explorer", layout="wide")

st.title(" Interactive Data Analysis Dashboard")
st.sidebar.header("1. Upload Your Data")

# The sidebar file uploader
uploaded_file = st.sidebar.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # --- PHASE 1: Data Architect's Domain ---
    # Calling Role 1's function to load and clean the data
    df = dh.load_and_clean_data(uploaded_file) 
    
    st.subheader("Data Overview")
    st.dataframe(df.head()) # Shows an interactive table of the first 5 rows

    # --- PHASE 2: Visualization Expert's Domain ---
    st.markdown("---")
    st.subheader(" Visual Insights")
    
    # We use st.columns to put charts side-by-side for a professional look
    col1, col2 = st.columns(2)
    
    # Note for Interface Lead: You will need to change 'df.columns[0]' etc., 
    # to the actual column names you want to graph once you know your dataset!
    
    with col1:
        st.markdown("#### Category Analysis")
        # Calling Subhakanta's bar chart function
        bar_fig = vs.create_bar_chart(df, x_axis=df.columns[0], y_axis=df.columns[1])
        # st.plotly_chart is required to render Plotly figures!
        st.plotly_chart(bar_fig, use_container_width=True)
        
    with col2:
        st.markdown("#### Distribution")
        # Calling Subhakanta's pie chart function
        pie_fig = vs.create_pie_chart(df, names_col=df.columns[0], values_col=df.columns[1])
        st.plotly_chart(pie_fig, use_container_width=True)

    st.markdown("---")
    st.markdown("#### Feature Correlation")
    
    # Calling Subhakanta's seaborn heatmap function
    heatmap_fig = vs.create_correlation_heatmap(df)
    
    if heatmap_fig is not None:
        # st.pyplot is required to render Matplotlib/Seaborn figures!
        st.pyplot(heatmap_fig)
    else:
        st.warning("Not enough numerical data to generate a correlation heatmap.")
        
else:
    st.info("Awaiting file upload. Please upload a dataset in the sidebar to begin.")
