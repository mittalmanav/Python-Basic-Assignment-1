# Write a Python script that checks the uptime of provided URLs and notifies the user if any of the URLs return 4xx or 5xx HTTP status codes (indicating client or server errors). For demonstration purposes, you can use the following URLs as inputs:
# 4xx (Client Error):
# http://www.example.com/nonexistentpage or
# http://httpstat.us/404
# 5xx (Server Error):
# http://httpstat.us/500
# 200 (Successful Response):
# https://www.google.com/
# Requirements:
# URL Check: The script should check the provided URLs and get their HTTP status codes.
# Handle Multiple URLs: The script should be able to handle multiple URLs at once, checking each one.
# Error Detection: If the status code of any URL is either 4xx or 5xx, the program should:
# Notify the user via a print message.
# Alternatively, you can implement more advanced logging methods, (log in any log file).
# Loop and Monitor: You should set up a simple loop that continuously monitors the URLs for a certain interval (e.g., every 10 seconds) to simulate a basic uptime monitoring system.
# Status Message: For each URL, the script should output the URL and its current HTTP status code (e.g., 200 OK, 404 Not Found).

import requests
import time
urls = [
    "http://www.example.com/nonexistentpage", 
    "http://httpstat.us/404",                 
    "http://httpstat.us/500",                 
    "https://www.google.com/"                  
]
def check_urls():
    for url in urls:
        try:
            response = requests.get(url, timeout=5)  
            status_code = response.status_code
            status_text = f"{url} → {status_code} {response.reason}"
            if 400 <= status_code < 600:
                print(f"ALERT: {status_text} (Site might be down!)")
                with open("error_log.txt", "a") as log_file:
                    log_file.write(status_text + "\n")
            else:
                print(f"OK: {status_text}")
        except requests.exceptions.RequestException as e:
            error_message = f"ERROR: {url} → Request Failed ({str(e)})"
            print(error_message)
while True:
    check_urls()
    time.sleep(1)
