# demo-morfis


export HOST=http://localhost:8000

# Логин
curl -s -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}' $HOST/api/v1/auth/token/ | json_pp


export ACCESS_TOKEN=###ACCESS_TOKEN###
export REFRESH_TOKEN=###REFRESH_TOKEN###

# Показать пользователей
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" $HOST/api/v1/auth/users/ | json_pp

# Обновить токен
curl -s -X POST -H "Content-Type: application/json" -d '{"refresh":"'$REFRESH_TOKEN'"}' $HOST/api/v1/auth/refresh/ | json_pp