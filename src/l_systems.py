import turtle as tr

def sentence_generator(axiom, rules, iterations):
    for i in range(iterations):
        sentence = ""
        for symbol in axiom:
            if symbol in rules:
                sentence += rules[symbol]
            else: 
                sentence += symbol
        axiom = sentence
    return sentence                

def plant_plotter(sentence, step, angle):
    # setup
    screen = tr.Screen()
    window_w = screen.window_width()
    window_h = screen.window_height()
    tr.left(90)
    tr.teleport(-window_w/2 + 10, -window_h/2 + 10)
    tr.screensize(bg="black")
    tr.color("white")
    tr.write(sentence, font=("Arial", 8, "normal"))
    tr.teleport(0, -window_h/2 + 30)

    turtle_stack = []  # save turtle states (position and heading) checkpoints in a stack
    for symbol in sentence:
        match symbol:                
            case "F":
                tr.forward(step)
            case "+":
                tr.right(angle)
            case "-":
                tr.left(angle)
            case "[":
                turtle_stack.append((tr.pos(), tr.heading()))
            case "]":
                (target_x, target_y), heading = turtle_stack.pop()
                tr.teleport(target_x, target_y)
                tr.seth(heading)
                
    tr.done()
