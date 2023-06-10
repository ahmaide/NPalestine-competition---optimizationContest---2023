import math


def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def startTime(distance, goTime, driverArrival):
    if distance + goTime < driverArrival:
        return float(driverArrival)
    else:
        return float(driverArrival)

def willMakeIt(distance, goTime, driverLeave):
    if distance + goTime < driverLeave:
        return True
    else:
        return False

def timefromGoToStart(distance, goTime, driverArrival):
    if distance + goTime < driverArrival:
        return float(driverArrival - goTime)
    else:
        return float(distance)

class Site:
    def __init__(self, xs, ys, Ts, Cs, ss, es, As):
        self.xs = xs
        self.ys = ys
        self.Ts = Ts
        self.Cs = Cs
        self.ss = ss
        self.es = es
        self.As = As
        self.left = As


class Install:
    def __init__(self, xr , yr , Tr , Wr , sr , er, index):
        self.xr = xr
        self.yr = yr
        self.Tr = Tr
        self.Wr = Wr
        self.sr = sr
        self.er = er
        self.index = index

inf = open ( 'input.txt' , 'r')
info = inf.readlines()
firstLine = info[0].split(' ')
S=abs(int(firstLine[0]))
R=abs(int(firstLine[1]))
sites=[]
installs=[]
i=0
for i in range(S):
    line = info[i+1].split()
    sites.append(Site(float(line[0]), float(line[1]), float(line[2]),
                      float(line[3]), float(line[4]), float(line[5]), float(line[6])))

for i in range(R):
    line = info[i+S+1].split()
    installs.append(Install(float(line[0]), float(line[1]), float(line[2]),
                      float(line[3]), float(line[4]), float(line[5]), i+1))
    #i+=1
answers=[]

i=0
j=0
anss=9999999
        k=0
        found=False
        mmm = len(installs)
        while k< mmm and not found:
            mmm = len(installs)
            dis = float(distance(sites[i].xs, sites[i].ys, installs[k].xr, installs[k].yr))
            case1 = (sites[i].Cs >= installs[k].Wr)
            case2 = (willMakeIt(dis, sites[i].ss, installs[k].er))
            case3 = ( 2*dis + installs[k].Tr <= sites[i].Ts)
            case4 = ((2*dis + installs[k].Tr + sites[i].ss) <= sites[i].es)
            if case1 and case2 and case3 and case4:

                ans2=(float(installs[k].sr) - dis)
                if(ans2<anss):
                    ansss = ans2
                sites[i].left-=1
                installs.pop(k)
                k-=1
                found = True
            k += 1
        if not found:
            answers.append(-1)
            answers.append(-1)

answers.append(ans2)
outt = open ( 'output.txt' , 'w')
for ans in answers:
    print(ans)
    outt.write(str(ans) + "\n")





