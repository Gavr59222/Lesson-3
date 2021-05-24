def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Pupkin', name='Vasiliy', year='2000', city='New York', email='error@mail.us',
              telephone='937-99-92'))
