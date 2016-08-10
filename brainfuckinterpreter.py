def get_input():
    print ("Introduce your brainfuck code here\n--------------------------\n\n")
    brainfuck = list(input())
    return brainfuck

def brainfuck_interpreter(brainfuck):
    print (brainfuck)
    brainfuck_translated = {0:0}
    position = 0
    while brainfuck: # == True
        current_char = brainfuck.pop(0)
        #if current_char == "[":
            #while brainfuck_translated.get(init_position) != 0

        if current_char == "<":
            if (position - 1) in brainfuck_translated:
                position -= 1
            else:
                brainfuck_translated[position-1] = 0
                position -= 1


        elif current_char == ">":
            if (position + 1) in brainfuck_translated:
                position += 1
            else:
                brainfuck_translated[position+1] = 0
                position += 1

        elif current_char == "+":
            if brainfuck_translated.get(position) < 255:
                brainfuck_translated[position] += 1
            else:
                brainfuck_translated[position] = 0

        elif current_char == "-":
            if brainfuck_translated.get(position) > 0:
                brainfuck_translated[position] -= 1
            else:
                brainfuck_translated[position] = 255

        elif current_char == ".":
            print (chr(brainfuck_translated.get(position)))

        elif current_char == "[":
            #Getting the content into a new List
            tempvar = brainfuck.index("]")
            newbrainfuck = []
            while (tempvar + 1) > 0:
                newitem = brainfuck.pop(0)
                newbrainfuck.append(newitem)
                tempvar -= 1
            newbrainfuck.pop()
            print (brainfuck)
            # Now newbrainfuck = content between parentheses
            positionrecord = position
            while brainfuck_translated[positionrecord] != 0:
                brainfuck_interpreter(newbrainfuck)
            print (brainfuck_translated)

        #else:
        print (brainfuck_translated)

brainfuck_interpreter(get_input())
