import wikipediaapi
import yfinance as yf
import requests

# Function to fetch a Wikipedia page summary using wikipedia-api SDK
def fetch_wikipedia_summary(page_title):
    # Define a proper user-agent as per Wikipedia's User-Agent policy
    user_agent = "YourAppName/1.0 (https://yourwebsite.com; your-email@example.com)"

    # Pass the language and user-agent explicitly to the Wikipedia API client
    wiki_wiki = wikipediaapi.Wikipedia(language='en', user_agent=user_agent)  # Wikipedia API client

    # Fetch the page by title
    page = wiki_wiki.page(page_title)

    if page.exists():
        return {
            "title": page.title,
            "summary": page.summary[:500]  # Fetching only the first 500 characters of the summary
        }
    else:
        return {"error": f"Page '{page_title}' does not exist on Wikipedia."}

# Function to fetch stock data using yfinance SDK
def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)  # Stock ticker symbol
    stock_info = stock.info

    # Safely access stock information with default fallback values
    return {
        "symbol": stock_info.get('symbol', 'N/A'),
        "current_price": stock_info.get('regularMarketPrice', 'N/A'),
        "market_cap": stock_info.get('marketCap', 'N/A'),
        "previous_close": stock_info.get('previousClose', 'N/A'),
    }

# Function to fetch weather data from a public API using requests
def fetch_weather(city):
    url = f'http://wttr.in/{city}?format=%C+%t'  # Using wttr.in for free weather data

    response = requests.get(url)

    if response.status_code == 200:
        return {"city": city, "weather": response.text.strip()}
    else:
        return {"error": f"Failed to fetch weather for {city}. Status Code: {response.status_code}"}

# Main function to call the SDKs and API, and print the results
def main():
    # Fetch data using wikipedia-api SDK
    wiki_data = fetch_wikipedia_summary('Python (programming language)')

    # Fetch stock data using yfinance SDK
    stock_data = fetch_stock_data('AAPL')  # AAPL is the ticker symbol for Apple Inc.

    # Fetch weather data using requests
    weather_data = fetch_weather('London')

    # Print Wikipedia data
    if "error" in wiki_data:
        print(wiki_data["error"])
    else:
        print(f"Wikipedia Summary for {wiki_data['title']}:")
        print(f"{wiki_data['summary']}\n")

    # Print stock data
    print(f"Stock Data for {stock_data['symbol']}:")
    print(f"Current Price: {stock_data['current_price']} USD")
    print(f"Market Cap: {stock_data['market_cap']}")
    print(f"Previous Close: {stock_data['previous_close']} USD\n")

    # Print weather data
    if "error" in weather_data:
        print(weather_data["error"])
    else:
        print(f"Weather in {weather_data['city']}: {weather_data['weather']}\n")

# Call the main function
if __name__ == "__main__":
    main()
