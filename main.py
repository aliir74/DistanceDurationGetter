import googlemaps
import csv

def writeResultToCSV(file, result1, result2):
    csvwriter = csv.writer(file)

    #write headers
    header = ['origins/destinations']
    for idx, i in enumerate(result1['destination_addresses']+result2['destination_addresses']):
        header.append(idx+1)
    csvwriter.writerow(header)

    #add content
    for (idx, i) in enumerate(result1['origin_addresses']):
        row = [idx+1]
        for j in (result1['rows'][idx]['elements']+result2['rows'][idx]['elements']):
            if(j['status'] == 'ZERO_RESULTS'):
                print(j)
                row.append(0)
            else:
                row.append(j['duration_in_traffic']['value'])

        csvwriter.writerow(row)


def getDataFromFile(file):
    origins = []
    dests = []
    cnt = 0
    for idx, line in enumerate(file):
        if(line == "\n"):
            continue
        if(cnt < 36):
            location = [(i) for i in line.split()]
            dests.append((float(location[1][:-1]), float(location[2])))
            cnt += 1
        elif(cnt < 40):
            location = [(i) for i in line.split()]
            origins.append((float(location[1][:-1]), float(location[2])))
            cnt += 1
    return origins, dests


apikey = open('key.txt', 'r').readline()

gmaps = googlemaps.Client(key=apikey)

locations = open('Input.txt', 'r')
origins, dests = getDataFromFile(locations)

print('origins:')
for i in origins:
    print(i)

print('dests:')
for i in dests:
    print(i)

resultCSV = open('result.csv', 'w')
ret1 = gmaps.distance_matrix(origins, dests[:25], mode="driving", traffic_model="best_guess", departure_time="now")
print('result 1 finished')
ret2 = gmaps.distance_matrix(origins, dests[25:], mode="driving", traffic_model="best_guess", departure_time="now")
print('result 2 finished')

writeResultToCSV(resultCSV, ret1, ret2)
print('merge finished!')
