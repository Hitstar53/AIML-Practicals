import time

def make_move(pos, t, sub):
    new_pos = pos.copy()
    for i in range(3):
        new_pos[t[i]] = sub[i]
    return new_pos

def trianglepeg(pos, goal):
    queue, solution = [], []
    path = {tuple(pos): None}
    while pos != goal:
        for next_move in iterate_puzzle(pos):
            c = tuple(next_move)
            if c in path:
                continue
            path[c] = pos
            queue.append(next_move)
        if len(queue) == 0:
            return None
        pos = queue.pop(0)
    while pos:
        solution.insert(0, pos)
        pos = path[tuple(pos)]
    return solution

def iterate_puzzle(pos):
    valid_moves = [[0,1,3], [1,3,6], [3,6,10], [2,4,7], [4,7,11], [5,8,12],
                   [10,11,12], [11,12,13], [12,13,14], [6,7,8], [7,8,9], [3,4,5],
                   [0,2,5], [2,5,9], [5,9,14], [1,4,8], [4,8,13], [3,7,12]]
    for t in valid_moves:
        if pos[t[0]] == 1 and pos[t[1]] == 1 and pos[t[2]] == 0:
            yield make_move(pos, t, [0, 0, 1])
        if pos[t[0]] == 0 and pos[t[1]] == 1 and pos[t[2]] == 1:
            yield make_move(pos, t, [1, 0, 0])

def main():
    initial_board = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    goal = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    t = time.time()
    solution = trianglepeg(initial_board, goal)
    d = time.time() - t
    for s in solution:
        print("\nCurrent State:\n")
        for i in range(5):
            print(' ' * (4 - i), end='')
            row = s[i * (i + 1) // 2:i * (i + 1) // 2 + i + 1]
            print(' '.join(map(str, row)))
    print("\nTotal Steps: %d" % (len(solution) - 1))
    print("\nDuration for Solving: %d ms" % (d * 1000))
    

if __name__ == '__main__':
    main()
