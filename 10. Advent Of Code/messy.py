demo_input = """
    [D]    
[N] [C]    
[Z] [M] [P] 
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

crates, recipe = demo_input.split("\n\n")

boxes = [[], [], []]

for line in crates.split("\n"): 

    for col in range(0, len(line), 4):
        box = line[col:col+4]

        box = box.replace("[", "")

        if box in ["1", "2", "3"]: continue

        if box != "": boxes[col//4].insert(0, box)

for line in recipe.split("\n"):
    instruction = []

    for char in line:

        if char in ["1", "2", "3"]:
            instruction.append(int(char))

    times = instruction[0]
    from_ = instruction[1]
    to_ = instruction[2] - 1

    for i in range(times):
        box = boxes[from_][0]

        boxes[to_].append(box)
        boxes[from_].pop()

# DON'T MAKE EDITS BELOW THIS LINE

for i in range(max([len(l) for l in boxes]), -1, -1):
    for col in boxes:
        if i < len(col): print(f"[{col[i]}]", end=" ")
        else: print("    ", end="")
    print()
        
