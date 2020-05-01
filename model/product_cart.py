from random import randint

import faker


from common.constans import SIZE


class ProductCart:
    def __init__(self, count=1, size=None, color=None):
        self.count = count
        self.size = size
        self.color = color

    @staticmethod
    def random_cart_data():
        fake = faker.Faker()
        random_size_count = randint(0, len([SIZE]))
        return ProductCart(count=fake.pyint(1, 10),
                           size=SIZE[random_size_count])
