import streamlit as st
import numpy as np
from PIL import Image
import os
from eval import eval_image

#Title of the website#
st.subheader(":rocket: Data Science for Public Health|Capstone Project :rocket:")
url = 'https://github.com/CigriWang/DS4PH_Course_Project'
st.subheader("Copyright@[:orange[DS4PH]](%s) :zombie:"%url )
st.title("This is the demostration website for :blue[photo denoising], have some fun!!! :genie:")

#Modules for images selection#
#image file path
Natural_image_path = "./dataset/test/Natural_Images/input"
Por_image_path = "./dataset/test/Old_Photos/input"
Natural_image = os.listdir(Natural_image_path)
Por_image = os.listdir(Por_image_path)

st.subheader("Please Select The Type of Images")
option1 = st.selectbox(
    'Which types of image you want to play with?',
    ('Natural Images', 'Old Photos', 'Upload your own image'))

if option1 == 'Natural Images':
    image_type = "Natural_Images"
    element = [Natural_image_path+'/'+'%s'%i for i in Natural_image]
    st.write("Here are examples of natural images")
    element = [np.asarray(Image.open(i)) for i in element]
    #Display the 
    col1,col2,col3 = st.columns(3)
    with col1:
        st.image(element[0],caption = 'Example1')
    with col2:
        st.image(element[1],caption = 'Example2')
    with col3:
        st.image(element[2],caption = 'Example3')
    option2 = st.radio(
        'Which deep learning model do you want to play with?',
        ('SUNet', 'SWIN', 'UNet')
    )
    option3 = st.radio(
        'Which example do you want to use?',
        ('Example1','Example2','Example3')
    )
    if option2 == 'SUNet':
        st.write("The denoised image from %s model is generated below!"%option2)
        eval_image(image_type,option2)
        cola, colb = st.columns(2)
        with cola:
            st.image(Image.open('./dataset/test/%s/input/%s.png'%(image_type,option3)), caption = 'Original Image')
        with colb:
            st.image(Image.open('./model_'+option2+"/gen_images/"+option3+'.png'),caption = 'Denoised Images with %s'%option2)
        

    if option2 == 'SWIN':
        st.write("The denoised image from %s model is generated below!"%option2)
        eval_image(image_type,option2)
        cola, colb = st.columns(2)
        with cola:
            st.image(Image.open('./dataset/test/%s/input/%s.png'%(image_type,option3)), caption = 'Original Image')
        with colb:
            st.image(Image.open('./model_'+option2+"/gen_images/"+option3+'.png'),caption = 'Denoised Images with %s'%option2)
              
    if option2 == 'UNet':
        st.write("The denoised image from %s model is generated below!"%option2)
        eval_image(image_type,option2)
        cola, colb = st.columns(2)
        with cola:
            st.image(Image.open('./dataset/test/%s/input/%s.png'%(image_type,option3)), caption = 'Original Image')
        with colb:
            st.image(Image.open('./model_'+option2+"/gen_images/"+option3+'.png'),caption = 'Denoised Images with %s'%option2)
          
elif option1 == 'Old Photos':
    image_type = "Old_Photos"
    element = [Por_image_path+'/'+'%s'%i for i in Por_image]
    st.write("Here are examples of old photos")
    #st.write(element)
    element = [np.asarray(Image.open(i)) for i in element]
    #st.write(np.array(element).shape)
    col1,col2,col3 = st.columns(3)
    with col1:
        st.image(element[0],caption = 'Example1')
    with col2:
        st.image(element[1],caption = 'Example2')
    with col3:
        st.image(element[2],caption = 'Example3')
    option2 = st.radio(
    'Which deep learning model do you want to play with?',
    ('SUNet', 'SWIN', 'UNet'))
    option3 = st.radio(
        'Which example do you want to use?',
        ('Example1','Example2','Example3')
    )
    if option2 == 'SUNet':
        st.write("The denoised image from %s model is generated below!"%option2)
        eval_image(image_type,option2)
        cola, colb = st.columns(2)
        with cola:
            st.image(Image.open('./dataset/test/%s/input/%s.png'%(image_type,option3)), caption = 'Original Image')
        with colb:
            st.image(Image.open('./model_'+option2+"/gen_images/"+option3+'.png'),caption = 'Denoised Images with %s'%option2)
        
    if option2 == 'SWIN':
        st.write("The denoised image from %s model is generated below!"%option2)
        eval_image(image_type,option2)
        cola, colb = st.columns(2)
        with cola:
            st.image(Image.open('./dataset/test/%s/input/%s.png'%(image_type,option3)), caption = 'Original Image')
        with colb:
            st.image(Image.open('./model_'+option2+"/gen_images/"+option3+'.png'),caption = 'Denoised Images with %s'%option2)
        
    if option2 == 'UNet':
        st.write("The denoised image from %s model is generated below!"%option2)
        eval_image(image_type,option2)
        cola, colb = st.columns(2)
        with cola:
            st.image(Image.open('./dataset/test/%s/input/%s.png'%(image_type,option3)), caption = 'Original Image')
        with colb:
            st.image(Image.open('./model_'+option2+"/gen_images/"+option3+'.png'),caption = 'Denoised Images with %s'%option2)
        
elif option1 == 'Upload your own image':
    uploaded_file = st.file_uploader("Choose an image...", )
    image_type = "upload"
    if uploaded_file is not None:
        option2 = st.radio(
        'Which deep learning model do you want to play with?',
        ('SUNet', 'SWIN', 'UNet'))
        image = np.asarray(Image.open(uploaded_file))
        #Save the upload file into working directory#
        image = Image.fromarray(image)
        image.save('./dataset/test/%s/input/temp.png'%image_type)
        image.save('./dataset/test/%s/label/temp.png'%image_type)

        #Denoise the model with selected model#
        if option2 == 'SUNet':
            st.write("The denoised image from %s model is generated below!"%option2)
            eval_image(image_type,option2)
            cola, colb = st.columns(2)
            with cola:
                st.image(Image.open(uploaded_file), caption = 'Uploaded Image')
            with colb:
                st.image(Image.open('./model_'+option2+"/gen_images/"+'temp.png'),caption = 'Denoised Images with %s'%option2)
        if option2 == 'SWIN':
            st.write("The denoised image from %s model is generated below!"%option2)
            eval_image(image_type,option2)
            cola, colb = st.columns(2)
            with cola:
                st.image(Image.open(uploaded_file), caption = 'Uploaded Image')
            with colb:
                st.image(Image.open('./model_'+option2+"/gen_images/"+'temp.png'),caption = 'Denoised Images with %s'%option2)
        if option2 == 'UNet':
            st.write("The denoised image from %s model is generated below!"%option2)
            eval_image(image_type,option2)
            cola, colb = st.columns(2)
            with cola:
                st.image(Image.open(uploaded_file), caption = 'Uploaded Image')
            with colb:
                st.image(Image.open('./model_'+option2+"/gen_images/"+'temp.png'),caption = 'Denoised Images with %s'%option2)
                
