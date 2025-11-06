from stockfish import Stockfish

sf1 = Stockfish("/opt/homebrew/bin/stockfish")
sf2 = Stockfish("/opt/homebrew/bin/stockfish")

sf1.set_skill_level(10)
sf2.set_skill_level(15)

moves = []

for turn in range(10):  # play 10 half-moves
    sf1.set_position(moves)
    move1 = sf1.get_best_move()
    if move1 is None:
        break
    moves.append(move1)
    print(f"White plays: {move1}")

    sf2.set_position(moves)
    move2 = sf2.get_best_move()
    if move2 is None:
        break
    moves.append(move2)
    print(f"Black plays: {move2}")

print("Final moves:", moves)
