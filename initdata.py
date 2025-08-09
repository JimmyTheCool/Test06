# initialize data to be stored in files, pickles, shelves

# records
Bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
Sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
Tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}
James = {'name': 'James Bond2', 'age': 35, 'pay': 50000, 'job': 'spy'}
Joe = {'name':'Joe Shaw'}

# database
db = {}
db['bob'] = Bob
db['sue'] = Sue
db['tom'] = Tom
db['james'] = James
db['joe'] = Joe

if __name__ == '__main__': # when run as a script
    for key in db:
        print(key, '=>\n ', db[key])