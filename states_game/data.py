import pandas as pd


df = pd.read_csv("./50_states.csv")
state_list = df.state.to_list()
df = df[df.state == 'South Dakota']
print(df.x)
print(df.y)