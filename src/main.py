from menu import mainScreen, endScreen, storyScreen

def main():
    while True:
        choice = mainScreen()

        if choice is None or choice == -1 or choice == 7:
            break

        else:
            storyScreen()

    
if __name__ == "__main__":
    main()