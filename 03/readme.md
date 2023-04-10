# HW 3 - Social network analysis

- First of all I loaded the csv file using pandas library and created graph from it using networkx library. The csv file is really large, so I decide to work only with subset of nodes (10000 nodes).
- Then I computed general statistics:
    ```
    Number of nodes: 5832
    Maximum degree of node: 794
    Minimum degree of node: 0
    Average degree of nodes: 10.549039780521262
    Number of edges: 30761
    Graph density: 0.0018091304717066134
    Number of components: 301
    ```
- After that I computed centralities of all nodes using different functions (degree_centrality closeness_centrality, betweenness_centrality, eigenvector_centrality). These centralities are added to nodes like attributes and can be found in `result/graph.gexf` file. And I saved 10 nodes with highest centrality for each centrality function to `result/centralitiesOutput.txt` file.
- The next step was alanytic of communities. I added next attribute to all nodes - communityId and visualized the communities into plot, but thanks to large number of nodes (10000) they are overlapping. All communities are logged in `result/communitiesOutput.txt` file.
- Next I computed Kevin Bacon's number of all nodes and added it as an attribute. This number represents the shortest path to node Kevin Bacon. The graph contains of several components, so I set this number for nodes, which are not in the same component as Kevin Bacons as infinity.
    ```
    Average Kevin Bacon number of nodes with finite Kevin Bacon number: 3.6641509433962263
    Number of nodes with finite Kevin Bacon number: 5035
    ```
- The entire graph is saved in `result/graph.gexf. I visualized this file using Gephi software.
![gephi visualization](/results/gephi-vizualization.png)
![gephi detail visualization](/results/gephi-detail-visualization.png)
- I also visualized the graph using several python functions, the visualization are in Jupyter notebook. The last visualization is created by graph embedding into vector space.
- Feature improvements: some graphs are unreadable thanks to their size, but I don't want to reduce the number of nodes because I would have to select the data more carefully. For example when I used smaller dataset Kevin Bacon was only in 2-node component.