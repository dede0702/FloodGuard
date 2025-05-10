import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from prophet import Prophet
import joblib
import os

class FloodPredictor:
    def __init__(self, model_type='random_forest'):
        self.model_type = model_type
        self.model = None
        self.scaler = None

    def preprocess(self, df):
        df = df.copy()
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['hour'] = df['timestamp'].dt.hour
        df['day'] = df['timestamp'].dt.day
        df['month'] = df['timestamp'].dt.month
        df['weekday'] = df['timestamp'].dt.weekday
        df = df.sort_values('timestamp')
        return df

    def train(self, df):
        df = self.preprocess(df)
        if self.model_type == 'random_forest':
            features = ['precipitation_mm', 'hour', 'day', 'month', 'weekday']
            X = df[features]
            y = df['water_level']
            self.scaler = StandardScaler()
            X_scaled = self.scaler.fit_transform(X)
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
            self.model.fit(X_scaled, y)
        elif self.model_type == 'prophet':
            prophet_df = df[['timestamp', 'water_level']].rename(columns={'timestamp': 'ds', 'water_level': 'y'})
            self.model = Prophet()
            self.model.fit(prophet_df)
        else:
            raise ValueError("Unsupported model type. Choose 'random_forest' or 'prophet'.")

    def predict(self, df):
        df = self.preprocess(df)
        if self.model_type == 'random_forest':
            features = ['precipitation_mm', 'hour', 'day', 'month', 'weekday']
            X = df[features]
            X_scaled = self.scaler.transform(X)
            predictions = self.model.predict(X_scaled)
            df['predicted_water_level'] = predictions
        elif self.model_type == 'prophet':
            future = df[['timestamp']].rename(columns={'timestamp': 'ds'})
            forecast = self.model.predict(future)
            df['predicted_water_level'] = forecast['yhat'].values
        else:
            raise ValueError("Unsupported model type. Choose 'random_forest' or 'prophet'.")
        return df

    def evaluate(self, df):
        y_true = df['water_level']
        y_pred = df['predicted_water_level']
        mae = mean_absolute_error(y_true, y_pred)
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        r2 = r2_score(y_true, y_pred)
        return {'MAE': mae, 'RMSE': rmse, 'R2': r2}

    def save_model(self, path='models/model.pkl'):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump({'model': self.model, 'scaler': self.scaler}, path)

    def load_model(self, path='models/model.pkl'):
        data = joblib.load(path)
        self.model = data['model']
        self.scaler = data['scaler']
