def transform(w, h, iw, ih):
    if iw < ih:
        H = h
        W = round((h / ih) * iw)
        return (W, H)
    elif iw > ih:
        H = round((w / iw) * ih)
        W = w
        return (W, H)
    else:
        return (iw, ih)
