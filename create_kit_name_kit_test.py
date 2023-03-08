import sender_stand_request
import data




# эта функция меняет значения в параметре kit_name
def get_kit_body(kit_name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.kit_body.copy()
    # изменение значения в поле kit_name
    current_body["name"] = kit_name
    # возвращается новый словарь с нужным значением kit_name
    return current_body


#Функция для позитивной проверки
def positive_assert(kit_name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(kit_name)
    # В переменную kit_response сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_client_kit(kit_body)


    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверяется, что имя в ответе совпадает с именем в запросе
    assert kit_response.json()["name"] == kit_body["name"]



#Функция для негативной проверки
def negative_assert_code_400(kit_name):
    kit_body = get_kit_body(kit_name)
    response = sender_stand_request.post_new_client_kit(kit_body)

    assert response.status_code == 400





#Тест 1. Успешное создание набора
#Параметр kit_name состоит из 1 символа
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


#Тест 2. Успешное создание набора
#Параметр kit_name состоит из 511 символа
def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda")


#Тест 3. Ошибка. Параметр kit_name содержит символов меньше допустимого (0)
def test_create_kit_0_letters_in_name_get_error_response():
    negative_assert_code_400("")


#Тест 4. Ошибка. Параметр kit_name содержит символов больше допустимого (512)
def test_create_kit_512_letters_in_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab")


#Тест 5. Успешное создание набора
#Параметр kit_name состоит из английских букв
def test_create_kit_english_letters_in_name_get_success_response():
    positive_assert("QWErty")


#Тест 6. Успешное создаение набора
#Параметр kit_name состоит из русских букв
def test_create_kit_russian_letters_in_name_success_response():
    positive_assert("Мария")


#Тест 7. Успешное создание набора
#Параметр kit_name содержит спецсимволы
def test_create_kit_special_characters_in_name_success_response():
    positive_assert("№%@,")


# Тест 8. Успешное создание набора
# Параметр kit_name позволяет использовать пробелы
def test_create_kit_spaces_in_name_success_response():
    positive_assert("Человек и КО")


# Тест 9. Успешное создание набора
# Параметр kit_name содержит цифры
def test_create_kit_nummbers_in_name_success_response():
    positive_assert("123")

#Тест 10. Ошибка. Параметр kit_name не передан в запросе
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)

#Тест 11. Ошибка. Передан другой тип параметра (число)
def test_create_kit_type_name_get_error_response():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400