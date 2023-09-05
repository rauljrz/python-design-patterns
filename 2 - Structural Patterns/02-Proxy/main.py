from proxy import Proxy

def main():
    #Instantiate a Proxy
    p = Proxy()

    #Make the proxy: Artist produce until Producer is available
    p.produce()

    #Change the state to 'occupied'
    p.occupied = 'Yes'

    #Make the Producer produce
    p.produce()

if __name__=="__main__":
    main()