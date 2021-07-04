from user.models import User


class UserService:
    @staticmethod
    def create_user(*, first_name: str, last_name: str, email: str, social_number: str, password: str) -> User:
        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                        is_active=True, social_number=social_number,
                                        username=email, company=None, password=password)
        return user
