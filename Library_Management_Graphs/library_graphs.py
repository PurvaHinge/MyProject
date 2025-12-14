import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("library_data.csv")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# ------------------------------------------------
# 1. Line Graph: Books Issued vs Books Returned
# ------------------------------------------------
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Books_Issued'], marker='o', label='Books Issued')
plt.plot(df['Date'], df['Books_Returned'], marker='o', label='Books Returned')
plt.title("Books Issued vs Returned")
plt.xlabel("Date")
plt.ylabel("Number of Books")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------------------------------------
# 2. Bar Chart: Daily New Members
# ------------------------------------------------
plt.figure(figsize=(10,5))
plt.bar(df['Date'], df['New_Members'])
plt.title("Daily New Members Joined")
plt.xlabel("Date")
plt.ylabel("Members")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------------------------------------
# 3. Bar Chart: Total Books in Library
# ------------------------------------------------
plt.figure(figsize=(10,5))
plt.bar(df['Date'], df['Total_Books'])
plt.title("Total Books Available")
plt.xlabel("Date")
plt.ylabel("Books Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------------------------------------
# 4. Line Graph: Fine Collected Over Time
# ------------------------------------------------
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Fine_Collected'], marker='o')
plt.title("Fine Collected Over Time")
plt.xlabel("Date")
plt.ylabel("Amount (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------------------------------------
# 5. Bar Chart: Active Members
# ------------------------------------------------
plt.figure(figsize=(10,5))
plt.bar(df['Date'], df['Active_Members'])
plt.title("Active Library Members")
plt.xlabel("Date")
plt.ylabel("Members")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------------------------------------
# 6. Line Graph: Books Damaged
# ------------------------------------------------
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Books_Damaged'], marker='o')
plt.title("Damaged Books Report")
plt.xlabel("Date")
plt.ylabel("Number of Books")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------------------------------------
# 7. Pie Chart: Issued vs Returned Books
# ------------------------------------------------
issued = df['Books_Issued'].sum()
returned = df['Books_Returned'].sum()

plt.figure(figsize=(6,6))
plt.pie([issued, returned], labels=['Issued', 'Returned'], autopct='%1.1f%%')
plt.title("Issued vs Returned Books")
plt.show()

# ------------------------------------------------
# 8. Bar Chart: Comparison of Issued & Returned
# ------------------------------------------------
plt.figure(figsize=(10,5))
plt.bar(df['Date'], df['Books_Issued'], label='Issued')
plt.bar(df['Date'], df['Books_Returned'], bottom=df['Books_Issued'], label='Returned')
plt.title("Books Circulation Comparison")
plt.xlabel("Date")
plt.ylabel("Books Count")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
