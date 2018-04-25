def one_dimension_overlap(x1,dim1,x2,dim2):
    greater=max(x1,x2)
    lower=min(x1+dim1,x2+dim2)

    if greater>=lower:
        return (None,None)

    overlap=lower-greater

    return (greater,overlap)


def calc_rect_overlap(r1,r2):
    x_overlap,w_overlap=one_dimension_overlap(r1["x"],r1["w"],r2["x"],r2["w"])
    y_overlap,h_overlap=one_dimension_overlap(r1["y"],r1["h"],r2["y"],r2["h"])
    if w_overlap is None or h_overlap is None:
        print("There is no overlap")
        return
    return {"x":x_overlap,"y":y_overlap,"w":w_overlap,"h":h_overlap}



r1 = {'x': 2 , 'y': 4,'w':5,'h':12}
r2 = {'x': 1 , 'y': 5,'w':7,'h':14}
print(calc_rect_overlap(r1,r2))
