import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pickle, sys
sys.path.append('.')
from app.services.data_cleaner import load_and_clean_data

def train_model():
    df = load_and_clean_data('data/sales.csv')
    df = pd.get_dummies(df, columns=['product', 'region'])
    df = df.drop(columns=['date'])
    X = df.drop('revenue', axis=1)
    y = df['revenue']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print('Model trained! Error:', mean_absolute_error(y_test, model.predict(X_test)))
    pickle.dump(model, open('app/ml/model.pkl', 'wb'))
    print('Model saved!')

if __name__ == '__main__':
    train_model()
