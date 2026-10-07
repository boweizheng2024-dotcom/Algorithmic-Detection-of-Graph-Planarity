from ConnectedComponents import COMPREP, MERGE, FIND_COMPONENT
from Components_Induced_Subgraph import Finding_Components_of_Induced_Subgraph
from Bridges_Induced_Subgraph import Finding_the_Bridges
from Updated_Attachments import Finding_Vertices_of_Attachment
from Updated_Chords import FIND_CHORDS
from Conversion import AdjList_to_AdjMatrix, AdjMatrix_to_AdjList
from interleaving import TEST_INTERLEAVING,TEST_EDGES, CONSTRUCTION
from Test_Bipartite_Graph import ASSIGNMENT, TEST_BIPARTITE
from Core import DELETING_DEGREE_ONE_AND_TWO, FIND_THE_CORE
from FindCycleChord import Find_a_Cycle_with_a_Chord
import numpy as np
from Examples import Dodecahedron

def Planar_Detection(AdjList_G):
    def Finding_Bridegs_Attachments(AdjList_G, V_C):
        CompPtr = Finding_Components_of_Induced_Subgraph(AdjList_G, V_C)
        for i in range(len(CompPtr)):
            if CompPtr[i] == -1:
                CompPtr[i] = 0  # isolated vertices in the core are not bridges

        bridges_from_induced_graph = Finding_the_Bridges(AdjList_G, CompPtr)
        m = bridges_from_induced_graph[0]
        BRIDGE = bridges_from_induced_graph[1]
        B = bridges_from_induced_graph[2]
        Attachments = Finding_Vertices_of_Attachment(AdjList_G, V_C, BRIDGE, m)

        AdjMatrix_G = AdjList_to_AdjMatrix(AdjList_G)
        
        bridges_from_chords = FIND_CHORDS(AdjMatrix_G, m, V_C, B, Attachments)
        Attachments_ = bridges_from_chords[2]

        return Attachments_
    
    def whether_core_is_empty(AdjMatrix_core):
        n = AdjMatrix_core.shape[0]
        for i in range(n):
            for j in range(i,n):
                if AdjMatrix_core[i][j] == 1:
                    return False
        return True


    AdjMatrix_G = AdjList_to_AdjMatrix(AdjList_G)
    AdjMatrix_core = FIND_THE_CORE(AdjMatrix_G)

    if whether_core_is_empty(AdjMatrix_core) == True:
        return True
    
    else:
        AdjList_core = AdjMatrix_to_AdjList(AdjMatrix_core)
        cycle_and_chord = Find_a_Cycle_with_a_Chord(AdjList_core)
        V_C = cycle_and_chord[0]
        chord_v1 = cycle_and_chord[2]
        chord_v2 = cycle_and_chord[3]

        Attachments = Finding_Bridegs_Attachments(AdjList_core, V_C)
        Interleave_Graph = CONSTRUCTION(Attachments)

        if TEST_BIPARTITE(Interleave_Graph) == False:
            return False
        else:
            AdjMatrix_core[chord_v1 - 1][chord_v2 - 1] = 0
            AdjMatrix_core[chord_v2 - 1][chord_v1 - 1] = 0
            AdjList_core_ = AdjMatrix_to_AdjList(AdjMatrix_core)
            return Planar_Detection(AdjList_core_)
    
# example
print(Planar_Detection(Dodecahedron))
