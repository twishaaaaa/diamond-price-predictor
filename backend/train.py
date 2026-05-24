import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def download_dataset():
    if not os.path.exists('diamonds.csv'):
        print("⏳ Downloading dataset from Kaggle...")

        token = os.getenv('KAGGLE_API_TOKEN')

        if not token:
            raise Exception("❌ KAGGLE_API_TOKEN environment variable not set!")

        # Save token to kaggle config folder
        os.makedirs(os.path.expanduser('~/.kaggle'), exist_ok=True)
        with open(os.path.expanduser('~/.kaggle/access_token'), 'w') as f:
            f.write(token)

        # Download and unzip dataset
        os.system('kaggle datasets download -d shivam2503/diamonds --unzip')
        print("✅ Dataset downloaded!")
    else:
        print("✅ Dataset already exists, skipping download.")

def train():
    download_dataset()

    print("⏳ Training model...")

    df = pd.read_csv('diamonds.csv')
    df = df.drop(columns=['Unnamed: 0'], errors='ignore')
    df = df[(df['x'] > 0) & (df['y'] > 0) & (df['z'] > 0)]

    cut_order     = {'Fair':1,'Good':2,'Very Good':3,'Premium':4,'Ideal':5}
    color_order   = {'J':1,'I':2,'H':3,'G':4,'F':5,'E':6,'D':7}
    clarity_order = {'I1':1,'SI2':2,'SI1':3,'VS2':4,'VS1':5,'VVS2':6,'VVS1':7,'IF':8,'FL':9}

    df['cut']     = df['cut'].map(cut_order)
    df['color']   = df['color'].map(color_order)
    df['clarity'] = df['clarity'].map(clarity_order)

    X = df[['carat','cut','color','clarity','depth','table','x','y','z']]
    y = np.log(df['price'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    joblib.dump(model, 'diamond_model.pkl')
    print("✅ Model trained and saved!")

if __name__ == "__main__":
    train()