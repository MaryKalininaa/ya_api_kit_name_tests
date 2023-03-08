import configuration
import requests
import data

#эта функция создает нового пользоватлея
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставялем полный url
                         json=body,  # тут тело
                          headers=data.headers)  # а здесь заголовки

response = post_new_user(data.user_body);


print(response.status_code)
print(response.json()["authToken"])

#тут в переменную auth_token сохраняем результат созданного пользователя, а именно его authToken
auth_token = response.json()["authToken"]


#эта функция создает набор авторизированному пользователю
def post_new_client_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_CLIENT_KIT_PATH,
                         json=body,
                         headers={
                             "Content-Type": "application/json",
                             "Authorization": "Bearer " + auth_token
                         })

response = post_new_client_kit(data.kit_body);


print(response.status_code)
print(response.json())