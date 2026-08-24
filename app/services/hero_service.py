from fastapi import HTTPException
from sqlmodel import Session, select

from app.models.hero import Hero


def create_hero(session: Session, hero: Hero) -> Hero:
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero


def get_heroes(session: Session) -> list[Hero]:
    return session.exec(select(Hero)).all()


def get_hero(session: Session, hero_id: int) -> Hero:
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


def update_hero(session: Session, hero_id: int, hero: Hero) -> Hero:
    hero_db = session.get(Hero, hero_id)
    if not hero_db:
        raise HTTPException(status_code=404, detail="Hero not found")
    hero_db.name = hero.name
    hero_db.age = hero.age
    hero_db.secret_name = hero.secret_name
    session.add(hero_db)
    session.commit()
    session.refresh(hero_db)
    return hero_db


def delete_hero(session: Session, hero_id: int) -> dict:
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"message": "Hero deleted successfully"}
