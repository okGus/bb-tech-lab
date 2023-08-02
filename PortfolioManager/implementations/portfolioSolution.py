#Uncomment line above & run cell to save solution
#TODO Define class that implements portFolioInterface & allows for the management of a portfolio
from interfaces.portfolioInterface import portfolioInterface
from interfaces.accountInterface import accountInterface
from implementations.accountSolution import account
from typing import Set, Iterable

class portfolio(portfolioInterface):
    def __init__(self, portfolioName: str, accounts: Set[accountInterface]) -> None:
        super().__init__(portfolioName, accounts)
        self.m_name = portfolioName
        self.m_accountsMap = {accItem.getName() : accItem for accItem in accounts}

    def getAllAccounts(self) -> Iterable[accountInterface]:
        return list(self.m_accountsMap.values())

    def getAccounts(self, accountNamesFilter: Set[str], securitiesFilter: Set) -> Iterable[accountInterface]:
        if len(accountNamesFilter) == 0 and len(securitiesFilter) == 0:
            return self.getAllAccounts()

        if len(accountNamesFilter) != 0:
            filteredAcc = set()

            for acc in accountNamesFilter:
                if acc in self.m_accountsMap:
                    filteredAcc.add(self.m_accountsMap[acc])
        else:
            filteredAcc = set(self.m_accountsMap.values())

        finalSet = set()
        if len(securitiesFilter) != 0:
            for acc in filteredAcc:
                if len(acc.getPositions(securitiesFilter)) != 0:
                    finalSet.add(acc)
        else:
            finalSet = filteredAcc

        return finalSet
                
    def addAccounts(self, accounts: Set[accountInterface]) -> None:
        for acc in accounts:
            if acc.getName() in self.m_accountsMap:
                self.m_accountsMap.pop(acc.getName())
            else:
                self.m_accountsMap[acc.getName()] = acc

    def removeAccounts(self, accountNames: Set[str]) -> None:
        for acc in accountNames:
            if acc in self.m_accountsMap:
                self.m_accountsMap.pop(acc, None)

    def __aggregateAccountMV(self, accounts: Iterable[accountInterface]):
        #Aggregate positions at this level & query their security value.
        aggregatePosMap = {}
        
        for account in accounts:
            for position in account.getAllPositions():
                if position.getSecurity().getName() in aggregatePosMap:
                    aggregatePosMap[position.getSecurity().getName()][0] += position.getPosition()
                else:
                    #List with reference to underlying security
                    aggregatePosMap[position.getSecurity().getName()] = [position.getPosition(), position.getSecurity()]
                    
        summedMarketValue = 0
        for posTuple in aggregatePosMap.values():
            summedMarketValue += posTuple[0] * posTuple[1].getCurrentMarketValue()

        return summedMarketValue

    def getCurrentMarketValue(self) -> dict:
        return self.__aggregateAccountMV(self.m_accountsMap.values())

    def getCurrentFilteredMarketValue(self, securities: Set, accountNames: Set[str]) -> float:
        return self.__aggregateAccountMV(self.trimAccountPositions(self.getAccounts(accountNames, securities), securities))

    def trimAccountPositions(self, accounts: Iterable[accountInterface], securities: Set) -> Iterable[accountInterface]:
        if len(securities) == 0:
            return accounts

        trimmedAccounts = set()
        for acc in accounts:
            trimmedAccounts.add(account(acc.getPositions(securities).values(), "trimmed"))    

        return trimmedAccounts
