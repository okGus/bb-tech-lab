#Uncomment line above & run cell to save solution
#TODO Define class that implements accountInterface & allows for the management of an account
from interfaces.positionInterface import positionInterface
from interfaces.accountInterface import accountInterface
from interfaces.securityInterface import securityInterface
from typing import Any, Dict, Set, Iterable
from math import fsum

class account(accountInterface):
    def __init__(self, position: Set[positionInterface], accountName: str) -> None:
        self.m_accountName = accountName
        self.m_positionMap = {posItem.getSecurity().getName() : posItem for posItem in position}
        
    def getName(self) -> str:
        return self.m_accountName

    def getAllPositions(self) -> Iterable[positionInterface]: #  is iterable of type positionInterface
        return list(self.m_positionMap.values())

    def getPositions(self, securities: Set) -> Dict[Any, positionInterface]:
        returnPositionMap = dict()

        for securityKey in securities:
            if isinstance(securityKey, securityInterface) and securityKey.getName() in self.m_positionMap:
                returnPositionMap[securityKey] = self.m_positionMap[securityKey.getName()]
            elif securityKey in self.m_positionMap:
                returnPositionMap[securityKey] = self.m_positionMap[securityKey]
        
        return returnPositionMap

    def addPositions(self, positions: Set[positionInterface]) -> None:
        for posItem in positions:
            if posItem.getSecurity().getName() in self.m_positionMap:
                self.m_positionMap[posItem.getSecurity().getName()].setPosition(posItem.getPosition())
            else:
                self.m_positionMap[posItem.getSecurity().getName()] = posItem
    
    def removePositions(self, securities: Set) -> None:
        for securityKey in securities:
            if isinstance(securityKey, securityInterface):
                self.m_positionMap.pop(securityKey.getName(), None)
            else: 
                self.m_positionMap.pop(securityKey, None)

    def getCurrentMarketValue(self) -> float:
        mv = float(0)
        for posItem in self.getAllPositions():
            mv += posItem.getCurrentMarketValue()
        return mv

    def getCurrentFilteredMarketValue(self, securities: Set) -> float:
        return fsum([pos.getCurrentMarketValue() for pos in self.getPositions(securities).values()])
        
