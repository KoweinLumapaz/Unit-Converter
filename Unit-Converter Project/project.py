import csv
import tkinter as tk
from tkinter import ttk, messagebox
import requests

def main():
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("700x600")
        self.root.configure(bg='#f0f0f0')

        self.Lmultiply_conversions = read_conversions("LMultiply.csv")
        self.Ldivide_conversions = read_conversions("LDivide.csv")
        self.Wmultiply_conversions = read_conversions("WMultiply.csv")
        self.Wdivide_conversions = read_conversions("WDivide.csv")

        self.CURRENCY_API_KEY = 'fca_live_E8SjEc3ALFtJblyGrwOwxLTGO2Qlo3vuz4ULdBMN'
        self.currency_rates = None

        self.current_category = tk.StringVar(value="")

        self.components()
        self.get_currency()

    def get_currency(self):
        try:
            url = f'https://api.freecurrencyapi.com/v1/latest?apikey={self.CURRENCY_API_KEY}&base_currency=PHP&currencies=PHP%2CEUR%2CUSD%2CJPY'
            response = requests.get(url)
            if response.status_code == 200:
                self.currency_rates = response.json()['data']
            else:
                messagebox.showwarning("API Error", "Cannot get currency")
        except Exception as e:
            messagebox.showerror(" Error", str(e))

    def components(self):

        tk.Label(self.root, text="Welcome to Unit Converter",font=('Arial', 18, 'bold'), bg='#f0f0f0',pady=5).pack()
        tk.Label(self.root, text="Please Select a Category",font=('Arial', 14, 'italic'), bg='#f0f0f0',pady=10).pack()

        category = tk.Frame(self.root, bg='#f0f0f0',pady=10)
        category.pack()

        categories = [
            ("Length", "length"),
            ("Weight", "weight"),
            ("Temperature", "temperature"),
            ("Currency", "currency")
        ]

        button_style = {
            'font': ('Arial', 14, 'bold'),
            'width': 15,
            'bg': '#e0e0e0',
            'activebackground': '#c0c0c0'
        }

        for text, value in categories:
            btn = tk.Button(category, text=text, command=lambda v=value: self.select_category(v), **button_style)
            btn.pack(side=tk.LEFT, padx=5)

        self.unit_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.unit_frame.pack(pady=10)

        tk.Label(self.root, text="Enter Value", font=('Arial', 12), bg='#f0f0f0').pack()
        self.value_entry = tk.Entry(self.root, font=('Arial', 15), justify='center', bd=1, relief='solid')
        self.value_entry.pack(pady=5)

        convert_bttn = tk.Button(self.root, text="Convert", command=self.convert_units, font=('Arial', 12, 'bold'),bg='#4CAF50', fg='white')
        convert_bttn.pack(pady=10)

        self.dis_result = tk.StringVar()
        result_label = tk.Label(self.root, textvariable=self.dis_result, font=('Arial', 12, 'bold'), bg='#f0f0f0')
        result_label.pack(pady=10)

    def select_category(self, category):
        for widget in self.unit_frame.winfo_children():
            widget.destroy()

        self.current_category = category

        if category == 'length':
            units = ['mm', 'cm', 'm', 'km']
            self.value_entry.delete(0, tk.END)
            self.dis_result.set("")
        elif category == 'weight':
            units = ['mg', 'g', 'kg', 't']
            self.value_entry.delete(0, tk.END)
            self.dis_result.set("")
        elif category == 'temperature':
            units = ['C', 'F', 'K']
            self.value_entry.delete(0, tk.END)
            self.dis_result.set("")
        elif category == 'currency':
            units = ['PHP', 'EUR', 'USD', 'JPY']
            self.value_entry.delete(0, tk.END)
            self.dis_result.set("")
        else:
            return

        self.select_units(units)

    def select_units(self, units):
        tk.Label(self.unit_frame, text="From Unit", font=('Arial', 12), bg='#f0f0f0').grid(row=0, column=0, padx=10)
        self.from_unit_var = tk.StringVar()
        from_Units = ttk.Combobox(self.unit_frame, textvariable=self.from_unit_var, values=units, font=('Arial', 12), state='readonly')
        from_Units.grid(row=1, column=0, padx=10)
        from_Units.current(0)

        tk.Label(self.unit_frame, text="To Unit", font=('Arial', 12), bg='#f0f0f0').grid(row=0, column=1, padx=10)
        self.to_unit_var = tk.StringVar()
        to_Units = ttk.Combobox(self.unit_frame, textvariable=self.to_unit_var, values=units, font=('Arial', 12), state='readonly')
        to_Units.grid(row=1, column=1, padx=10)
        to_Units.current(1)

    def convert_units(self):
        if not self.current_category:
            messagebox.showerror("Error", "Please select a category")
            return

        try:
            value = float(self.value_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
            self.value_entry.delete(0, tk.END)
            return

        category = self.current_category
        from_unit = self.from_unit_var.get()
        to_unit = self.to_unit_var.get()

        try:
            if category == 'length':
                result = self.convert_length(value, from_unit, to_unit)
            elif category == 'weight':
                result = self.convert_weight(value, from_unit, to_unit)
            elif category == 'temperature':
                result = self.convert_temperature(value, from_unit, to_unit)
            elif category == 'currency':
                result = self.convert_currency(value, from_unit, to_unit)
            else:
                messagebox.showerror("Error", "Invalid category")
                return

            self.dis_result.set(f"{value} {from_unit} = {result:.4f} {to_unit}")

        except Exception as e:
            messagebox.showerror("Conversion Error", str(e))

    def convert_length(self, value, from_unit, to_unit):
        if (from_unit, to_unit) in self.Lmultiply_conversions:
            return multiply_units(value, from_unit, to_unit, self.Lmultiply_conversions)

        if (from_unit, to_unit) in self.Ldivide_conversions:
            return divide_units(value, from_unit, to_unit, self.Ldivide_conversions)

        raise ValueError("Conversion not available")


    def convert_weight(self, value, from_unit, to_unit):
        if (from_unit, to_unit) in self.Wmultiply_conversions:
            return multiply_units(value, from_unit, to_unit, self.Wmultiply_conversions)

        if (from_unit, to_unit) in self.Wdivide_conversions:
            return divide_units(value, from_unit, to_unit, self.Wdivide_conversions)

        raise ValueError("Conversion not available")


    def convert_temperature(self, value, from_unit, to_unit):
        if from_unit == 'C' and to_unit == 'F':
            if value < -273.15:
                raise ValueError("Temperature should not below absolute zero")
            return (value * 9 / 5) + 32
        elif from_unit == 'C' and to_unit == 'K':
            if value < -273.15:
                raise ValueError("Temperature should not below absolute zero")
            return value + 273.15
        elif from_unit == 'F' and to_unit == 'C':
            if value < -459.67:
                raise ValueError("Temperature should not below absolute zero")
            return (value - 32) * 5 / 9
        elif from_unit == 'F' and to_unit == 'K':
            if value < -459.67:
                raise ValueError("Temperature should not below absolute zero")
            return ((value - 32) * 5 / 9) + 273.15
        elif from_unit == 'K' and to_unit == 'C':
            if value < 0:
                raise ValueError("Temperature should not below absolute zero")
            return value - 273.15
        elif from_unit == 'K' and to_unit == 'F':
            if value < 0:
                raise ValueError("Temperature should not below absolute zero")
            return ((value - 273.15) * 9 / 5) + 32
        raise ValueError("Conversion not available")

    def convert_currency(self, value, from_unit, to_unit):

        if not self.currency_rates:
            raise ValueError("Sorry, currency not available.")

        php_value = value / self.currency_rates[from_unit]
        converted_value = php_value * self.currency_rates[to_unit]

        return converted_value


def read_conversions(file_name):
    conversions = {}
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = (row['From'], row['To'])
            conversions[key] = float(row['Convert'])
    return conversions

def multiply_units(value, from_unit, to_unit, conversions):
    key = (from_unit, to_unit)
    if key in conversions:
        return value * conversions[key]
    return None

def divide_units(value, from_unit, to_unit, conversions):
    key = (from_unit, to_unit)
    if key in conversions:
        return value / conversions[key]
    return None


if __name__ == "__main__":
    main()