import googlemaps

def getDataFromFile(file):
    origins = []
    dests = []
    oo = False
    od = False
    for line in file:
        if("origin" in line):
            oo = True
            od = False
        elif("destination" in line):
            od = True
            oo = False
        else:
            if(od):
                location = [(i) for i in line.split()]
                #print(location)
                dests.append((float(location[1]), float(location[2])))
            elif(oo):
                location = [(i) for i in line.split()]
                #print(location)
                origins.append((float(location[1]), float(location[2])))
    return origins, dests


apikey = open('key.txt', 'r').readline()

gmaps = googlemaps.Client(key=apikey)

locations = open('URL.txt', 'r')
origins, dests = getDataFromFile(locations)

print('origins:')
for i in origins:
    print(i)

print('dests:')
for i in dests:
    print(i)
ret = gmaps.distance_matrix(origins[:10], dests[:])


print(ret)