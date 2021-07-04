import jwt
from rest_framework.exceptions import ValidationError, AuthenticationFailed

from config.settings import REFRESH_TOKEN_SECRET
from user.selectors import find_user_by_username, find_user_by_id
from util.auth import generate_access_token, generate_refresh_token


class AuthenticationService:
    @staticmethod
    def get_token(*, username: str, password: str):
        user = find_user_by_username(username=username)
        if user is None or not user.check_password(password):
            raise ValidationError('User not found or wrong password')
        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)
        response = dict(
            access_token=access_token,
            user=user,
            refresh_token=refresh_token
        )
        return response

    @staticmethod
    def update_token(*, refresh_token: str):
        try:
            payload = jwt.decode(
                refresh_token, REFRESH_TOKEN_SECRET, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed(
                'expired refresh token, please login again.')
        user = find_user_by_id(id=payload.get('user_id'))
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.is_active:
            raise AuthenticationFailed('user is inactive')

        response = dict(access_token=generate_access_token(user))
        return response
