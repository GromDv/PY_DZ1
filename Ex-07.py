# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
state = [0,1]
for x in state:
    for y in state:
        for z in state:
            print( x,",",y,",",z," ", not(x or y or z) == (not(x) and not(y) and not(z)))