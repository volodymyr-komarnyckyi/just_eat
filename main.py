import re

from just_eat_client.client import JustEatClient


def validate_postcode(postcode: str):
    pattern = r"^([A-Za-z][A-Ha-hJ-Yj-y]?[0-9][A-Za-z0-9]? ?[0-9][A-Za-z]{2}|[Gg][Ii][Rr] ?0[Aa]{2})$"

    if len(postcode) < 4:
        pattern = r"^\w{1,2}\d{1,2}"

    if not re.match(pattern, postcode):
        return False
    return True


if __name__ == '__main__':
    client = JustEatClient()
    while True:
        postcode = input("Enter postal code: ")
        if validate_postcode(postcode=postcode):
            break
        print("Please enter valid postal code")
    restaurants = client.by_post_code(postcode)
    for restaurant in restaurants:
        print(restaurant)
