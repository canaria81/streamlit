# 웹 대시보드에 이미지 파일, 동영상 파일 등록 방법
import streamlit as st
# 이미지 처리를 위한 라이브러리
from PIL import Image

def main() :
    img = Image.open('image_03.jpg')
    print(img)
    st.image(img)
    st.image(img,use_column_width=True)
    image_url = 'https://andar.co.kr/web/upload/category/shop1_2405_top_463389.jpg'
    st.image(image_url)

# 동영상
# rb => 파일을 읽는 모드
video_file = open('secret_of_success.mp4','rb')
st.video(video_file)
if __name__== '__main__' :
   
    main()