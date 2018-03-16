import hashlib
import re


class User:
    email = None
    password = None
    password_hash = None

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.validate_user_has_all_fields()

    def validate_user_has_all_fields(self):
        if self.email is None:
            raise Exception("Empty email")
        if self.password is None:
            raise Exception("Empty password")

    def register(self):
        regexp = re.compile(r'@vicdoz.com')
        if not regexp.search(self.email):
            raise Exception("Not allowed")
