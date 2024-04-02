def well(x: list):
    good = x.count('good')
    if good == 0:
        return 'Fail!'
    elif good == 1 or good == 2:
        return 'Publish!'
    return 'I smell a series!'
    
'best'
# def well(x):
    # c = x.count('good')
    # return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'