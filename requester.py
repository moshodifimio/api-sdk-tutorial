import requests

# List of URLs with different hostnames (API endpoints)
urls = [
    'https://jsonplaceholder.typicode.com/posts/1',   # JSONPlaceholder API
    'https://api.spacexdata.com/v4/launches/latest',  # SpaceX API
    'https://dog.ceo/api/breeds/image/random',        # Dog CEO API
    'https://catfact.ninja/fact',                     # Cat Facts API
    'https://official-joke-api.appspot.com/jokes/random',  # Joke API
    'https://api.coindesk.com/v1/bpi/currentprice.json',   # CoinDesk API
    'https://api.github.com'                          # GitHub API
]

# Function to make requests to each endpoint and print the response body
def fetch_responses(urls):
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
            data = response.json()  # Parse the JSON response
            print(f"Response from {url}:\n", data, "\n")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} for URL: {url}")
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err} for URL: {url}")

# Call the function to make the requests and print their responses
fetch_responses(urls)
