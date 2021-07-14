from user.models import User


class AddUser:

    def add(self, *, email: str, first_name: str, last_name: str, password: str, social_number: str) -> User:
        user = User(
            username=email,
            first_name=first_name,
            last_name=last_name,
            social_number=social_number,
            email=email
        )
        user.set_password(raw_password=password)
        user.save()

        return user

