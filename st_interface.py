import PIL

import sahi
import streamlit as st
from sahi import AutoDetectionModel
from sahi.predict import get_prediction, get_sliced_prediction, predict



detection_model = AutoDetectionModel.from_pretrained(
    model_type='yolov5',
    model_path='./last_st.pt',
    confidence_threshold=0.3,
    device="cpu",)


def define_doc_state(doc):

    with open(doc.name,"wb") as f:
         f.write(doc.getbuffer())

    result = get_sliced_prediction(
        doc.name,
        detection_model,
        slice_height=250,
        slice_width=250,
        postprocess_match_threshold=0.45,
        overlap_height_ratio=0.6,
        overlap_width_ratio=0.6
    )
    result.export_visuals(export_dir='./')





uploaded_file = st.file_uploader("Выберите файл", type=[".JPG", ".jpg", ".png",], accept_multiple_files=False)
if uploaded_file:
    st.success("Файл успешно загружен", icon="✅")
    define_button_state = st.button("Определить")
    if define_button_state:
         define_doc_state(uploaded_file)
         res_image = PIL.Image.open('./prediction_visual.png')
         st.image(res_image, caption='Detection')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
