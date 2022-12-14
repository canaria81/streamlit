import pandas as pd
import streamlit  as st

# ui 요소들을 처리하는 방법
# 버튼, 라디오버튼, 셀렉트 박스, 멀티 셀렉트,슬라이더
def main():
   df= pd.read_csv('iris.csv')
  

   #버튼을 클릭하면, 데이터 프레임이 보이게 만들기
   if st.button('데이터프레임 보기'):
        st.dataframe(df)

   name ='Mike'
   if st.button('대문자로'):
    #    print(name.upper())
        st.text(name.upper())

   if st.button('소문자로'):
        st.text(name.lower())

        # st.radio('정렬을 선택하세요',['오름차순,내림차순',])
       status = st.radio('정렬을 선택하세요',['오름차순','내림차순'])
        if status == '오름차순' :
            # df의 petal_length 컬럼을 오름차순 출력
           st.dataframe( df.sort_values('petal_penght'))

        elif status =='내림차순' :
            # df의 petal_length 컬럼을 내림차순 출력
              st.dataframe(df.sort_values('petal_penght',ascending= False))

   
    # 체크박스를 체크하면 데이터 프레임이 나오고, 해제하면 테이터프레임이 나오지 않게함
    if  st.checkbox('show / hide') :
        st.dataframe(df)
    else :
        st.write(' ')
    # 셀렉트 박스 : 여러 개 중에 한 개 선택
    languege = ['python','c','java,','php']
    my_choice=st.selectbox('좋아하는 언어를  선택하세요',languege)
    print (my_choice)
    #유저가 선택하면 해당 언어를 다음처럼 표시함
    # python언어를  가장 좋아합니다
   st.write( {}'언어를 가장 좋아합니다'.format(my_choice))
    st.text('ㄴ'+ my_choice +'언어를 가장 좋아합니다')
   
# 유저가 선택한 언어가 파이썬이나 php나 go언어이면 배우기 쉽습니다 화면에 출력
# 자바나 씨언어 선택 => 배우기 어렵습니다 출력

if my_choice=='python' or my_choice=='php' :
    st.text('배우기 쉽습니다')
elif my_choice == 'c' or my_choice =='java':
    st.text('배우기 어렵ㅂ습니다.')
if __name__=='__main__':
    main()

    # 여러 개를 선택 할 수 있게 하는 multiselect
    # 아이리스 데이터 프레임의 컬럼이름을 가져오세요

    # st.text(df.columns)
     selected_list = st.multiselect('원하는 컬럼을 선택',df.columns)
     print(selected_list)

     #유저가 컬럼을 선택하면 해당컬럼의 화면에 보여주고, 선택하지 않으면 데이터프레임을 출력하지 않음


    if len(selected_list)==0 :
        st.text(' ')
        else :
            st.dataframe(df[selected_list])
    # 슬라이더 => st.slider('나이',1,100)
    age= st.slider('나이',1,100)
    st.text('당신이 선택한 나이는'+ str(age)+ '입니다')

    st.slider('데이터',1,100,step=5)
    # 디폴드값
    st.slider('데이터',1,200,value=75)
    # 0.1소수점 
    st.slider('데이터',0.0,1.0,step=0.1)
    
    with st.expander('hello') :
        st.text('안녕하세요')

 if __name__== '__main__' :
    main()           