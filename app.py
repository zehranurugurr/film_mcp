import requests

def get_ghibli_films():
    api_url = "https://ghibliapi.vercel.app/films"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return [film['title'] for film in data]
    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}

# Kullanım
print(get_ghibli_films())
