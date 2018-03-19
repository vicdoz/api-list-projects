import re

valid_domains = ['@vicdoz.com']


class User:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.validate_user_has_all_fields()
        self.validate_email()

    def validate_user_has_all_fields(self):
        if self.email is None:
            raise Exception("Empty email")
        if self.password is None:
            raise Exception("Empty password")

    def validate_email(self):
        is_valid = False
        for domain in valid_domains:
            regexp = re.compile(domain)
            if not regexp.search(self.email):
                raise UserException("Not allowed domain for this user")
        return is_valid


class UserException(Exception):
    pass
