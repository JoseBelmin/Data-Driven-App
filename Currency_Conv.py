from tkinter import Tk, ttk, Frame, Label, Button, Entry
from PIL import Image, ImageTk
import json
import requests

class CurrencyCompanion(Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")
        self.geometry("414x590")
        self.configure(bg="#212529")
        self.resizable(width=False, height=False)

        self.colors = {
            "C1": "#FF9F1C",  # Orange
            "C2": "#FFBF69",  # Light Orange
            "C3": "#FFFFFF",  # White
            "C4": "#212529",  # Space Gray
            "C5": "#CBF3F0",  # Mint Green
            "C6": "#2EC4B6",  # Teal
        }

        self.create_frames()
        self.create_widgets()

    def create_frames(self):
        self.top_frame = Frame(self, width=414, height=120, bg=self.colors["C6"])
        self.top_frame.grid(row=0, column=0)

        self.main_frame = Frame(self, width=414, height=784, bg=self.colors["C4"])
        self.main_frame.grid(row=1, column=0)

    def create_widgets(self):
        self.create_banner()
        self.create_result_label()
        self.create_currency_comboboxes()
        self.create_value_entry()
        self.create_convert_button()

    def create_banner(self):
        icon = Image.open('Images\Coin_Guy.png')
        icon = icon.resize((100, 100))
        icon = ImageTk.PhotoImage(icon)
        self.iconphoto(False, icon)

        banner = Label(self.top_frame, image=icon, compound="left", text="Currency Converter", font="arial 20 bold",
                       fg=self.colors["C4"], bg=self.colors["C6"], height=5, padx=5, pady=50, anchor="center")
        banner.place(x=0, y=0)

    def create_result_label(self):
        self.result_label = Label(self.main_frame, text=" ", font="inter 16", fg=self.colors["C4"], bg=self.colors["C1"],
                                  width=25, height=5, pady=7, anchor="center")
        self.result_label.place(x=50, y=50)

    def create_currency_comboboxes(self):
        currency = ['EUR', 'USD', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK', 'NOK',
                    'HRK', 'RUB', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'ILS', 'INR', 'KRW', 'MXN', 'PHP',
                    'SGD', 'THB', 'ZAR']
        currency.sort()

        from_label = Label(self.main_frame, text="From", font="inter 13 bold", fg=self.colors["C6"], bg=self.colors["C4"],
                           width=8, height=1, pady=0, relief="flat", anchor="nw")
        from_label.place(x=50, y=225)

        self.from_combo = ttk.Combobox(self.main_frame, width=10, justify="center", font="inter 14", state="readonly")
        self.from_combo['values'] = tuple(currency)
        self.from_combo.place(x=50, y=255)

        to_label = Label(self.main_frame, text="To", font="inter 13 bold", fg=self.colors["C6"], bg=self.colors["C4"],
                         width=8, height=1, pady=0, relief="flat", anchor="nw")
        to_label.place(x=222, y=225)

        self.to_combo = ttk.Combobox(self.main_frame, width=10, font="inter 14", state="readonly")
        self.to_combo['values'] = tuple(currency)
        self.to_combo.place(x=222, y=255)

    def create_value_entry(self):
        self.value_entry = Entry(self.main_frame, width=27, justify="center", font="inter 14")
        self.value_entry.place(x=52, y=325)

    def create_convert_button(self):
        button = Button(self.main_frame, command=self.converter, text="Convert", font="inter 14", relief="raised",
                        overrelief="ridge", width=10, height=1, bg=self.colors["C1"], fg=self.colors["C4"])
        button.place(x=142, y=380)

    def converter(self):
        url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
        ccy_1 = self.from_combo.get()
        ccy_2 = self.to_combo.get()
        amt = self.value_entry.get()

        querystring = {"from": ccy_1, "to": ccy_2, "amount": amt}

        ccy_symbol_map = {
            'EUR': '€', 'USD': '$', 'JPY': '¥', 'BGN': 'лв', 'CZK': 'Kč', 'DKK': 'kr', 'GBP': '£', 'HUF': 'Ft',
            'PLN': 'zł', 'RON': 'lei', 'SEK': 'kr', 'CHF': 'Fr', 'ISK': 'Kr', 'NOK': 'kr', 'HRK': 'kn', 'RUB': '₽',
            'TRY': '₺', 'AUD': '$', 'BRL': 'R$', 'CAD': '$', 'CNY': '¥', 'HKD': '$', 'IDR': 'Rp', 'ILS': '₪',
            'INR': '₹', 'KRW': '₩', 'MXN': '$', 'PHP': '₱', 'SGD': '$', 'THB': '฿', 'ZAR': 'R'
        }
        symbol = ccy_symbol_map.get(ccy_2, '')

        headers = {
            "X-RapidAPI-Key": "d9c9a9ce8cmsh36e8be071e6516cp13e109jsn80510aaec594",
            "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = json.loads(response.text)
        converted_amt = data['result']['convertedAmount']
        formatted_amt = symbol + " {:,.2f}".format(converted_amt)

        self.result_label['text'] = formatted_amt
        print(converted_amt, formatted_amt)

if __name__ == "__main__":
    app = CurrencyCompanion()
    app.mainloop()