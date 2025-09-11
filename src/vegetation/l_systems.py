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
