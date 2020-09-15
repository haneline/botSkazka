class CodeGenerator:
    from pymongo import MongoClient
    import datetime
    client = MongoClient()
    codes = client.makestorybot.codes

    @staticmethod
    def build_block(size):
        from random import choice
        from string import ascii_letters, digits
        return ''.join(choice(ascii_letters + digits) for _ in range(size))

    def __init__(self, client=True):
        if not client:
            import threading
            watcher = threading.Thread(target=self.code_watcher, args=(), daemon=True)
            watcher.start()

    def code_add(self):
        generated_code = self.build_block(8)
        while self.codes.count_documents({'code': generated_code}) != 0:
            generated_code = self.build_block(8)
        one_code = {'code': generated_code, 'expired': self.datetime.datetime.now() + self.datetime.timedelta(days=3)}
        self.codes.insert_one(one_code)
        return generated_code

    def code_watcher(self):
        from time import sleep
        while True:
            self.codes.delete_many({'expired': {'$lte': self.datetime.datetime.now()}})
            sleep(60)

    def code_use(self, one_code):
        if self.codes.delete_one({'code': one_code}).deleted_count > 0:
            return True
        return False

if __name__ == '__main__':
    Generator = CodeGenerator(client=False)
    print(Generator.build_block(20))
    # Generator.code_add()



#time.sleep(10)

#
# two = codes.find()
# for one in codes.find({'code': 'V4H8OpvI'}):
#     print(one['expired'] - datetime.datetime.now())
#
# codes.insert_one(one_code)
