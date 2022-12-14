import streamlit as st
# 유저하테 데이터를 입력받는 방법

def main() :
# 텍스트를 입력받는 방법    
    name =st.text_input('이름을 입력하세요')
    st.title(name)

    name2= st.text_input('이름을 입력 : ',max_chars=5)
    st.title(name2)

    mesg1 = st.text_area('메시지 입력 : ')
    st.text(mesg1)
    mesg2 = st.text_area('메시지 입력 : ',height=2)
    st.text(mesg2)
 # 숫자 입력 받는 방법
# 디폴트는 소수로 되어 있지만, 정수로 입력하면 (,1000,3000) 됨
    year =st.number_input('출생년도 입력하세요',1000,3000) 
    st.text(year)

    number =st.number_input('소수를 입력하세요',0.1,100.0,step=0.7)

    # -- 날짜 입력
    my_date= st.date_input('약속 날짜 입력')
    st.write(my_date)

    #시간 입력
    my_time =st.time_input('약속시간을 입력')
    st.write(my_time)

        #-- st.text() my_time.strftime
    # 비밀번호 입력
    pws  =st.text_input('비밀번호 입력',type='password')
    st.text(pws)
    #색깔 입력(rgb로 컬러 표시-16진수)
    color= st.color_picker('색을 선택')
    st.text(color)

if __name__== '__main__' :
   
    main()