import pandas as pd
import matplotlib.pyplot as plt

file = "./data/vehicles.csv"
auto = pd.read_csv(file)
print(f"Loaded {len(auto):,} records")

(auto
 .groupby(['year', 'make'])
 .size()
 .unstack('make')
 .loc[:, ['Ford', 'Lexus', 'Toyota']]
 .plot(kind='bar', figsize=(14, 10))
 )
plt.show()
