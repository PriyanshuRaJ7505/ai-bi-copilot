import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    print('File loaded!')
    df.dropna(inplace=True)
    df['revenue'] = df['price'] * df['quantity']
    print(df.head())
    return df

if __name__ == '__main__':
    df = load_and_clean_data('data/sales.csv')
    print("done!")
    
