# run it like 'streamlit run app.py'

import streamlit as st
import pandas as pd
import numpy as np


#title
st.title("Hello StreamLit")

#display a simple text
st.write("This is a simple text")

# create a simple Dataframe
data = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[4,5,6,7]
})

## Display the dataframe

st.write("Here is the dataframe")
st.write(data)

# create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
