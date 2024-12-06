import numpy as np
from sklearn.model_selection import train_test_split
from ml.model import create_model

def train_model(df):
    X = df[['competitor_prices', 'inventory_levels', 'demand']].values
    y = df['optimal_price'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = create_model(X.shape[1])
    model.fit(X_train, y_train, epochs=10, batch_size=32)
    loss = model.evaluate(X_test, y_test)
    print(f'Test Loss: {loss}')
    return model
