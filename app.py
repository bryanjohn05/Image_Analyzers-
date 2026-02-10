import streamlit as st
import tempfile
import os
import requests
from PIL import Image

from vision_client import analyze_image
from decision_engine import interpret_results, extract_description
from draw_boxes import draw_bounding_boxes
from config import AZURE_ENDPOINT, AZURE_KEY


# --------------------------------------------------
# Streamlit Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Image Analyser App",
    layout="wide"
)

st.title("🧠 Image Analyser App")
st.caption("Azure Vision API • Probabilistic AI • Uncertainty Aware")

st.divider()

# --------------------------------------------------
# Image Input Mode
# --------------------------------------------------
st.subheader("📥 Image Input")

input_mode = st.radio(
    "Choose image source:",
    ["Upload Image", "Image URL"]
)

image_input = None
local_image_path = None

# --------------------------------------------------
# Upload Image Mode
# --------------------------------------------------
if input_mode == "Upload Image":
    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
            temp.write(uploaded_file.read())
            local_image_path = temp.name
            image_input = local_image_path

# --------------------------------------------------
# Image URL Mode
# --------------------------------------------------
elif input_mode == "Image URL":
    image_url = st.text_input(
        "Enter image URL",
        placeholder="https://example.com/image.jpg"
    )

    if image_url:
        image_input = image_url

# --------------------------------------------------
# Run Analysis
# --------------------------------------------------
if image_input:
    st.info("🔍 Analyzing image with Azure Vision API...")

    try:
        vision_result = analyze_image(
            image_input,
            AZURE_ENDPOINT,
            AZURE_KEY
        )
    except Exception as e:
        st.error(f"❌ Error analyzing image: {e}")
        st.stop()

    # --------------------------------------------------
    # Layout
    # --------------------------------------------------
    col1, col2 = st.columns(2)

    # --------------------------------------------------
    # Original Image
    # --------------------------------------------------
    with col1:
        st.subheader("📷 Original Image")

        if input_mode == "Upload Image":
            st.image(Image.open(local_image_path), use_container_width=True)
        else:
            st.image(image_input, use_container_width=True)

    # --------------------------------------------------
    # Bounding Boxes (only for local images)
    # --------------------------------------------------
    with col2:
        st.subheader("📦 Detected Objects")

        if input_mode == "Upload Image":
            output_image = draw_bounding_boxes(
                local_image_path,
                vision_result,
                output_path="output_streamlit.jpg"
            )
            st.image(Image.open(output_image), use_container_width=True)
        else:
            st.warning(
                "Bounding box visualization requires downloading the image.\n\n"
                "Object detection results are shown below."
            )

    st.divider()

    # --------------------------------------------------
    # Image Description
    # --------------------------------------------------
    description, desc_confidence = extract_description(vision_result)

    st.subheader("📝 Image Description")
    st.markdown(f"**{description}**")
    st.progress(min(desc_confidence, 1.0))
    st.caption(f"Confidence: {desc_confidence:.2f}")

    st.divider()

    # --------------------------------------------------
    # Probabilistic Insights
    # --------------------------------------------------
    st.subheader("📊 Probabilistic Insights")

    insights = interpret_results(vision_result)

    for item in insights:
        label = (
            f"{item['type'].upper()} • {item['value']} "
            f"({item['confidence']:.2f})"
        )

        if item["confidence"] >= 0.75:
            st.success(label + " — High confidence")
        elif item["confidence"] >= 0.5:
            st.warning(label + " — Medium confidence")
        else:
            st.error(label + " — Low confidence / Uncertain")

    st.divider()

    st.caption("⚠️ AI outputs are probabilistic and may be incorrect.")
