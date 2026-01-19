import streamlit as st
import pandas as pd
import numpy as np


# Title of the app
st.title("Hello Streamlit App")

# Display a simple text
st.write("This is a simple text displayed using Streamlit.")


# Create a simple dataframe

df=pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D']
})


# Display the dataframe
st.write("Here is a simple dataframe:")
st.write(df)

#create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),                   #20 rows 3 col
    columns=['a','b','c']
)
st.line_chart(chart_data)






# to run this app, use the command:
# streamlit run app.py