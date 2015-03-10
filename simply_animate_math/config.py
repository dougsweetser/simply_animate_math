"""Stores values used in all drawing."""

from bunch import Bunch

# Short names for files.
D1t2, D1t3, D1t6 = "N1_2_3.jpg", "N1_2_3.jpg", "N1_2_3_4_5_6.jpg"

D2t2, D2t3, D2t6 = "N1n1_2n1_3n1.jpg", "N1n1_2n1_3n1.jpg", "N1n1_2n1_3n1_4n1_5n1_6n1.jpg"
D2r2, D2r3, D2r6 = "N1n1_1n2_1n3.jpg", "N1n1_1n2_1n3.jpg", "N1n1_1n2_1n3_1n4_1n5_1n6.jpg"
D2rt2, D2rt3, D2rt6 = "N1n1_2n2_3n3.jpg", "N1n1_2n2_3n3.jpg", "N1n1_2n2_3n3_4n4_5n5_6n6.jpg"

equal = "equal.jpg"

width = 600
height = 600

plane_t = Bunch()
plane_t.equation = "3_plus_3.jpg"
plane_t.operator = "plus.jpg"
plane_t.numbers = [D2t3, D2t3, D2t6]
plane_t.footer = "Constant Time Addition"
