#я списал этот код у Алии, потому что я запутался в задании
def update_dictionary(d, key, value):
    if len(d) == 0:
        d[2 * key] = [value]
    else:
        if key in d:
            d[key].append(value)
        elif 2 * key in d:
            d[2 * key].append(value)
        else:
            d[2 * key] = value

