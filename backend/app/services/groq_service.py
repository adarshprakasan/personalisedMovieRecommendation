import httpx

SANITY_PROJECT_ID = "u72tnd1c"
SANITY_DATASET = "production"
SANITY_API_VERSION = "2021-03-25"
SANITY_API_URL = f"https://{SANITY_PROJECT_ID}.api.sanity.io/v{SANITY_API_VERSION}/data/query/{SANITY_DATASET}"

def fetch_movies():
    query = '*[_type == "movie"] {title, description, tags}'
    response = httpx.get(SANITY_API_URL, params={"query": query})
    response.raise_for_status()
    return response.json()

movies = fetch_movies()
print(movies)
