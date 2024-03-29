class decorator:
    """
    Декоратор дескриптор.
    При декорировании функции или метода класса
    происходит следующий порядок внутренних вызовов:
        1. Для методов классов:
            decorator.__get__() -> wrapper.__call__() -> decorator.__call__()
        2. Для функций:
            decorator.__call__()
    """

    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        # def wrapper(*args, **kwargs):
            # return self(instance, *args, **kwargs)
        # return wrapper
        return wrapper(self, instance)


class wrapper:
    """
    Обертка, которая использует дескриптор.
    Конструктор класса получает дескриптор - экземпляр декоратора
    и экземпляр декорируемого объекта.
    """

    def __init__(self, descriptor, subject) -> None:
        self.desc = descriptor
        self.subj = subject

    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)
