# 📄 Smart Text Classifier (Spam & Sentiment Analysis)

## 🚀 Project Overview

This project is an **NLP-based Smart Text Classifier** that classifies text into:

* 📩 **Spam / Not Spam**
* 😊 **Positive / Negative Sentiment**

It uses **TF-IDF vectorization** and **Multinomial Naive Bayes** to perform efficient and accurate text classification.

---

## 🧠 Features

* 🔍 Spam Detection
* 💬 Sentiment Analysis
* ⚡ Fast prediction using Naive Bayes
* 🌐 Optional Flask Web Interface
* 📊 Works on real-world datasets

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:**

  * scikit-learn
  * pandas
  * numpy
  * Flask (for web app)

---

## 📁 Project Structure

```
smart-text-classifier/
 ├── data/
 │    └── dataset.csv
 ├── model.pkl
 ├── vectorizer.pkl
 ├── app.py
 ├── train.py
 ├── templates/
 │    └── index.html
 ├── requirements.txt
 └── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/smart-text-classifier.git
cd smart-text-classifier
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### 1️⃣ Train the Model

```bash
python train.py
```

### 2️⃣ Run Web App

```bash
python app.py
```

👉 Open in browser:

```
http://127.0.0.1:5000
```

---

## 🧪 Example

**Input:**

```
Congratulations! You won a free lottery 🎉
```

**Output:**

```
Spam + Positive Sentiment
```

---

## 📊 Model Details

* **Vectorization:** TF-IDF
* **Algorithm:** Multinomial Naive Bayes
* **Tasks:**

  * Spam Classification
  * Sentiment Analysis

---

## 🎯 Future Improvements

* 🔥 Deep Learning (LSTM / BERT)
* 📈 Improve accuracy with larger dataset
* 🌍 Deploy on cloud (Render / AWS)
* 📊 Add confidence score

---

## 💼 Resume Description

> Built an NLP-based Smart Text Classifier using TF-IDF vectorization and Multinomial Naive Bayes to classify spam and sentiment with high accuracy.

---

## 🤝 Contributing

Feel free to fork this repo and improve it!

---

## 📜 License

This project is open-source and available under the MIT License.

![image alt](https://github.com/anup-sys/Built-a-Smart-Text-Classifier-using-NLP-techniques-to-classify-spam-and-sentiment-using-Naive-Bayes/blob/4dab271ea61c034cbfa13d5fc481e81a2f9edd05/Screenshot%20from%202026-04-19%2019-14-39.png)
![image alt](https://github.com/anup-sys/Built-a-Smart-Text-Classifier-using-NLP-techniques-to-classify-spam-and-sentiment-using-Naive-Bayes/blob/e185bc72135c5955deed4f0f24370d46b0717d37/Screenshot%20from%202026-04-19%2019-14-25.png)
