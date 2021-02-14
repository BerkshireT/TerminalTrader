from binance.client import Client
import Keys
import Notifs

# Test email notifs
def main():
   print("SNEDING MESSAGE")
   Notifs.send("Test", "Testing notifications. Success!")
   print("MESSAGE SENT")

if __name__ == "__main__":
   main()

# Setup client
#client = Client(Keys.BINANCE_API, Keys.BINANCE_SECRET)