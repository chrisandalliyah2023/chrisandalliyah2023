import requests
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

json_key_data = json.loads('{"type": "service_account", "project_id": "wedding-rsvps-381621", "private_key_id": "be4bec0015399095f3295613e946cc49b1e10279", "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEugIBADANBgkqhkiG9w0BAQEFAASCBKQwggSgAgEAAoIBAQDMidyg6OEImdUt\\nN96ST5gbKcTnfo76QYLHl9hb71qtB0wi8q0Q3NiY6d8gsO+KHPqcMvUlD4e+FIRL\\nAr0KptwVtAwuJTlD2dgwJBjhRnXtkkb4EKd11DSp2MUuJc5zBJXgyj8GQz18sYKi\\nxhQSRI89Et/ZXpDeTneVuK7C+BxNCzBYkr5HC0q3PoXGQ/b3iVKefBInVoywn7bM\\nSGaATntz4Ev7o5u6glfUnqZZUbqZm5LRjkFiZdBob81VMaBxis3ugWWxgW9cOd2D\\nZSK/HcXcN4FAF8EwSSSV3kUEE7ZMQqtuQiHfmXz7CG7z7xWifnn/xYPsi7+vsV6G\\nPXWL5bCPAgMBAAECgf8I6/qJCkob60SL3w6rqHfPYi20lftRRIpFKoUa0tX3C4Uc\\nASSLbRawP4NRabuzyo/Olb/GXhG4Y4IMbjzQuiE00SW23ZN3N4lhOtyFobfYel5I\\nyRvaMpIZgTBt/Y2DzC9oHr+hBk3S9+s62ROxuEvciMuQL7p3TUo/aE7h3PC0a4nh\\nqV/Ap5ItF1EUgOxeHMgRbCaQ5AtNRG6XlRHL1nq6XBaZXMJix2CTUhd6+LVcxrba\\nXzicUb6JELxo5OiptEP1+l9bnvEIpiTiCqF7IFWXWkrvNN990dP3anwEocPE8Dhb\\nAQ4KbsZvj7PBKEO3VQ5cbN0syiLHOccOuLmM690CgYEA7JuZBMOR/u3K14hk7pdf\\n/Mvj6USGSVo12z93Mtoh6PLDKuXrp9VuJpdYMsX5PVpreadZBFnOitUaPhAdItdz\\nR4wuPJ0TrTh2JdAkgEYU4r/P6hkswx0kl1yCXxTi/BVsULaxgDzRb7gaZLAWqGFp\\n3F0ag4VMIaGQpFBkkIzqPusCgYEA3U1mfljJwkt3qlFGHm6gL0wB86iMyHlNklrR\\nUS4Hr5BDut2Jhwpp3LMBqc8HvjBBcedGpJjbja6fk6lCrfcGD/lmQ8RXnDTLGk95\\nofUNHxRLryMdQiHUoWlCRvf8ZJlYgdTP0kddd3C1YovX/Yd1ieuxTlhD9GGKbvEX\\nMtGaE+0CgYAOGSNf/ks3tnGMsCrbcJeel4OIBbY+rqpg2wI+PHMizzxD1RlakcQT\\ndpchx1wXhMi8ofUS5ksBSLtckVc7GT1cOQUURYPDoYagsCtMnWBnNmisGT3qjlT8\\n091MzxDLVndyw8AF1Rnhn0WrVDa1Z8CICeAnkAy+QEM/Fy820b6vawKBgFiC8I9w\\nK6IOVRpFz2m0jVTdbZpqu4QjICd9M2LoqiJJ7Qz8NllQjO68mdm0+D/VRRetjM+g\\nY4/TW/fPJuA1gLM66PAJw5CyfNlVGCzyugDIOU0fGkCtD0JPuzZvUP9bZc7nswdD\\ni9qNtb5oeEbqutQi9JOFMgi4Son8225z7tAxAoGAAWNWcX/wLnh3i6DtPp/6/yV4\\nkBUsfvYIYN9sOzptF5lAl2yPXpFR1qG7s4nbgXgJlY2aCcDKR2gOZLRaisfdGg2o\\n0yRZY8eZ6E9jAFZwl1nVXqCOESgz1TgScp7BUkuwU+XJ1wfCcM+6p1+Q3nPJw/LE\\n7nRYTupl5EXjMHStlew=\\n-----END PRIVATE KEY-----\\n", "client_email": "rsvp-sheet@wedding-rsvps-381621.iam.gserviceaccount.com", "client_id": "113107919624284661712", "auth_uri": "https://accounts.google.com/o/oauth2/auth", "token_uri": "https://oauth2.googleapis.com/token", "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs", "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/rsvp-sheet%40wedding-rsvps-381621.iam.gserviceaccount.com"}')

creds = service_account.Credentials.from_service_account_info(
    json_key_data,
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)


# Create a new Google Sheet or locate an existing one
sheet_id = '19ED8KFavUw0p9Bmlr6EMD2xr8UwDCogRJTncH5aM8Fc'

# Make HTTP request to Usebasin API to retrieve form submissions
form_id = "3adec6591599"
api_token = "a01a655e56ef3aed539a2587d29ef05f"
response = requests.get(f"https://usebasin.com/api/v1/submissions?form_id={form_id}&api_token={api_token}")
response.raise_for_status()
data = response.json()

# Define the header row for the sheet
header_row = ['rsvp', 'plusOne', 'firstName', 'lastName', 'streetAddress', 'city', 'province', 'postalCode', 'country', 'email', 'plusOneFirstName', 'plusOneLastName', 'comments']
# Create the data to be written to the sheet by combining the header row with the data from the API
values = [header_row]
for submission in data['submissions']:
    payload_params = submission['payload_params']
    row_data = []
    for header in header_row:
        value = payload_params.get(header, '')
        if ',' in value:
            # Add quotation marks around the value and remove the Excel formula
            value = f'"{value}"'
            value = value.replace('="', '').replace('"', '')
        row_data.append(value)
    values.append(row_data)

# Build the Google Sheets API client
service = build('sheets', 'v4', credentials=creds)

# Write the data to the sheet
body = {
    'values': values
}
result = service.spreadsheets().values().update(
    spreadsheetId=sheet_id, range='Sheet1!A1', valueInputOption='RAW', body=body).execute()

print(f'{result["updatedCells"]} cells updated.')
