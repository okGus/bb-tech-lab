#Uncomment line above & run cell to save solution
#TODO Define class that implements securityInterface & allows for the management of a security
from interfaces.securityInterface import securityInterface
from generators.priceDataGenerator import priceData

class security(securityInterface):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.m_name = name
        self.m_priceData = priceData()

    def getName(self) -> str:
        return self.m_name

    def getCurrentMarketValue(self) -> float:
        return self.m_priceData.getCurrentPrice(self.m_name)
