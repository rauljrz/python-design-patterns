from client import Client

def main():
    # Create a client
    c = Client()

    # Create requests
    requests = [2, 5, 30]

    # Send the requests
    c.delegate(requests)

if __name__=="__main__":
    main()