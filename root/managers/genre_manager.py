from sqlalchemy import select, delete, func
from sqlalchemy.orm import Session

from models import *


class GenreManager:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str) -> Genre:
        genre = Genre(name=name)
        self.session.add(genre)
        self.session.commit()
        return genre

    def get(self, genre_id: int) -> Genre | None:
        return self.session.get(Genre, genre_id)

    def get_all(self):
        return self.session.execute(select(Genre)).scalars().all()

    def get_genre_by_name(self, name: str) -> Genre | None:
        return self.session.execute(
            select(Genre).where(Genre.name == name)
        ).scalar_one_or_none()

    def update(self, genre_id: int, new_name: str) -> Genre:
        genre = self.get(genre_id)
        genre.name = new_name
        self.session.commit()
        return genre

    def delete(self, genre_id: int) -> bool:
        result = self.session.execute(
            delete(Genre).where(Genre.id == genre_id)
        )
        self.session.commit()
        return result.rowcount > 0

    def get_genres_with_most_movies(self) -> list[tuple]:
        return self.session.execute(
            select(Genre, func.count(MovieGenre.movie_id).label("movie_count"))
            .join(MovieGenre, MovieGenre.genre_id == Genre.id)
            .group_by(Genre.id)
            .order_by(func.count(MovieGenre.movie_id).desc())
        ).all()