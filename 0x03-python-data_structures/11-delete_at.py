#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    temp = []
    for i in range(len(my_list)):
        if i != idx:
            temp.append(my_list[i])
    my_list[:] = temp

    return my_list
