
def calcVal(disp):
    val1 = val2= val3= val4 = 0
    tPixels = 240*320
    
    for i in range (0,240):
        for j in range (0, 320):
            val1 += disp[i][j]

    for i in range (0,240):
        for j in range (320, 640):
            val2 += disp[i][j]

    for i in range (240,480):
        for j in range (0, 320):
            val3 += disp[i][j]

    for i in range (240, 480):
        for j in range (320, 640):
            val4 += disp[i][j]
            
    val1 /= tPixels
    val2 /= tPixels
    val3 /= tPixels
    val4 /= tPixels
    return val1, val2, val3, val4
