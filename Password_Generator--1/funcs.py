import random, string

class Genrate_Password:
    def __init__(self, length=12, use_upper=True, use_Digits=True, use_Special=True):
        self.length = length
        self.use_upper = use_upper
        self.use_Digits = use_Digits
        self.use_Special = use_Special

    def generate_password(self):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase if self.use_upper else ''
        digits = string.digits if self.use_Digits else ''
        special = string.punctuation if self.use_Special else ''

        pool = lower + upper + digits + special
        if not pool:
            return 'Error: No characters to choose from'  # or raise ValueError

        password = ''.join(random.choice(pool) for _ in range(self.length))
        return password

    def save_Password(self, password):
        with open('password.txt', 'a', encoding='utf-8') as file:
            file.write(password + '\n')
        return 'Password saved to password.txt'
