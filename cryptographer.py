def tableDyct():
    table = {}
    tableEnds = False
    while not tableEnds:
        inputSymbols = input()  # input corresponding simbols for table1
        if inputSymbols == 'STOP' or inputSymbols == 'HALT' or inputSymbols == 'END':
            table['flag'] = inputSymbols
            tableEnds = True
        else:
            symbols = inputSymbols.split()
            table[symbols[0]] = symbols[-1]

    return table

def encryptFirst(tables, string):
    for table in tables:
        if 'STOP' in table['flag']:
            for key, value in table.items():
                if key in string:
                    string = string.replace(key, value)
                    STRING = [char for char in string]
    return STRING

def encryptSecond(tables, STRING):
    for table in tables:
        if 'HALT' in table['flag']:
            for index in range(0, len(STRING), 2):
                if STRING[index] in table:
                    STRING[index] = table[STRING[index]]
    return STRING

def encryptThird(tables, STRING):
    result = ''
    for table in tables:
        if 'END' in table['flag']:
            for index in range(0, len(STRING), 3):
                if STRING[index] in table:
                    STRING[index] = table[STRING[index]]
    result = ''.join(STRING)
    return result

table1 = tableDyct()
table2 = tableDyct()
table3 = tableDyct()
tables = [table1, table2, table3]
message = input()

firtList = encryptFirst(tables, message)
secList = encryptSecond(tables, firtList)
thirthList = encryptThird(tables, secList)
print(thirthList)