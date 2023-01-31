squares = []
for i in range(1,11):
    squares.append(i*i)
    print(squares)
    #yukarıdaki kod dizinini list comp.kullanrak aşşağıda yapalım
squares = [i * i for i in range(1,11)]
squares
