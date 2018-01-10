import googlemaps

apikey = open('key.txt', 'r').readline()

gmaps = googlemaps.Client(key=apikey)

l = [float(i) for i in input().split()]
ret = gmaps.distance_matrix((l[0], l[1]), (l[2], l[3]))

print(ret)