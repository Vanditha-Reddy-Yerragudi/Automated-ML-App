# Automated-ML-App

## **Overview**  
The **Automated ML WebApp** is a powerful, no-code machine learning tool designed to **automate the entire ML workflow**—from data preprocessing and model selection to training and deployment. Developed using **Python, Pandas-Profiling, PyCaret, and Streamlit**, this web application allows users to quickly build, evaluate, and export machine learning models without writing extensive code.  

Additionally, the **Model Testing Script** serves as a validation tool that loads a saved model (`finalized_model.sav`) and tests it on new input data. This ensures that trained models perform correctly before deployment.  

Together, these components provide a **complete, end-to-end machine learning solution**, making ML accessible to both beginners and experienced data scientists.

---

## **Main Components**  

### **Input**  
- **WebApp Input:**  
  - Users upload a structured dataset (CSV format).  
  - They configure ML settings, select target variables, and choose features.  
- **Model Testing Script Input:**  
  - A saved machine learning model (`finalized_model.sav`).  
  - New input data (features) in a structured format for making predictions.  

### **Process**  
- **WebApp Process:**  
  - Performs **automated exploratory data analysis (EDA)** using **Pandas-Profiling**.  
  - Uses **PyCaret** to handle **feature engineering, model selection, training, and tuning**.  
  - Provides real-time **model performance metrics** to help users select the best model.  
  - Allows users to **download trained models** for further use.  
- **Model Testing Script Process:**  
  - Loads the trained model using `pickle`.  
  - Processes new input data to match the model's expected format.  
  - Makes predictions on unseen data.  

### **Output**  
- **WebApp Output:**  
  - A trained machine learning model ready for deployment.  
  - Downloadable `.sav` model file.  
  - Model performance metrics (accuracy, precision, recall, F1-score, etc.).  
- **Model Testing Script Output:**  
  - Prints the predicted result for new input data.  
  - Helps verify if the trained model performs correctly before deployment.  

---

## ** Key Benefits**  

**End-to-End Automation** – No need for manual coding; everything from EDA to model training is automated.  
**User-Friendly Interface** – Built with Streamlit, providing an intuitive web-based UI.  
**Faster Model Development** – Automates tedious ML tasks like preprocessing, feature selection, and hyperparameter tuning.  
**Download & Deploy Models** – Trained models can be easily exported for production use.  
**Seamless Model Testing** – The Model Testing Script allows quick validation of model predictions before deployment.  
**Accessible to All** – Ideal for both **beginners** (who want a no-code ML solution) and **experts** (who need rapid prototyping).  

This project streamlines the machine learning workflow, **saving time and effort**, and enabling users to focus on insights rather than technical complexities.  
