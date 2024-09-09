import streamlit as st

# "Hello!!! ㅎㅇ"
# streamlit run home.py

# st.title("title")
# st.write("Hello")
# st.header("header")
# st.subheader("subheader")
# st.code("print('hello world')") # 코드박스로 명령어를 표현
# with st.echo():
#     st.write("Writing this") # 명령어 여러줄을 하나의 코드 박스로 표현

# st.markdown("*안녕하세요* 제 **이름은** ***손민섭***입니다.")
# st.markdown('''
#     :red[안녕하세요] :orange[오늘] :green[날씨가] :blue[참] : violet[좋은]
#     :gray[것] :rainbow[같아요] and :blue-background[맞아요] !.
# ''')
# st.markdown("여기에 &mdash;\
#                 :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
#
# multi = '''If you end a line with two spaces,
# a soft return is used for the next line.
#
# Two (or more) newline characters in a row will result in a hard return.
# '''
# st.markdown(multi)

if st.button('a'):
    st.write('안녕하세요')
else:
    st.write('안녕히 가세요')

st.button('b')
# interaction 되는 순간 전체 rerendering
# 버튼은 가장 미잠ㄱ에 누른 버튼만 true, 나머지는 false

