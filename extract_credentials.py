import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

# STEP 1: Define the API scopes
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# STEP 2: Authenticate using absolute path to credentials.json
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "D:/TOOLS MAKING/GOOGLE SPREADSHEET/credentials.json", scope
)
client = gspread.authorize(creds)

# STEP 3: Ask user for the Google Spreadsheet URL
sheet_url = input("Enter Google Spreadsheet URL: ")

# STEP 4: Open spreadsheet and select first sheet
spreadsheet = client.open_by_url(sheet_url)
worksheet = spreadsheet.sheet1

# STEP 5: Read all rows of data
all_data = worksheet.get_all_values()

# STEP 6: Extract credentials from each row
credentials = []
for row in all_data:
    if len(row) >= 3:
        website = row[0].strip()
        username = row[1].strip()
        password = row[2].strip()
        credentials.append({
            'website': website,
            'username': username,
            'password': password
        })

# STEP 7: Display the extracted data
print("\n🔐 Extracted Credentials:")
for cred in credentials:
    print(f"🌐 Website: {cred['website']}, 👤 Username: {cred['username']}, 🔑 Password: {cred['password']}")

# STEP 8: Save to CSV
csv_file = "D:/TOOLS MAKING/GOOGLE SPREADSHEET/credentials.csv"
with open(csv_file, "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["website", "username", "password"])
    writer.writeheader()
    writer.writerows(credentials)

print(f"\n✅ Credentials saved to '{csv_file}'")
