from binance.client import Client
import Keys
import Notifs

# Test email notifs
def main():
   Notifs.send("Testing notifications. Success!")

if __name__ == "__main__":
   main()

# Setup client
#client = Client(Keys.BINANCE_API, Keys.BINANCE_SECRET)