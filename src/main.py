from menu import storyScreen, mainScreen

MAX_ENERGY = 100
state = {

    "day": 1,
    "energy": MAX_ENERGY,
    "choices" : []
}

def main():
    while True:
        choice = mainScreen()

        if choice is None or choice == -1 or choice == 7:
            break

        else:
            storyScreen()
    
if __name__ == "__main__":
    main()