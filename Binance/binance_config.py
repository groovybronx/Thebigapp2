
class BinanceConfig:
    def __init__(self):
        self.api_key = ""
        self.api_secret = ""
        self.testnet = False

    def load_config(self, filename="binance_config.txt"):
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
                self.api_key = lines[0].strip()
                self.api_secret = lines[1].strip()
                self.testnet = lines[2].strip().lower() == "true"
        except FileNotFoundError:
            print("Config file not found. Using default settings.")
        except IndexError:
            print("Incomplete config file. Using default settings.")

    def save_config(self, filename="binance_config.txt"):
        with open(filename, "w") as f:
            f.write(self.api_key + "\n")
            f.write(self.api_secret + "\n")
            f.write(str(self.testnet) + "\n")

if __name__ == '__main__':
    config = BinanceConfig()
    config.load_config()
    print(f"API Key: {config.api_key}")
    print(f"API Secret: {config.api_secret}")
    print(f"Testnet: {config.testnet}")

    # Example of how to modify and save the config
    config.api_key = "YOUR_NEW_API_KEY"
    config.api_secret = "YOUR_NEW_API_SECRET"
    config.testnet = True
    config.save_config()
    print("Config saved.")
