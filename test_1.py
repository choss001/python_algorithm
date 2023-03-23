year = 2016
event = 'Referendum'
f'Results of the {year} {event}'


transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed

[[row[i] for row in matrix] for i in range(4)]
