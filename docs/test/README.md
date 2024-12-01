# Тестування працездатності системи

Тестування сервісу проводилося за допомогою застосунку [Postman](https://www.google.com/search?q=postman&rlz=1C1GCEA_enUA1034UA1034&oq=postman&gs_lcrp=EgZjaHJvbWUqCQgAEEUYOxiABDIJCAAQRRg7GIAEMgcIARAAGIAEMgcIAhAAGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgcICBAAGIAEMgcICRAAGIAE0gEIMTA4NGowajeoAgCwAgA&sourceid=chrome&ie=UTF-8).

## Отримання користувача з методом GET
### Успішне отримання усіх користувачів

![1 getall](https://github.com/user-attachments/assets/1b3960f5-797f-4bf5-8cb0-51eabf187e36)


### Успішне отримання одного користувача

![2 get1](https://github.com/user-attachments/assets/657d9a30-44c1-44f5-ba91-592e887d83c5)


### Спроба отримати неіснуючого користувача

![3 get404](https://github.com/user-attachments/assets/dfab8561-3bd9-4549-bc2f-83ec31038295)


## Створення користувача з методом POST
### Успішне створення користувача

![4 post1](https://github.com/user-attachments/assets/5b467ff7-1a00-47e8-8cef-fc6ee58bb2ab)


### Спроба створити користувача з вже існуючими даними

![5 postexist](https://github.com/user-attachments/assets/76757720-c839-4d07-8785-2e3a6dcd8b71)


### Спроба створити користувача без відповідних даних

![6 posterror](https://github.com/user-attachments/assets/7cd533bf-39aa-480d-b4fe-63b590aba041)


## Оновлення користувача з методом PATCH
### Успішне оновлення користувача

![7 patch1](https://github.com/user-attachments/assets/1f988549-ad0a-47d5-9005-3a87bd3bfdf3)


### Оновлення неіснуючого користувача

![8 patcherror](https://github.com/user-attachments/assets/6865851b-b8b3-4a06-8e03-395bcd1d0020)


## Видалення користувача з методом DELETE
### Успішне видалення користувача

![9 delete1](https://github.com/user-attachments/assets/8b9ccbff-b72a-4dcc-9ebe-ca0046a2bc69)


### Видалення неіснуючого користувача

![10 deleteerror](https://github.com/user-attachments/assets/794f24fd-3df4-4fec-b40b-ed4b2872870b)
