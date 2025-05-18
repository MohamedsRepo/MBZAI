Dementia Risk Prediction App

Overview

Welcome to the Dementia Risk Prediction App! This friendly tool uses a trained machine learning model to give you a quick estimate of someone’s likelihood of dementia based on factors like age, years of education, and cognitive test scores. 

What’s Included

Data Preparation: Clean and process your dementia dataset

Model Training: Script to train or fine-tune the model on your data

Pretrained Model: Ready-to-use artifact at model/dementia_model.pkl

Web Interface: Interactive Streamlit app for making predictions in real time

Simple run using a RunApp.bat file

Quick Start

Clone the repository

git clone https://github.com/your-username/dementia-risk-prediction-app.git
cd dementia-risk-prediction-app

Set up a virtual environment

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate

Install dependencies

pip install --upgrade pip
pip install -r requirements.txt

Project Structure

dementia-risk-prediction-app/
├── app/                         # Streamlit prediction interface
│   └── the dementia app.py
├── data/                        # Example dataset for training/testing
│   └── dementia_data.csv
├── model/                       # Saved machine learning model
│   └── dementia_model.pkl
├── Trainer/                     # Training scripts
│   └── train_model.py
├── .gitignore                   # Untracked files and folders
├── requirements.txt             # Python dependencies
└── README.md                    # This documentation

Usage

Train the Model

Run the training script with your data:

python Trainer/train_model.py --data data/dementia_data.csv --output model/dementia_model.pkl

Customize hyperparameters by passing additional flags (see the script’s docstring).

Run the App

Note: The app requires a trained model file at model/dementia_model.pkl. If you haven't generated it yet, first run the training script (see Train the Model) and place the resulting dementia_model.pkl into the model/ directory.

Launch the Streamlit interface:

streamlit run "app/the dementia app.py"

Open your browser to http://localhost:8501 to start making predictions.

Contributing

Contributions and feedback are welcome! Please open an issue or submit a pull request.

License

This project is released under the MIT License. See LICENSE for details.

Contact

Got questions or suggestions? Email me at malshkeili01@gmail.com.

