class AccountManager:
    from pymongo import MongoClient
    import datetime
    client = MongoClient()
    users = client.makestorybot.users

    def user_add(self, user_firstname, user_surname, user_id):
        one_user = {'_id': user_id, 'firstname': user_firstname, 'surname': user_surname, 'activated': False,
                    'time_registration': self.datetime.datetime.now()}
        self.users.insert_one(one_user)

    def user_activate
if __name__ == '__main__':
    Manager = AccountManager()
