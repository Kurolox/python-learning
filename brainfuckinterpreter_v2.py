def get_input():
    print ("Introduce your brainfuck code here\n--------------------------\n\n")
    brainfuck = list(input())
    return brainfuck

def brainfuck_interpreter(brainfuck):
    brainfuck_translated = {0:0}
    position = 0
    listindex = 0
    while brainfuck: # == True
        #if current_char == "[":
            #while brainfuck_translated.get(init_position) != 0

        if brainfuck[listindex] == "<":
            if (position - 1) in brainfuck_translated:
                position -= 1
            else:
                brainfuck_translated[position-1] = 0
                position -= 1


        elif brainfuck[listindex] == ">":
            if (position + 1) in brainfuck_translated:
                position += 1
            else:
                brainfuck_translated[position+1] = 0
                position += 1

        elif brainfuck[listindex] == "+":
            if brainfuck_translated.get(position) < 255:
                brainfuck_translated[position] += 1
            else:
                brainfuck_translated[position] = 0

        elif brainfuck[listindex] == "-":
            if brainfuck_translated.get(position) > 0:
                brainfuck_translated[position] -= 1
            else:
                brainfuck_translated[position] = 255

        elif brainfuck[listindex] == ".":
            print (chr(brainfuck_translated.get(position)))

        elif brainfuck[listindex] == "[":
            #Getting the content into a new List
            startloop = (listindex + 1)
            print (brainfuck)
            endloop =  (brainfuck.index("]", startloop))
            looplength = endloop - startloop
            newbrainfuck = []
            for i in range(looplength):
                newbrainfuck.append(brainfuck[startloop + i])
            # Now newbrainfuck = content between parentheses
            while brainfuck_translated[position] != 0:
                brainfuck_interpreter(newbrainfuck)
        #else:
        listindex += 1

brainfuck_interpreter(get_input())
