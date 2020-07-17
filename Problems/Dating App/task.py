def select_dates(potential_dates):
    names = []
    for value in potential_dates:
        if value["age"] > 30 and value["city"] == "Berlin" and "art" in value["hobbies"]:
            names.append(value["name"])
    return ", ".join(names)
