import streamlit  as st
def main() :
    # 문자열 표현방식
    st.title('웹 대시보드')
      #  print('웹 대시보드')
    st.text('웹 대시보드 개발하기')
    st.header('이 영역은 헤더 영역')
    st.subheader('서브헤더 영역')
    st.success('성공했을 때 보여줄때 사용')
    st.warning('경고 메시지')
    st.info('정보 메시지')
    st.error('문제가 발생했음')
    # 파이썬의 함수들의 정보를 출력하고 싶을때 
    st.help(sum)
if __name__== '__main__':
    main()