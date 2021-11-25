from blog import db
from blog.models import Publication, User

db.create_all()

p1 = Publication(author="Ted_Mosby", post_title="Не друзья.",
                 post_txt="Но мы не друзья! Мы два человека, которые притворяются друзьями потому, "
                          "что было бы неудобно не быть ими.",
                 publication_date="24.11.2021", tags="#друзья #цитата #джейсонстетхем")
p2 = Publication(author="Barney_Stinson", post_title="Ложь",
                 post_txt="Ложь — это прекрасная история, которую портят правдой.",
                 publication_date="24.11.2021", tags="#ложь #цитата #джейсонстетхем")
p3 = Publication(author="Robin_Sherbatsky", post_title="Пугающее будущее",
                 post_txt="Будущее действительно пугает, но нельзя возвращаться в прошлое просто потому, что там тебе "
                          "все знакомо. Возможность заманчивая, но… Так нельзя.",
                 publication_date="24.11.2021", tags="#будущее #цитата #джейсонстетхем")
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)

u1 = User(username="Ted_Mosby", age=30, register_date="24.11.2021")
u2 = User(username="Barney_Stinson", age=33, register_date="24.11.2021")
u3 = User(username="Robin_Sherbatsky", age=29, register_date="24.11.2021")

db.session.add(u1)
db.session.add(u2)
db.session.add(u2)

db.session.commit()


