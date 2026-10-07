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

The main Python implementation is provided in [(main_code)Planar_Detection_Algorithm.py](https://github.com/boweizheng2024-dotcom/Algorithmic-Detection-of-Graph-Planarity/blob/main/(main_code)Planar_Detection_Algorithm.py). The other .py files contain the sub-algorithms used by the main implementation.

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

## Implementation of Important Variables

| Variable | Meaning |
| --- | --- |
| `CompPtr` | For the $i$-th element in the list `CompPtr`, if it is a positive number $j$, it means that vertex $j$ is the parent of vertex $i$. If it is a negative number $k$, it means that vertex $i$ is the vertex representation of the connected component of size $-k$ containing $i$ in the induced subgraph $G\[V(G) \setminus V(C)\]$. `0` marks an excluded cycle vertex. |
| `BRIDGE` | `BRIDGE$[u]` > 0 indicates the vertex $u$ belongs to the $m$-th bridge.|
| `m` |  The number of bridges except chords. |
| `B` | The edge lists for the bridges. |
| `Attachments` | `Attachments[i]` collects the vertices of attachment of the $(i+1)$-th bridge of $C$. |
| `Attachments_` | `Attachments` together with the vertices of attachment of chords of $C$. |
| `chord_v1`, `chord_v2` | The two endpoints of the chord selected for removal in a recursive step. |


## Supporting data

- `Examples.py`: Defines the `Tetrahedron`, `Cube`, `Octahedron`, `Dodecahedron`, and `Icosahedron` sample adjacency lists. The main file uses `Dodecahedron` for its included example.

## Computational Complexity

- $O(n^4 \log_2 n)$, where $n$ is the number of vertices


## Reference

Part ii - catam. https://www.maths.cam.ac.uk/undergrad/catam/II, 2024. Accessed: 2024-09-07.


