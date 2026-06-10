# BAD practice
# class Bird:
#     def fly(self):
#         return "Я лечу!"


# class Ostrich(Bird):
#     def fly(self):
#         # Порушення принципу: нащадок ламає базову логіку суперкласу!
#         raise NotImplementedError("Страуси не літають")


# def make_bird_fly(bird: Bird):
#     return bird.fly()


class Bird:
    def eat(self):
        return "Я їм"


class FlyingBird(Bird):
    def fly(self):
        return "Я лечу!"


class Ostrich(Bird):
    # Тепер страус не зобов'язаний вміти літати
    pass
