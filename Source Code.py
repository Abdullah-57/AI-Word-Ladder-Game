import random
import heapq
import msvcrt
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Controls for the Game
def get_key():
    key = msvcrt.getch()
    if key == b'\xe0':  #Arrow keys
        key = msvcrt.getch()
        if key == b'H':
            return 'up'
        elif key == b'P':
            return 'down'
        elif key == b'K':
            return 'left'
        elif key == b'M':
            return 'right'
    elif key == b'\r': 
        return 'enter'
    else:
        try:
            return key.decode('utf-8').lower()
        except UnicodeDecodeError:
            return None

# Loads the dictionary from the text file
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        words = {line.strip().lower() for line in file if line.strip().isalpha()}
    return words

DICTIONARY_FILE = "C:/Users/Admin/OneDrive/Desktop/Portfolio Projects/6/AI/AI Word Ladder Game/words.txt"
dictionary = load_dictionary(DICTIONARY_FILE)

# Checks if a word is valid from the dictionary
def is_valid_word(word, banned_words=None, restricted_letters=None):
    if banned_words and word in banned_words:
        return False
    if restricted_letters and any(letter in word for letter in restricted_letters):
        return False
    return word in dictionary

# Gets a random valid word from the dictionary of a specific length based on difficulty selected
def get_random_valid_word(length, banned_words=None, restricted_letters=None):
    valid_words = [word for word in dictionary if len(word) == length and is_valid_word(word, banned_words, restricted_letters)]
    return random.choice(valid_words) if valid_words else None

# Allow player to choose difficulty which sets the AI and turn limits as well
def select_difficulty():
    difficulties = {
        "1": ("Beginner", 15, 5, None, None),
        "2": ("Advanced", 10, 3, None, None),
        "3": ("Challenge", 7, 0, {"banned", "words"}, {'x', 'z'}) #disabled AI hints
    }
    print(Fore.CYAN + "\n══════════════════════════════════")
    print(Fore.CYAN + "⚡ WELCOME TO THE WORD LADDER GAME! ⚡")
    print(Fore.CYAN + "══════════════════════════════════")
    print(Fore.YELLOW + "\nSelect Difficulty Level:")
    for key, (value, _, _, _, _) in difficulties.items():
        print(f"{Fore.GREEN}{key}. {value}")
    
    choice = input("Enter choice (1-3): ")
    return difficulties.get(choice, ("Beginner", 15, 5, None, None))

# Keeps searching for a word which contains a valid transformation path
def get_valid_start_and_target(word_length, banned_words, restricted_letters):
    while True:
        start_word = get_random_valid_word(word_length, banned_words, restricted_letters)
        if not start_word:
            continue
        target_word = get_target_word(start_word, banned_words, restricted_letters)
        if target_word:
            return start_word, target_word

# Gets a target word that is of same length as starting word
def get_target_word(start_word, banned_words=None, restricted_letters=None):
    word_length = len(start_word)
    valid_words = [word for word in dictionary if len(word) == word_length and word != start_word and is_valid_word(word, banned_words, restricted_letters)]
    
    for target_word in valid_words:
        if bfs_hint(start_word, target_word):
            return target_word
    return None

# Calculate heuristic value based on letter differences
def heuristic(word, target):
    return sum(1 for a, b in zip(word, target) if a != b)

# Generate valid neighboring words with one letter change
def get_neighbors(word):
    neighbors = []
    for i in range(len(word)):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            new_word = word[:i] + char + word[i+1:]
            if new_word != word and is_valid_word(new_word):
                neighbors.append(new_word)
    return neighbors

# Breadth-First Search Algorithm
def bfs_hint(start, target):
    """Breadth-First Search (BFS) to find the next optimal word transformation."""
    queue = [(start, [start])]
    visited = set()
    while queue:
        current_word, path = queue.pop(0)
        if current_word == target:
            return path[1] if len(path) > 1 else None
        visited.add(current_word)
        for neighbor in get_neighbors(current_word):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    return None

# Uniform Cost Search Algorithm
def ucs_hint(start, target):
    """Uniform Cost Search (UCS) for finding the optimal next move."""
    queue = [(0, start, [start])]
    visited = set()
    while queue:
        cost, current_word, path = heapq.heappop(queue)
        if current_word == target:
            return path[1] if len(path) > 1 else None
        visited.add(current_word)
        for neighbor in get_neighbors(current_word):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + 1, neighbor, path + [neighbor]))
                visited.add(neighbor)
    return None

# A* Algorithm
def a_star_hint(start, target):
    """A* Search Algorithm for the next best move."""
    queue = [(heuristic(start, target), start, [start])]
    visited = set()
    while queue:
        _, current_word, path = heapq.heappop(queue)
        if current_word == target:
            return path[1] if len(path) > 1 else None
        visited.add(current_word)
        for neighbor in get_neighbors(current_word):
            if neighbor not in visited:
                heapq.heappush(queue, (heuristic(neighbor, target), neighbor, path + [neighbor]))
                visited.add(neighbor)
    return None

# Graph Visualization with a limit of 10 words
def visualize_graph(word_length):
    """Visualize the dictionary as a word graph."""
    print(Fore.MAGENTA + "\n══════════════════════════════════════════")
    print(Fore.MAGENTA + "📌 DICTIONARY WORD GRAPH (PARTIAL VIEW)")
    print(Fore.MAGENTA + "══════════════════════════════════════════")
    words = [word for word in dictionary if len(word) == word_length]
    for word in words[:10]:  
        neighbors = get_neighbors(word)
        print(Fore.CYAN + f"| {word} → " + Fore.YELLOW + f"{', '.join(neighbors[:5])} ..." if neighbors else f"| {word} → No connections")
    print(Fore.MAGENTA + "══════════════════════════════════════════")

# Game Status
def display_game_status(current_word, target_word, turns_left, hints_left):
    """Display the game status including controls, score, turns, and hints."""
    print(Fore.CYAN + "\n════════════════════════════════════════════")
    print(Fore.YELLOW + "🎮 CONTROLS: [H] Hint  |  [V] Visualize Dictionary")
    print(Fore.GREEN + f"🏆 SCORE: TBD  |  🔄 TURNS LEFT: {turns_left}  |  💡 HINTS LEFT: {hints_left}")
    print(Fore.BLUE + f"📌 CURRENT WORD: {Fore.GREEN}{current_word}")
    print(Fore.RED + f"🎯 TARGET WORD: {Fore.RED}{target_word}")
    print(Fore.CYAN + "════════════════════════════════════════════")

# Main Function
if __name__ == "__main__":
    difficulty, turn_limit, hint_limit, banned_words, restricted_letters = select_difficulty()
    print(Fore.BLUE + f"\n🎮 YOU SELECTED: {difficulty}")
    
    word_length = 3 if difficulty == "Beginner" else (5 if difficulty == "Advanced" else 7)
    start_word, target_word = get_valid_start_and_target(word_length, banned_words, restricted_letters)
        
    current_word = start_word
    turns_used = 0
    hints_used = 0

    while current_word != target_word and turns_used < turn_limit:
        display_game_status(current_word, target_word, turn_limit - turns_used, hint_limit - hints_used)
        
        print(Fore.YELLOW + "\nPress any character to continue.")
        key = get_key()
        
        if key == 'v':
            visualize_graph(word_length)
            continue
        elif key == 'h' and hints_used < hint_limit:
            print(Fore.CYAN + "Select algorithm: [B] BFS, [U] UCS, [A] A*")
            algo = get_key().upper()
            algo_map = {"B": "BFS", "U": "UCS", "A": "A*"}
            if algo in algo_map:
                hint = bfs_hint(current_word, target_word) if algo_map[algo] == "BFS" else \
                       ucs_hint(current_word, target_word) if algo_map[algo] == "UCS" else \
                       a_star_hint(current_word, target_word)
                if hint:
                    print(Fore.GREEN + f"💡 AI SUGGESTS: {hint}")
                    hints_used += 1
                else:
                    print(Fore.RED + "⚠ NO SUGGESTIONS AVAILABLE")
            continue
        elif key == 'h' and hints_used >= hint_limit:
            print(Fore.RED + "⚠ NO AI HINTS LEFT! TRY YOUR LUCK")
        
        print(Fore.CYAN + "\nEnter the index (0-{}): ".format(len(current_word)-1))
        index = int(input())
        new_letter = input(Fore.CYAN + "Enter new letter: ").lower()
        
        new_word = current_word[:index] + new_letter + current_word[index+1:]
        if is_valid_word(new_word, banned_words, restricted_letters):
            current_word = new_word
            turns_used += 1
        else:
            print(Fore.RED + "⚠ INVALID WORD. TRY AGAIN.")
            turns_used += 1 
    
    if current_word == target_word:
        score = max(0, (turn_limit - turns_used) * 10 - hints_used * 5)
        print(Fore.GREEN + f"🎉 CONGRATULATIONS! YOU FOUND THE TARGET WORD! SCORE: {score}")
    else:
        print(Fore.RED + "💀 GAME OVER! YOU'VE RUN OUT OF TURNS.")
