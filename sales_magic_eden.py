import tweepy
import requests
import os

from dotenv import load_dotenv

load_dotenv()

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth)

# Set up a loop to check the Magic Eden API for NFT sales
while True:
    # Query the Magic Eden API for recent NFT sales
    response = requests.get("https://api.magiceden.io/v1/nft/sales")
    if response.status_code == 200:
        # Parse the response and extract the information we need
        nft_sales = response.json()
        for sale in nft_sales:
            # Tweet about the sale using the Twitter API
            api.update_status(
                f"An NFT was just sold on Magic Eden for {sale['price']}! "
                f"Check it out here: {sale['nft_url']}"
            )
    # Wait a few minutes before checking for more NFT sales
    time.sleep(60 * 5)
