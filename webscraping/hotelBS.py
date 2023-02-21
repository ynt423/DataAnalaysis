import requests
from bs4 import BeautifulSoup
""" To be continued """
# send a GET request to the website and get the response
response = requests.get("https://www.trip.com/hotels/list?city=New+York+City")

# parse the response using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# find the cheapest hotel
hotels = soup.find_all("div", class_="hotel-item")
cheapest_hotel = hotels[0]
name = cheapest_hotel.find("h3").text
price = cheapest_hotel.find("div", class_="price").text

# print the name and price of the cheapest hotel
print(name + ": " + price)
