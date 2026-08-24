from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database.session import get_session
from app.models.hero import Hero
from app.services import hero_service

router = APIRouter(
    prefix="/heroes",
    tags=["Heroes"]
)

@router.post("/")
def create_hero(
    hero: Hero,
    session: Session = Depends(get_session)
):
    return hero_service.create_hero(session, hero)


@router.get("/")
def read_heroes(
    session: Session = Depends(get_session)
):
    return hero_service.get_heroes(session)


@router.get("/debug/{hero_id}")
def read_hero(
    hero_id: int,
    session: Session = Depends(get_session)
):
    print("INSIDE HERO ROUTE")
    return hero_service.get_hero(session, hero_id)


@router.put("/{hero_id}")
def update_hero(
    hero_id: int,
    hero: Hero,
    session: Session = Depends(get_session)
):
    return hero_service.update_hero(session, hero_id, hero)


@router.delete("/{hero_id}")
def delete_hero(
    hero_id: int,
    session: Session = Depends(get_session)
):
    return hero_service.delete_hero(session, hero_id)
