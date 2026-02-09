import streamlit as st
import tempfile
from PIL import Image

from vision_client import analyze_image
from decision_engine import interpret_results, extract_description
from draw_boxes import draw_bounding_boxes
from config import AZURE_ENDPOINT, AZURE_KEY


st.set_page_config(
    page_title="Image Analyser App",
    layout="wide"
)

st.title("🧠 Image Analyser App")
st.caption("Azure Vision API • Probabilistic AI • Uncertainty Aware")

uploaded_file = st.file_uploader(
    "📤 Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    # Save uploaded image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.read())
        image_path = temp_file.name

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📷 Original Image")
        st.image(Image.open(image_path), use_container_width=True)

    st.info("🔍 Analyzing image with Azure Vision API...")

    vision_result = analyze_image(
        image_path,
        AZURE_ENDPOINT,
        AZURE_KEY
    )

    description, desc_confidence = extract_description(vision_result)

    output_image = draw_bounding_boxes(
        image_path,
        vision_result,
        output_path="output_streamlit.jpg"
    )

    with col2:
        st.subheader("📦 Detected Objects")
        st.image(Image.open(output_image), use_container_width=True)

    st.divider()

    st.subheader("📝 Image Description")
    st.markdown(f"**{description}**")
    st.progress(min(desc_confidence, 1.0))
    st.caption(f"Confidence: {desc_confidence:.2f}")

    st.divider()

    st.subheader("📊 Probabilistic Insights")

    insights = interpret_results(vision_result)

    for item in insights:
        if item["confidence"] >= 0.75:
            st.success(
                f"{item['type'].upper()} • {item['value']} "
                f"({item['confidence']:.2f}) — High confidence"
            )
        elif item["confidence"] >= 0.5:
            st.warning(
                f"{item['type'].upper()} • {item['value']} "
                f"({item['confidence']:.2f}) — Medium confidence"
            )
        else:
            st.error(
                f"{item['type'].upper()} • {item['value']} "
                f"({item['confidence']:.2f}) — Low confidence / Uncertain"
            )

    st.divider()
    st.caption("⚠️ AI outputs are probabilistic and may be incorrect.")
