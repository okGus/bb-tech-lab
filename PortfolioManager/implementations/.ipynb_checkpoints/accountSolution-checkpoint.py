#Uncomment line above & run cell to save solution
#TODO Define class that implements accountInterface & allows for the management of an account

from interfaces.positionInterface import positionInterface
from interfaces.accountInterface import accountInterface
from interfaces.securityInterface import securityInterface
from typing import Any, Dict, Set, Iterable

class account(accountInterface):
    def __init__(self, position: Set[positionInterface], accountName: str) -> None:
        self.m_accountName = accountName
        self.m_positionMap = {posItem.getSecurity().getName() : posItem for posItem in position}
        
    def getName(self) -> str:
        return self.m_accountName

    def getAllPositions(self) -> Iterable[positionInterface]: #  is iterable
        return list(self.m_positionMap.values())

    def getPositions(self, securities: Set) -> Dict[Any, positionInterface]:
        returnPositionMap = {}

        print(securities)
        for securityKey in securities:
            print(securityKey)
            if isinstance(securityKey, securityInterface) and securityKey.getName() in self.m_positionMap:
                returnPositionMap[securityKey] = self.m_positionMap[securityKey.getName()]
            elif securityKey in self.m_positionMap:
                returnPositionMap[securityKey] = self.m_positionMap[securityKey]

        return returnPositionMap

    def addPositions(self, positions: Set[positionInterface]) -> None:
        # self.positions.add(positions)
        pass
    
    def removePositions(self, securities: Set) -> None:
        pass
