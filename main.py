import sqlalchemy as sq

from datetime import datetime

from sqlalchemy.orm import  sessionmaker

from models import create_tables, Publisher, Shop, Book, Stock, Sale


def main():

    login = 'postgres'
    password = 'postgres'
    name_base = 'lesson_4'
    server = 'localhost'
    port = '5432'

    DSN = f'postgresql://{login}:{password}@{server}:{port}/{name_base}'
    engine = sq.create_engine(DSN)

    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    #введем какие-нибудь данные
    #издатель
    p1 = Publisher(name = 'Канн')
    p2 = Publisher(name = 'Манн')

    #магазин
    s1 = Shop(name = 'Инвис')
    s2 = Shop(name = 'Центральный')

    #книги
    b1 = Book(title = 'Анна Каренина', publisher =p1)
    b2 = Book(title = '12 стульев', publisher =p2)

    #продажи

    st1 = Stock(count = 1, book = b1, shop = s1)
    st2 = Stock(count = 1, book = b2, shop = s2)

    sl1 = Sale(price = 100, date_sale = "2018-10-25T09:45:24.552Z", count = 1, stock = st1)
    sl2 = Sale(price = 200, date_sale = "2018-10-25T09:45:24.552Z", count = 1, stock = st2)


    session.add_all([p1,p2,s1,s2,b1,b2,st1,st2,sl1,sl2])
    session.commit()

    name_publisher = input("Введите имя издателя: ")

    for c in session.query(Publisher).filter(Publisher.name == name_publisher).all():
        print(c)

    session.close()

if __name__ == '__main__':
    main()

