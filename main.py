from fastapi import FastAPI, HTTPException, status

from models.db import db
from models.models import Sheep

app = FastAPI(title="Sheep Compendium")


@app.get("/sheep/{sheep_id}", response_model=Sheep)
def get_sheep_by_id(sheep_id: int) -> Sheep:
    sheep = db.get_sheep(sheep_id)
    if sheep is None:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return sheep


@app.get("/sheep", response_model=list[Sheep])
def get_all_sheep() -> list[Sheep]:
    return db.get_all_sheep()


@app.post("/sheep", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def create_sheep(sheep: Sheep) -> Sheep:
    try:
        return db.add_sheep(sheep)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.put("/sheep/{sheep_id}", response_model=Sheep)
def update_sheep(sheep_id: int, sheep: Sheep) -> Sheep:
    if sheep_id != sheep.id:
        raise HTTPException(status_code=400, detail="Path ID must match body ID")
    updated = db.update_sheep(sheep_id, sheep)
    if updated is None:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return updated


@app.delete("/sheep/{sheep_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheep(sheep_id: int) -> None:
    deleted = db.delete_sheep(sheep_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Sheep not found")
