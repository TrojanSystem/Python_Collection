from prettytable import PrettyTable

x = PrettyTable()

y = PrettyTable()

x.add_column('Pokemon Name', ["Pikachu", 'Squirtle', 'Charmander'])
x.add_column('Type', ["Electric", 'Water', 'Fire'])
x.align = 'l'
x.header_style = 'title'
print(x)

print(' ')


y.add_column('Tic', ["1", '4', '7'])
y.add_column('Tac', ["2", '5', '8'])
y.add_column('Toe', ["3", '6', '9'])
print(y)


