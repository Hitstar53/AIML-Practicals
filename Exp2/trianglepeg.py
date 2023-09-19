import time

def make_move(pos, t, sub):
    return pos[:t[0]] + sub[0] + pos[t[0]+1:t[1]] + sub[1] + pos[t[1]+1:t[2]] + sub[2] + pos[t[2]+1:]

def solve_puzzle(pos, goal):
    queue, solution = [], []
    trail = {str(pos): None}
    while not pos == goal:
        for next_move in iterate_puzzle(pos):
            c = str(next_move)
            if c in trail:
                continue
            trail[c] = pos
            queue.append(next_move)
        if len(queue) == 0:
            return None
        pos = queue.pop(0)
    while pos:
        solution.insert(0, pos)
        pos = trail[str(pos)]
    return solution

def iterate_puzzle(pos):
    valid_moves = [[0,1,3], [1,3,6], [3,6,10], [2,4,7], [4,7,11], [5,8,12],
               [10,11,12], [11,12,13], [12,13,14], [6,7,8], [7,8,9], [3,4,5],
               [0,2,5], [2,5,9], [5,9,14], [1,4,8], [4,8,13], [3,7,12]]
    for t in valid_moves:
        if pos[t[0]] == '1' and pos[t[1]] == '1' and pos[t[2]] == '0':
            yield make_move(pos, t, '001')
        if pos[t[0]] == '0' and pos[t[1]] == '1' and pos[t[2]] == '1':
            yield make_move(pos, t, '100')

def main():
    t = time.time()
    initial_pos = '011111111111111'
    goal_pos = '100000000000000'
    solution = solve_puzzle(initial_pos, goal_pos)
    for s in solution:
        print("\nCurrent State:\n")
        for i in range(5):
            print(' ' * (4 - i), end='')
            row = s[i * (i + 1) // 2:i * (i + 1) // 2 + i + 1]
            print(' '.join(map(str, row)))
    print("\nTotal Steps: %d" % (len(solution) - 1))
    d = time.time() - t
    print("\nDuration for Solving: %d ms" % (d * 1000))

if __name__ == '__main__':
    main()