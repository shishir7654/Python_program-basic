class Car:
    def SetType(self,type):
        self._Type =type
    def GetType(self):
        return self._Type

    def SetModel(self,model):
        self._Model =model
    def GetType(self):
        return self._Model


    def SetPrice(self,price):
        self._Price =price
    def GetType(self):
        return self._Price


    def SetMilesDrive(self,milesDrive):
        self._MilesDrive =milesDrive
    def GetMilesDrive(self):
        return self._Milesdrive



    def SetOwner(self,owner):
        self._Owner =owner
    def GetOwner(self):
        return self._Owner


    def GetCurrentPrice(self):
        return self._Price-(self._MilesDrive*10)


def main():
    myCar = Car()
    myCar.SetType("BMW")
    myCar.SetModel(2015)
    myCar.SetPrice(26000)
    myCar.SetMilesDrive(15)
    myCar.SetOwner("shihsir")
    CurrentPrice=myCar.GetCurrentPrice()
    print("New price{}".format(CurrentPrice))




if __name__== '__main__':main()

