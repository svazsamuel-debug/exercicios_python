def fatorial(n, show=False):
    fat = 1
    for c in range(n, 0, -1):
        fat = fat * c
        if show:
            if c > 1:
                print(f'{c}', end=' x ')
            elif c == 1:
                print(f'{c}', end=' = ')
    return f'{fat}'

#Programa Principal
print(fatorial(10, show = True))
