import requests
from bs4 import BeautifulSoup


def fetch_html(url):
    """Fetch HTML safely with error handling."""
    print(f"Fetching: {url}")

    try:
        r = requests.get(url, timeout=10, headers={"User-Agent":"Mozilla/5.0"})
        r.raise_for_status()
        return r.text

    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
    except requests.exceptions.ConnectionError:
        print("Network Error: Could not connect.")
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
    except requests.exceptions.RequestException as e:
        print("Unexpected Error:", e)

    return None


def extract_title_and_topics(html):
    """Extract article title + topics (TOC or fallback headings)."""
    soup = BeautifulSoup(html, "html.parser")

    # ----- Title -----
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "No title found"

    # ----- Try TOC first -----
    topics = []

    toc = soup.find("div", id="toc")
    if toc:
        for li in toc.find_all("li"):
            txt = li.get_text(" ", strip=True)
            topics.append(txt)

    # ----- Fallback: use all <h2> if TOC missing -----
    if not topics:
        for h2 in soup.find_all("h2"):
            txt = h2.get_text(" ", strip=True)
            if txt:
                topics.append(txt)

    return title, topics


def main():
    """Interactive loop."""
    while True:
        print("\nEnter a Wikipedia article URL:")
        try:
            url = input().strip()
        except EOFError:
            print("Input ended.")
            return

        if not url.startswith("https://en.wikipedia.org/wiki/"):
            print("Invalid Wikipedia URL.")
        else:
            html = fetch_html(url)

            if html:
                title, topics = extract_title_and_topics(html)

                print("\nTITLE:")
                print(title)

                print("\nTOPICS:")
                if topics:
                    for t in topics:
                        print("-", t)
                else:
                    print("No topics found.")
            else:
                print("Failed to load article.")

        print("\nProcess another article? (y/n)")
        ans = input().strip().lower()
        if ans != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
