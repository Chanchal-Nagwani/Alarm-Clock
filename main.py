import pandas as pd

# Sample data
data = {
    "Name": ["Anshika", "Chanchal"],
    "Age": [19, 20]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel file
df.to_excel("people.xlsx", index=False)  # index=False means don’t write row numbers
