import base64
import binascii

from rest_framework import HTTP_HEADER_ENCODING
from rest_framework.authentication import get_authorization_header

from apps.payments.paylov.credentials import get_credentials


def authentication(request) -> bool:
    auth = get_authorization_header(request).split()
    if not auth or auth[0].lower() != b"basic":
        return False
    
    if len(auth) != 2:
        return False
    
    try:
        auth_parts = (
            base64.b64decode(auth[1]).decode(HTTP_HEADER_ENCODING).partition(":")
        )
    except(TypeError, UnicodeDecodeError, binascii.Error):
        return False
    
    print(auth_parts)
    
    username, password = auth_parts[0], auth_parts[2]
    credentials = get_credentials()

    paylov_username = credentials["PAYLOV_USERNAME"]
    paylov_password = credentials["PAYLOV_PASSWORD"]

    return username == paylov_username and password == paylov_password