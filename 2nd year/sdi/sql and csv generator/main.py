# This is a sample Python script.
import codecs
import random
import uuid

if __name__ == '__main__':

    #
    # Generate SQL query to add records to the database
    # query = 'INSERT INTO platform VALUES (id, name, active, screen, handheld, size, description)\n'
    query = ''
    values = []

    consoles = [
        'help', 'mobile', 'computer', 'laptop', 'nintendo', 'frog', 'python'
    ]
    for i in range(1000000):
        id = uuid.uuid4()
        name = uuid.uuid4().hex[:10].upper()
        activeUsers = random.randint(15, 90)
        screen = random.choice([True, False])
        handheld = random.choice([True, False])
        size=random.choice([10,20,4])
        description = random.choice(consoles)
        query += str(id)+','+str(name)+','+str(activeUsers)+','+str(screen)+','+str(handheld)+','+str(size)+','+str(description)+'\n'

    with codecs.open("output_csv.csv", "w", "utf-8-sig") as f:
        f.writelines(query)

    print("Done!")
