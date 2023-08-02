#Uncomment line above & run cell to save solution
#TODO Define class that implements positionInterface & allows for the management of a position
import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from implementations.securityInterface import securityInterface

class positionInterface:
    def __init__(self, security, initialPosition: int) -> None:
        self.security = security
        self.initialPosition = initialPosition

    def getSecurity(self) -> securityInterface:
        return self.security

    def getPosition(self) -> int:
        return self.initialPosition
    
    def setPosition(self, inputValue: int) -> None:
        self.initialPosition = inputValue
    
    def addPosition(self, inputValue: int) -> None:
        self.initialPosition += inputValue

class position(positionInterface):
    def __init__(self, positionType, initialPosition: int) -> None:
        if type(positionType) == str:
            super().__init__(securityInterface(positionType), initialPosition)
        else:
            super().__init__(positionType, initialPosition)
