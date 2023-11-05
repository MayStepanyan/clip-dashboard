import streamlit as st
from PIL import Image

from dashboard.handlers import CLIP

handler = CLIP()


def main(
    title: str = "Image Classification with CLIP"
):
    """The main loop"""
    st.title(title)

    # Upload one or many images
    uploaded_file = st.file_uploader(
        "Upload a file images",
        type=["jpg", "png", "jpeg"],
        accept_multiple_files=False)
    classes = st.text_area("Possible classes. Each class in new line")
    button = st.button("SUBMIT")
    if uploaded_file and button and classes:
        # Display uploaded image
        classes = classes.split('\n')
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        # Perform image classification
        result = handler.classify(image=img, classes=classes)

        st.json(result)


main()
