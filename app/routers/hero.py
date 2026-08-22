from fastapi import APIRouter, Depends,HTTPException
from sqlmodel import Session, select
from app.database import Hero, get_session

router = APIRouter(
    prefix="/heroes",
    tags=["Heroes"]
)

@router.post("/")
def create_hero(
    hero: Hero,
    session: Session = Depends(get_session)
):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero

@router.get("/")
def read_heroes(
    session: Session = Depends(get_session)
):
    heroes = session.exec(
        select(Hero)
    ).all()

    return heroes

@router.get("/{hero_id}")
def read_hero(
    hero_id: int,
    session: Session = Depends(get_session)
):
    hero = session.get(
        Hero,
        hero_id
    )
    if not hero:
        raise HTTPException(
            status_code=404,
            detail="Hero not found"
        )

    return hero

@router.put("/{hero_id}")
def update_hero(
    hero_id: int,
    hero: Hero,
    session: Session = Depends(get_session)
):
    hero_db = session.get(
        Hero,
        hero_id
    )
    if not hero_db:
        raise HTTPException(
            status_code=404,
            detail="Hero not found"
        )

    hero_db.name = hero.name
    hero_db.age = hero.age
    hero_db.secret_name = hero.secret_name
    session.add(hero_db)
    session.commit()
    session.refresh(hero_db)
    return hero_db

@router.delete("/{hero_id}")
def delete_hero(
    hero_id: int,
    session: Session = Depends(get_session)
):
    hero = session.get(
        Hero,
        hero_id
    )
    if not hero:
        raise HTTPException(
            status_code=404,
            detail="Hero not found"
        )
    session.delete(hero)
    session.commit()
    return {
        "message": "Hero deleted successfully"
    }