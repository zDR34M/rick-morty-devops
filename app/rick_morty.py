import requests
import csv

API_URL = "https://rickandmortyapi.com/api/character"

def fetch_characters():
    characters = []
    page = 1

    while True:
        response = requests.get(API_URL, params={"page": page})
        response.raise_for_status()
        data = response.json()

        for char in data["results"]:
            if (
                char["species"] == "Human"
                and char["status"] == "Alive"
                and char["origin"]["name"].startswith("Earth")
            ):
                characters.append({
                    "name": char["name"],
                    "location": char["location"]["name"],
                    "image": char["image"]
                })

        if not data["info"]["next"]:
            break

        page += 1

    return characters


def write_csv(characters, filename="data.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["name", "location", "image"]
        )
        writer.writeheader()
        writer.writerows(characters)
