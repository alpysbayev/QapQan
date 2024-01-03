import models as mdl
import schemas as sch


class UserConverter:
    @staticmethod
    def to_model(user: sch.UserCreate) -> mdl.User:
        return mdl.User(
            email = user.email,
            username = user.username,
            hashed_password = user.password,
            first_name = user.first_name,
            last_name = user.last_name
        )
    
    @staticmethod
    def to_schema(user: mdl.User) -> sch.User:
        return sch.User(
            id = user.id,
            email = user.email,
            username = user.username,
            first_name = user.first_name,
            last_name = user.last_name,
            is_active = user.is_active
        )