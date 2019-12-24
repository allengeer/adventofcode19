def import_text_file(filename: str, parse_function = lambda x: x):
    f = open(filename, "r")
    f1 = f.readlines()
    return list(map(parse_function, map(lambda x: x.strip(), f1)))