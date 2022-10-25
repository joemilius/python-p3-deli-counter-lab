def line(list):
    if(len(list) >= 1):
        line_order = 'The line is currently:'
        line_number = 1
        for name in list:
            line_order = line_order + f' {line_number}. {name}'
            line_number += 1
        print(line_order)
        return line_order
    else:
        print("The line is currently empty.")
        return "The line is currently empty."


def take_a_number(list, name):
    list.append(name)
    print(f'Welcome, {name}. You are number {len(list)} in line.')
    pass


def now_serving(list):
    if(len(list) == 0):
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {list[0]}.')
        list.pop(0)

    pass