def get_input():
    print ("Introduce your brainfuck code here\n--------------------------\n\n")
    brainfuck = list(input())
    brainfuck.reverse()
    return brainfuck

def brainfuck_interpreter(brainfuck):
    brainfuck_translated = {}
    init_position = 0
    init_value = 0
    while brainfuck: # == True
        current_char = brainfuck.pop()
        brainfuck_translated[init_position] = init_value

        #if current_char == "[":
            #while brainfuck_translated.get(init_position) != 0

        if current_char == "<":
            init_position -= 1

        elif current_char == ">":
            init_position += 1

        elif current_char == "+":
            if brainfuck_translated.get(init_position) < 255:
                brainfuck_translated[init_position] += 1
            else:
                brainfuck_translated[init_position] = 0

        elif current_char == "-":
            if init_value > 0:
                init_value -= 1
            else:
                init_value = 255

        elif current_char == ".":
            print (chr(init_value))
            brainfuck_translated = {init_position, init_value}

        #elif current_char == ",":


        #else:



        brainfuck_translated = {init_value, current_char}
        # print (brainfuck_translated)

brainfuck_interpreter(get_input())
