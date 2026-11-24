import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

st.set_page_config(page_title="Traffic Sign Classifier", page_icon="🚦", layout="centered")

CLASS_NAMES = [
    "Green Light",
    "Red Light",
    "Speed Limit 10",
    "Speed Limit 100",
    "Speed Limit 110",
    "Speed Limit 120",
    "Speed Limit 20",
    "Speed Limit 30",
    "Speed Limit 40",
    "Speed Limit 50",
    "Speed Limit 60",
    "Speed Limit 70",
    "Speed Limit 80",
    "Speed Limit 90",
    "Stop",
]
IMG_SIZE = (128, 128)

@st.cache_resource
def load_model():
    # This app uses the CNN model trained in the supplied notebook.
    return tf.keras.models.load_model("best_traffic_sign_cnn.keras", compile=False)

def prepare_image(image):
    image = image.convert("RGB")
    resized = image.resize(IMG_SIZE)
    array = np.asarray(resized, dtype=np.float32) / 255.0
    return np.expand_dims(array, axis=0)

st.title("🚦 Traffic Sign Recognition")
st.write(
    "Upload a traffic-sign crop or capture one with your camera. "
    "The CNN predicts one of the 15 classes used during training."
)
st.warning(
    "Important: this model is a **classifier**, not an object detector. "
    "It expects an image containing one traffic sign, preferably cropped closely "
    "around the sign. It does not locate signs in a full road-scene image."
)

source = st.radio("Choose input method", ["Upload an image", "Use camera"], horizontal=True)
uploaded = None
if source == "Upload an image":
    uploaded = st.file_uploader("Choose a traffic-sign image", type=["jpg", "jpeg", "png"])
else:
    uploaded = st.camera_input("Capture a traffic-sign image")

if uploaded is not None:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Input image", use_container_width=True)

    if st.button("Predict traffic sign", type="primary"):
        try:
            model = load_model()
            batch = prepare_image(image)
            probabilities = model.predict(batch, verbose=0)[0]
            predicted_id = int(np.argmax(probabilities))
            confidence = float(probabilities[predicted_id])

            st.subheader(f"Prediction: {CLASS_NAMES[predicted_id]}")
            st.metric("Model confidence", f"{confidence * 100:.2f}%")

            top_ids = np.argsort(probabilities)[::-1][:3]
            st.write("Top 3 predictions")
            for idx in top_ids:
                st.write(f"**{CLASS_NAMES[int(idx)]}** — {probabilities[idx] * 100:.2f}%")
                st.progress(float(probabilities[idx]))

            if confidence < 0.60:
                st.info("Confidence is relatively low. Try a clearer, closer, well-lit image.")
        except Exception as exc:
            st.error(f"Prediction failed: {exc}")
            st.caption("Check that best_traffic_sign_cnn.keras is in the same folder as app.py.")
