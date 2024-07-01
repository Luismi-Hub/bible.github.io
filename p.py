import os

# Leer la plantilla HTML
with open('template.html', 'r') as file:
    template = file.read()

# Generar archivos HTML
for i in range(1, 5):
    puzzle_html = template.replace('{{PUZZLE_NUMBER}}', str(i))
    with open(f'{i}.html', 'w') as file:
        file.write(puzzle_html)

print('Se han generado 100 archivos HTML.')
