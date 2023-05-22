import random

# Game setup
GRID_SIZE = 5
NUM_TREASURES = 3
NUM_KNIGHTS = 2

# Create the grid
grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Place treasures randomly on the grid
for _ in range(NUM_TREASURES):
    x = random.randint(0, GRID_SIZE - 1)
    y = random.randint(0, GRID_SIZE - 1)
    grid[x][y] = "T"

# Place knights randomly on the grid
for _ in range(NUM_KNIGHTS):
    x = random.randint(0, GRID_SIZE - 1)
    y = random.randint(0, GRID_SIZE - 1)
    grid[x][y] = "K"

# Game loop
game_over = False
treasures_collected = 0

while not game_over:
    # Display the grid
    print("\n" + "-" * (GRID_SIZE * 4 + 1))
    for row in grid:
        print("|", end="")
        for cell in row:
            print(f" {cell} ", end="|")
        print("\n" + "-" * (GRID_SIZE * 4 + 1))

    # Get the player's move
    move = input("Enter your move (up/down/left/right): ")

    # Update the player's position
    if move == "up":
        x -= 1
    elif move == "down":
        x += 1
    elif move == "left":
        y -= 1
    elif move == "right":
        y += 1

    # Check if the player is out of bounds
    if x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE:
        print("You fell off the edge! Game over.")
        game_over = True
        continue

    # Check if the player found a treasure
    if grid[x][y] == "T":
        print("Congratulations! You found a treasure.")
        treasures_collected += 1
        grid[x][y] = "."  # Remove the treasure from the grid

        if treasures_collected == NUM_TREASURES:
            print("You collected all the treasures! You win!")
            game_over = True
            continue

    # Check if the player encountered a knight
    if grid[x][y] == "K":
        print("Oh no! You encountered a knight. Game over.")
        game_over = True
        continue

print("Thanks for playing Knights!")
