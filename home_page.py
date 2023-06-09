import streamlit_pandas as sp
import pandas as pd
import streamlit as st
from pathlib import Path
file = Path(__file__).parent/ 'C:/Users/willi/OneDrive/Desktop/Data/Coding_Temple_Week_6/titanic_cleaned.csv' 
@st.cache(allow_output_mutation=True)

def pipeline(filepath):
    dataframe = pd.read_csv(filepath)
    return dataframe

df = pipeline(file)

st.title('Titanic Data')
st.text("Here I've built an application where you can filter throught the Titanic data set using the buttons on the side of the page." )


features = {

    'sex': 'multiselect',
    'embarked': 'select',
    'survived': 'multiselect',
    'p_class': 'multiselect',
    'sib_sp': 'multiselect',
    'parch': 'multiselect'
}

all_widgets = sp.create_widgets(df, features, ignore_columns=['passanger_id'])
res = sp.filter_df(df, all_widgets)
st.write(res)