# Algorithmic Detection of Graph Planarity

An algorithm is designed to detect the planarity of any simple graph, the pseudocode is shown as follows.

## Planar Detection

```text
PlanarDetection(G):
    Find the core G* of G

    if G* is empty:
        return G is planar
    else:
        Find a cycle C in G* with a chord e
        Find all bridges of C in G* and construct the interleave graph H
        if H is not bipartite:
            return G is not planar
        else:
            return PlanarDetection(G* - e)
```

The main Python implementation is provided in [(main_code)Planar_Detection_Algorithm.py](https://github.com/boweizheng2024-dotcom/Algorithmic-Detection-of-Graph-Planarity/edit/main/README.md#:~:text=Planar_Detection_Algorithm). The other .py files contain the sub-algorithms used by the main implementation.

## Concepts and terminology

- **Graph $G$**: The input is a simple, undirected graph. The code accepts an adjacency list with vertices numbered consecutively from 1 to n. List position i stores the neighbors of vertex i+1.
- **Core $G^*$**: The graph remaining after repeatedly removing vertices of degree one and suppressing vertices of degree two. Suppression removes the degree-two vertex and joins its two neighbors. This reduction preserves whether the graph is planar.
- **Cycle $C$**: A closed path.
- **Chord $e$**: An edge joining two non-consecutive vertices of a cycle $C$.
- **Bridge of a Cycle $C$**: In this content, a bridge is either a connected component outside $C$ together with any edges joining that connected component to $C$, or a single chord of $C$. This is distinct from the common graph-theory meaning of a cut edge.
- **Vertex of attachment of a bridge of $C$**: Vertices of $C$ which are end vertices of edges in the bridge.
- **Interleaving bridges**: Two bridges interleave when their attachment vertices alternate around $C$: for distinct cycle vertices $a,b,c,d$ in cyclic order, one bridge attaches to $a$ and $c$, and the other to $b$ and $d$.
- **Interleave graph $H$**: $H$ has one vertex per bridge. Two vertices are adjacent exactly when their corresponding bridges interleave.
- **Bipartite graph**: A graph whose vertices can be divided into two independent sets.
## Code definitions

### Main routine

- `Planar_Detection(AdjList_G)`: Implements Algorithm 2. It converts the input to a matrix, finds the core, selects a cycle with a chord, builds bridge attachments and H, tests H for bipartiteness, and recurses after removing the chord. Returns `True` for planar and `False` for non-planar.
- `Finding_Bridegs_Attachments(AdjList_G, V_C)` (nested helper): Collects components outside C, numbers their bridges, finds their cycle attachments, then adds each chord as its own bridge.
- `whether_core_is_empty(AdjMatrix_core)` (nested helper): Returns whether the core matrix contains any edges; an empty core is the planar base case.

### Core, cycles, and representations

- `DELETING_DEGREE_ONE_AND_TWO(AdjMatrix, w)`: Recursively removes a degree-one vertex or suppresses a degree-two vertex `w`, updating the matrix in place.
- `FIND_THE_CORE(AdjMatrix)`: Applies the degree-one/two reduction to every vertex and returns the resulting core matrix.
- `Find_a_Cycle_with_a_Chord(AdjList)`: Searches the adjacency-list graph and returns the selected cycle, chord, and chord endpoints. Its nested `FIND_CYCLE_CHORD(v, p)` performs the depth-first traversal and assembles the cycle and chord from parent links.
- `AdjList_to_AdjMatrix(AdjList)`: Converts the 1-based adjacency-list representation to a NumPy adjacency matrix.
- `AdjMatrix_to_AdjList(AdjMatrix)`: Converts a matrix back to adjacency lists with 1-based neighbor labels.

### Components, bridges, and attachments

- `COMPREP(CompPtr, u)`: Finds the representative of the component containing `u`, with path compression.
- `MERGE(CompPtr, uRep, vRep)`: Joins two component representatives by size.
- `FIND_COMPONENT(AdjList)`: Computes connected-component representatives for the graph; used by the bipartite checker.
- `Finding_Components_of_Induced_Subgraph(AdjList_G, V_C)`: Finds components induced by vertices outside the selected cycle; cycle vertices are marked and excluded.
- `Finding_the_Bridges(AdjList_G, CompPtr)`: Labels the outside components as bridges and returns the bridge count, vertex-to-bridge map, and edge lists.
- `Finding_Vertices_of_Attachment(AdjList_G, V_C, BRIDGE, m)`: Collects cycle positions that attach to each non-chord bridge.
- `FIND_CHORDS(AdjMatrix, m, V_C, B, Attachments)`: Finds chords of the ordered cycle and adds each chord as a one-edge bridge with its two attachment positions.

### Interleaving and bipartiteness

- `TEST_INTERLEAVING(front, back, a, b)`: Recursively checks whether attachment positions alternate between two bridges on the cycle.
- `TEST_EDGES(attB_q, attB_p)`: Determines whether two bridges interleave based on their attachment lists.
- `CONSTRUCTION(Attachments)`: Builds H as an adjacency list from the bridge attachment lists.
- `ASSIGNMENT(AdjList_G, partition, parents)`: Propagates the two-color assignment across a frontier; returns `False` if an edge joins equal colors.
- `TEST_BIPARTITE(AdjList_G)`: Checks every connected component of H and returns whether H is bipartite.

### Supporting data

- `Examples.py`: Defines the `Tetrahedron`, `Cube`, `Octahedron`, `Dodecahedron`, and `Icosahedron` sample adjacency lists. The main file uses `Dodecahedron` for its included example.


## Reference

Part ii - catam. https://www.maths.cam.ac.uk/undergrad/catam/II, 2024. Accessed: 2024-09-07.


