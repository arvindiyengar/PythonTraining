
configuration = {
    "DEV": {
        "Database": {
            "host": "10.10.10.10",
            "port": 3306,
            "username": "sampleUser",
            "password": "password"
        },
        "Smtp": {
            "host": "smtp.com",
            "port": 25,
            "usename": "user",
            "password": "password"
        }
    },
    "Prod": {
        "Database": {
            "host": "10.10.10.10",
            "port": 3306,
            "username": "prodUser",
            "password": "Prod"
        },
        "Smtp": {
            "host": "prod.smtp.com",
            "port": 25,
            "usename": "prod",
            "password": "prodPassword"
        }
    },
    "Stage": {
        "Database": {
            "host": "10.10.10.10",
            "port": 3306,
            "username": "stageUser",
            "password": "password"
        },
        "Smtp": {
            "host": "stage.smtp.com",
            "port": 25,
            "usename": "stageUser",
            "password": "stagePassword"
        }
    },

}
