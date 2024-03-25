from bs4 import BeautifulSoup
import requests
from form_filling_bot import FormFiller

# Google form url
google_form_url = "https://forms.gle/MDDa9paPRBt2nWkj7"
zillow_url = "https://appbrewery.github.io/Zillow-Clone/"

# Scrape the listings
listings_page = requests.get(zillow_url).text
soup = BeautifulSoup(listings_page, "html.parser")

# Obtain the links
list_of_listings_links = []
[list_of_listings_links.append(soup.find_all("a", class_="property-card-link")[link_id]["href"]) for link_id in
 range(len(soup.find_all("a", class_="property-card-link")))]

# Obtain the prices
list_of_listings_prices = []
for price_id in range(len(soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine"))):
    price_current = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")[price_id].text

    # Some prices come with fiddly bits, like + or bd, gotta rmv these
    price_current = price_current.replace("+", "")
    price_current = price_current.replace(" 1 bd", "")
    price_current = price_current.replace(" 1bd", "")
    list_of_listings_prices.append(price_current.split("/")[0])

# Obtain the addresses
list_of_listings_addresses = []
for add_id in range(len(soup.find_all("address"))):
    # Ensure proper formatting (remove the line breaks and the multiple spaces
    address_current = ' '.join(soup.find_all("address")[add_id].text.replace("\n", "").split())
    list_of_listings_addresses.append(address_current)

# Fill out forms using the scraped information with Selenium. Initialise
form_filler_bot = FormFiller()

# Call the function, passing in the scraped info
form_filler_bot.fill_out_form(
    form_url=google_form_url,
    links_list=list_of_listings_links,
    prices_list=list_of_listings_prices,
    addresses_list=list_of_listings_addresses
)
