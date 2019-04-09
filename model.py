import requests


class Person(object):
    def __init__(self, name=None, email=None, phone=None, website=None):
        self.full_name = name
        self.email = email
        self.phone = phone
        self.website = website
        self.first_name, self.last_name = name.split(' ', 1)

    def contact_info(self):
        return self.full_name + ' || ' + self.email + ' || ' + self.phone

    @classmethod
    def getAll(self):
        database = requests.get('https://jsonplaceholder.typicode.com/users')
        result = []
        json_list = database.json()
        for item in json_list:
            person = Person(
                item['name'], item['email'],
                item['phone'], item['website']
            )
            result.append(person)
        return result
