from libgravatar import Gravatar
from sqlalchemy.orm import Session

from src.database.models import User
from schemas import UserModel


async def get_user_by_email(email: str, db: Session) -> User:
    """
    get user by email.

    :param email: Data for the created contact.
    :type email: str
    :param db: The database session.
    :type db: Session
    :return: Get user by email.
    :rtype: User
    """
    return  db.query(User).filter(User.email == email).first()


async def check_role(role: str, db: Session) -> User:
    return db.query(User).filter(User.role == role).first()
    


async def create_user(body: UserModel, db: Session) -> User:
    avatar = None
    
    try:
        g = Gravatar(body.email)
        avatar = g.get_image()
    except Exception as e:
        print(e)

    if db.query(User).count() == 0:   
        role = 'admin'
    else:
        role = 'user'
        
    new_user = User(**body.model_dump(), avatar=avatar, role=role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_token(user: User, token: str | None, db: Session) -> None:
    user.refresh_token = token
    db.commit()


async def confirmed_email(email: str, db: Session) -> None:
    user = await get_user_by_email(email, db)
    user.confirmed = True
    db.commit()


async def update_avatar(email: str, url: str, db: Session) -> User:
    """
        Update the avatar URL for a user.

        :param email: The email address of the user whose avatar is to be updated.
        :type email: str
        :param url: The new avatar URL.
        :type url: str
        :param db: The database session.
        :type db: Session
        :return: The user with the updated avatar URL.
        :rtype: User
    """
    user = await get_user_by_email(email, db)
    user.avatar = url
    db.commit()
    return user