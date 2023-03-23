import secrets


def generate_token() -> str:
    return secrets.token_urlsafe(4)[:6]
