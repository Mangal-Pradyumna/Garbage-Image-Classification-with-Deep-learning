# Garbage-Image-Classification-using-CNN
This project develops a deep learing-based image classification system to automatically categorize waste items into different types such as paper, metal, plastic, glass, cardboard, and general trash. Using convolutional neural networks trained from scratch, the system aims to achieve high accuracy in distinguishing between various waste categories.

The model will be trained on the Garbage Dataset Classification from Kaggle, which contains labeled images of different waste types. The project focuses on creating a custom CNN architecture that can distinguish between biodegradable and non-biodegradable waste while further categorizing items into specific subcategories such as e-waste, food waste, and plastic bottles.

Key Features:
* Multi-class image classification for waste categorization
* Custom CNN architecture built from scratch
* Data augmentation techniques to improve model generalization
* Support for both biodegradable/non-biodegradable classification and detailed waste type identification
* Model performance evaluation and optimization

**Technologies**: Python, TensorFlow/PyTorch, OpenCV, custom convolutional neural networks, data preprocessing and augmentation libraries

**Applications**: Environmental sustainability, automated waste management systems, recycling optimization, and smart city initiatives.

This project focuses on **classifying garbage images** into different categories using a Convolutional Neural Network (CNN).  
The dataset is hosted on **Kaggle** and can be automatically downloaded using the provided script.

---

## 📂 Project Structure
Garbage-Image-Classification-using-CNN/
│── download_dataset.py # Script to download dataset from Kaggle
│── notebooks/ # Jupyter notebooks for experiments
│── src/ # Source code for model and training
│── data/ # Dataset will be downloaded here
│── README.md # Project documentation

## 📥 Download Dataset

1. **Get Kaggle API Token**  
   - Go to [Kaggle → Account → API → Create New Token](https://www.kaggle.com/account)  
   - This downloads a file named `kaggle.json`  
   - Place it in:  
     - **Linux/Mac:** `~/.kaggle/kaggle.json`  
     - **Windows:** `C:\Users\<username>\.kaggle\kaggle.json`

2. **Install dependencies**  
   ```bash
   pip install kaggle
