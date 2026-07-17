# Pneumonia Classifier
## <a name="introduction">Introduction</a>

Pneumonia Classifier is a **Flask-based web application** that predicts the presence of pneumonia from chest X-ray images. Built with **Python,** **TensorFlow and Streamlit**, it provides a minimalistic interface for uploading images and viewing predictions instantly.

The model was trained using public dataset [Chest X-Ray Images for Classification](https://data.mendeley.com/datasets/rscbjbr9sj/2)

## <a name="features">Features</a>
👉 Upload chest X-rays, it accepts .jpg, .png files for analysis.

👉 Uses a pre-trained Keras model to classify pneumonia with confidence scores.

👉 Displays uploaded image and prediction results directly on the page.

👉 Clean, responsive interface built with Tailwind CSS for simplicity and ease of use.

👉 Users can try the app using validation images in the img/ folder.

-------

## <a name="run_it">How to Run the App</a>

```bash
1. Clone the repository

git clone https://github.com/your-username/pneumonia-classifier.git
cd pneumonia-classifier

2. Create a virtual environment

python -m venv venv

3. Install dependencies

pip install -r requirements.txt

4. Run the Flask app

python app.py
