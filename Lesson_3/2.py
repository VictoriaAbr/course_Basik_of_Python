name = input('Ваше имя: ')
surname = input('Ваша фамилия: ')
year_of_b = int(input('Ваш год рождения: '))
city = input('Ваш город: ')
email = input('Ваш email: ')
phone_numb = int(input('Ваш телеофн: '))

def user (name, surname, year_of_b, city, email, phone_numb):
    print(f'Вы - {name} {surname}, {year_of_b} года рождения, живете в городе {city}, ваш email - {email}, ваш телефон {phone_numb}')

user(name, surname, year_of_b, city, email, phone_numb)