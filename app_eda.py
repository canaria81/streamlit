import streamlit as st
import pandas as pd 

def run_eda_app() :
    st.subheader('eda 화면입니다')
    df=pd.read_csv('iris.csv')
    st.text('eda화면에서 할 일을 여기에 코딩합니다')