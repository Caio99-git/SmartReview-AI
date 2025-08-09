import requests  # For calling APIs that return JSON
import feedparser  # For reading RSS news feeds

# Get latitude/longitude for a city 
def geocode_city(name: str):
    try:
        name = (name or "").strip()  # "" is an empty string 
                                     # .strip() removes spaces from the start and end of the string.
        if not name:
            return None
        
        # Call Open-Meteo's geocoding API
        r = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": name, "count": 1, "language": "en", "format": "json"},
            timeout=10,
        ).json()
        
        if not r.get("results"):  # No city found
            return None
        
        # Return first match with coordinates
        c = r["results"][0]
        return {
            "latitude": c["latitude"],
            "longitude": c["longitude"],
            "name": c.get("name", name),
            "country": c.get("country", ""),
        }
    except Exception:
        return None


# Get current weather for a city 
def get_weather(city: str = "New York"):
    loc = geocode_city(city)  # First, find city coordinates
    if not loc:
        return {"error": f"Couldn't find location for '{city}'."}

    try:
        # Call Open-Meteo's weather API
        r = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": loc["latitude"],
                "longitude": loc["longitude"],
                "current_weather": "true",
            },
            timeout=10,
        ).json()
        
        # Extract only the "current_weather" section
        data = r.get("current_weather", {})
        if not data:
            return {"error": "Weather data unavailable."}
        
        # Add resolved city name for clarity
        # Adds a resolved_city field to the weather data so the result clearly shows the exact city (and country) that the API matched.
        data["resolved_city"] = f'{loc["name"]}{", " + loc["country"] if loc["country"] else ""}'
        return data
    except Exception as e:
        return {"error": str(e)}


# Get latest BBC News headlines
def get_news():
    try:
        # Parse BBC News RSS feed
        rss = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
        return rss.entries[:5]  # Only first 5 headlines
    except Exception as e:
        return [{"title": "Error fetching news", "link": "#", "error": str(e)}]