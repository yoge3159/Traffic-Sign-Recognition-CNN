# Traffic Sign Recognition with CNN + Streamlit

A Streamlit demo for the 15-class CNN classifier trained in `traffic_sign_cnn_project`.

## What it does
- Accepts a traffic-sign image through file upload or camera capture.
- Resizes the image to 128 × 128 RGB.
- Converts pixel values to the 0–1 range, matching the notebook preprocessing.
- Displays the predicted class, confidence, and top-three classes.

## Important model limitation
The notebook trains the CNN using **cropped traffic-sign regions extracted from YOLO annotations**. The saved CNN is a classifier; it does not detect or draw bounding boxes around signs in a full road image. For this demo, provide one sign per image, cropped closely around the sign. To classify signs automatically in full road footage, add an object-detection model first and pass each detected crop to this CNN.

## Project files
- `app.py` — Streamlit user interface and inference pipeline
- `best_traffic_sign_cnn.keras` — trained model
- `requirements.txt` — Python dependencies

## Run locally (Windows PowerShell)

Use Python 3.10 or 3.11.

```powershell
# 1. Create and open the project folder
cd path\to\traffic-sign-streamlit-app

# 2. Create a virtual environment
py -3.11 -m venv .venv

# 3. Activate it
.\.venv\Scripts\Activate.ps1

# If PowerShell blocks activation, run this once in the current terminal:
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# Then activate again.

# 4. Upgrade pip and install packages
python -m pip install --upgrade pip
pip install -r requirements.txt

# 5. Start the app
streamlit run app.py
```

Your browser should open the local Streamlit app. Stop it with `Ctrl+C`.

## Push to GitHub

Create an empty repository on GitHub (do not add a README if you already have this one), then run:

```powershell
git init
git add app.py requirements.txt README.md .gitignore best_traffic_sign_cnn.keras
git commit -m "Add Streamlit traffic sign classifier"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the remote URL with your own GitHub repository URL. Do not upload private data, credentials, or the original training dataset unless you have permission.

## Deploy on Streamlit Community Cloud

1. Push the project to GitHub.
2. Sign in to Streamlit Community Cloud with GitHub.
3. Select **Create app** and choose this repository, branch `main`, and file `app.py`.
4. Deploy. Streamlit Cloud installs dependencies from `requirements.txt`.
5. Test both upload and camera input in the deployed app.

If deployment fails because of memory or TensorFlow compatibility, inspect the build logs and adjust the Python/runtime and dependency versions together. Keep the `.keras` model file in the repository root for this starter setup.
