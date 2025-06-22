from sklearn.base import BaseEstimator

def train_model(X_train, y_train, model):
    print(f"🚀 Training model: {model.__class__.__name__}")
    model.fit(X_train, y_train)
    print(f"✅ {model.__class__.__name__} training complete.")
    return model

