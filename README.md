# Outreachy tasks notes
### 
Hi! I am Sania, and this document contains my solutions and notes for the microtasks for project T418284.

From my understanding, this project is about building tools that help the Portuguese-speaking Wikimedia community. The goal is to improve their editing experience, either by improving the Wikiscore tool to track Wikidata edits (Wish #8), or by adding a feature in the Visual Editor to detect duplicate references automatically (Wish #3).

For Task 1, I worked with JSON data and used JavaScript to display it in a clean and readable format on a webpage. I see this as practice for handling real data from MediaWiki APIs. To run it, you can open the `Task 1 - Intern.html` file in any browser.

While working on this, I explored different ways to handle dates and learned that using built-in date functions can sometimes cause issues due to timezone differences. So I handled the date manually to make sure it stays accurate.

For Task 2, I read URLs from a CSV file and printed their status codes using Python. This connects well with the project because checking links is important when working with references.

Some links in the CSV are broken or very old, so I made sure the script handles errors properly. I used a faster approach (HEAD request) to check URLs without downloading full pages, and added a timeout and error handling so the script doesn’t stop if a link fails.
