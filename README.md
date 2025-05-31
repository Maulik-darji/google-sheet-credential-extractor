# Google Sheet Credential Extractor

A simple Python script to extract website credentials (website, username/email, password) from a Google Spreadsheet and save them into a CSV file.

---

## Features

- Connects to Google Sheets using a service account.
- Automatically extracts credentials from the spreadsheet.
- Saves extracted data into a CSV file.
- Simple and easy to use.

---

## Prerequisites

- Python 3 installed on your computer.
- A Google account.
- Google Cloud project with Google Sheets API enabled.
- Service account JSON credentials file.

---

## Setup Guide

### 1. Clone or download this repository

```bash
git clone https://github.com/Maulik-darji/google-sheet-credential-extractor.git
cd google-sheet-credential-extractor
2. Install required Python packages
bash
Copy
Edit
pip install gspread oauth2client
3. Create a Google Cloud project and get service account credentials
Follow these steps carefully:

Go to Google Cloud Console:
Open Google Cloud Console and log in.

Create a new project:

Click on the project dropdown at the top-left corner.

Click New Project.

Give your project a name (e.g., Google Sheets API Project) and click Create.

Enable Google Sheets API:

In the search bar, type Google Sheets API and select it.

Click Enable.

Create a service account:

Navigate to IAM & Admin > Service Accounts from the left sidebar.

Click Create Service Account.

Enter a name for the service account (e.g., credential-extractor-sa) and click Create.

For the role, select Project > Editor or Sheets Editor.

Click Continue and then Done.

Create and download the service account key (JSON):

Find your service account in the list.

Click the three-dot menu on the right and select Manage keys.

Click Add Key > Create new key.

Select JSON as the key type and click Create.

A JSON file will be downloaded—save this file safely.

Share your Google Sheet with the service account:

Open your Google Spreadsheet.

Click Share (top-right).

From the downloaded JSON file, copy the value of the client_email field.

Paste this email in the Add people and groups field.

Set permission to Viewer or Editor and click Send.

4. Place the credentials JSON file
Move your downloaded credentials.json file to the project folder or any location you want.

Update the path in the script accordingly (default in script is: "D:/TOOLS MAKING/GOOGLE SPREADSHEET/credentials.json").

5. Run the script
bash
Copy
Edit
python extract_credentials.py
Enter the Google Spreadsheet URL when prompted.

The script will extract credentials and display them.

The credentials will also be saved into a CSV file at D:/TOOLS MAKING/GOOGLE SPREADSHEET/credentials.csv (you can change this path in the script).

Script Overview
python
Copy
Edit
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
Notes
Keep your credentials.json file private and do not upload it to public repositories.

Make sure your Google Sheet is shared with the service account email.

Adjust file paths in the script as needed for your system.

License
MIT License

Author
Maulik Darji
GitHub
