from funcs import Genrate_Password  # keep your class name for now

def Main():
    length = int(input('Enter the length of the password: '))
    use_upper = input('Do you want to use uppercase letters? (y/n): ').lower() == 'y'
    use_digits = input('Do you want to use digits? (y/n): ').lower() == 'y'
    use_special = input('Do you want to use special characters? (y/n): ').lower() == 'y'

    generator = Genrate_Password(length, use_upper, use_digits, use_special)
    f_pass = generator.generate_password()
    print(f'Generated password: {f_pass}')

    save = input('Do you want to save the password to a file? (y/n): ').strip().lower() == 'y'
    if save:
        print(generator.save_Password(f_pass))

if __name__ == '__main__':
    Main()
