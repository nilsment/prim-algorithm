def prim(edges):
    besucht = []
    ergebnis = []
    erreichbar = []
    #The algorithm always starts with the first vertex of the first edge it is given
    #All of its neighbours are added to the list of reachable vertices
    startknoten = edges[0]
    for e in edges:
        if e[0] == startknoten[0]:
            erreichbar.append(e)
    besucht.append(0)
    #The outer loop, which is repeated as long as there are reachable vertices
    while len(erreichbar) > 0:
        #First all edges are removed, which would lead to a circle being formed
        for e in erreichbar:
            if e[0] in besucht and e[1] in besucht:
                erreichbar.remove(e)
        #If there is no reachable vertex after this, the loop is prematurely terminated
        if len(erreichbar) == 0:
            break
        #The reachable edge with the smallest weight is found
        kleinstes = erreichbar[0][2]
        for e in erreichbar:
            if e[2] < kleinstes:
                kleinstes = e[2]
        #The edge with the smallest weight is gonna be the one added to the mimimum spanning tree next
        naechste_kante = erreichbar[0]
        for e in erreichbar:
            if e[2] == kleinstes:
                naechste_kante = e
        #The vertex needs to be marked as visited
        if naechste_kante[0] in besucht:
            besucht.append(naechste_kante[1])
        else:
            besucht.append(naechste_kante[0])
        ergebnis.append(naechste_kante)
        #Now the edges that are reachable as a result of the new vertex being visited are checked if they would leed to a circle
        #If they dont, they are marked as reachable
        for e in edges:
            if e[0] == naechste_kante[0] or e[0] == naechste_kante[1]:
                if e[0] not in besucht or e[1] not in besucht:
                    if e not in erreichbar:
                        erreichbar.append(e)
            elif e[1] == naechste_kante[0] or e[1] == naechste_kante[1]:
                if e[1] not in besucht or e[1] not in besucht:
                    if e not in erreichbar:
                        erreichbar.append(e)
    #As soon as the loop terminated, all connected vertices are included in the minimum spanning tree,
    #which is returned in the form of the original graph
    return ergebnis

#sample of an weighted graph
edges = [(0,1,4), (1,6,3), (0,2,7), (1,3,1), (3,6,3), (2,4,2), (3,4,7), (4,5,6),
(5,8,2), (0,7,5), (4,7,4), (5,8,3), (6,8,10), (8,9,1), (4,9,4), (7,9,2)]

#main method
if __name__ == '__main__':
    print(prim(edges))
