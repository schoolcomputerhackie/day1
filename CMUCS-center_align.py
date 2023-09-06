def convert_coords(xin, yin):
    middle = [200, 200]
    # 0, 0 becomes -200, -200 due to linear expansion
    # therefore max boundary = 200, -200 (max area 400)
    xin += 200
    yin += 200
    return [xin, yin]
    
def convertedCircle(xin, yin, radius, rgblist=None):
    converted = convert_coords(xin, yin)
    if rgblist == None:
        color = rgb(0, 0, 0)
    else:
        color = rgb(rgblist[0], rgblist[1], rgblist[2])
    Circle(converted[0], converted[1], radius, fill=color)
    
#convertedCircle(0, 0, 50, [0, 0, 0])
