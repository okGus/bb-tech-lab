#Uncomment line above & run cell to save solution
#TODO Define class that implements portFolioInterface & allows for the management of a portfolio

from interfaces.portfolioInterface import portfolioInterface
from interfaces.accountInterface import accountInterface
from typing import Set, Iterable

class portfolio(portfolioInterface):
    def __ini__(self, portfolioName: str, accounts: Set[accountInterface]) -> None:
        super().__init__(portfolioName, accounts)
        self.m_name = portfolioName
        self.m_accountsMap = {accItem.getName() : accItem for accItem in accounts}

    def getAllAccounts(self) -> Iterable[accountInterface]:
        return list(self.m_accountsMap.values())

    def getAccounts(self, accountNamesFilter: Set[str], securitiesFilter: Set) -> Iterable[accountInterface]:
        pass 

    def addAccounts(self, accounts: Set[accountInterface]) -> None:
        pass

    def removeAccounts(self, accountNames: Set[str]) -> None:
        pass
