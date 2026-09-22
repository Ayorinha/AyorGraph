from dataclasses import dataclass, field
from typing import Callable, Generic, TypeVar
T=TypeVar("T")
@dataclass
class AgentGraph(Generic[T]):
    nodes: dict[str,Callable[[T],T]]=field(default_factory=dict); edges: dict[str,str]=field(default_factory=dict)
    def add_node(self,name,fn):
        if not name or name in self.nodes: raise ValueError("node name must be unique")
        self.nodes[name]=fn
    def add_edge(self,source,target):
        if source not in self.nodes or target not in self.nodes: raise KeyError("unknown node")
        self.edges[source]=target
    def run(self,start,state,max_steps=32):
        if start not in self.nodes: raise KeyError(start)
        cur=start
        for _ in range(max_steps):
            state=self.nodes[cur](state)
            if cur not in self.edges: return state
            cur=self.edges[cur]
        raise RuntimeError("graph exceeded max_steps")