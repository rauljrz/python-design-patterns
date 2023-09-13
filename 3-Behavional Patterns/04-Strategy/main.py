from strategy import Strategy

#Replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))

#Replacement method 2    
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))

def main():
    #Let's create our default strategy
    s0 = Strategy()
    #Let's execute our default strategy
    s0.execute()

    #Let's create the first varition of our default strategy by providing a new behavior
    s1 =  Strategy(strategy_one)
    #Let's set its name
    s1.name = "Strategy One"
    #Let's execute the strategy
    s1.execute()

    s2 = Strategy(strategy_two)
    s2.name = "Strategy Two"
    s2.execute()

if __name__=="__main__":
    main()