#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = []
    x = 0
    for i in set_1:
        set_3.append(i)
    for k in set_2:
        set_3.append(k)
    while x < len(set_3) - 1:
        if set_3[x] == set_3[x + 1]:
            set_3[x] = ""
            set_3[x + 1] = ""
        x += 1
    return set_3
set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

