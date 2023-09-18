import matplotlib.pyplot as plt

population = [2972, 1622, 1570, 1579, 1469, 1426, 1436, 1374, 1292, 1303, 1265, 1253, 1218, 1170, 1165, 1142, 1051, 1061, 1006, 971, 984, 947, 1013, 994, 1050, 1071, 1051, 1080, 1059, 1012, 959, 979, 913, 917, 921, 930, 845, 874, 866, 889, 860, 842, 853, 884, 809, 787, 789, 775, 813, 815, 871, 825, 840, 831, 818, 835, 859, 858, 902, 890, 835, 864, 843, 845, 863, 818, 852, 837, 843, 837, 866, 827, 836, 802, 844, 804, 856, 826, 906, 788, 864, 801, 829, 772, 820, 781, 784, 778, 748, 714, 730, 695, 747, 692, 760, 731, 700, 717, 708, 721, 676, 723, 664, 706, 650, 686, 663, 687, 689]

x = population
y = [n for n in range(len(x))]

plt.bar(y, x, width=1)
plt.legend()
plt.xlabel('time')
plt.ylabel('population')
plt.show()