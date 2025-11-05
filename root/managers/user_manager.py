from sqlalchemy import func, select, delete, update
from sqlalchemy.orm import Session

from models import Review, User


class UserManager:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str, email: str) -> User:
        user = User(name=name, email=email)
        self.session.add(user)
        self.session.commit()
        return user

    def get(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)

    def get_all(self):
        return self.session.execute(select(User)).scalars().all()

    def get_user_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        return self.session.execute(stmt).scalar_one_or_none()

    def get_most_active_users(self, limit=5):
        stmt = select(Review.user_id, func.count(Review.id).label("review_count")) \
            .group_by(Review.user_id) \
            .order_by(func.count(Review.id).desc()) \
            .limit(limit)
        return self.session.execute(stmt).all()

    def update(self, user_id: int, update_data: dict) -> User:
        self.session.execute(
            update(User).where(User.id == user_id).values(update_data)
        )
        self.session.commit()
        return self.get(user_id)

    def delete(self, user_id: int) -> bool:
        result = self.session.execute(
            delete(User).where(User.id == user_id)
        )
        self.session.commit()
        return result.rowcount > 0

    def verify_user(self, user_id: int) -> User:
        self.session.execute(
            update(User).where(User.id == user_id).values(is_verified=True)
        )
        self.session.commit()
        return self.get(user_id)