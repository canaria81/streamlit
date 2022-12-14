import streamlit as st
import pandas as pd 
from datetime import date, datetime
from PIL import Image
# 다른 파일의 함수를 호출하고 싶으면 함수를 임포트 함
from app_home import run_home_app
from app_eda import run_eda_app 
from app_ml import run_ml_app
from app_About import run_about_app

def main():
    st.title('파일분리 앱')
    # exploratory data analysis
    menu = ['HOME','EDA','ML','About']
    choice =st.sidebar.selectbox('메뉴',menu)
    if  choice=='HOME' :
        run_home_app()
    elif choice=='EDA' :
        run_eda_app() 
    elif choice=='ML' :
        run_ml_app()
    elif choice=='About' :
        run_about_app()
if __name__=='__main__' :
    main()