from hvacspecialist import HvacSpecialist
from electrician import Electrician
from house import House

def main():
    #Create an HVAC specialist
    hv= HvacSpecialist()

    #Create an electrician
    e = Electrician()

    #Create a house
    home = House()

    #Let the house accept the HVAC specialist and work on the house by invoking the visit() method
    home.accept(hv)

    #Let the house accept the electrician and work on the house by invoking the visit() method
    home.accept(e)


if __name__=="__main__":
    main()