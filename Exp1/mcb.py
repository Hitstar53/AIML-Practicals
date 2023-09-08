def main():
    print("Welcome to Missionary and Cannibals Game!\nRules:\nNo. of Missionaries cannot be less than no. of cannibals at any point on any bank!\n\nLet's Begin!")
    lm = int(input("Enter the no. of missionaries: "))
    lc = int(input("Enter the no. of cannibals: "))
    b = rm = rc = 0
    print(f"Initial State(on left):\nMissionaries: {lm}\nCannibals: {lc}\nBoat is on left Bank!\n")
    while(True):
        if lm == 0 and lc == 0:
            print("You Won the Game!\n")
            print(f"Final State on Left:\nMissionaries: {lm}\nCannibals: {lc}\n")
            print(f"Final State on Right:\nMissionaries: {rm}\nCannibals: {rc}\n")
            break
        while(True):
            um, uc = map(int, input("Enter the no. of missionaries and cannibals: ").split())
            if um > 2 or uc > 2 or um < 0 or uc < 0 or um + uc > 2:
                print("Invalid Input! Try Again!")
            elif b == 0 and (uc > lc or um > lm):
                print("Invalid Input! Try Again!")
            elif b == 1 and (uc > rc or um > rm):
                print("Invalid Input! Try Again!")
            else:
                break
        if b == 0:
            lm -= um
            lc -= uc
            rm += um
            rc += uc
        else:
            lm += um
            lc += uc
            rm -= um
            rc -= uc
        if (rm < rc and rm != 0) or (lm < lc and lm!= 0):
            print("Missionaries are less than cannibals!\nYou Lost the Game!")
            break
        else:
            print(f"Current State on Left Bank:\nMissionaries: {lm}\nCannibals: {lc}\n")
            print(f"Current State on Right Bank:\nMissionaries: {rm}\nCannibals: {rc}\n")
            if b == 0:
                b = 1
            elif b == 1:
                b = 0
            print("Boat is on left Bank!\n") if b == 0 else print("Boat is on right Bank!\n")
    
if __name__ == "__main__":
    main()