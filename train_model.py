import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# 1. Load dataset
data = pd.read_csv("data/spam.csv", encoding='latin-1')

# 2. Fix column names (Kaggle dataset)
data = data[['v1', 'v2']]
data.columns = ['label', 'text']

# 3. Clean data (important)
data = data.dropna()

# 4. Convert labels to binary
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# 5. Features & labels
X = data['text']
y = data['label']

# 6. TF-IDF vectorization
vectorizer = TfidfVectorizer(
    stop_words='english',
    ngram_range=(1, 2),
    max_features=5000
)

X_vector = vectorizer.fit_transform(X)

# 7. Train-test split (with stratify)
X_train, X_test, y_train, y_test = train_test_split(
    X_vector, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 8. Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# 9. Evaluate model
y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 10. Save model & vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("\n✅ Model saved successfully!")

# 11. Test with user input
print("\n--- Smart Spam Classifier ---")

while True:
    text = input("\nEnter message (or type 'exit'): ")

    if text.lower() == "exit":
        print("Exiting...")
        break

    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]

    print("Prediction:", "Spam" if pred == 1 else "Not Spam")