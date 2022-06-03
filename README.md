# Dokumentasi API

Happy Lucky Smile Yay!

Header Attribute:
```json
"Authorization": "Token {token}"
```
Example:
```json
"Authorization": "Token 6043bfb4f53e03382cebf6c38729b702f70eac8f"
```

## Endpoint

---

### (POST) api/login/

Body JSON file

```json
{
    "username": "string",
    "password": "string"
}
```

Example:
```json
{
    "username": "creditfool",
    "password": "rahasia"
}
```
Return example:
```json
{
    "token": "6043bfb4f53e03382cebf6c38729b702f70eac8f",
    "email": "bichlasulbulqiah@gmail.com",
    "username": "creditfool"
}
```
---
### (DELETE) api/logout/ 🔐

Pastikan sudah melakukan login untuk mendapatkan token terlebih dahulu!

Return Example:
```json
{
    "detail": "Token Deleted Successfully"
}
```
---
### (POST) api/register/
Body JSON file:
```json
{
    "username": "string",
    "email": "string",
    "password": "string"
}
```
example:
```json
{
    "username": "foobar",
    "email": "foobar@barfoo.bar",
    "password": "foofoofoo"
}
```
return example:
```json
{
    "id": 3,
    "username": "foobar",
    "email": "foobar@barfoo.bar"
}
```
---
### (GET) api/items/
Return Example:
```json
[
    {
        "id": 1,
        "name": "Apple Gel",
        "description": "Menambah HP 30%",
        "price": "300.00",
        "owner": 1
    },
    {
        "id": 2,
        "name": "Orange Gel",
        "description": "Menambah MP 30%",
        "price": "600.00",
        "owner": 1
    },
    {
        "id": 3,
        "name": "Lemon Gel",
        "description": "Menambah MP 60%",
        "price": "1000.00",
        "owner": 1
    }
]
```
---
### (POST) api/items/ 🔐
Body JSON file:
```json
{
    "name": "string",
    "description": "string",
    "price": "float"
}
```
example:
```json
{
    "name": "Phoenix Down",
    "description": "Hidupin teman",
    "price": "1000.00"
}
```
return example:
```json
{
    "id": 4,
    "name": "Phoenix Down",
    "description": "Hidupin teman",
    "price": "1000.00",
    "owner": 2
}
```
---
### (GET) api/items/id/
Example:
```
https://api-items-manager.herokuapp.com/api/items/4/
```
Return example:

```json
{
    "id": 4,
    "name": "Phoenix Down",
    "description": "Hidupin teman",
    "price": "1000.00",
    "owner": 2
}
```

---

### (PUT) api/items/id/ 🔐

Body JSON file:
```json
{
    "name": "string",
    "description": "string",
    "price": "float"
}
```
example:
```json
{
    "name": "Phoenix Down",
    "description": "Membangkitkan teman dengan HP 50%",
    "price": "2000.00"
}
```
return example:
```json
{
    "id": 4,
    "name": "Phoenix Down",
    "description": "Membangkitkan teman dengan HP 50%",
    "price": "2000.00",
    "owner": 2
}
```
---
### (DELETE) api/items/id/ 🔐
Example:
```
https://api-items-manager.herokuapp.com/api/items/5/
```
Return example:
```json
1
```
---
### (GET) api/users/
Example:
```
https://api-items-manager.herokuapp.com/api/users/
```
Return example:
```json
[
    {
        "id": 1,
        "username": "creditfool",
        "items": [
            1,
            2,
            3
        ]
    },
    {
        "id": 2,
        "username": "manusia",
        "items": [
            4
        ]
    },
    {
        "id": 3,
        "username": "foobar",
        "items": []
    }
]
```
---

### (GET) api/users/<int:id>/
Example:
```
https://api-items-manager.herokuapp.com/api/users/1/
```
Return example:
```json
{
    "id": 1,
    "username": "creditfool",
    "items": [
        1,
        2,
        3
    ]
}
```
---
