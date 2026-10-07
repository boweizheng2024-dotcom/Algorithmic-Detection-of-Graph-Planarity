# Algorithmic Detection of Graph Planarity

A Python implementation of the recursive planarity test described as **Algorithm 2: Planar Detection** in *2145768_Bowei Zheng_2025.pdf* (Chapter 3, Graph Planarity Detection). The algorithm is based on graph cores, cycle bridges, bridge attachments, and bipartiteness of the interleave graph.

## Algorithm 2: Planar Detection

```text
PlanarDetection(G):
    G* <- Find the core of G

    if G* is empty:
        return PLANAR

    Find a cycle C in G* that has a chord e
    Find all bridges of C in G* and construct the interleave graph H

    if H is not bipartite:
        return NON-PLANAR

    return PlanarDetection(G* - e)
```

The thesis states the recursive step as: **G is planar if and only if G* - e is planar**. The code realizes this by recursively testing the core with the selected chord removed.

## Concepts and terminology

- **Graph G**: The input is a simple, undirected graph. The code accepts an adjacency list with vertices numbered consecutively from 1 to n. List position i stores the neighbors of vertex i+1.
- **Core G\***: The graph remaining after repeatedly removing vertices of degree one and suppressing vertices of degree two. Suppression removes the degree-two vertex and joins its two neighbors. This reduction preserves whether the graph is planar. In the implementation, `FIND_THE_CORE` applies this reduction to an adjacency matrix.
- **Cycle C**: A closed path in the core. `V_C` stores its vertices in cyclic order, using the code's 1-based vertex labels.
- **Chord e**: An edge joining two non-consecutive vertices of C. `Find_a_Cycle_with_a_Chord` returns a cycle and a chord; `Planar_Detection` removes that chord before its recursive call.
- **Bridge of C**: In the thesis's terminology, a bridge is either a connected component outside C together with its edges to C, or a single chord of C. This is distinct from the common graph-theory meaning of a cut edge.
- **Vertex of attachment**: A vertex of C incident to an edge in a given bridge. A bridge may attach to several vertices of the cycle.
- **Interleaving bridges**: Two bridges interleave when their attachment vertices alternate around C: for distinct cycle vertices a,b,c,d in cyclic order, one bridge attaches to a and c, and the other to b and d.
- **Interleave graph H**: H has one vertex per bridge. Two vertices are adjacent exactly when their corresponding bridges interleave.
- **Bipartite graph**: A graph whose vertices can be divided into two independent sets. The two sets represent placing bridges on opposite sides of C. If H is not bipartite, the input graph is non-planar; if it is bipartite, the algorithm removes a chord and continues recursively.

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

## Important implementation variables

| Name | Meaning |
| --- | --- |
| `AdjList_G` | Input graph as an adjacency list; vertex IDs and neighbor values are 1-based. |
| `AdjMatrix` | NumPy 0/1 adjacency matrix; matrix index `i` corresponds to vertex `i+1`. |
| `V_C` | Cycle vertices in cyclic order. Attachment lists store positions in this sequence, starting at 0. |
| `CompPtr` | Disjoint-set structure: a negative value marks a representative and stores component size; a positive value points to a parent; 0 marks an excluded cycle vertex. |
| `BRIDGE` | Maps each non-cycle vertex to a positive bridge number; cycle entries are not assigned a bridge. |
| `m` | Number of bridges found so far, before adding the chords. |
| `B` | Edge lists for the bridges; chord edges are stored as strings such as `"2-5"`. |
| `Attachments` | For each bridge, the positions of its attachment vertices in `V_C`. |
| `H` / `Interleave_Graph` | The interleave graph whose bipartiteness determines whether the bridges can be placed on two sides of the cycle. |
| `chord_v1`, `chord_v2` | Endpoints of the chord selected for removal in a recursive step. |

## Run

Requirements: Python 3 and NumPy.

```bash
python -m pip install numpy
python Planar_Detection_Algorithm.py
```

The script prints the result for the dodecahedron example. To test another graph, pass an adjacency list to `Planar_Detection(AdjList_G)`. The supplied source also contains a top-level example print in `Conversion.py`, so importing the main module prints the conversion example before the planarity result.

## Repository files

The helper modules imported by the main routine are included alongside it so that the relative imports work from the repository root. The source PDF is not included.
