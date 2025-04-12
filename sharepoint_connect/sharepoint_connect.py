import pandas as pd
import io
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.authentication_context import AuthenticationContext

# SharePoint site info
sharepoint_url = "https://yourcompany.sharepoint.com/sites/yoursite"
username = "your-email@yourcompany.com"
password = "your-password"

# Folder inside SharePoint where you want to upload
target_folder = "Shared Documents/Reports"  # or "Documents" or custom name

# Create a CSV in memory
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Score': [95, 88]
})
csv_buffer = io.StringIO()
df.to_csv(csv_buffer, index=False)
csv_bytes = io.BytesIO(csv_buffer.getvalue().encode())

# Authenticate and connect
ctx_auth = AuthenticationContext(sharepoint_url)
if ctx_auth.acquire_token_for_user(username, password):
    ctx = ClientContext(sharepoint_url, ctx_auth)
    folder = ctx.web.get_folder_by_server_relative_url(target_folder)

    target_file_name = "example_upload.csv"
    upload_result = folder.upload_file(target_file_name, csv_bytes)
    ctx.execute_query()
    print(f"✅ File uploaded successfully to SharePoint: {target_file_name}")
else:
    print("❌ Authentication failed. Please check your credentials or site URL.")
