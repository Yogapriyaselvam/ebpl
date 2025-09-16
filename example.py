import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", None],
    "Age": [25, 30, 35, 28],
    "City": ["Paris", "London", "Berlin", "Rome"]
}

df = pd.DataFrame(data)

df.info()
