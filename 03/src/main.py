import networkx as nx
import pandas as pd
import itertools as itertools
import matplotlib.pyplot as plt
import pprint


def loadData(path = "src/casts.csv", nrows=100):
    df = pd.read_csv(path, nrows=nrows, delimiter=";")
    df.columns = ["movieId", "movieTitle", "actorName", "roleType", "roles"]
    return df


def createGraph(dataFrame):
    actors = df.actorName.unique()
    
    G = nx.Graph()
    
    # add nodes        
    G.add_nodes_from(actors)
    
    # create dictionary, where keys are movie titles, values are lists of actor names
    movieActorDict = {}
    for index, row in df.iterrows():
        if row.movieTitle in movieActorDict:
            movieActorDict[row.movieTitle].append(row.actorName)
        else:
            movieActorDict[row.movieTitle] = [row.actorName]
            
    # add edges    
    for movie, actors in movieActorDict.items():
        for actorsPair in itertools.combinations(actors, 2):
            G.add_edge(actorsPair[0], actorsPair[1])
    
    return G

def computeGeneralStatistics(G):
    maxDegree = -1
    minDegree = len(G.nodes) - 1
    degreesSum = 0
    for node in G.nodes:
        degreesSum += G.degree(node)
        if G.degree(node) > maxDegree:
            maxDegree = G.degree(node)
        if G.degree(node) < minDegree:
            minDegree = G.degree(node)
            
    print(f'Number of nodes: {len(G.nodes)}')
    print(f'Maximum degree of node: {maxDegree}')
    print(f'Minimum degree of node: {minDegree}')
    print(f'Average degree of nodes: {degreesSum / len(G.nodes)}')
    print(f'Number of edges: {len(G.edges)}')
    print(f'Graph density: {nx.density(G)}')
    print(f'Number of components: {nx.number_connected_components(G)}')
    

def centralities(G):
    centralities = [
        nx.degree_centrality,
        nx.closeness_centrality,
        nx.betweenness_centrality,
        nx.eigenvector_centrality
    ]
    numberOfBestResults = 10
    for centrality in centralities:
        result = centrality(G)
        print(f'\n{numberOfBestResults} highest centralities using {centrality.__name__.upper()}')
        # pprint.pprint(sorted([(key, value) for key, value in result.items()],
                            #  key=lambda x: x[1], reverse=True)[:numberOfBestResults])


def communities(G):
    communities = {node: communityId + 1 for communityId , community in enumerate(nx.algorithms.community.k_clique_communities(G,3)) for node in community}
    # print(communities)
    pos = nx.spring_layout(G)
    nx.draw(G, pos,
        labels={v: str(v) for v in G},
        cmap = plt.get_cmap("rainbow"),
        node_color=[communities[v] if v in communities else 0 for v in G])


df = loadData()
graph = createGraph(df)
computeGeneralStatistics(graph)
centralities(graph)
communities(graph)