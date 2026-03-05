# Labmentix Internship Projects

## Overview

This repository contains multiple machine learning projects developed during the Labmentix internship program. The projects focus on solving real-world problems using data analysis, predictive modeling, and deep learning techniques.

---

# Projects Included

## 1. Glassdoor Salary Prediction

### Overview

This project focuses on predicting the **average salary of employees based on company and job-related attributes** using machine learning techniques.

The dataset contains information about companies and job roles similar to those available on platforms like Glassdoor. The trained model estimates salary ranges based on company characteristics and job-related attributes.

### Dataset Features

The dataset includes features such as:

- Job Role / Job Title
- Company Size
- Company Founding Year
- Industry / Sector
- Company Age
- Other company-related attributes

### Objective

The goal of this project is to build a machine learning model that can **predict the average salary of an employee** based on information about the job role and company characteristics.

### Applications

- Salary estimation tools
- Job market analysis
- HR analytics
- Career planning platforms

---

# 2. Paisabazaar Credit Risk Classification

### Overview

This project focuses on **classifying loan applicants based on how likely they are to repay their loans**. The system predicts the repayment likelihood category of a borrower using financial and behavioral attributes.

The classification categories include:

- Highly Likely to Repay
- Medium Likelihood
- Low Likelihood

This type of model can help banks and financial institutions identify potential credit risks before approving loans.

### Dataset Features

The dataset includes multiple attributes related to the borrower's financial profile and repayment behavior, such as:

- Age
- Occupation
- Annual Income
- Monthly Inhand Salary
- Number of Bank Accounts
- Number of Credit Cards
- Interest Rate
- Number of Loans
- Type of Loan
- Delay from Due Date
- Number of Delayed Payments
- Changed Credit Limit

### Objective

The goal of this project is to develop a machine learning model that helps financial institutions **identify borrowers who are likely to repay their loans and those who may default**.

### Applications

- Credit risk analysis
- Loan approval systems
- Banking analytics
- Financial risk management

---

# 3. Brain Tumor MRI Image Classification

### Overview

This project focuses on **classifying brain tumors using MRI scan images** through deep learning techniques.

The dataset contains image filenames and corresponding tumor labels. Each MRI image belongs to one of the following classes:

- No Tumor
- Glioma Tumor
- Pituitary Tumor
- Meningioma Tumor

### Models Used

The project explores multiple deep learning approaches including:

- Sequential Neural Network
- Transfer Learning with ResNet50
- Transfer Learning with InceptionV3

Transfer learning allows pre-trained convolutional neural networks to extract meaningful visual features from MRI images, improving classification performance.

### Objective

The goal of this project is to build a deep learning model capable of **classifying MRI images into different tumor categories**, which can assist in early medical diagnosis and automated medical image analysis.

### Applications

- Medical image analysis
- AI-assisted diagnostics
- Healthcare research
- Computer-aided tumor detection

---

# Streamlit Demo Application

A Streamlit web application is included in the repository to demonstrate the Brain Tumor MRI classification model.

The application provides a simple user interface where users can:

- Upload an MRI image
- Run the trained model
- View the predicted tumor category

This allows users to interact with the deep learning model without writing any code.

---

# Tech Stack

Python  
Pandas  
NumPy  
Scikit-learn  
TensorFlow / Keras  
Deep Learning (CNN, Transfer Learning)  
Matplotlib  
Seaborn  
Streamlit

---

# Repository Structure

```
Labmentix-Internship
│
├── Glassdoor_Project
│
├── Paisabazaar_Project
│
├── Brain_Tumor_MRI_Classification
│
├── Streamlit_Demo
│
├── requirements.txt
│
└── README.md
```

---

# How to Run the Project

Clone the repository

```
git clone https://github.com/mayank2004201/Labmentix-Internship.git
```

Navigate to the project directory

```
cd Labmentix-Internship
```

Install dependencies

```
pip install -r requirements.txt
```

Run the Streamlit application

```
streamlit run app.py
```

The Streamlit interface will open in your browser where you can upload MRI images and view predictions.

---

# Author

Mayank Goel
