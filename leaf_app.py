#import packages. These also need to be in the requirements.txt
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array, array_to_img
import numpy as np
from PIL import Image
import base64
import sys
import io

#to allow for larger size photos from phone
sys.setrecursionlimit(10000)

#set datapath for call later
datapath = "app_pics/"

#This allows for multiple pages
def main():
    page = st.sidebar.selectbox("App Selections", ["Homepage", "About"])
    if page == "Homepage":
        health()
    elif page == "About":
        about()

#this is the upload/prediction page
def health():
    st.title("Your plant, is it healthy or what?!")
    st.subheader("Soon you will know.")
    set_background_image(datapath+'image_1.jpg') # set background image for page
    leaf_classifier = load_model('model/model0.h5') #upload repository model
    st.set_option('deprecation.showfileUploaderEncoding', True)
    st.subheader("Take photo of a leaf with your camera and upload here.")
    upload_photo = st.file_uploader("Upload an image", type = ['jpg', 'png', 'jpeg']) #can adjust to include different image types
    if upload_photo is not None:
        image = Image.open(upload_photo)
        st.image(image, use_column_width=True)
        st.write("")
        name = "temp2.jpg"
        image.save(datapath+name)
        result = model_predict(datapath+name, leaf_classifier)
        pred = type[result]
        #st.header("Your leaf is - " + str(result)) #for error checking the lists
        st.header("Your leaf is - " + pred )
        st.subheader("The suggested recovery plan for "+ pred + " is: "+ suggestion[pred])

#run the model predictions
def model_predict(image_path,model):
    image = load_img(image_path,target_size=(248,248))
    image = img_to_array(image)
    image = image/255
    image = np.expand_dims(image,axis=0)
    result = np.argmax(model.predict(image))
    return result

#the about page
def about():
    html_template = """
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
    set_background_image(datapath+'image_1.jpg')
    st.title("Leaf Life")
    st.header("Supported Plants: Apple, blueberry, cherry, corn, grape, orange, peach, bell pepper, potato, raspberry, soybean, squash, strawberry, tomato, with more coming soon!")
    st.subheader("Author's Linkedin: https://www.linkedin.com/in/jesse-villines/")
    st.subheader("Author's Github: https://github.com/jesservillines")
    st.subheader("Version 1.0")

def base64_background(background_file):
    with open(background_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background_image(jpg_image):
    bin_str = base64_background(jpg_image)
    background_image_style = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: 2200px;
    background-repeat: no-repeat;
    }
    </style>
    ''' % bin_str
    st.markdown(background_image_style, unsafe_allow_html=True)

#suggestions are based on the type of disease. Future development will expand this section to include
#real suggestions
suggestion = {
'Plant - Healthy':"Congratulations; healthy leaf, healthy life. Continue doing what you are doing.",
'Apple - Black Rot':"You have got the Black Rot! Do the Black Rot treatment as soon as possible!",
 'Apple - Cedar Apple Rust':"You have got the Cedar Apple Rust! Do the Cedar Apple Rust treatment as soon as possible!",
 'Apple - Healthy':"Congratulations; healthy leaf, healthy life. Continue doing what you are doing.",
 'Blueberry - Healthy':"Congratulations; healthy leaf, healthy life. Continue doing what you are doing.",
 'Cherry - Powdery Mildew':"You have got the Powdery mildew! Do the Powdery mildew treatment as soon as possible!",
 'Cherry - Healthy':"Congratulations; healthy leaf, healthy life. Continue doing what you are doing.",
 'Corn - Gray Leaf Spot':"You have got the Gray Leaf Spot! Do the Gray Leaf Spot treatment as soon as possible!",
 'Corn - Common Rust':"You have got the Common Rust! Do the Common Rust treatment as soon as possible!",
 'Corn - Northern Leaf Blight':"You have got the Northern Leaf Blight! Do the Northern Leaf Blight treatment as soon as possible!",
 'Corn - Healthy':"Congratulations; healthy leaf, healthy life. Continue doing what you are doing.",
 'Grape - Black Rot':"You have got the Black Rot! Do the Black Rot treatment as soon as possible!",
 'Grape - Esca':"You have got the Esca! Do the Esca treatment as soon as possible!",
 'Grape - Leaf Blight':"You have got the Leaf blight! Do the Leaf blight treatment as soon as possible!",
 'Grape - Healthy':"Congratulations; healthy leaf, healthy life. Continue doing what you are doing.",
 'Orange - Haunglongbin':"You have got the Haunglongbin! Do the Haunglongbin treatment as soon as possible!",
 'Peach - Bacterial Spot':"You have got the Bacterial spot! Do the Bacterial spot treatment as soon as possible!",
 'Peach - Healthy':"Congratulations; healthy leaf, healthy life. Continue doing what you are doing.",
 'Bell Pepper - Bacterial Spot':"You have got the Bacterial spot! Do the Bacterial spot treatment as soon as possible!",
 'Bell Pepper - Healthy':"You are healthy! Continue doing what you are doing.",
 'Potato - Early blight':"You have got the Early blight! Do the Early blight treatment as soon as possible!",
 'Potato - Late blight':"You have got the Late blight! Do the Late blight treatment as soon as possible!",
 'Potato - Healthy':"Congratulations; healthy leaf, healthy life. Continue doing what you are doing.",
 'Rasberry - Healthy':"Congratulations; healthy leaf, healthy life. Continue doing what you are doing.",
 'Soybean - Healthy':"Congratulations; healthy leaf, healthy life. Continue doing what you are doing.",
 'Squash - Powdery Mildew':"You have got the Powdery mildew! Do the Powdery mildew treatment as soon as possible!",
 'Strawberry - Leaf scorch':"You have got the Leaf scorch! Do the Leaf scorch treatment as soon as possible!",
 'Strawberry - Healthy':"Congratulations; healthy leaf, healthy life. Continue doing what you are doing.",
 'Tomato - Bacterial spot':"You have got the Bacterial spot! Do the Bacterial spot treatment as soon as possible!",
 'Tomato - Early blight':"You have got the Early blight! Do the Early blight treatment as soon as possible!",
 'Tomato - Late Blight':"You have got the Late blight! Do the Late blight treatment as soon as possible!",
 'Tomato - Leaf Mold':"You have got the Leaf Mold! Do the Leaf Mold treatment as soon as possible!",
 'Tomato - Septoria Leaf spot':"You have got the Septoria Leaf spot! Do the Septoria Leaf spot treatment as soon as possible!",
 'Tomato - Spider mite':"You have got the Spider mite! Do the Spider mite treatment as soon as possible!",
 'Tomato - Target Spot':"You have got the Target Spot! Do the Target Spot treatment as soon as possible!",
 'Tomato - Yellow Leaf':"You have got the Yellow Leaf! Do the Yellow Leaf treatment as soon as possible!",
 'Tomato - Mosaic virus':"You have got the Mosaic virus! Do the Mosaic virus treatment as soon as possible!",
 'Tomato - Healthy':"Congratulations; healthy leaf, healthy life. Continue doing what you are doing.",
 }

# this is the type of disease, this section will be expanded in the future to allow for additional
#leaf types
type = ['Plant - Healthy',
'Apple - Black Rot',
 'Apple - Cedar Apple Rust',
 'Apple - Healthy',
 'Blueberry - Healthy',
 'Cherry - Healthy',
 'Cherry - Powdery Mildew',
 'Corn - Gray Leaf Spot',
 'Corn - Common Rust',
 'Corn - Northern Leaf Blight',
  'Corn - Healthy',
 'Grape - Black Rot',
 'Grape - Esca',
 'Grape - Leaf Blight',
  'Grape - Healthy',
 'Orange - Haunglongbing',
 'Peach - Bacterial Spot',
 'Peach - Healthy',
 'Bell Pepper - Bacterial Spot',
 'Bell Pepper - Healthy'
 'Potato - Early blight',
 'Potato - Late blight',
  'Potato - Healthy',
 'Rasberry - Healthy',
 'Soybean - Healthy',
 'Squash - Powdery Mildew',
 'Strawberry - Healthy',
 'Strawberry - Leaf scorch',
 'Tomato - Bacterial spot',
 'Tomato - Early blight',
 'Tomato - Late Blight',
 'Tomato - Leaf Mold',
 'Tomato - Septoria Leaf spot',
 'Tomato - Spider mite',
 'Tomato - Target Spot',
 'Tomato - Yellow Leaf',
 'Tomato - Mosaic virus',
 'Tomato - Healthy',
 'Healthy'
 ]

if __name__ == '__main__':
    main()
