import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import os

# Step 1: Load and preprocess the dataset
data = pd.read_csv(os.path.join(os.path.dirname(__file__), "employee-processed.csv"))

# Perform data preprocessing, including encoding categorical variables and handling missing values.
data = pd.get_dummies(data, drop_first=True)
data = data.dropna()

# Step 2: Split the data
X = data.drop("LeaveOrNot", axis=1)  # Features
y = data["LeaveOrNot"]  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Feature selection/engineering (if needed)

# Step 4: Build the models
naive_bayes = GaussianNB()
decision_tree = DecisionTreeClassifier()
random_forest = RandomForestClassifier()

# Step 5: Train the models
naive_bayes.fit(X_train, y_train)
decision_tree.fit(X_train, y_train)
random_forest.fit(X_train, y_train)

# Step 6: Model evaluation
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    return acc, cm

nb_accuracy, nb_confusion_matrix = evaluate_model(naive_bayes, X_test, y_test)
dt_accuracy, dt_confusion_matrix = evaluate_model(decision_tree, X_test, y_test)
rf_accuracy, rf_confusion_matrix = evaluate_model(random_forest, X_test, y_test)

# Step 7: Model comparison
print("Naive Bayes Accuracy:", nb_accuracy)
print("Naive Bayes Confusion Matrix:\n", nb_confusion_matrix)
print("Decision Tree Accuracy:", dt_accuracy)
print("Decision Tree Confusion Matrix:\n", dt_confusion_matrix)
print("Random Forest Accuracy:", rf_accuracy)
print("Random Forest Confusion Matrix:\n", rf_confusion_matrix)
