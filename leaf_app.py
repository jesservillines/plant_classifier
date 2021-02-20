import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from PIL import Image
import base64
import sys
import io

#classes = {0:"Scab",1:"Rot",2:"Rust",3:"Healthy"}

suggestions = {
'Scab':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Rot':"You have got the Rot! Do the Rot treatment as soon as possible!",
 'Rust':"You have got the Rust! Do the Rust treatment as soon as possible!" ,
 'Healthy':"You are healthy! Continue doing what you are doing.",
 'Healthy':"You are healthy! Continue doing what you are doing.",
 'Powdery mildew':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Healthy':"You are healthy! Continue doing what you are doing.",
 'Leaf spot':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Common_rust':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Northern Leaf Blight':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Healthy':"You are healthy! Continue doing what you are doing.",
 'Black rot':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Black Measles':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Leaf blight':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Healthy':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Citrus greening':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Bacterial spot':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Healthy':"You are healthy! Continue doing what you are doing.",
 'Bacterial spot':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Healthy':"You are healthy! Continue doing what you are doing.",
 'Early blight':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Late blight':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Healthy':"You are healthy! Continue doing what you are doing.",
 'Healthy':"You are healthy! Continue doing what you are doing.",
 'Healthy':"You are healthy! Continue doing what you are doing.",
 'Powdery mildew':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Leaf_scorch':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'healthy':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Bacterial spot':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Early blight':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Late blight':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Leaf Mold':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Leaf spot':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Spider mite':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Target Spot':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Yellow Leaf':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Mosaic virus':"You have got the Scab! Do the Scab treatment as soon as possible!",
 'Healthy':"You are healthy! Continue doing what you are doing."}

sys.setrecursionlimit(10000)


healthType = ['Scab',
 'Rot',
 'Rust',
 'Healthy',
 'Healthy',
 'Powdery mildew',
 'Healthy',
 'Leaf spot',
 'Common_rust',
 'Northern Leaf Blight',
 'Healthy',
 'Black rot',
 'Black Measles',
 'Leaf blight',
 'Healthy',
 'Citrus greening',
 'Bacterial spot',
 'Healthy',
 'Bacterial spot',
 'Healthy',
 'Early blight',
 'Late blight',
 'Healthy',
 'Healthy',
 'Healthy',
 'Powdery mildew',
 'Leaf_scorch',
 'healthy',
 'Bacterial spot',
 'Early blight',
 'Late blight',
 'Leaf Mold',
 'Leaf spot',
 'Spider mite',
 'Target Spot',
 'Yellow Leaf',
 'Mosaic virus',
 'Healthy']


datapath = "app_pics/"


def main():

    page = st.sidebar.selectbox("App Selections", ["Homepage", "About", "Plant_Health"])
    if page == "Identify":
        st.title("Soil Identifier")
        identify()
    elif page == "Homepage":
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
    uploaded_file = st.file_uploader("Upload an image", type = "jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)


        st.image(image, use_column_width=True)
        st.write("")
        name = "temp1.jpg"

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
    image = Image.open(datapath+'image_1.jpg')
    st.image(image, use_column_width = True)


def about():
    set_png_as_page_bg(datapath+'image_1.jpg')
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

    image = load_img(image_path,target_size=(224,224))
    image = img_to_array(image)
    image = image/255
    image = np.expand_dims(image,axis=0)

    result = np.argmax(model.predict(image))
    return result


if __name__ == '__main__':
    main()
