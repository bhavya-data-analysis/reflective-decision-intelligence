import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load data
df = pd.read_csv("decision_fragility.csv")

X = df["decision_text"]
y = df["fragility_label"]

# Vectorize text
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    min_df=1,
    stop_words="english"
)
X_vec = vectorizer.fit_transform(X)

# Train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.3, random_state=42, stratify=y
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

