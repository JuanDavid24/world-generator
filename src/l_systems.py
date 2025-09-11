import turtle as tr

def sentence_generator(axiom, rules, n):
    for _ in range(n):
        sentence = ""
        for symbol in axiom:
            if symbol in rules:
                sentence += rules[symbol]
            else: 
                sentence += symbol
        axiom = sentence
    return sentence                

def plant_plotter(sentence, step, angle, speed=6, branch_color="white", leaf_color="green", leaf_width=1.0, leaf_length=1.0, animation=True):
    # setup
    screen = tr.Screen()
    window_w = screen.window_width()
    window_h = screen.window_height()
    tr.left(90)
    tr.teleport(-window_w/2 + 10, -window_h/2 + 10)
    tr.screensize(bg="black")
    tr.color(branch_color)
    tr.write(sentence, font=("Arial", 8, "normal"))
    tr.teleport(0, -window_h/2 + 30)
    tr.tracer(animation)
    tr.speed(speed)
    tr.shapesize(leaf_width, leaf_length) # leaves size (width, size)

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
            case "L":
                tr.color(leaf_color)
                tr.stamp()
                tr.color(branch_color)
    tr.done()
