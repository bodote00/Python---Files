def read_points(text, separator=";"):
    """Reads points from text, splits them by a separator and returns a list of them at the end"""    
    points_list = []
    
    for point in text.split(separator):
        x, y = point.split(",") 
        points_list.append({"x": float(x), "y": float(y)})   
    return points_list 