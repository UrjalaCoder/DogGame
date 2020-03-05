from Dog import Dog

def printOptions():
    optionString = [
        "[0] LOPETA",
        "[1] Rapsutus",
        "[2] Ulkoilutus",
        "[3] Ruoki"
    ]
    print('\n'.join(optionString))

def printTargetDogs(dogs):
    dogStrings = [f"[{i}]: {dogs[i]}" for i in range(len(dogs))]
    print('\n'.join(dogStrings))

def parseInput():
    option = input("Select option\n")
    return int(option)

def printActs(acts):
    print("Actions:")
    for i in range(len(acts)):
        dogActions = acts[i][1]
        dog = acts[i][0]
        print(dog)
        for a in dogActions:
            print(str(a))

def loop():
    dogs = []
    # First dog
    firstDog = Dog("Doggo", "Corgi")
    dogs.append(firstDog)
    done = False
    while not done:
        acts = []
        printOptions()
        action = parseInput()
        if action == 0:
            done = True
        else:
            printTargetDogs(dogs)
            dog = parseInput()
            if action == 1:
                dogs[dog].rapsuttaa()
            elif action == 2:
                dogs[dog].walking()
            elif action == 3:
                dogs[dog].feed()
        for d in dogs:
            d.update()
            acts.append([d, d.act()])
        printActs(acts)


def main():
    loop()


# Dont mind this
if __name__ == '__main__':
    main()
