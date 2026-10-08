import pandas as pd

data = {
    "users" : ["Aman", "Riya", "Aman", "Kabir"],
    "text" : [
        "AWS is Great",
        "Google Cloud Session",
        "AWS is GREAT",
        None
    ]
}

df = pd.DataFrame(data)
df = df.drop_duplicates(data)
df["text"] = df["text"].fillna("")
df["text"] = df["text"].str.strip().str.lower()

print("Cleaned Data:")
print(df)