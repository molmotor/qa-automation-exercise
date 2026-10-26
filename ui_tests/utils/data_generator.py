from faker import Faker

fake = Faker()


def generate_user():
    return {
        "password": fake.password(),
        "birthday": "15",
        "birthmonth": "5",
        "birthyear": "1995",
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "country": "Canada",
        "mobilenumber": fake.phone_number(),
        "address": fake.street_address(),
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),
    }