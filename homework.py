class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

    def set_access_level(self, access_level):
        self._access_level = access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')

    def add_user(self, user_list, user):
        if self.get_access_level() == 'admin':
            user_list.append(user)
        else:
            print("Доступ запрещен. Только администраторы могут добавлять пользователей.")

    def remove_user(self, user_list, user_id):
        if self.get_access_level() == 'admin':
            for user in user_list:
                if user.get_user_id() == user_id:
                    user_list.remove(user)
                    break
        else:
            print("Доступ запрещен. Только администраторы могут удалять пользователей.")


# Пример использования

# Создание списка пользователей
user_list = []

# Создание обычных пользователей
user1 = User(1, "Иван Иванов")
user2 = User(2, "Петр Петров")

# Создание администратора
admin1 = Admin(3, "Анна Админова")

# Добавление пользователей через администратора
admin1.add_user(user_list, user1)
admin1.add_user(user_list, user2)

# Вывод списка пользователей
print("Список пользователей:")
for user in user_list:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

# Удаление пользователя через администратора
admin1.remove_user(user_list, 1)

# Вывод списка пользователей после удаления
print("\nПосле удаления пользователя с ID 1:")
for user in user_list:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")
