from count_to import Count_to

def main():
    #Let's test the generator returned by our iterator
    for num in Count_to(3):
        print("{}".format(num))

    for num in Count_to(4):
        print("{}".format(num))

if __name__=="__main__":
    main()