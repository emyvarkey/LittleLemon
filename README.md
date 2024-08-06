# LittleLemon
Coursera Capstone Project
Booking tables 
    http://127.0.0.1:8000/restaurant/booking/tables/
    sample request JSON for POST: 
    {
        "name": "Arya",
        "booking_date": "2024-08-08",
        "no_of_guests": 5
    }

Registration:
    POST
    http://127.0.0.1:8000/auth/users/
    {
        "email": "dj@littlelemon.com",
        "username": "Deloris",
        "password": "Del123#1"
    }


AuthTokenGeneration:
    http://127.0.0.1:8000/auth/token/login
    {
        "password": "Deloris",
        "username": "Del123#1"
    }

Menu API:
    POST,GET
    http://127.0.0.1:8000/restaurant/menu
    sample request JSON for POST:
    {
        "title": "Pizza",
        "price": 20.00,
        "inventory": 15
    }

    PATCH,PUT,DELETE
    http://127.0.0.1:8000/restaurant/menu/15

    Get users:
    http://127.0.0.1:8000/auth/users/