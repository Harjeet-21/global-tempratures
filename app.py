import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import warnings

st.set_page_config(
    page_title="Global Temperature App",
    page_icon="🌍",
    layout="wide"
)
st.title("🌍 Global Temperature")

@st.cache_data
def load_data():
    try:
       df = pd.read_csv("all_countries_global_temperature.csv")
       return df
    except:
        st.error("Something went wrong")

df = load_data()

st.dataframe(df)
@st.cache_data
def clean_data():
    cleaned_data = df.copy()
    cleaned_data.drop("ObjectId", axis=1,inplace=True)
    cleaned_data.fillna({
    "1970":cleaned_data["1970"].median(), 
    "1971":cleaned_data["1971"].median(), 
    "1972":cleaned_data["1972"].median(), 
    "1973":cleaned_data["1973"].median(), 
    "1974":cleaned_data["1974"].median(), 
    "1975":cleaned_data["1975"].median(),
    "1976":cleaned_data["1976"].median(),
    "1977":cleaned_data["1977"].median(), 
    "1978":cleaned_data["1978"].median(),
    "1979":cleaned_data["1979"].median(), 
    "1980":cleaned_data["1980"].median(), 
    "1981":cleaned_data["1981"].median(), 
    "1982":cleaned_data["1982"].median(), 
    "1983":cleaned_data["1983"].median(),
    "1984":cleaned_data["1984"].median(), 
    "1985":cleaned_data["1985"].median(), 
    "1986":cleaned_data["1986"].median(), 
    "1987":cleaned_data["1987"].median(), 
    "1988":cleaned_data["1988"].median(), 
    "1989":cleaned_data["1989"].median(), 
    "1990":cleaned_data["1990"].median(), 
    "1991":cleaned_data["1991"].median(),
    "1992":cleaned_data["1992"].median(),
    "1993":cleaned_data["1993"].median(),
    "1994":cleaned_data["1994"].median(),
    "1995":cleaned_data["1995"].median(),
    "1996":cleaned_data["1996"].median(),
    "1997":cleaned_data["1997"].median(),
    "1998":cleaned_data["1998"].median(),
    "1999":cleaned_data["1999"].median(),
    "2000":cleaned_data["2000"].median(),
    "2001":cleaned_data["2001"].median(),
    "2002":cleaned_data["2002"].median(),
    "2003":cleaned_data["2003"].median(),
    "2004":cleaned_data["2004"].median(),
    "2005":cleaned_data["2005"].median(),
    "2006":cleaned_data["2006"].median(),
    "2007":cleaned_data["2007"].median(),
    "2008":cleaned_data["2008"].median(),
    "2009":cleaned_data["2009"].median(),
    "2010":cleaned_data["2010"].median(),
    "2011":cleaned_data["2011"].median(),
    "2012":cleaned_data["2012"].median(),
    "2013":cleaned_data["2013"].median(),
    "2014":cleaned_data["2014"].median(),
    "2015":cleaned_data["2015"].median(),
    "2016":cleaned_data["2016"].median(),
    "2017":cleaned_data["2017"].median(),
    "2018":cleaned_data["2018"].median(),
    "2019":cleaned_data["2019"].median(),
    "2020":cleaned_data["2020"].median(),
    "2021":cleaned_data["2021"].median()},
    inplace=True)
    return cleaned_data



cleaned_df = clean_data()
st.write("Cleaned Data:")
st.dataframe(cleaned_df)
