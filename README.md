# Fast-API

## Task Overview: Deploying a FastAPI Application for Financial Data Analysis

### Objective

Develop and deploy a FastAPI application that utilizes a machine learning model to predict the authenticity of banknotes based on features extracted from images. This involves:

1. **Data Extraction**: Preparing the data by extracting relevant features from banknote images.
2. **Model Training**: Building a machine learning model to classify banknotes.
3. **API Development**: Creating an API to serve predictions.

### Context

#### Data Extraction

- **Source**: The images are taken from genuine and forged banknote-like specimens.
- **Resolution and Format**: The final images are 400x400 pixels with a resolution of 660 dpi, usually in grayscale.
- **Feature Extraction**: Wavelet Transform tools are used to derive statistical features such as variance, skewness, curtosis, and entropy from these images.

#### Model Training

- **Goal**: Use the extracted features to train a machine learning model that can distinguish between genuine and forged banknotes.
- **Data Format**: Typically, the data is stored in a CSV file where each row represents a banknote and each column represents a feature (e.g., variance_wavelet, skewness_wavelet).
- **Model**: Various models can be employed, but a Random Forest classifier is commonly used due to its robustness and accuracy.

#### API Development

- **Purpose**: The FastAPI application provides a RESTful interface for making predictions based on input features.
- **Endpoints**:
  - **Root Endpoint (`/`)**: A simple welcome message to verify the API is running.
  - **Prediction Endpoint (`/predict`)**: Accepts feature inputs and returns a prediction on whether a banknote is genuine or forged.

### Steps to Implement

#### 1. Data Preparation

1. **Collect Images**: Gather images of both genuine and forged banknotes.
2. **Extract Features**: Apply wavelet transform and other image processing techniques to extract statistical features.
3. **Store Data**: Save the extracted features in a structured format, typically CSV.

**Example Feature Extraction:**
```text
variance_wavelet, skewness_wavelet, curtosis_wavelet, entropy_image, label
2.643, 5.085, -2.189, -0.123, 0
4.525, 8.167, -3.876, 0.014, 1
```

#### 2. Model Training

1. **Load Data**: Read the prepared data file.
2. **Train Model**: Use a machine learning algorithm to train a model on the features.
3. **Save Model**: Serialize the trained model using a tool like `pickle`.

**Example Training Script (`train_model.py`):**
```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model(data_path='data/banknote_features.csv'):
    df = pd.read_csv(data_path)
    X = df.drop(columns=['label'])
    y = df['label']
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Model trained and saved as model.pkl")
```

#### 3. API Development

1. **Setup FastAPI**: Install FastAPI and Uvicorn.
2. **Load Model**: Load the trained model within the FastAPI app.
3. **Create Endpoints**: Define the root and prediction endpoints.

**Example FastAPI Script (`main.py`):**
```python
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

app = FastAPI()

# Load the model
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the request body schema
class BanknoteFeatures(BaseModel):
    variance_wavelet: float
    skewness_wavelet: float
    curtosis_wavelet: float
    entropy_image: float

@app.get('/')
def read_root():
    return {'message': 'Welcome to the Banknote Authentication API'}

@app.post('/predict')
def predict(features: BanknoteFeatures):
    data = pd.DataFrame([features.dict()])
    prediction = model.predict(data)
    result = 'Genuine' if prediction[0] == 0 else 'Forged'
    return {'prediction': result}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)
```

### Project Structure

Organize the project into a directory structure for clarity and manageability:

```
/banknote-authentication
│
├── data
│   └── banknote_features.csv
│
├── models
│   └── model.pkl
│
├── scripts
│   └── train_model.py
│
├── main.py
├── README.md
└── requirements.txt
```

### Example GitHub Repository

- **Repository Name**: `banknote-authentication`
- **Primary Branch**: `main`
- **URL**: `https://github.com/username/banknote-authentication`

### Steps to Deploy on GitHub

1. **Initialize Repository**: Create a new GitHub repository named `banknote-authentication`.
2. **Clone Repository**: Clone the repository to your local machine.
3. **Add Files**: Add your project files (`data`, `models`, `scripts`, `main.py`, `README.md`, `requirements.txt`).
4. **Commit and Push**: Commit your changes and push them to the GitHub repository.
5. **Documentation**: Ensure the `README.md` contains detailed instructions on setting up and running the application.

**README.md Example:**
```markdown
# Banknote Authentication API

This project uses FastAPI to create a machine learning API for authenticating banknotes based on extracted image features.

## Features

- **Model Training**: Uses Random Forest to classify banknotes.
- **API Endpoints**:
  - `/`: Welcome message.
  - `/predict`: Predicts the authenticity of a banknote.

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model:
   ```bash
   python scripts/train_model.py
   ```
4. Run the API:
   ```bash
   python main.py
   
## Usage

- Access the API at `http://localhost:8000`.
- Use `/predict` to submit banknote features and receive predictions.
  
### Benefits of FastAPI for This Task

- **Performance**: FastAPI is designed for high performance and is built on standard Python type hints, making it fast and intuitive.
- **Ease of Use**: Provides automatic generation of interactive API documentation (using Swagger and Redoc).
- **Scalability**: Supports asynchronous programming, making it scalable and suitable for handling numerous concurrent requests.
