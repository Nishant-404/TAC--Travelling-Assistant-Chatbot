import requests

PEXELS_API_KEY = "" #enter your pexels api key

def get_place_images(place_name, limit=3):
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    params = {
        "query": place_name,
        "per_page": limit
    }
    url = "https://api.pexels.com/v1/search"
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            return [photo["src"]["medium"] for photo in data.get("photos", [])]
        else:
            return []
    except Exception as e:
        print(f"Error fetching images for {place_name}: {e}")
        return []
