from sklearn.metrics import accuracy_score, classification_report

def evaluate_model(model, X_test, y_test):
    print(f"📊 Evaluating model: {model.__class__.__name__}")
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"✅ Evaluation complete. Accuracy: {accuracy * 100:.2f}%\n")
    return accuracy, classification_report(y_test, predictions)

