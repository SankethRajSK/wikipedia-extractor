Wikipedia Extractor

A Python command-line tool that extracts the title and main topics (table of contents or section headings) from any Wikipedia article, given its URL.

Features
Fetches and parses live Wikipedia article pages
Extracts the article title
Extracts the list of topics from the article's Table of Contents (TOC)
Falls back to <h2> section headings if no TOC is present on the page
Handles common network errors gracefully (timeouts, connection issues, invalid URLs, HTTP errors)
Simple interactive loop — process multiple articles in one session
How It Works
Fetching: Uses the requests library to download the raw HTML of a Wikipedia article, with a custom User-Agent header and a request timeout to avoid hanging on slow responses.
Parsing: Uses BeautifulSoup (from bs4) to parse the HTML.
The article title is extracted from the page's <h1> tag.
Topics are extracted from the <div id="toc"> element (Wikipedia's table of contents), pulling the text of each <li> entry.
If no TOC is found on the page, the script falls back to collecting all <h2> section headings instead.
Interaction: The script runs in a loop, prompting the user for a Wikipedia URL, validating that it starts with https://en.wikipedia.org/wiki/, printing the extracted title and topics, and asking whether to process another article.
Tech Stack
Python 3
requests — for HTTP requests
beautifulsoup4 (bs4) — for HTML parsing
Usage

Install dependencies:

pip install requests beautifulsoup4

Run the script:

python wikipedia_extractor.py

Then paste a Wikipedia article URL when prompted, e.g.:

https://en.wikipedia.org/wiki/Python_(programming_language)
Example Output
Enter a Wikipedia article URL:
https://en.wikipedia.org/wiki/Python_(programming_language)

TITLE:
Python (programming language)

TOPICS:
- History
- Design philosophy and features
- Syntax and semantics
- Libraries
...
Possible Improvements
Extract and save full article text, not just titles/topics
Export results to CSV/JSON for downstream analysis
Add support for non-English Wikipedia domains
Add unit tests for HTML parsing edge cases (pages with no TOC, redirects, disambiguation pages)
