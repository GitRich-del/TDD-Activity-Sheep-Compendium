from typing import Dict, Optional

from models.models import Sheep


class FakeDB:
    def __init__(self) -> None:
        self._data: Dict[int, Sheep] = {
            1: Sheep(id=1, name="Spice", breed="Gotland", sex="female"),
            2: Sheep(id=2, name="Esther", breed="Border Leicester", sex="female"),
        }

    def get_sheep(self, sheep_id: int) -> Optional[Sheep]:
        return self._data.get(sheep_id)

    def get_all_sheep(self) -> list[Sheep]:
        return list(self._data.values())

    def add_sheep(self, sheep: Sheep) -> Sheep:
        if sheep.id in self._data:
            raise ValueError("Sheep with this ID already exists")
        self._data[sheep.id] = sheep
        return sheep

    def update_sheep(self, sheep_id: int, sheep: Sheep) -> Optional[Sheep]:
        if sheep_id not in self._data:
            return None
        self._data[sheep_id] = sheep
        return sheep

    def delete_sheep(self, sheep_id: int) -> bool:
        if sheep_id not in self._data:
            return False
        del self._data[sheep_id]
        return True


db = FakeDB()
