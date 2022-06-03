# Dokumentasi API

Cara pemanggilan API:

```url
https://api-items-manager.herokuapp.com/{endpoint}
```

Example:
```url
https://api-items-manager.herokuapp.com/items/1/
```

 Return example:

 ```json
 {
    "id": 1,
    "name": "Apple Gel",
    "description": "Menambah HP 30%",
    "price": "300.00",
    "owner": 1
}
 ```

List Endpoint:

- api/register/ (POST)
- api/login/ (POST)
- api/logout/ 🔐 (DELETE)
- api/items/ (GET)
- api/items/ 🔐 (POST)
- api/items/<int:id>/ (GET)
- api/items/<int:id>/ 🔐 (PUT, DELETE)
- api/users/ (GET)
- api/users/<int:id>/ (GET)
  
🔐 Wajib menggunakan Authorization token pada header. Token didapatkan pada login menggunakan akun yang telah di-register

Header Attribute:

```json
"Authorization": "Token {token}"
```

Example:

```json
"Authorization": "Token 6043bfb4f53e03382cebf6c38729b702f70eac8f"
```

## Endpoint

### (POST) api/register/

Deskripsi:

```text
Melakukan registrasi pengguna.
```

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

### (POST) api/login/

Deskripsi:

```text
Melakukan pembuatan/pengambilan token untuk auntentifikasi pengguna.
```

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

Deskripsi:

```text
Melakukan penghapusan token yang dimiliki oleh pengguna.
```

Return Example:

```json
{
    "detail": "Token Deleted Successfully"
}
```

---

### (GET) api/items/

Deskripsi:

```text
Mengambil list seluruh item yang telah disimpan oleh semua pengguna.
```

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

Deskripsi:

```text
Melakukan penambahan item.
```

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

### (GET) api/items/<int:id>/

Deskripsi:

```text
Mengambil data suatu item pada id tertentu.
```

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

### (PUT) api/items/<int:id>/ 🔐

Deskripsi:

```text
Melakukan perubahan data suatu item pada id tertentu.
```

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

### (DELETE) api/items/<int:id>/ 🔐

Deskripsi:

```text
Menghapus data suatu item pada id tertentu.
```

Example:

```url
https://api-items-manager.herokuapp.com/api/items/5/
```

Return example:

```json
1
```

---

### (GET) api/users/

```text
Mengambil data seluruh user terdaftar.
```

Example:

```url
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

Deskripsi:

```text
Mengambil data suatu user pada id tertentu.
```

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
