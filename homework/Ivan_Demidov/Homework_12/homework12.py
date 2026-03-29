# 1. Базовый класс
class Flower:
    def __init__(self, name, color, stem_length, freshness, cost, lifetime):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness
        self.cost = cost
        self.lifetime = lifetime

    def __repr__(self):
        return f"{self.name}({self.color}, " f"{self.cost}руб)"


# 2. Дочерние классы
class Rose(Flower):
    def __init__(self, color, stem_length, freshness, cost):
        super().__init__(
            "Роза", color, stem_length, freshness, cost, lifetime=7
        )


class Tulip(Flower):
    def __init__(self, color, stem_length, freshness, cost):
        super().__init__(
            "Тюльпан", color, stem_length, freshness, cost, lifetime=5
        )


class Chamomile(Flower):
    def __init__(self, color, stem_length, freshness, cost):
        super().__init__(
            "Ромашка", color, stem_length, freshness, cost, lifetime=10
        )


# 3. Класс Букет
class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def get_cost(self):
        return sum(flower.cost for flower in self.flowers)

    def get_wilting_time(self):
        if not self.flowers:
            return 0
        return sum(f.lifetime for f in self.flowers) / len(self.flowers)

    def sort_flowers(self, by="cost"):
        if by == "cost":
            self.flowers.sort(key=lambda f: f.cost)
        elif by == "freshness":
            self.flowers.sort(key=lambda f: f.freshness)
        elif by == "stem_length":
            self.flowers.sort(key=lambda f: f.stem_length)
        elif by == "color":
            self.flowers.sort(key=lambda f: f.color)

    def find_flowers(self, **kwargs):
        result = []
        for flower in self.flowers:
            match = True
            for key, value in kwargs.items():
                if getattr(flower, key, None) != value:
                    match = False
                    break
            if match:
                result.append(flower)
        return result

    def print_bouquet(self):
        print(f"Букет ({len(self.flowers)} цветов):")
        for flower in self.flowers:
            print(
                f"  {flower.name}, {flower.color}, "
                f"{flower.stem_length}см, свежесть:{flower.freshness}, "
                f"{flower.cost}руб, {flower.lifetime}дней"
            )
        print(f"Стоимость: {self.get_cost()}руб")
        print(f"Время увядания: {self.get_wilting_time():.1f} дней")


# 4. Создаём букет
bouquet = Bouquet()
bouquet.add_flower(Rose("красный", 40, 8, 100))
bouquet.add_flower(Rose("белый", 45, 9, 120))
bouquet.add_flower(Tulip("жёлтый", 30, 7, 50))
bouquet.add_flower(Tulip("красный", 35, 8, 60))
bouquet.add_flower(Chamomile("белый", 20, 6, 30))

# 5. Тестируем методы
print("=== Исходный букет ===")
bouquet.print_bouquet()

print("\n=== Сортировка по стоимости ===")
bouquet.sort_flowers(by="cost")
bouquet.print_bouquet()

print("\n=== Поиск красных цветов ===")
red_flowers = bouquet.find_flowers(color="красный")
print(f"Найдено: {len(red_flowers)} красных цветов")
for f in red_flowers:
    print(f"  {f.name}")

print("\n=== Поиск по свежести > 7 ===")
fresh_flowers = [f for f in bouquet.flowers if f.freshness > 7]
print(f"Найдено: {len(fresh_flowers)} свежих цветов")
