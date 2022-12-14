import streamlit as st
import pandas as pd 
def run_ml_app() :
    st.subheader('ml 화면입니다')
    df=pd.read_csv('iris.csv')
    st.text('ml화면에서 할 일을 여기에 코딩합니다')