"""Stores values used in all drawing."""

from bunch import Bunch
import matplotlib.font_manager

convert = "/usr/local/bin/convert"

# Short names for files.
p0, q0 = "pure_0.jgp", "qft_0.jpg"
p1, p2, p3 = "pure_1.jpg", "pure_2.jpg", "pure_3.jpg"
p4, p5, p6 = "pure_4.jpg", "pure_5.jpg", "pure_6.jpg"
q1, q2, q3 = "qft_1.jpg", "qft_2.jpg", "qft_3.jpg"
q4, q5, q6 = "qft_4.jpg", "qft_5.jpg", "qft_6.jpg"


d1r1, d1r2, d1r3 = "N1.jpg", "N2.jpg", "N3.jpg"
d1r4, d1r5, d1r6 = "N4.jpg", "N5.jpg", "N6.jpg"
d1r12, d1r123, d1r123456 = "N1_2.jpg", "N1_2_3.jpg", "N1_2_3_4_5_6.jpg"
d10 = "N0.jpg"

d3t1, d3t2, d3t3 = "N1n1n1.jpg", "N2n1n1.jpg", "N3n1n1.jpg"
d3t4, d3t5, d3t6 = "N4n1n1.jpg", "N5n1n1.jpg", "N6n1n1.jpg"
d3t12, d3t123, d3t123456 = "N1n1n1_2n1n1.jpg", "N1n1n1_2n1n1_3n1n1.jpg", "N1n1n1_2n1n1_3n1n1_4n1n1_5n1n1_6n1n1.jpg"
d30 = "N000.jpg"

d3r1, d3r2, d3r3 = "N1n1n1.jpg", "N1n2n1.jpg", "N1n3n1.jpg"
d3r4, d3r5, d3r6 = "N1n4n1.jpg", "N1n5n1.jpg", "N1n6n1.jpg"
d3r12, d3r123, d3r123456 = "N1n1n1_1n2n1.jpg", "N1n1n1_1n2n1_1n3n1.jpg", "N1n1n1_1n2n1_1n3n1_1n4n1_1n5n1_1n6n1.jpg"
d30 = "N000.jpg"

d3m1, d3m2, d3m3 = "N1n1n1_bigger.jpg", "N2n2n1.jpg", "N3n3n1.jpg"
d3m4, d3m5, d3m6 = "N4n4n1.jpg", "N5n5n1.jpg", "N6n6n1.jpg"
d3m12, d3m123, d3m123456 = "N1n1n1_2n2n1.jpg", "N1n1n1_2n2n1_3n3n1.jpg", "N1n1n1_2n2n1_3n3n1_4n4n1_5n5n1_6n6n1.jpg"
d30_bigger = "N000_bigger.jpg"

d2t2, d2t3, d2t6 = "N1n1_2n1.jpg", "N1n1_2n1_3n1.jpg", "N1n1_2n1_3n1_4n1_5n1_6n1.jpg"
d2r2, d2r3, d2r6 = "N1n1_1n2.jpg", "N1n1_1n2_1n3.jpg", "N1n1_1n2_1n3_1n4_1n5_1n6.jpg"
d2rt2, d2rt3, d2rt6 = "N1n1_2n2.jpg", "N1n1_2n2_3n3.jpg", "N1n1_2n2_3n3_4n4_5n5_6n6.jpg"

equal = "equal.jpg"

width = 300
height = 300

f6_1 = [d1r1, d10, d10, d10, d10, d10]
f6_12 = [d1r1, d1r1, d10, d10, d10, d10]
f6_123 = [d1r1, d1r1, d1r1, d10, d10, d10]
f6_123456 = [d1r1, d1r1, d1r1, d1r1, d1r1, d1r1]

equations = ("3_plus_3.jpg", "6_minus_3.jpg", "3_times_2.jpg", "6_div_2.jpg")
operators = ("plus.jpg", "minus.jpg", "times.jpg", "div.jpg")

d1 = Bunch()
d1.t = Bunch()
d1.t.plus = [[d1r1, d1r1, d1r1], [d1r1, d1r1, d1r1], [d1r1, d1r1, d1r1], [d10, d10, d1r1], [d10, d10, d1r1], [d10, d10, d1r1]]

d1.t.minus = [[d1r1, d1r1, d1r1], [d1r1, d1r1, d1r1], [d1r1, d1r1, d1r1], [d1r1, d10, d10], [d1r1, d10, d10], [d1r1, d10, d10]]

d1.t.times = [[d1r1, d1r1, d1r1], [d1r1, d1r1, d1r1], [d1r1, d10, d1r1], [d10, d10, d1r1], [d10, d10, d1r1], [d10, d10, d1r1]]

d1.t.div = [[d1r1, d1r1, d1r1], [d1r1, d1r1, d1r1], [d1r1, d10, d1r1], [d1r1, d10, d10], [d1r1, d10, d10], [d1r1, d10, d10]]

d1.t.numbers = [d1.t.plus, d1.t.minus, d1.t.times, d1.t.div]

d1.r = Bunch()
d1.r.plus = [[d1r123, d1r123, d1r123456], [d10, d10, d10], [d10, d10, d10], [d10, d10, d10], [d10, d10, d10], [d10, d10, d10]]

d1.r.minus = [[d1r123456, d1r123, d1r123], [d10, d10, d10], [d10, d10, d10], [d10, d10, d10], [d10, d10, d10], [d10, d10, d10]]

d1.r.times = [[d1r123, d1r1, d1r123456], [d10, d1r1, d10], [d10, d10, d10], [d10, d10, d10], [d10, d10, d10], [d10, d10, d10]]

d1.r.div = [[d1r123456, d1r1, d1r123], [d10, d1r1, d10], [d10, d10, d10], [d10, d10, d10], [d10, d10, d10], [d10, d10, d10]]

d1.r.numbers = (d1.r.plus, d1.r.minus, d1.r.times, d1.r.div)

d1.m = Bunch()
d1.m.plus = [[d1r1, d1r1, d1r1], [d1r2, d1r2, d1r2], [d1r3, d1r3, d1r3], [d10, d10, d1r4], [d10, d10, d1r5], [d10, d10, d1r6]]

d1.m.minus = [[d1r1, d1r1, d1r1], [d1r2, d1r2, d1r2], [d1r3, d1r3, d1r3], [d1r4, d10, d10], [d1r5, d10, d10], [d1r6, d10, d10]]

d1.m.times = [[d1r1, d1r1, d1r1], [d1r2, d1r1, d1r2], [d1r3, d10, d1r3], [d10, d10, d1r4], [d10, d10, d1r5], [d10, d10, d1r6]]

d1.m.div = [[d1r1, d1r1, d1r1], [d1r2, d1r1, d1r2], [d1r3, d10, d1r3], [d1r4, d10, d10], [d1r5, d10, d10], [d1r6, d10, d10]]

d1.m.numbers = (d1.m.plus, d1.m.minus, d1.m.times, d1.m.div)

pure_numbers = [[p3, p3, p6], [p6, p3, p3], [p3, p2, p6], [p6, p2, p3]]
qft_numbers = [[q3, q3, q6], [q6, q3, q3], [q3, q2, q6], [q6, q2, q3]]

d2_constant_numbers = Bunch()
d2_constant_numbers.t = [[d2t3, d2t3, d2t6], [d2t6, d2t3, d2t3], [d2t3, d2t2, d2t6], [d2t6, d2t2, d2t3]]
d2_constant_numbers.r = ([d2r3, d2r3, d2r6], [d2r6, d2r3, d2r3], [d2r3, d2t2, d2r6], [d2r6, d2t2, d2r3])
d2_constant_numbers.m = ([d2rt3, d2rt3, d2rt6], [d2rt6, d2rt3, d2rt3], [d2rt3, d2t2, d2rt6], [d2rt6, d2t2, d2rt3])



d3 = Bunch()
d3.t = Bunch()
d3.t.plus = [[d3t1, d3t1, d3t1], [d3t1, d3t1, d3t1], [d3t1, d3t1, d3t1], [d30, d30, d3t1], [d30, d30, d3t1], [d30, d30, d3t1]]

d3.t.minus = [[d3t1, d3t1, d3t1], [d3t1, d3t1, d3t1], [d3t1, d3t1, d3t1], [d3t1, d30, d30], [d3t1, d30, d30], [d3t1, d30, d30]]

d3.t.times = [[d3t1, d3t1, d3t1], [d3t1, d3t1, d3t1], [d3t1, d30, d3t1], [d30, d30, d3t1], [d30, d30, d3t1], [d30, d30, d3t1]]

d3.t.div = [[d3t1, d3t1, d3t1], [d3t1, d3t1, d3t1], [d3t1, d30, d3t1], [d3t1, d30, d30], [d3t1, d30, d30], [d3t1, d30, d30]]

d3.t.numbers = (d3.t.plus, d3.t.minus, d3.t.times, d3.t.div)


d3.r = Bunch()
d3.r.plus = [[d3r123, d3r123, d3r123456], [d30, d30, d30], [d30, d30, d30], [d30, d30, d30], [d30, d30, d30], [d30, d30, d30]]

d3.r.minus = [[d3r123456, d3r123, d3r123], [d30, d30, d30], [d30, d30, d30], [d30, d30, d30], [d30, d30, d30], [d30, d30, d30]]

d3.r.times = [[d3r123, d3r1, d3r123456], [d30, d3r1, d30], [d30, d30, d30], [d30, d30, d30], [d30, d30, d30], [d30, d30, d30]]

d3.r.div = [[d3r123456, d3r1, d3r123], [d30, d3r1, d30], [d30, d30, d30], [d30, d30, d30], [d30, d30, d30], [d30, d30, d30]]

d3.r.numbers = (d3.r.plus, d3.r.minus, d3.r.times, d3.r.div)

d3.m = Bunch()
d3.m.plus = [[d3m1, d3m1, d3m1], [d3m2, d3m2, d3m2], [d3m3, d3m3, d3m3], [d30_bigger, d30_bigger, d3m4], [d30_bigger, d30_bigger, d3m5], [d30_bigger, d30_bigger, d3m6]]

d3.m.minus = [[d3m1, d3m1, d3m1], [d3m2, d3m2, d3m2], [d3m3, d3m3, d3m3], [d3m4, d30_bigger, d30_bigger], [d3m5, d30_bigger, d30_bigger], [d3m6, d30_bigger, d30_bigger]]

d3.m.times = [[d3m1, d3m1, d3m1], [d3m2, d3m1, d3m2], [d3m3, d30_bigger, d3m3], [d30_bigger, d30_bigger, d3m4], [d30_bigger, d30_bigger, d3m5], [d30_bigger, d30_bigger, d3m6]]

d3.m.div = [[d3m1, d3m1, d3m1], [d3m2, d3m1, d3m2], [d3m3, d30_bigger, d3m3], [d3m4, d30_bigger, d30_bigger], [d3m5, d30_bigger, d30_bigger], [d3m6, d30_bigger, d30_bigger]]

d3.m.numbers = (d3.m.plus, d3.m.minus, d3.m.times, d3.m.div)

# Font stuff.
FM = matplotlib.font_manager.FontManager()
font = FM.findfont(r'Times New Roman')
font_size = int( 32 * height / 600)
