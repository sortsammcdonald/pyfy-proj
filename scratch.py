import pandas as pd

df = pd.read_csv("credit6.csv")

expense_amounts = df.loc[df["Type"] == "Expense", "Amount"]

print(expense_amounts)
