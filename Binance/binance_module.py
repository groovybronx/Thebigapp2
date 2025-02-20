
import tkinter as tk
from tkinter import ttk
from binance.client import Client
from binance.enums import SIDE_BUY, SIDE_SELL, ORDER_TYPE_MARKET
from binance_config import BinanceConfig  # Import the config class

class BinanceGUI:
    def __init__(self, master):
        self.master = master
        master.title("Binance API Interface")

        self.config = BinanceConfig()
        self.config.load_config()

        self.api_key = tk.StringVar(value=self.config.api_key)
        self.api_secret = tk.StringVar(value=self.config.api_secret)
        self.testnet = tk.BooleanVar(value=self.config.testnet)

        # API Key Label and Entry
        self.api_key_label = ttk.Label(master, text="API Key:")
        self.api_key_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.api_key_entry = ttk.Entry(master, textvariable=self.api_key, width=40)
        self.api_key_entry.grid(row=0, column=1, sticky=tk.E, padx=5, pady=5)

        # API Secret Label and Entry
        self.api_secret_label = ttk.Label(master, text="API Secret:")
        self.api_secret_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.api_secret_entry = ttk.Entry(master, textvariable=self.api_secret, width=40, show="*")
        self.api_secret_entry.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

        # Testnet Checkbutton
        self.testnet_check = ttk.Checkbutton(master, text="Testnet", variable=self.testnet)
        self.testnet_check.grid(row=2, column=0, columnspan=2, pady=5)

        # Save Config Button
        self.save_config_button = ttk.Button(master, text="Save Configuration", command=self.save_configuration)
        self.save_config_button.grid(row=3, column=0, columnspan=2, pady=5)

        # Connect Button
        self.connect_button = ttk.Button(master, text="Connect to Binance", command=self.connect_to_binance)
        self.connect_button.grid(row=4, column=0, columnspan=2, pady=5)

        # Status Label
        self.status_label = ttk.Label(master, text="Status: Not connected")
        self.status_label.grid(row=5, column=0, columnspan=2, pady=5)

        self.client = None

    def save_configuration(self):
        self.config.api_key = self.api_key.get()
        self.config.api_secret = self.api_secret.get()
        self.config.testnet = self.testnet.get()
        self.config.save_config()
        self.status_label.config(text="Status: Configuration saved")

    def connect_to_binance(self):
        api_key = self.api_key.get()
        api_secret = self.api_secret.get()
        testnet = self.testnet.get()

        try:
            if testnet:
                self.client = Client(api_key, api_secret, testnet=True)
            else:
                self.client = Client(api_key, api_secret)

            # Test connection
            self.client.ping()
            self.status_label.config(text="Status: Connected to Binance")
        except Exception as e:
            self.status_label.config(text=f"Status: Connection failed - {e}")

def main():
    root = tk.Tk()
    gui = BinanceGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
