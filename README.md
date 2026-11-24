# Traffic Sign Recognition using CNN

## Project Overview
This project uses a Convolutional Neural Network (CNN) to recognize and classify traffic signs from input images.

## Technologies Used
- Python
- TensorFlow / Keras
- CNN (Convolutional Neural Network)
- Streamlit
- NumPy
- Pillow

## Features
- Live image upload through Streamlit
- Traffic sign image preprocessing
- CNN-based image classification
- Prediction with confidence score
- Interactive web interface

## Project Structure
```text
traffic-sign-streamlit-app/
│
├── app.py
├── best_traffic_sign_cnn.keras
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/yoge3159/Traffic-Sign-Recognition-CNN.git
```

Navigate into the project:

```bash
cd Traffic-Sign-Recognition-CNN
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

## Model
The trained CNN model is saved in Keras format and is used to predict traffic sign classes from uploaded images.

## Author
Yogeeswar Reddy

## GitHub
https://github.com/yoge3159/Traffic-Sign-Recognition-CNN
