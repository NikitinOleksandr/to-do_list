def tallest_people(**kwargs):
    for name, height in sorted(kwargs.items()):
        if height == max(kwargs.values()):
            print(name, ":", height)
