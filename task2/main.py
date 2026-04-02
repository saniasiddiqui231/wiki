import csv
import requests

def check_urls(file_path):
    # Open the CSV file in read mode
    # utf-8-sig' helps clean up hidden characters from the file
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            # Skip empty rows just in case
            if not row:
                continue
            
            url = row[0].strip()
            
            # Skip the header row if present
            if url.lower() == 'urls' or url.lower() == 'url':
                continue

            try:
                # I looked up different ways to check URLs and learned that
                # HEAD requests are faster since they don't download full content
                
                # We use a 5-second timeout so the script doesn't freeze on broken servers.
                response = requests.head(url, allow_redirects=True, timeout=5)
                
                # Some servers block HEAD requests and return a 405 or 403 error.
                # If that happens, we fallback to a normal GET request but only stream the headers.
                if response.status_code in [405, 403]:
                    response = requests.get(url, stream=True, timeout=5)

                # Print result in required format
                print(f"({response.status_code}) {url}")

            except requests.exceptions.RequestException:
                # If URL fails (invalid, timeout, etc.)
                print(f"(ERROR) {url}")

# Run the script
if __name__ == "__main__":
    check_urls('Task 2 - Intern.csv')
