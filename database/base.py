
class data_base:
    def __init__(self):
        # self.data = {
        #     'Куртка': 5000,
        #     'Худи': 3000,
        #     'Кепка': 1500,
        #     'Футболка': 1000,
        #     'Джинсы': 5000,
        # }
        self.data = [
            {'name': 'Куртка',
                'price': 5000,
                'color': 'Красный'
            },
            {'name': 'Худи',
             'price': 3000,
             'color': 'Зеленый'
             },
            {'name': 'Кепка',
             'price': 1500,
             'color': 'Синий'
             },
            {'name': 'Футболка',
             'price': 1000,
             'color': 'Белый'
             },
            {'name': 'Джинсы',
             'price': 5000,
             'color': 'Черный'
             },
        ]

    def get_data(self):
        return self.data
