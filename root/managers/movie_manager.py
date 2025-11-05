from sqlalchemy import select, func, update, delete
from sqlalchemy.orm import Session

from models import Movie, Genre, Review


class MovieManager:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, title: str, release_year: int) -> Movie:
        movie = Movie(title=title, release_year=release_year)
        self.session.add(movie)
        self.session.commit()
        return movie

    def get(self, movie_id: int) -> Movie | None:
        return self.session.get(Movie, movie_id)

    def get_all(self):
        return self.session.execute(select(Movie)).scalars().all()

    def add_genre(self, movie_id: int, genre: Genre) -> Movie:
        movie = self.get(movie_id)
        movie.genres.append(genre)
        self.session.commit()
        return movie

    def get_reviews(self, movie_id: int):
        stmt = select(Review).where(Review.movie_id == movie_id)
        return self.session.execute(stmt).scalars().all()

    def get_average_rating(self, movie_id: int):
        stmt = select(func.avg(Review.rating)).where(Review.movie_id == movie_id)
        return self.session.execute(stmt).scalar()

    def update(self, movie_id: int, update_data: dict) -> Movie:
        self.session.execute(
            update(Movie).where(Movie.id == movie_id).values(update_data)
        )
        self.session.commit()
        return self.get(movie_id)

    def delete(self, movie_id: int) -> bool:
        result = self.session.execute(
            delete(Movie).where(Movie.id == movie_id)
        )
        self.session.commit()
        return result.rowcount > 0

    def remove_genre(self, movie_id: int, genre: Genre) -> Movie:
        movie = self.get(movie_id)
        movie.genres.remove(genre)
        self.session.commit()
        return movie

    def get_top_movies_by_rating(self, limit: int = 10) -> list[tuple]:  # Join & Aggregation & Sort
        return self.session.execute(
            select(Movie, func.avg(Review.rating).label("average_rating"))
            .join(Review, Review.movie_id == Movie.id)
            .group_by(Movie.id)
            .order_by(func.avg(Review.rating).desc())
            .limit(limit)
        ).all()

    def get_movies_by_genre(self, genre_name: str) -> list[Movie]:
        return self.session.execute(
            select(Movie).join(Movie.genres).filter(Genre.name == genre_name)
        ).scalars().all()

    def get_top_rated_movies_by_genre(self):  # Join & Group by & Sort
        return self.session.execute(
            select(
                Genre.name,
                Movie.title,
                func.avg(Review.rating).label("average_rating")
            )
            .join(Movie.genres)
            .join(Review)
            .group_by(Genre.name, Movie.title)
            .order_by(Genre.name, func.avg(Review.rating).desc())
        ).all()
