for i in range(10):
    a = input()
    if a == "END":
        break

    new_a = []
    for elem in a:
        new_a.append(elem)
        
    for elem in new_a[::-1]:
        print(elem, end = "")
    print()