import random as r

import matplotlib.pyplot as plt


def rand_check(tries):
    var0 = 0
    var1 = 0
    var2 = 0
    for i in range(tries):
        rnumb = round(r.randrange(0, 3))
        if rnumb == 0:
            var0 += 1
        elif rnumb == 1:
            var1 += 1
        elif rnumb == 2:
            var2 += 1
        else:
            print('shiii')
    print(var0, var1, var2)
    print(var0 + var1 + var2)


def graph_rand(tries):
    rnumb = []
    for i in range(tries):
        rnumb.append(r.randrange(0, 3))
    plt.hist(rnumb)
    plt.show()


mod = 1000
evu = ['A', 'B', 'AB']
evp = [45 * mod, 30 * mod, 25 * mod]


def single_test(samp_size):
    evall = []

    i1: int
    for i1 in range(evp[0]):
        evall.append(evu[0])
    for i1 in range(evp[1]):
        evall.append(evu[1])
    for i1 in range(evp[2]):
        evall.append(evu[2])

    r.shuffle(evall)

    samp = r.sample(evall, samp_size)

    res = [0, 0, 0]

    for e in samp:
        if 'A' in e and 'B' in e:
            res[2] += 1
        elif 'A' in e:
            res[0] += 1
        elif 'B' in e:
            res[1] += 1
    return res


def single_test2(samp_size):
    evall = []

    for i in range(evp[0]):
        evall.append(evu[0])
    for i in range(evp[1]):
        evall.append(evu[1])
    for i in range(evp[2]):
        evall.append(evu[2])

    r.shuffle(evall)

    samp = r.sample(evall, samp_size)

    res = [0, 0, 0]

    for e in samp:
        if 'A' in e and 'B' in e:
            res[2] += 1
        elif 'A' == e:
            res[0] += 1
        elif 'B' == e:
            res[1] += 1
    return res


samp_size = mod * 10

res1 = []
for i in range(10):
    res1.append(single_test(samp_size))

res2 = []
for i in range(10):
    res2.append(single_test2(samp_size))

meanres1 = [0, 0, 0]
for e in res1:
    for i in range(len(e)):
        meanres1[i] = e[i]
meanres1 = [x / len(res1) for x in meanres1]
print(meanres1)

meanres2 = [0, 0, 0]
for e in res2:
    for i in range(len(e)):
        meanres2[i] = e[i]
meanres2 = [x / len(res2) for x in meanres2]
print(meanres2)
