"""Stores values used in all drawing."""

from bunch import Bunch

# Short names for files.
D1r1, D1r2, D1r3 = "N1.jpg", "N2.jpg", "N3.jpg"
D1r4, D1r5, D1r6 = "N4.jpg", "N5.jpg", "N6.jpg"
D1r12, D1r123, D1r123456 = "N1_2.jpg", "N1_2_3.jpg", "N1_2_3_4_5_6.jpg"
D10 = "N0.jpg"

D3r1, D3r2, D3r3 = "N1n1n1.jpg", "N2n1n1.jpg", "N3n1n1.jpg"
D3r4, D3r5, D3r6 = "N4n1n1.jpg", "N5n1n1.jpg", "N6n1n1.jpg"
D3r12, D3r123, D3r123456 = "N1n1n1_2n1n1.jpg", "N1n1n1_2n1n1_3n1n1.jpg", "N1n1n1_2n1n1_3n1n1_4n1n1_5n1n1_6n1n1.jpg"
D30 = "N000.jpg"

D2t2, D2t3, D2t6 = "N1n1_2n1.jpg", "N1n1_2n1_3n1.jpg", "N1n1_2n1_3n1_4n1_5n1_6n1.jpg"
D2r2, D2r3, D2r6 = "N1n1_1n2.jpg", "N1n1_1n2_1n3.jpg", "N1n1_1n2_1n3_1n4_1n5_1n6.jpg"
D2rt2, D2rt3, D2rt6 = "N1n1_2n2.jpg", "N1n1_2n2_3n3.jpg", "N1n1_2n2_3n3_4n4_5n5_6n6.jpg"

equal = "equal.jpg"

width = 600
height = 600

f6_1 = [D1r1, D10, D10, D10, D10, D10]
f6_12 = [D1r1, D1r1, D10, D10, D10, D10]
f6_123 = [D1r1, D1r1, D1r1, D10, D10, D10]
f6_123456 = [D1r1, D1r1, D1r1, D1r1, D1r1, D1r1]

equations = ("3_plus_3.jpg", "6_minus_3.jpg", "3_times_2.jpg", "6_div_2.jpg")
operators = ("plus.jpg", "minus.jpg", "times.jpg", "div.jpg")

D1 = Bunch()
D1.t = Bunch()
D1.t.plus = [[D1r1, D1r1, D1r1], [D1r1, D1r1, D1r1], [D1r1, D1r1, D1r1], [D10, D10, D1r1], [D10, D10, D1r1], [D10, D10, D1r1]]

D1.t.minus = [[D1r1, D1r1, D1r1], [D1r1, D1r1, D1r1], [D1r1, D1r1, D1r1], [D1r1, D10, D10], [D1r1, D10, D10], [D1r1, D10, D10]]

D1.t.times = [[D1r1, D1r1, D1r1], [D1r1, D1r1, D1r1], [D1r1, D10, D1r1], [D10, D10, D1r1], [D10, D10, D1r1], [D10, D10, D1r1]]

D1.t.div = [[D1r1, D1r1, D1r1], [D1r1, D1r1, D1r1], [D1r1, D10, D1r1], [D1r1, D10, D10], [D1r1, D10, D10], [D1r1, D10, D10]]

D1.t.numbers = (D1.t.plus, D1.t.minus, D1.t.times, D1.t.div)

D1.r = Bunch()
D1.r.plus = [[D1r123, D1r123, D1r123456], [D10, D10, D10], [D10, D10, D10], [D10, D10, D10], [D10, D10, D10], [D10, D10, D10]]

D1.r.minus = [[D1r123456, D1r123, D1r123], [D10, D10, D10], [D10, D10, D10], [D10, D10, D10], [D10, D10, D10], [D10, D10, D10]]

D1.r.times = [[D1r123, D1r1, D1r123456], [D10, D1r1, D10], [D10, D10, D10], [D10, D10, D10], [D10, D10, D10], [D10, D10, D10]]

D1.r.div = [[D1r123456, D1r1, D1r123], [D10, D1r1, D10], [D10, D10, D10], [D10, D10, D10], [D10, D10, D10], [D10, D10, D10]]

D1.r.numbers = (D1.r.plus, D1.r.minus, D1.r.times, D1.r.div)

D1.m = Bunch()
D1.m.plus = [[D1r1, D1r1, D1r1], [D1r2, D1r2, D1r2], [D1r3, D1r3, D1r3], [D10, D10, D1r4], [D10, D10, D1r5], [D10, D10, D1r6]]

D1.m.minus = [[D1r1, D1r1, D1r1], [D1r2, D1r2, D1r2], [D1r3, D1r3, D1r3], [D1r4, D10, D10], [D1r5, D10, D10], [D1r6, D10, D10]]

D1.m.times = [[D1r1, D1r1, D1r1], [D1r2, D1r1, D1r2], [D1r3, D10, D1r3], [D10, D10, D1r4], [D10, D10, D1r5], [D10, D10, D1r6]]

D1.m.div = [[D1r1, D1r1, D1r1], [D1r2, D1r1, D1r2], [D1r3, D10, D1r3], [D1r4, D10, D10], [D1r5, D10, D10], [D1r6, D10, D10]]

D1.m.numbers = (D1.m.plus, D1.m.minus, D1.m.times, D1.m.div)

D2_constant_time_numbers = ([D2t3, D2t3, D2t6], [D2t6, D2t3, D2t3], [D2t3, D2t2, D2t6], [D2t6, D2t2, D2t3])
D2_constant_space_numbers = ([D2r3, D2r3, D2r6], [D2r6, D2r3, D2r3], [D2r3, D2t2, D2r6], [D2r6, D2t2, D2r3])
D2_constant_motion_numbers = ([D2rt3, D2rt3, D2rt6], [D2rt6, D2rt3, D2rt3], [D2rt3, D2t2, D2rt6], [D2rt6, D2t2, D2rt3])



D3 = Bunch()
D3.t = Bunch()
D3.t.plus = [[D3r1, D3r1, D3r1], [D3r1, D3r1, D3r1], [D3r1, D3r1, D3r1], [D30, D30, D3r1], [D30, D30, D3r1], [D30, D30, D3r1]]

D3.t.minus = [[D3r1, D3r1, D3r1], [D3r1, D3r1, D3r1], [D3r1, D3r1, D3r1], [D3r1, D30, D30], [D3r1, D30, D30], [D3r1, D30, D30]]

D3.t.times = [[D3r1, D3r1, D3r1], [D3r1, D3r1, D3r1], [D3r1, D30, D3r1], [D30, D30, D3r1], [D30, D30, D3r1], [D30, D30, D3r1]]

D3.t.div = [[D3r1, D3r1, D3r1], [D3r1, D3r1, D3r1], [D3r1, D30, D3r1], [D3r1, D30, D30], [D3r1, D30, D30], [D3r1, D30, D30]]

D3.t.numbers = (D3.t.plus, D3.t.minus, D3.t.times, D3.t.div)



plane_t = Bunch()
plane_t.equation = "3_plus_3.jpg"
plane_t.operator = "plus.jpg"
plane_t.numbers = [D2t3, D2t3, D2t6]
plane_t.file_name = "plane_t"
plane_t.file_names = ("plane_t_plus.gif", "plane_t_minus.gif", "plane_t_times.gif", "plane_t_div.gif", )
