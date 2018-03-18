import hashlib
import re


valid_domains = ['@vicdoz.com']
class User:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.validate_user_has_all_fields()

    def validate_user_has_all_fields(self):
        if self.email is None:
            raise Exception("Empty email")
        if self.password is None:
            raise Exception("Empty password")

    def validate_email(self):
        is_valid = True
        for domain in valid_domains:
            regexp = re.compile(domain)
            if not regexp.search(self.email):
                raise Exception("Not allowed")
        return is_valid
