import requests
"""Методы для проверки ответов запросов"""

class Checking():

    """Метод для проверки статус-кода"""

    @staticmethod
    def check_status_code(response, status_code):
        assert status_code == response.status_code, 'ОШИБКА, Статус-код не совпадает'
        print("Успешно!!! Статус код = " + str(response.status_code))

    """Метод для наличия полей в ответе запроса"""
    @staticmethod
    def check_json_token(response, expected_value):
        token = response.json()
        assert list(token) == expected_value
        print ("Все поля присутствуют")

    """Метод для проверки значений обязательных полей"""

    @staticmethod
    def check_json_value(response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верен!!!")

    @staticmethod
    def check_json_search_json_in_value(response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        assert search_word in check_info
        print(field_name + " есть в ответе!!!")