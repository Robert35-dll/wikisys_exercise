# Final Demo Version (edited by Robert Koch)
from collections import deque

# State representation: (alex, wolf, goat, cabbage)
initial_state = (0, 0, 0, 0)  # all on the left
goal_state = (1, 1, 1, 1)     # all on the right

def is_valid_state(state):
    alex, wolf, goat, cabbage = state

    #!Ensure the goat is not left alone with the wolf or cabbage!
    if ((wolf == goat or goat == cabbage) and goat != alex):
        return False
    return True


# generate neighbors in search problem for a specific state
def get_neighbors(state):

    alex, wolf, goat, cabbage = state
    neighbors = []

    # Generate all possible moves (Alex carries one item or none)
    possible_moves = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]

    for move in possible_moves:

        wolf_move, goat_move, cabbage_move = move

        # Ensure that the move is valid
        if alex == 0:  # Alex is on the left side
            # compute new state based on move
            new_alex_pos = 1
            new_wolf = wolf + wolf_move
            new_goat = goat + goat_move
            new_cabbage = cabbage + cabbage_move
        else:  # Alex is on the right side
            new_alex_pos = 0
            new_wolf = wolf - wolf_move
            new_goat = goat - goat_move
            new_cabbage = cabbage - cabbage_move

        # Ensure the new state is within valid bounds (0 or 1)
        if not (0 <= new_wolf <= 1 and
                0 <= new_goat <= 1 and
                0 <= new_cabbage <= 1):
            continue

        new_state = (new_alex_pos, new_wolf, new_goat, new_cabbage)
        if is_valid_state(new_state):
            neighbors.append(new_state)

    return neighbors

def bfs():
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path + [state]
        
        # else
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [state]))

    return None

if __name__ == "__main__":
    solution = bfs()
    names = ['Alex', 'Wolf', 'Goat', 'Cabbage']
    
    if solution:
        for step_number in range(len(solution)):
            print(f'[{step_number + 1}]:')
            state = solution[step_number]
            
            for character_number in range(len(state)):
                print(f' |- {names[character_number]} is on the ' \
                      f'{'left' if state[character_number] == 0 else 'right'} ' \
                       'side')
                
        print(' |\n[^] Alle Figuren haben es sicher ' \
              'zur anderen Seite geschafft (✿◠‿◠)')
    else:
        print('[!]- Keine Lösung gefunden (っ◞‸◟c)')

