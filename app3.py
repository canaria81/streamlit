# 판다스 데이터 프레임을 웝화면으로 출력하는 방법

import pandas as pd
import streamlit  as st

def main():
   df= pd.read_csv('iris.csv')
 #  print (df)
   # 화면
   st.dataframe(df)
   species = df['species'].unique()
   st.text('아이리스 꽃은 '+species +'으로 되어있다')
if __name__=='__main__':
    main()