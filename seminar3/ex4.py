def songGenerator(notes, moves, start):
    toReturnList = []
    toReturnList.extend([notes[start]])
    for move in moves:
        toReturnList.extend([notes[(start+move) % len(notes)]])
        start = start + move
    return toReturnList


notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2, ]
start = 2
print(songGenerator(notes, moves, start))
