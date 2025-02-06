# Ingest Data
import os
import json
from datetime import datetime
from webscraper import get_policy_links, scrape_policy
from exception import CustomException

ARTIFACTS_DIR = "artifacts"
os.makedirs(ARTIFACTS_DIR, exist_ok=True)

def ingest_data(url):
    """Ingests scraped policy data and saves it with a timestamp."""
    try:
        policies = get_policy_links(url)

        data = {}
        for policy, link in policies.items():
            if link:
                print(f"Scraping {policy} from: {link}")
                policy_text = scrape_policy(link)
                data[policy] = policy_text

        if not data:
            raise CustomException("No policy data found!")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(ARTIFACTS_DIR, f"scraped_{timestamp}.json")

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"Data saved in '{filename}'")
        return filename
    except CustomException as e:
        print(f"Data ingestion failed: {e}")
