class Graph(object):
    def __init__(self,graph_dict=None):
        if graph_dict==None:
            graph_dict={}
        self.graph_dict=graph_dict


    def vertices(self):
        return list(self.graph_dict.keys())


    def edges(self):
        return self.generate_edges()


    def add_vertex(self,vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex]=[]


    def add_edge(self,edge):
        edge=set(edge)
        (v1,v2)=tuple(edge)
        if v1 in self.graph_dict:
            self.graph_dict[v1].append(v2)
        else:
            self.graph_dict[v1]=[v2]


        if v2 in self.graph_dict:
            self.graph_dict[v2].append(v1)
        else:
            self.graph_dict[v2]=[v1]




    def generate_edges(self):
        edges=[]
        for node in self.graph_dict:
            for neighbor in self.graph_dict[node]:
                if {node,neighbor} not in edges:
                    edges.append({node,neighbor})

        return edges

    def find_all_paths(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return path

        if start not in self.graph_dict:
            return None

        for node in self.graph_dict[start]:
            if node not in path:
                newpath=self.find_all_paths(node,end,path)
                if newpath:
                    return newpath
        return None





    def find_shortest_path(self,start,end):
        pass
    def __str__(self):
        res = "vertices: "
        for k in self.graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.generate_edges():
            res += str(edge) + " "
        return res
