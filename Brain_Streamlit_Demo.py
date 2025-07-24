import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Define class names (update order as per your labels during training)
CLASS_NAMES = ['Glioma', 'Meningioma', 'Pituitary', 'No Tumor']

# Load your trained model
model = load_model("Brain_Tumor_MRI_Image_Classification.h5")

st.title("Brain Tumor MRI: Tumor Type Prediction")

uploaded_file = st.file_uploader("Upload an MRI image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded MRI Image", width=300)
    img = img.convert("RGB")
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    if st.button("Get Tumor Prediction"):
        prediction = model.predict(img_array)
        st.write("Prediction output:", prediction)

        pred_class_index = int(np.argmax(prediction, axis=1)[0])
        pred_tumor_name = CLASS_NAMES[pred_class_index]
        st.markdown(f"## Tumor name: **{pred_tumor_name}**")

confidence = float(np.max(prediction))
st.markdown(f"## Tumor name: **{pred_tumor_name}** (Confidence: {confidence:.2%})")
