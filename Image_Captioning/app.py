"""Image Captioning App using BLIP model and Streamlit.
Run: streamlit run app.py
"""
import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

st.set_page_config(page_title='Image Captioning AI', page_icon='🖼️')
st.title('Image Captioning AI')
st.write('Upload an image and the AI model will generate a caption.')

@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-base')
    model = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')
    return processor, model

processor, model = load_model()

uploaded_file = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_container_width=True)

    if st.button('Generate Caption'):
        with st.spinner('Generating caption...'):
            inputs = processor(image, return_tensors='pt')
            output = model.generate(**inputs, max_new_tokens=30)
            caption = processor.decode(output[0], skip_special_tokens=True)
        st.success('Caption Generated')
        st.subheader('Generated Caption:')
        st.write(caption)
