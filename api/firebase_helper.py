import firebase_admin
from firebase_admin import credentials, db

def helper_function():
    # Store your JSON credentials directly in a Python dictionary
    firebase_cred = {
    "type": "service_account",
    "project_id": "open-insider",
    "private_key_id": "c901a33e0e6ce6551238adf9f0daae0c03ea93f5",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDW0eHoZE1/ko4b\nTivy1R55GCZ58Uj7CJHjd5jMKPS3EyLZxIEuPRa1a88JlKbKLQ1m8kw/M0FlmBFV\nyfoi1j+pDVAFDJdCXJ8Csy6Oy+XnDAz6G+QSs/4+nu9PsTfeOHQli/FrtDJLe/KK\nDQE60Lyl0+6xeQ+ovb4SzHt/1fWjAnGIE/BOA0iDSfiRXbvBiGDucfvauY+C+Hm2\newb4Nb7dWgN7Jy4v6LWNYIjLNdeJpMJBNEhKF1E19NBOHA5z5p0A4mPnucE3gMrq\nyW01cWKykO3CqS1DBmw0qJ24gozBf0j+JHoSXaqOmzo1Mkgz/k0yveihFvbiKdoF\n4+vF803pAgMBAAECggEAE/IW3KH7hB3SbfybHgfltW6lm+roUM6h5RHksQgYeKsh\nMEELkYSAiEXDSmtv9ROry+QxaijTKKCu8102iWeFL6gZxu49WR8KcJC8gOuzo/k9\ndzeBvK7Tq3LMW4Tj4BEzz4yn1M09Yj7W7TR56cEZ0vfTkMzhxFQhwtMToHH4RbM3\n1MqH/YqIYoPObuK1lsH+teYy6yVKFfggJt3F3P+qBfF/cvpHOhcmEKqlo5bEkktq\nJLPuy+IGT6ELedN51nxgN8SrLZXnmbiIVsGZiCpnsF8mdqxQt5mOtsP/AwBKKbtb\nlEu8sWPhWPrFYToTAjatCyPs0PDwkQv3aHP7Rco9VQKBgQDsPygxTbc9R7AGiAdd\ns0qZ1JlhEdBV/d76ZuDNx+0sNHAtzcVWk3QCRYNFOwkcrb8HiTjldFHBMGFWsPCs\nm3K+SFUXeVkzYnr8SGaOFf5Tf7ddDHq6POHz9ns14M+2a4kW83vSWZ6j9Gu2m70S\nNpsTOwqT+BxjwK9g8mJoVsLkAwKBgQDoyBXTccgdBtYxXaQYEozPDohs9JJWykwE\n4roKShe6WVX7WkMUeM5jcDjhh1Kg+56HAkaLm/liryXgZeQAny95vsh+htEV0fzt\ngIWcHTjsf+4aSkeMkIBWvbSsFNCIQHESH+QkwBWeRd75xqoq/0tHBGg8hGM5paRb\nMDlKJMlgowKBgF07A1qJp+GIE+BP+FAy/CK+8pSLGiOFX2SECv1Kg79pJkf9J35m\nDGcFFavRg2QM8RFBRvHOOKE7vX4fr6r+YYbUNrhfzCLqH0zGKaqy5T4AbdVLoncy\npZzITZFSmcYMo/optlipw2BCietzhGbWo9Yv+5mvVUzMcqmYnds9OgYPAoGAXToc\n+6TbFzzwta6iFH4BZL+WRcShgx7b2S0QgyRvYlN7CwJ4UQ+c4NhF/5TZs91x/PId\nXLZn52zsB3XnHZSjR+fvljTaMhn6aQgK+p39eUI3EtJi21nX/GVXoX9okNj2L+MT\n1OAVCGFFTtWQu02pUVTjhjEjKCg9rcOffiFDgW8CgYA/rjqZ5s/2l6jfC5o9CuNX\nEVvgTC+9xZptBciFFwJW9oGGLKDh0ky234jQPbSS8SZOnvsHS8xdpg+pGqWZRmyI\n+ya98/K7bq5t1I/afYE7RXOKZuVKaT1qpGlln5mMSdo4fKN1EwLVzZfKNIahqqGM\ny3l5Pbo5YZQE4qVshFQrCw==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-lgs56@open-insider.iam.gserviceaccount.com",
    "client_id": "103462504657156150913",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-lgs56%40open-insider.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com",
    }

    firebase_config = {
        "apiKey": "AIzaSyD2tGeepolQanvYk7hHdUC0D3dMT7_fZG0",
        "authDomain": "open-insider.firebaseapp.com",
        "databaseURL": "https://open-insider-default-rtdb.firebaseio.com",
        "projectId": "open-insider",
        "storageBucket": "open-insider.appspot.com",
        "messagingSenderId": "436931876090",
        "appId": "1:436931876090:web:f8e3450126b5fc4d7c6543",
        "measurementId": "G-EQ9N777R6Y"
    }

    # Initialize Firebase Admin SDK with the credentials
    cred = credentials.Certificate(firebase_cred)
    firebase_admin.initialize_app(cred, firebase_config)


    # Reference to your Firebase Realtime Database root
    ref = db.reference('/')

    # Read Data
    data = ref.get()
    print("Data from the Firebase Realtime Database:")
    print(data)

    # Write Data
    data_to_write = {
        'example_key2': 'example_value2',
        'another_key2': 'another_value2'
    }

    ref.update(data_to_write)
    print("Data has been written to the Firebase Realtime Database.")
