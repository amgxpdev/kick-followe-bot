import tls_client
from datetime import datetime

session = tls_client.Session(
    client_identifier="chrome112",
    random_tls_extension_order=True
)

res = session.get(
    "https://kick.com/kick-token-provider",
    headers={
        "accept": "application/json",
        "accept-encoding": "gzip",
        "accept-language": "de_DE",
        "connection": "Keep-Alive",
        "content-type": "application/json",
        "host": "kick.com",
        "if-modified-since": datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT"),
        "user-agent": "okhttp/4.9.2"
    },
)

response_data = res.json()
name_field = response_data.get('nameFieldName')
encrypted_valid_from = response_data.get('encryptedValidFrom')

email = input("Email/Username: ")
password = input("Password: ")

session = tls_client.Session(
    client_identifier="chrome112",
    random_tls_extension_order=True
)


rus = session.post(
    "https://kick.com/mobile/login",
    headers={
        "accept": "application/json",
        "accept-encoding": "gzip",
        "connection": "Keep-Alive",
        "content-type": "application/json",
        "host": "kick.com",
        "user-agent": "okhttp/4.9.2"
    },
    json={
        "email": "{}".format(email),
        "password": "{}".format(password),
        name_field: "",
        "_kick_token_valid_from": encrypted_valid_from,
        "isMobileRequest": True
    },
)

response_data = rus.json()
token = response_data.get('token')
print(token)


ref = session.post(
    "https://kick.com/api/v2/channels/uwuw/follow",
    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip",
        "accept-language": "de_DE",
        "authorization": "Bearer {}".format(token),
        "connection": "Keep-Alive",
        "content-length": "0",
        "content-type": "application/json",
        "host": "kick.com",
        "user-agent": "okhttp/4.9.2"
    },
)

response_data = ref.json()
print(response_data)