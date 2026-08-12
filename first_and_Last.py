def first_and_last(value):
    if value == "":
        return {"first": "", "last": ""}
    first = value[0]
    last = value[-1]
    return {
        "first": first,
        "last": last
    }