#Uncomment line above & run cell to save solution
#TODO Define class that implements positionInterface & allows for the management of a position
from interfaces.securityInterface import securityInterface
from interfaces.positionInterface import positionInterface

from implementations.securitySolution import security

class position(positionInterface):
    def __init__(self, positionType, initialPosition: int) -> None:
        self.positionType = positionType
        self.m_initialPosition = initialPosition
        
        if isinstance(positionType, securityInterface):
            self.m_security = positionType
        else:
            self.m_security = security(positionType)
            
    def getSecurity(self) -> securityInterface:
        return self.m_security

    def getPosition(self) -> int:
        return self.m_initialPosition
    
    def setPosition(self, inputValue: int) -> None:
        if inputValue < 0:
            raise Exception('Short position', inputValue)
        self.m_initialPosition = inputValue
    
    def addPosition(self, inputValue: int) -> None:
        newPosition = self.m_initialPosition + inputValue
        if newPosition < 0:
            raise Exception('Short position', newPosition)
        self.m_initialPosition = newPosition

    def getCurrentMarketValue(self) -> float:
        return self.m_security.getCurrentMarketValue() * self.m_initialPosition
