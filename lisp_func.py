#комменты добавляла нейросеть, как и проверка на ошибки. Чтобы не запутался потом. 

def push_scope(env):
    """Добавляет новый пустой словарь в конец списка окружений."""
    env.append({})


def assign_to_current_scope(env, key, value):
    """Присваивает значение в самой вложенной мапе."""
    if not env:
        raise ValueError("Нет доступных областей видимости")
    env[-1][key] = value


def lookup(env, key):
    """Ищет значение ключа, начиная с самой вложенной мапы."""
    for scope in reversed(env):
        if key in scope:
            return scope[key]
    raise KeyError(f"Переменная {key} не найдена")


def push_scope(env):
    """Добавляет новый пустой словарь в конец списка окружений."""
    env.append({})


def assign_to_current_scope(env, key, value):
    """Присваивает значение в самой вложенной мапе."""
    if not env:
        raise ValueError("Нет доступных областей видимости")
    env[-1][key] = value


def lookup(env, key):
    """Ищет значение ключа, начиная с самой вложенной мапы."""
    for scope in reversed(env):
        if key in scope:
            return scope[key]
    raise KeyError(f"Переменная {key} не найдена")


def head(lst):
    """Возвращает первый элемент списка."""
    if not lst:
        raise ValueError("Нельзя получить head из пустого списка")
    return lst[0]


def tail(lst):
    """Возвращает список без первого элемента."""
    if not lst:
        raise ValueError("Нельзя получить tail из пустого списка")
    return lst[1:]
