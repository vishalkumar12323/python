import pandas as pd

data = {
    "students": ["bob", 'adam', 'casey', 'jake', 'alex', 'peter', 'john', 'liam'],
    "score": [89, 56, 87, 76, 89, 88, 55, 90]
}

df = pd.DataFrame(data=data)

# looping a dataframe
# for (key, value) in df.items():
#     print(value)

for (index, row) in df.iterrows():
    print(row["score"])
    # if row.score > 85:
    #     print(row)