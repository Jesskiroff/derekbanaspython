while True:
    try:
        number = int(input("Please enter a number : "))
        break
    except ValueError:
        print("You didn't enter a number")
    except:
        print("An unknown error has occured")

print("Thank you for entering a number")