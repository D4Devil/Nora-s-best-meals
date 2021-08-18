import json
import connector

class Entity():
    def __init__(self, *args, **kwargs) -> None:
        pass


    def dump(self) -> json:
        return json.dumps(self.__dict__)


    def get_all(self):
        pass


    def get(name):
        pass


    def save():
        pass


    def update():
        pass


    def delete():
        pass


class Dish(Entity):
    def __init__(self, name: str, description: str) -> None:
        if name == None or description == None:
            raise Exception("Name nor Description should be empty")
        
        self.name = name
        self.description = description


if __name__ == '__main__':
    dish = Dish(name="Soup", description="It's just delicious")
    print(dish.dump())