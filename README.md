# Morfis auth demo

Демо api token авторизации.

Для запуска достаточно выполнить
```docker-compose up --build```

Проект запустится по http://localhost:80/


Доступны следующие адреса:

http://localhost/api/v1/auth/token/

http://localhost/api/v1/auth/refresh/

http://localhost/api/v1/auth/users/

Порядок авторизации такой:
Делаем POST запрос по адресу [auth/token/](). В нагрузке нужно указать логин/пароль.

```export HOST=http://localhost```
*(сохраняем хост в env переменные linux shell'a)*

```curl -s -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}' $HOST/api/v1/auth/token/ | json_pp```

В ответ получим access и refresh токены.

Access токен короткоживущий - его мы прикладываем к каждому нашему запросу к бекенду.

Refresh токен живет долго - при помощи него мы можем обновить access токен.

Для тестировния настроенно, что токены протухают через 5 и 10 минут соответственно.

```export ACCESS_TOKEN=###ACCESS_TOKEN###```

```export REFRESH_TOKEN=###REFRESH_TOKEN###```

*(сохраняем пролученнные токены)*

Для общения с сервером мы к каждому нашему запросу прикладываем заголовок вида ```Authorization: Bearer $ACCESS_TOKEN```.
В демке для этого пока реализован только один эндпоинт: [auth/users/]().
В ответ получим список из 3х тестовых пользователей. Поскольку пользователей может быть много - предположу что их хорошобы выдавать постранично.

```curl -s -H "Authorization: Bearer $ACCESS_TOKEN" $HOST/api/v1/auth/users/ | json_pp```

По истечении 5 минут access токен протухнет и нужно будет его обновить. Для этого делаем POST запрос на [auth/refresh/]() с нагрузкой в виде refresh токена:

```curl -s -X POST -H "Content-Type: application/json" -d '{"refresh":"'$REFRESH_TOKEN'"}' $HOST/api/v1/auth/refresh/ | json_pp```

Если и refresh токен уже протух, то нужно будет пройти всю процедуру получения токенов заного.