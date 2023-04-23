import matplotlib.pyplot as plt
from pyedflib import highlevel as edf

electrodes = {0: [2740, 6230],
              1: [1630, 5200],
              2: [900, 4000],
              3: [1580, 1580],
              4: [3000, 1000],
              5: [3000, 6230],
              6: [2400, 3750],
              7: [3000, 2000],
              8: [5330, 6230],
              9: [4840, 4290],
              10: [4810, 3000],
              11: [5000, 1890],
              12: [5060, 6230],
              13: [3950, 5200],
              14: [3220, 4000],
              15: [3900, 1580],
              16: [5320, 1000],
              17: [900, 3500],
              18: [2700, 1600],
              19: [4000, 3650],
              20: [5860, 3820],
              21: [7000, 3500],
              22: [6540, 1800]}

for i in range(23):
    electrodes[i][0] = electrodes[i][0] * 0.775 * 1.5
    electrodes[i][1] = electrodes[i][1] * 1.125 * 1.5

fig = plt.figure(frameon=False)
extent = 0, 6200 * 1.5, 0, 9000 * 1.5

img = plt.imread("the_brain.jpg")
im3 = plt.imshow(img, cmap=plt.cm.viridis, alpha=1.0, interpolation='bilinear', extent=extent)

test_files = [
    r'C:\Users\march\PycharmProjects\end\chb24_04.edf',  # Файл с СМВ
]

test_file = test_files[0]
print(f"\nFile: {test_file}")
signals, signal_headers, header = edf.read_edf(test_file)
arr = [0] * len(signals)

for j in range(len(signals)):
    print(signal_headers[j])

max_value_signal = 1468.5225885225884
min_value_signal = -1353.2600732600733

plt.axis('off')

check = False

maxi = 0
arr_of_ind = []
if not check:
    for i in range(len(signals[0])):
        for j in range(len(signals)):
            if (((signals[j][i] + max_value_signal) / (max_value_signal * 2)) > 0.7) or \
                    (((signals[j][i] + max_value_signal) / (max_value_signal * 2)) < 0.3):
                arr_of_ind.append(i)
    for i in range(len(arr_of_ind)):
        for j in range(len(signals)):
            helper3 = 1
            helper4 = 1
            power = 0
            helper = ((signals[j][arr_of_ind[i]] + max_value_signal) / (max_value_signal * 2))
            for k in range(10):
                if helper < 0.45 + k / 100:
                    power = 0.125 + (k / 12)
                    break
                if power == 0:
                    power = 1
            if power < 0.55:
                helper3 = -1
            if power > 0.624:
                helper4 = -1
            helper2 = pow(helper, power)
            arr[j] = plt.scatter(electrodes[j][0] + (helper2 * 30 * helper3),
                                 electrodes[j][1] + (helper2 * 30 * helper4), alpha=helper * power,
                                 color=(0.3 * power, 0.7 * power, 1 - power), s=500 * helper * power * 2.5)
        plt.pause(0.01)
        for j in range(len(signals)):
            arr[j].remove()

for i in range(len(signals[0])):
    for j in range(len(signals)):
        helper3 = 1
        helper4 = 1
        power = 0
        helper = ((signals[j][i] + max_value_signal) / (max_value_signal * 2))
        for k in range(10):
            if helper < 0.45 + k / 100:
                power = 0.125 + (k / 12)
                break
            if power == 0:
                power = 1
        if power < 0.55:
            helper3 = -1
        if power > 0.624:
            helper4 = -1
        helper2 = pow(helper, power)
        coloro = (0.3 * power, 0.7 * power, 1 - power)
        arr[j] = plt.scatter(electrodes[j][0] + (helper2 * 30 * helper3), electrodes[j][1] + (helper2 * 30 * helper4),
                             alpha=helper * power, color=coloro, s=500 * helper * power * 2.5)
    plt.pause(0.01)
    for j in range(len(signals)):
        arr[j].remove()
