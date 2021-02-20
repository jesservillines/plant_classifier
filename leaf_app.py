import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array, array_to_img
import numpy as np
from PIL import Image
import base64
import sys
import io

#classes = {0:"Scab",1:"Rot",2:"Rust",3:"Healthy"}

suggestions = {
'Apple - Black Rot':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Apple - Cedar Apple Rust':"You have got the Rot! Do the Rot treatment as soon as possible!",
 'Apple - Healthy':"You have got the Rust! Do the Rust treatment as soon as possible!" ,
 'Blueberry - Healthy':"You are healthy! Continue doing what you are doing.",
 'Cherry - Healthy':"You are healthy! Continue doing what you are doing.",
 'Cherry - Powdery Mildew':"You have got the Powdery mildew! Do the Powdery mildew treatment as soon as possible!",
 'Corn - Gray Leaf Spot':"You are healthy! Continue doing what you are doing.",
 'Corn - Common Rust':"You have got the Leaf spot! Do the Leaf spot treatment as soon as possible!",
 'Corn - Healthy':"You have got the Common_rust! Do the Common_rust treatment as soon as possible!",
 'Corn - Northern Leaf Blight':"You have got the Northern Leaf Blight! Do the Northern Leaf Blight treatment as soon as possible!",
 'Grape - Black Rot':"You are healthy! Continue doing what you are doing.",
 'Grape - Esca':"You have got the Black rot! Do the Black rot treatment as soon as possible!",
 'Grape - Healthy':"You have got the Black Measles! Do the Black Measles treatment as soon as possible!",
 'Grape - Leaf Blight':"You have got the Leaf blight! Do the Leaf blight treatment as soon as possible!",
 'Orange - Haunglongbin':"You have got the Citrus greening! Do the Citrus greening treatment as soon as possible!",
 'Peach - Bacterial Spot':"You have got the Bacterial spot! Do the Bacterial spot treatment as soon as possible!",
 'Peach - Healthy':"You are healthy! Continue doing what you are doing.",
 'Bell Pepper - Bacterial Spot':"You have got the Bacterial spot! Do the Bacterial spot treatment as soon as possible!",
 'Bell Pepper - Healthy':"You are healthy! Continue doing what you are doing.",
 'Potato - Early blight':"You have got the Early blight! Do the Early blight treatment as soon as possible!",
 'Potato - Healthy':"You have got the Late blight! Do the Late blight treatment as soon as possible!",
 'Potato - Late blight':"You are healthy! Continue doing what you are doing.",
 'Rasberry - Healthy':"You are healthy! Continue doing what you are doing.",
 'Soybean - Healthy':"You are healthy! Continue doing what you are doing.",
 'Squash - Powdery Mildew':"You have got the Powdery mildew! Do the Powdery mildew treatment as soon as possible!",
 'Strawberry - Healthy':"You have got the Leaf_scorch! Do the Leaf_scorch treatment as soon as possible!",
 'Tomato - Bacterial spot':"You have got the healthy! Do the healthy treatment as soon as possible!",
 'Tomato - Early blight':"You have got the Bacterial spot! Do the Bacterial spot treatment as soon as possible!",
 'Tomato - Healthy':"You have got the Early blight! Do the Early blight treatment as soon as possible!",
 'Tomato - Late Blight':"You have got the Late blight! Do the Late blight treatment as soon as possible!",
 'Tomato - Leaf Mold':"You have got the Leaf Mold! Do the Leaf Mold treatment as soon as possible!",
 'Tomato - Septoria Leaf spot':"You have got the Leaf spot! Do the Leaf spot treatment as soon as possible!",
 'Tomato - Spider mite':"You have got the Spider mite! Do the Spider mite treatment as soon as possible!",
 'Tomato - Target Spot':"You have got the Target Spot! Do the Target Spot treatment as soon as possible!",
 'Tomato - Yellow Leaf':"You have got the Yellow Leaf! Do the Yellow Leaf treatment as soon as possible!",
 'Tomato - Mosaic virus':"You have got the Mosaic virus! Do the Mosaic virus treatment as soon as possible!",
 }

sys.setrecursionlimit(10000)


healthType = ['Apple - Black Rot',
 'Apple - Cedar Apple Rust',
 'Apple - Healthy',
 'Blueberry - Healthy',
 'Cherry - Healthy',
 'Cherry - Powdery Mildew',
 'Corn - Gray Leaf Spot',
 'Corn - Common Rust',
 'Corn - Healthy',
 'Corn - Northern Leaf Blight',
 'Grape - Black Rot',
 'Grape - Esca',
 'Grape - Healthy',
 'Grape - Leaf Blight',
 'Orange - Haunglongbing',
 'Peach - Bacterial Spot',
 'Peach - Healthy',
 'Bell Pepper - Bacterial Spot',
 'Bell Pepper - Healthy'
 'Potato - Early blight',
 'Potato - Healthy',
 'Potato - Late blight',
 'Rasberry - Healthy',
 'Soybean - Healthy',
 'Squash - Powdery Mildew',
 'Strawberry - Healthy',
 'Strawberry - Leaf scorch',
 'Tomato - Bacterial spot',
 'Tomato - Early blight',
 'Tomato - Healthy'
 'Tomato - Late Blight',
 'Tomato - Leaf Mold',
 'Tomato - Septoria Leaf spot',
 'Tomato - Spider mite',
 'Tomato - Target Spot',
 'Tomato - Yellow Leaf',
 'Tomato - Mosaic virus',
 ]


datapath = "app_pics/"


def main():
    page = st.sidebar.selectbox("App Selections", ["Homepage", "About", "Plant_Health"])
    if page == "Homepage":
        homepage()
    elif page == "About":
        about()
    elif page == "Plant_Health":
        health()




def health():
    st.title("Check the health of your plant")
    set_png_as_page_bg(datapath+'image_1.jpg')
    leaf_model = load_model('model/model.h5')
    st.set_option('deprecation.showfileUploaderEncoding', True)
    st.subheader("Take photo of a leaf with your camera and upload here.")
    uploaded_file = st.file_uploader("Upload an image", type = ['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)
        st.write("")
        name = "temp2.jpg"
        image.save(datapath+name)
        result = model_predict(datapath+name, leaf_model)
        pred = healthType[result]
        st.header("Your leaf is - "+ pred )
        st.subheader("The suggested recovery plan for "+ pred + " is: "+ suggestions[pred])



def homepage():
    html_temp = """
    <html>
    <head>
    <style>
    body {
      background-color: #fe2631;
    }
    </style>
    </head>
    <body>
    </body>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    image = Image.open(datapath +'image_1.jpg')
    st.image(image, use_column_width = True)


def about():
    set_png_as_page_bg(datapath+'temp1.jpg')
    st.title("Leaf Life")
    st.header("“How is your plant doing?“")
    st.header("Jesse Villines")
    st.subheader("Your leaf, is it healthy or what?!")
    st.subheader("Soon you will know.")
    st.subheader("Version 1.0")

#@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: 2200px;
    background-repeat: no-repeat;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def model_predict(image_path,model):
    image = load_img(image_path,target_size=(250,250))
    image = img_to_array(image)
    image = image/255
    image = np.expand_dims(image,axis=0)
    result = np.argmax(model.predict(image))
    return result

if __name__ == '__main__':
    main()
