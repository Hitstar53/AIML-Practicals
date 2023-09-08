def main():
    print("Welcome to Water Jug Problem!\nRules:You are given m and n litre jugs and you have to take out z litres of water to solve the problem. Jugs can be fully emptied or filled, or trasnferred from 1 to another!\n\nLet's Begin!!!")
    final = list(map(int, input("Enter quantity of jugs 1 and 2: ").split()))
    z = int(input("Enter Goal Amt: "))
    jugs = list(final)
    while(True):
        print(f"\nCurrent Status:\nJug1: {jugs[0]}L\tJug2: {jugs[1]}L\n")
        i = int(input("Pick a Jug (1 or 2): "))-1
        choice = int(input("Pick an Action:\n1. Empty\t2. Fill\n3. Pour to other Jug\n"))
        if choice == 1 and jugs[i] != 0:
            jugs[i] = 0
        elif choice == 2 and jugs[i] != final[i]:
            jugs[i] = final[i]
        elif choice == 3:
            source = i
            target = 1 - source
            temp = final[target]-jugs[target]
            amt = min(temp, jugs[source])
            jugs[source] -= amt
            jugs[target] += amt
        elif choice == 4:
            continue
        
        if jugs[0] > final[0] or jugs[1] > final[1]:
            print("A jug has had an overflow! Please start again!")
            break
        elif jugs[0]==z or jugs[1]==z:
            print(f"\nGoal state achieved!!!\nJug1: {jugs[0]}L\tJug2: {jugs[1]}L")  
            break    
    
if __name__ == '__main__':
    main()