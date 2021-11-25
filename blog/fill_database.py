from blog import db
from blog.models import Publication, User

publications = [Publication(
    author="Ted_Mosby",
    post_title="Не друзья.",
    post_txt="Но мы не друзья! Мы два человека, которые притворяются друзьями потому, "
             "что было бы неудобно не быть ими.",
    publication_date="24.11.2021",
    tags="#друзья #detectivemosby"),

    Publication(
        author="Barney_Stinson",
        post_title="Ложь",
        post_txt="Ложь — это прекрасная история, которую портят правдой.",
        publication_date="24.11.2021",
        tags="#ложь #lietogetlaid"),

    Publication(
        author="Robin_Sherbatsky",
        post_title="Пугающее будущее",
        post_txt="Будущее действительно пугает, но нельзя возвращаться в прошлое просто потому, что там тебе "
                 "все знакомо. Возможность заманчивая, но… Так нельзя.",
        publication_date="24.11.2021",
        tags="#будущее #джейсонстетхем #backincanada"),

    Publication(
        author="Marshal_Ericson",
        post_title="Быть вместе — это тяжело",
        post_txt="Быть вместе — это тяжело. Соглашаться, чем-то жертвовать — это всё очень тяжело, но если "
                 "ты с правильным человеком, то это просто... "
                 "Смотря на эту девушку, я знаю, что она все то, что ты хочешь от жизни, что должно быть "
                 "простейшей вещью в мире, но если это не так, то это не та девушка... и мне жаль.",
        publication_date="25.11.2021",
        tags="#отношениия #simplehard"),

    Publication(
        author="Lily_Aldrin",
        post_title="Дорогой Тед",
        post_txt="Тед, дорогуша, выйди, пожалуйста на улицу, найди стену и убейся. Мы подойдем через минуту.",
        publication_date="25.11.2021",
        tags="#тед")
]
users = [
    User(username="Ted_Mosby", age=27, register_date="24.11.2021", email_address="teg@mosby.com",
         password_hash='123' * 20),
    User(username="Barney_Stinson", age=27, register_date="24.11.2021", email_address="barney@stinson.com",
         password_hash='123' * 20),
    User(username="Robin_Sherbatsky", age=26, register_date="24.11.2021", email_address="robin@sherbatsky.com",
         password_hash='123' * 20),
    User(username="Marshal_Ericson", age=27, register_date="25.11.2021", email_address="marshal@ericson.com",
         password_hash='123' * 20),
    User(username="Lily_Aldrin", age=27, register_date="25.11.2021", email_address="lily@aldrin.com",
         password_hash='123' * 20)
]

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    for publication in publications:
        db.session.add(publication)

    for user in users:
        db.session.add(user)

    db.session.commit()
