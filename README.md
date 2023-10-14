# Potato-Disease-classification-predication-using-cnn-and-tensorflow-
## Potato Disease Prediction Web Application

![Screenshot (484)](https://github.com/AbhishekSingh010/Potato-Disease-classification-predication-using-cnn-and-tensorflow-/assets/113212983/52b46701-46a4-4762-8fad-42943e09ace9)


This web application is designed to predict potato diseases using a Convolutional Neural Network (CNN) implemented with TensorFlow. It provides a user-friendly interface to input potato leaf images and receive predictions regarding the health of the potatoes.
- In this projects model are trained on kaggle plantvillage dataset.
## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technology Stack](#technology-stack)
- [Contributing](#contributing)
- [License](#license)

## Features

- Predicts potato diseases with a high degree of accuracy almost 99%.
- Provides a simple and intuitive web interface for users to upload potato images.
- FastAPI backend for efficient image processing and prediction.
- Frontend built with HTML, CSS, and JavaScript.
- Well-structured codebase for easy customization and further development.


## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/AbhishekSingh010/potato-disease-prediction.git
Navigate to the project directory:

bash
Copy code
cd potato-disease-prediction
Install the required Python packages by creating a virtual environment and using pip:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
pip install -r requirements.txt
Usage
Start the FastAPI server:

#### bash
Copy code
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Access the web application by opening a web browser and navigating to http://localhost:8000.

- just simply running main.py file
    python main.py



![Screenshot (483)](https://github.com/AbhishekSingh010/Potato-Disease-classification-predication-using-cnn-and-tensorflow-/assets/113212983/f14428b5-725e-44c8-8f36-09ed50a072ba)

Technology Stack
Backend: FastAPI
Frontend: HTML, CSS, JavaScript
Machine Learning Framework: TensorFlow
Predictive Model: Convolutional Neural Network (CNN)

Contributing
If you would like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push to your fork and submit a pull request to the main branch of this repository.
License
This project is licensed under the MIT License - see the LICENSE file for details.
