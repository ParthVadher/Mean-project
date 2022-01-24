import csv
from collections import Counter

with open("SOCR-HeightWeight (1).csv", newline="") as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)

hw = []


filedata.pop(0)

hw = []

for i in range(len(filedata)):
    n = filedata[i][1]

    hw.append(float(n))

#Code for mean

l = len(hw)
total = 0

for i in hw:

    total += i

x = total/l
print("Mean is ->", x)


# The code for median


hw.sort()
l = len(hw)

if(l%2 == 0):
    m1 = float(hw[l//2])
    m2 = float(hw[l//2-1])

    med = (m1+m2)/2

else:
    med = float(hw[l//2])

print("Median is ->", med)

# code for mode

data = Counter(hw)

poiuy = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0
}

for i,o in data.items():
    if(75 < float(i) < 85):
        poiuy["75-85"]+=o
    elif(85 < float(i) < 95):
        poiuy["85-95"]+=o
    elif(95 < float(i) < 105):
        poiuy["95-105"]+=o
    elif(105 < float(i) < 115):
        poiuy["105-115"] += o
    elif(115 < float(i) < 125):
        poiuy["115-125"] += o
    elif(125 < float(i) < 135):
        poiuy["125-135"]+=o
    elif(135< float(i) < 145):
        poiuy["135-145"]+=o
    elif(145< float(i) < 155):
        poiuy["145-155"]+=o
    elif(155< float(i) < 165):
        poiuy["155-165"]+=o
    elif (165 < float(i) < 175):
        poiuy["165-175"] += o

mode_range = 0
mode_occurence = 0

for range,occurence in poiuy.items():
    if(occurence > mode_occurence):
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
        mode = float((mode_range[0] + mode_range[1]) / 2)
        print(f"Mode is -> {mode:2f}")

#











































