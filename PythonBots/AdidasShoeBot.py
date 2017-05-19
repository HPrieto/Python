# base URL = http://www.adidas.com/us/BB9043.html?forceSelSize=BB9043_600


def URLGen(model, size):
    BaseSize = 580
    # Base Size is for shoe size 6.5
    ShoeSize = size - 6.5
    ShoeSize = ShoeSize * 20
    RawSize = ShoeSize + BaseSize
    ShoeSizeCode = int(RawSize)
    URL = 'http://www.adidas.com/us/' + \
        str(model) + '.html?foreceSelSize=' + str(model) + ' ' + str(ShoeSizeCode)
    return URL


"""
Model = raw_input('Model #')
Size  = input('Size: ')
URL   = URLGen(Model,Size)

print(str(URL))
"""
