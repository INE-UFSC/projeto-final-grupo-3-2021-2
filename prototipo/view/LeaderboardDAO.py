import view.DAO as DAO
from os.path import dirname, realpath


class LeaderboardDAO(DAO.DAO):
    def __init__(self) -> None:
        super().__init__(f'{dirname(realpath(__file__))}/rank.json')
