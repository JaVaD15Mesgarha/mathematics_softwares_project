import pandas as pd
import matplotlib.pyplot as plt
import os
#reading data from excel file 
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'data.xlsx')

df = pd.read_excel(file_path)

# drawing charts
# linear plot
df.plot(kind='line', marker='o', figsize=(8, 5))
plt.title('Execution Time by Data Size (Line Plot)')
plt.ylabel('Time')
plt.grid()
plt.show()

# bar plot
df.plot(kind='bar', figsize=(8, 5))
plt.title('Execution Time by Data Size (Bar Plot)')
plt.ylabel('Time')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# box plot
df.plot(kind='box', figsize=(8, 5))
plt.title('Distribution of Execution Times (Box Plot)')
plt.ylabel('Time')
plt.grid(axis='y')
plt.show()

