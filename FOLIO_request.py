import requests
import json
import os
import csv
import time

BARCODES_FILE = "barcodes.txt"

# Folio token 
TOKEN_FILE = os.path.join(os.path.dirname(__file__), "FOLIO_TOKEN.txt")

# Read access token
try:    
    with open(TOKEN_FILE, "r") as f:
        ACCESS_TOKEN = f.read().strip()
except FileNotFoundError:
    raise FileNotFoundError(
        f"Missing token file: {TOKEN_FILE}\n"
        "Please create it and paste your access token."
    )

# Response header template
headers = {
    "x-okapi-token": ACCESS_TOKEN,
    "x-okapi-tenant": "scu",
    "Content-Type": "application/json",
}

BASE_URL = "https://scu-okapi.folio.indexdata.com/inventory/items"

def get_item_status(barcode: str) -> str:
    """
    Requests item status from FOLIO API using personal access token.
    Returns item[i].status.name, or "NULL" if not found or bad response.
    """
    params = {"query": f"barcode=={barcode}"}
    try:
        response = requests.get(BASE_URL, headers=headers, params=params, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Request error for barcode {barcode}: {e}")
        return "NULL"

    if response.status_code != 200:
        print(f"Error {response.status_code} for barcode {barcode}: {response.text}")
        return "NULL"

    data = response.json()
    items = data.get("items", [])
    if not items:
        print(f"No item found for barcode {barcode}")
        return "NULL"

    return items[0].get("status", {}).get("name", "NULL")

def write_csv(results, filename="results.csv"):
    """Write results to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Barcode", "FOLIO Status"])
        for r in results:
            writer.writerow([r["barcode"], r["FOLIO_status"]])

    print(f"{len(results)} results written to {filename}")

def main():
    # Read barcodes from file
    if not os.path.exists(BARCODES_FILE):
        print(f"Missing {BARCODES_FILE}")
        return

    with open(BARCODES_FILE, "r") as f:
        barcodes = [line.strip() for line in f if line.strip()]

    results = []

    for i, barcode in enumerate(barcodes, start=1):
        status = get_item_status(barcode)
        results.append({"barcode": barcode, "FOLIO_status": status})
        print(f"[{i}/{len(barcodes)}] {barcode}: {status}")
        time.sleep(0.2) # api delay

    write_csv(results)

if __name__ == "__main__":
    main()
