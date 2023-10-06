from just_eat_client.client import JustEatClient

if __name__ == "__main__":
    client = JustEatClient()
    postcode = input("Enter postal code: ")
    restaurants = client.by_post_code(postcode)
    print(restaurants)
