# KaryaGrafisku.py : merupakan program dengan menampilkan gambar warna analogous.
# Hafidul Umam, 21 Oktober 2018

from graphics import *
import math
rad = float(math.pi)/float(180)

win = GraphWin('Analogous', 850,600)
win.setBackground(color_rgb(226,121,5))
win.setCoords(-4.25,-3, 4.25,3)
pusat = Point(0,0)

grad = 0.8

# segitiga kiri atas pojok 
x1a = -4.25; y1a = 3; y2a = 2
warna_a = (color_rgb(198,157,19),color_rgb(211,169,20), color_rgb(235,190,37),color_rgb(239,204,82),color_rgb(242,214,113),\
           color_rgb(244,221,138), color_rgb(245,224,150),color_rgb(247,227,159), color_rgb(248,232,175),color_rgb(250,238,199))

for a in range(10):
    tr = Polygon(Point(x1a,y1a), Point(x1a,y2a), Point(x1a+((float(y1a-y2a)/float(grad))), y1a))
    tr.setFill(warna_a[a])
    tr.setOutline('white')
    tr.draw(win)
    y1a -= 0.3; y2a -= 0.2

# segitiga melingkar tengah
x1b = -2.25; y1b = 3; y2b = 2
warna_b = (color_rgb(153,89,2),color_rgb(168,98,2), color_rgb(183,106,2),color_rgb(208,121,2),color_rgb(227,132,2),\
           color_rgb(253,148,6), color_rgb(253,157,28),color_rgb(253,166,47), color_rgb(253,176,72),color_rgb(253,188,100))

for b in range(10):
    tr = Polygon(Point(x1b,y1b), Point(x1b, y2b), Point(x1b+((float(y1b-y2b)/float(grad))), y1b))
    tr.setFill(warna_b[b])
    tr.setOutline('white')
    tr.draw(win)
    x1b = 2*math.cos(x1b); y1b = 2*math.sin(y1b); y2b = 3*math.sin(2*y2b)
    y1b -= 1; y2b -= 1

# segitiga kanan atas
x1c = 3; y1c = 3; y2c = 2
warna_c = (color_rgb(211,31,5),color_rgb(237,34,5), color_rgb(250,36,5))

for c in range(3):
    tr = Polygon(Point(x1c,y1c), Point(x1c,y2c), Point(x1c+((float(y1c-y2c)/float(grad))), y1c))
    tr.setFill(warna_c[c])
    tr.setOutline('white')
    tr.draw(win)
    y1c -= 0.3; y2c -= 0.2

# segitiga kanan bawah
x1d = 4; y1d = -2; y2d = 0
warna_d = (color_rgb(251,87,64), color_rgb(251,104,83),color_rgb(251,115,96), color_rgb(252,123,105),color_rgb(252,145,129))

for d in range(5):
    tr = Polygon(Point(x1d,y1d), Point(x1d,y2d), Point(x1d+((float(y1d-y2d)/float(grad))), y1d))
    tr.setFill(warna_d[d])
    tr.setOutline('white')
    tr.draw(win)
    x1d -= 0.5; y1d -= 0.5; y2d -= 0.75


# kotak kiri atas kr
x1_1 = -4.25 ; x2_1 = -3.5 ; y1_1 = 1 ; y2_1 = 0
warna1_1 = (color_rgb(235,183,1),color_rgb(254,199,7), color_rgb(254,202,24),color_rgb(254,206,41),color_rgb(254,209,54),\
            color_rgb(254,214,73))

for e in range(6):
    p = Polygon(Point(x1_1,y1_1), Point(x1_1,y2_1), Point(x2_1,grad*(x2_1-x1_1)+y2_1), Point(x2_1,grad*(x2_1-x1_1)+y1_1))
    p.setFill(warna1_1[e])
    p.setOutline('white')
    p.draw(win)
    x1_1 += 0.25 ; x2_1 += 0.25 ; y1_1 += 0.25 ; y2_1 += 0.25

# kotak kiri atas kn
x1_2 = -3.5 ; x2_2 = -3 ; y1_2 = 1.5 ; y2_2 = 0.5
warna1_2 = (color_rgb(177,151,44),color_rgb(194,165,48), color_rgb(206,176,55),color_rgb(208,180,64),color_rgb(213,187,83),\
            color_rgb(215,190,91))

for f in range(6):
    p = Polygon(Point(x1_2,y1_2), Point(x1_2,y2_2), Point(x2_2,grad*(x2_2-x1_2)+y2_2), Point(x2_2,grad*(x2_2-x1_2)+y1_2))
    p.setFill(warna1_2[f])
    p.setOutline('white')
    p.draw(win)
    x1_2 += 0.25 ; x2_2 += 0.25 ; y1_2 += 0.25 ; y2_2 += 0.25

# segitiga kiri atas
x1_3 = -3.5 ; x2_3 = -3 ; y1_3 = 1.5 ; y2_3 = 0.5
warna1_3 = (color_rgb(157,53,28),color_rgb(168,57,30), color_rgb(187,65,34),color_rgb(200,69,36),color_rgb(217,78,43),\
            color_rgb(221,97,66), color_rgb(223,107,79), color_rgb(226,119,92))

for g in range(8):
    p = Polygon(Point(x1_3,y1_3), Point(x2_3,grad*(x2_3-x1_3)+y2_3), Point(x2_3,-grad*(x2_3-x1_3)+y1_3))
    p.setFill(warna1_3[g])
    p.setOutline('white')
    p.draw(win)
    x1_3 += 0.25 ; x2_3 += 0.25 ; y1_3 += 0.25 

# segitiga tengah
x1_4 = -3.5 ; x2_4 = 3.5 ; y1_4 = -2
warna1_4 = (color_rgb(81,57,2),color_rgb(100,70,2), color_rgb(126,89,3),color_rgb(156,111,3))

for h in range(4):
    p = Polygon(Point(x1_4,y1_4), Point(x2_4, y1_4), Point(x2_4-(0.5*(x2_4-x1_4)), y1_4+(grad*((x2_4-(0.5*(x2_4-x1_4)))-x1_4))))
    p.setFill(warna1_4[h])
    p.setOutline('white')
    p.draw(win)
    x1_4 += 0.5; y1_4 += 0


# kotak tengah
x1_5 = -4.5 ; x2_5 = -4 ; y1_5 = -3; y2_5 = -2.5
warna1_5 = (color_rgb(194,104,3),color_rgb(208,112,4), color_rgb(225,120,4),color_rgb(251,143,26),color_rgb(251,160,60),\
            color_rgb(252,169,78))

for i in range(6):
    p = Polygon(Point(x1_5, y1_5), Point(2+x2_5, y1_5), Point(2+x2_5,2+y2_5), Point(x1_5, 2+y2_5))
    p.setFill(warna1_5[i])
    p.setOutline('white')
    p.draw(win)
    x1_5 = math.cos(x1_5)-math.cos(4*x1_5); x2_5 = math.cos(x2_5*x2_5)
    y1_5 = 2*math.sin(y1_5); y2_5 = math.sin(y2_5)
    x1_5 += 0.5; x2_5 += 0.4; y1_5 += 0; y2_5 += 0.3
    
# lingkaran lapis atas
r1 = 2 ; x1 = 2 ; y1 = 1.5
warna1 = (color_rgb(142,23,6),color_rgb(168,27,6), color_rgb(180,29,7))

for j in range(3):
    li1 = Circle(Point(x1,y1), r1)
    li1.setFill(warna1[j])
    li1.setOutline('white')
    li1.draw(win)
    r1 -= 0.5 ; x1 += 0.45 ; y1 -= 0.25

# balok atas
k1 = Polygon(Point(-2,-3),Point(-1,-3),Point(4.25,grad*(4.25+1)-3),Point(4.25,grad*(4.25+2)-3))
k1.setFill(color_rgb(153,24,21))
k1.setOutline('white')
k1.draw(win)

# balok bawah
a2 = Polygon(Point(-1,-3),Point(-0.25,-3),Point(4.25,grad*(4.25+0.25)-3),Point(4.25,grad*(4.25+1)-3))
a2.setFill(color_rgb(204,32,28))
a2.setOutline('white')
a2.draw(win)

# lingkaran lapis bawah
r2 = 1.5 ; x2 = -3
warna2 = (color_rgb(185,92,5),color_rgb(207,101,5), color_rgb(236,116,6))

for k in range(3):
    li2 = Circle(Point(x2,-3), r2)
    li2.setFill(warna2[k])
    li2.setOutline('white')
    li2.draw(win)
    r2 -= 0.5; x2 += 0.5

# lingkaran ke atas
r3 = 0.5 ; y3 = -3
warna3 = (color_rgb(160,102,14),color_rgb(172,109,15), color_rgb(193,123,17),color_rgb(204,130,17),color_rgb(221,140,19),\
          color_rgb(233,148,20),color_rgb(236,155,34))

for l in range(7):
    li3 = Circle(Point(3.5,y3), r3)
    li3.setFill(warna3[l])
    li3.setOutline('white')
    li3.draw(win)
    r3 -= 0.075; y3 += 1

# lingkaran melingkar atas
sudut1 = 110
warna4 = (color_rgb(147,55,11),color_rgb(158,60,12), color_rgb(179,67,13),color_rgb(192,72,14),color_rgb(202,75,15),\
            color_rgb(224,84,16))

for m in range(6):
    xx = 2*math.cos(rad*sudut1)
    yy = 2*-math.sin(rad*sudut1)
    cp = Point(xx+1,yy+1.5)
    sl = Circle(cp, 0.35)
    sl.setFill(warna4[m])
    sl.setOutline('white')
    sl.draw(win)
    sudut1 += 45

# lingkarang melingkar bawah
sudut2 = 110
warna5 = (color_rgb(198,60,13),color_rgb(209,63,14), color_rgb(227,68,15),color_rgb(239,75,20),color_rgb(240,90,40),\
            color_rgb(242,105,60), color_rgb(243,116,73), color_rgb(224,130,91))

for n in range(8):
    xx = 3*math.cos(rad*sudut2)
    yy = 2*-math.sin(rad*sudut2)
    cp = Point(xx-1,yy-1.5)
    sl2 = Circle(cp, 0.35)
    sl2.setFill(warna5[n])
    sl2.setOutline('white')
    sl2.draw(win)
    sudut2 += 45

Rectangle(Point(-4.25,-3),Point(4.25,3)).draw(win)

try:
    raw_input("Klik 'Enter' untuk mengakhri...")
except:
    input("Klik 'Enter' untuk mengakhri...")

win.close()
