import view.DAO as DAO
from os.path import dirname, realpath


class LeaderboardDAO(DAO.DAO):
    def __init__(self) -> None:
        super().__init__(f'{dirname(realpath(__file__))}/rank.json')

    def add(self, key, obj):
        if key != None:
            super().add(key, obj)
