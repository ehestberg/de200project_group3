import pandas as pd

df = pd.read_csv('../../Data/original_data/2008.csv')

ord_df = df[df['Origin'] == 'ORD']

ord_df.to_csv('../../Data/original_data/ORD_2008.csv')