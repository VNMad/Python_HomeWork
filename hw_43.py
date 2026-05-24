#____________________________________________________________________
#1. Добавление товаров
#____________________________________________________________________
from pymongo import MongoClient, errors


class ProductsDatabase:
    PRODUCTS = [
        {
            'name': 'Pen',
            'price': 1.50,
            'stock': 300
        },
        {
            'name': 'Notebook',
            'price': 3.99,
            'stock': 120
        },
        {
            'name': 'Backpack',
            'price': 25.00,
            'stock': 50
        }
    ]

    def __init__(self, collection):
        self.collection = collection

    def clear_collection(self):
        self.collection.delete_many({})

    def add_products(self):
        return self.collection.insert_many(self.PRODUCTS)


def main():
    try:
        client = MongoClient(
            "mongodb://ich_editor:verystrongpassword"
            "@mongo.itcareerhub.de/?readPreference=primary"
            "&ssl=false&authMechanism=DEFAULT"
            "&authSource=ich_edit"
        )
        client.admin.command('ping')
        db = client['ich_edit']
        products_collection = db['products_121225_ptm_vnmad']
        products_database = ProductsDatabase(products_collection)
        products_database.clear_collection()
        result = products_database.add_products()
        print(f'{len(result.inserted_ids)} Products inserted.')
        client.close()

    except errors.ConnectionFailure:
        print('MongoDB connection error.')

    except errors.OperationFailure:
        print('MongoDB operation error(wrong authorization).')

    except errors.PyMongoError as e:
        print(f'MongoDB error: {e}')


if __name__ == '__main__':
    main()

#____________________________________________________________________
#2. Увеличение цен
#____________________________________________________________________
from pymongo import MongoClient, errors


class ProductsDatabase:
    PRODUCTS = [
        {
            'name': 'Pen',
            'price': 1.50,
            'stock': 300
        },
        {
            'name': 'Notebook',
            'price': 3.99,
            'stock': 120
        },
        {
            'name': 'Backpack',
            'price': 25.00,
            'stock': 50
        }
    ]

    def __init__(self, collection):
        self.collection = collection

    def add_products(self):
        return self.collection.insert_many(self.PRODUCTS)

    def update_prices(self):
        return self.collection.update_many(
            {},
            {'$mul': {'price': 1.2}}
        )

    def get_products(self):
        return list(self.collection.find())

    def products_exist(self):
        return self.collection.count_documents({}) > 0


def format_products(products):
    result = ['\nProducts list:']
    for product in products:
        result.append(f"- {product['name']} - ${product['price']:.2f}")
    return '\n'.join(result)


def menu():
    while True:
        try:
            print('1. Update prices')
            print('2. Show products')
            choice = int(input('Choose action: '))
            if choice in (1, 2):
                return choice
            raise ValueError
        except ValueError:
            print('Invalid menu number.')


def main():
    try:
        client = MongoClient(
            "mongodb://ich_editor:verystrongpassword"
            "@mongo.itcareerhub.de/?readPreference=primary"
            "&ssl=false&authMechanism=DEFAULT"
            "&authSource=ich_edit"
        )

        client.admin.command('ping')
        db = client['ich_edit']
        products_collection = db['products_121225_ptm_vnmad']
        products_database = ProductsDatabase(products_collection)
        if not products_database.products_exist():
            products_database.add_products()
        choice = menu()

        if choice == 1:
            result = products_database.update_prices()
            print(f'Prices updated for {result.modified_count} products.')
        print(format_products(products_database.get_products()))
        client.close()

    except errors.ConnectionFailure:
        print('MongoDB connection error.')
    except errors.OperationFailure:
        print('MongoDB operation error(wrong authorization).')
    except errors.PyMongoError as e:
        print(f'MongoDB error: {e}')


if __name__ == '__main__':
    main()