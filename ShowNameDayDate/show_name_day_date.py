import requests
import re

class ShowNameDay():

    country_codes = [
        "at",
        "bg",
        "cz",
        "de",
        "dk",
        "ee",
        "es",
        "fi",
        "fr",
        "gr",
        "hr",
        "hu",
        "it",
        "lt",
        "lv",
        "pl",
        "ru",
        "se",
        "sk",
        "us",
    ]
    URL = "https://nameday.abalin.net/api/V1/getname"

    def __init__(self):
        self.name = input("Please enter your name: ")
        self.country = input("Please enter your country code: ")
        if self.country not in self.country_codes:
            print(f"Please provide supported country code from list: \
{self.country_codes}")
        self.find_date()

    def find_date(self):
        url = f"?name={self.name}&country={self.country}"
        result = requests.get(self.URL + url)
        for i in result.json()["0"]:
            name = re.findall(rf"\b{self.name}\b", i["name"], flags=re.IGNORECASE)
            if name:
                print(f"Date of your name day is: {i['day']}.{i['month']} ({i['name']})")

if __name__ == "__main__":
    ShowNameDay()