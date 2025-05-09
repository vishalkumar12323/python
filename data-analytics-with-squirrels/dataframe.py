import pandas as pd


customer = {
    "name": ["bob", "casey", "adam"],
    "sex": ["male", "female", "male",],
    "age": [23, 21, 22],
    "score": [22, 35, 55],
    "reward": [4, 7, 2]
}
df = pd.DataFrame(customer)
print(df)
# print(df[["name", "age", 'score']])
# print(df.describe())
# print(df.head(3))
# print(df.tail(3))

# print(df.info())

# series = pd.Series([23, 21, 22, 30, 29, 31], name="age")
# print(series.max())

# how to select a subset of a DataFrame?
# print(df.iloc[2:3, 3:5])


# player_record_dict = pd.DataFrame(df).to_dict()
# print(player_record_dict)

