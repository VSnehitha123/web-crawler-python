import requests
import urllib3
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

# Disable SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Step 1: Crawl website
url = "https://example.com"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, "html.parser")

links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        links.append(href)

# Step 2: Email setup
sender_email ="snehithasnehi495@gmail.com"
receiver_email ="snehithasnehi495@gmail.com"
app_password = "ucebehdrqynyjbat"   # ← MUST be app password

# Prepare message
message = "Collected Links:\n\n"
for l in links:
    message += l + "\n"

msg = MIMEText(message)
msg["Subject"] = "Web Crawled Data"
msg["From"] = sender_email
msg["To"] = receiver_email

# Step 3: Send email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.send_message(msg)
    server.quit()

    print("✅ Email sent successfully!")

except Exception as e:
    print("❌ Error:", e)