import streamlit as st
import pandas as pd
# import cv2
from  PIL import Image, ImageEnhance

# header= st.container()
# dataset= st.container()
# features=st.container()

image = Image.open('nupco.png') #Brand logo image (optional)
# # col1, col2 = st.columns( [0.8, 0.2])
   
    
# with header:
#     st.image(image, width=150)
#     st.title('Welcome to Data Managment')
#     st.text('This is for collecte Data sharing Request')
    
# with dataset:
#     st.header('Data Request')
#     st.text('--')
#     text_data=pd.read_csv("book.csv",sep=';')
#     st.write(text_data)
#     st.subheader('pick-up loction ID distrbution on')

# # with open("style.css") as f:
# #     st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# st.sidebar.image('nupco.png', width=200)

# import streamlit as st
# import pandas as pd
# import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# st.sidebar.header('Dashboard `version 2`')
st.sidebar.image(image, width=150)
st.sidebar.title('Data Sharing Requests')
# st.sidebar.subheader('Heat map parameter')
# time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

# st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('Q1', 'Q2','Q3','Q4'))

# st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['date', 'code'], ['date', 'code'])
# plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

st.sidebar.markdown('''
---
Created by Data Managment Department 
''')


# Row A
st.markdown('### OVERVIEW ')
st.write('Summary of the data sharing requests')
col1, col2, col3 = st.columns(3)
col1.metric("Shared Data", "", "10")
col2.metric("Processed", "", "8")
col3.metric("Refuse", "", "-2")

# Row B
data = pd.read_csv('book.csv',sep=';')


# c1, c2 = st.columns((7,3))
# with c1:
#     st.markdown('### Heatmap')
#     plost.time_hist(
#     data=seattle_weather,
#     date='date',
#     x_unit='week',
#     y_unit='day',
#     color=time_hist_color,
#     aggregate='median',
#     legend=None,
#     height=345,
#     use_container_width=True)
# with c2:
#     st.markdown('### Donut chart')
#     plost.donut_chart(
#         data=stocks,
#         theta=donut_theta,
#         color='company',
#         legend='bottom', 
#         use_container_width=True)

# Row C
st.markdown('### Display Data')
st.write(data)
# st.line_chart(seattle_weather, x = 'date', y = plot_data, height = plot_height)
