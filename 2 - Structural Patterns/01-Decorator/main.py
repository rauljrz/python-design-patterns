from hello_world import Hello_world

def main():
    #Check the result of decorating
    print(Hello_world())

    #Check if the function name is still the same name of the function being decorated
    print(Hello_world.__name__)

    #Check if the docstring is still the same as that of the function being decoratedo
    print(Hello_world.__doc__)

if __name__ == "__main__":
    main()