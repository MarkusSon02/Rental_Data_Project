import requests
import pandas as pd
import json
import functions

# API endpoint for Edmonton (city_id=2)
url = "https://www.rentfaster.ca/api/search.json"
params = {
    "proximity_type": "location-city",
    "novacancy": "0",
    "city_id": "2",
    "limit": 10000,
}

response = requests.get(url, params=params)
data = response.json()

functions.upload_data(data, 'Edmonton', 'rental-data-son')



# with open("rental_data_test.json", 'w') as file:
#     json.dump(data, file)

# # Extract listings
# listings = data.get("listings", [])
# print("Number of listings: ", len(listings))

# # Transform into a DataFrame
# df = pd.DataFrame(listings)

# # Create full URLs for each listing
# df["full_url"] = "https://www.rentfaster.ca" + df["link"]

# # Show a few sample entries
# print(df[["title", "price", "bedrooms", "sq_feet", "full_url"]].head(3))
# print(df.loc[0, "full_url"])

# df.to_csv("rental_data_Edmonton.csv")
# print("Successfully saved in CSV file")