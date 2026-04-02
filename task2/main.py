import csv
import requests

def check_urls(file_path):
    # Open the CSV file in read mode
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            # Skip empty rows just in case
            if not row:
                continue
            
            url = row[0].strip()
            
            # Skip the header row if the CSV has one
            if url.lower() == 'urls' or url.lower() == 'url':
                continue

            try:
                # AI Note: I used an AI to research the most efficient way to ping URLs. 
                # I learned that using a HEAD request is much faster than a GET request 
                # because it doesn't download the entire webpage body.
                
                # We use a 5-second timeout so the script doesn't freeze on broken servers.
                response = requests.head(url, allow_redirects=True, timeout=5)
                
                # Some servers block HEAD requests and return a 405 or 403 error.
                # If that happens, we fallback to a normal GET request but only stream the headers.
                if response.status_code in [405, 403]:
                    response = requests.get(url, stream=True, timeout=5)

                # Print the result in the exact format requested
                print(f"({response.status_code}) {url}")

            except requests.exceptions.RequestException:
                # If the site is completely dead or doesn't exist, we catch the error 
                # so the script doesn't crash, and print a custom message.
                print(f"(ERROR) {url}")

# Run the function (make sure the CSV file is in the same folder as this script)
if __name__ == "__main__":
    check_urls('Task 2 - Intern.csv')