import googlemaps

def getDataFromFile(file):
    origins = []
    dests = []
    ob = False
    od = False
    for line in file:
        if("origin" in line):
            oo = True
            od = False
        elif("destination" in line):
            ob = True
            od = False
        else:
            if(od):
                location = (float(i) for i in line.split())
                dests.append(location)
            elif(ob):
                location = (float(i) for i in line.split())
                origins.append(location)
    return origins, dests


apikey = open('key.txt', 'r').readline()

gmaps = googlemaps.Client(key=apikey)

ret = gmaps.distance_matrix((l[0], l[1]), (l[2], l[3]))

print(ret)