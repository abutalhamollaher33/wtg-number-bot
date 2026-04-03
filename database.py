import pymongo
from pymongo import MongoClient

# Database connection
class Database:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client['wtg_number_bot']

    def add_user(self, user_data):
        self.db.users.insert_one(user_data)

    def get_user(self, user_id):
        return self.db.users.find_one({'_id': user_id})

    def add_country(self, country_data):
        self.db.countries.insert_one(country_data)

    def get_country(self, country_code):
        return self.db.countries.find_one({'code': country_code})

    def add_number(self, number_data):
        self.db.numbers.insert_one(number_data)

    def get_number(self, number_id):
        return self.db.numbers.find_one({'_id': number_id})

    def add_otp(self, otp_data):
        self.db.otps.insert_one(otp_data)

    def get_otp(self, otp_id):
        return self.db.otps.find_one({'_id': otp_id})

    def close(self):
        self.client.close()