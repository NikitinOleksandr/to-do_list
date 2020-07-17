def tracklist(**kwargs):
    for key, value in kwargs.items():
        print(key)
        for new_key in kwargs[key]:
            print("ALBUM:", new_key, "TRACK:", value[new_key])
