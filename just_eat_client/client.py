import re

import requests


class JustEatClient:
    BASE_URL = "https://uk.api.just-eat.io/restaurants/bypostcode/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      "AppleWebKit/537.36(KHTML, like Gecko) "
                      "Chrome/117.0.0.0 Safari/537.36"
    }

    @staticmethod
    def _validate_postcode(postcode: str):
        pattern = r"^(GIR 0AA|[A-PR-UWYZ]([0-9]{1,2}|([A-HK-Y][0-9]([0-9ABEHMNPRV-Y])?)|[0-9][A-HJKPS-UW])\ [0-9][ABD-HJLNP-UW-Z]{2})$"  # noqa
        return bool(re.match(pattern, postcode))

    @staticmethod
    def _format_restaurants(restaurants):
        formatted_restaurants = []
        for restaurant in restaurants:
            formatted_restaurant = {
                "Name": restaurant["Name"],
                "Rating": restaurant["Rating"],
                "Cuisines": restaurant["Cuisines"],
            }
            formatted_restaurants.append(formatted_restaurant)
        return formatted_restaurants

    def by_post_code(self, postcode):
        url = f"{self.BASE_URL}{postcode}"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()

            restaurants_data = response.json()
            restaurants = restaurants_data.get("Restaurants")
            formatted_restaurants = self._format_restaurants(restaurants)

            return formatted_restaurants
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to connect to Just Eat API: {e}")
        except ValueError as e:
            raise Exception(f"Failed to parse JSON response: {e}")
