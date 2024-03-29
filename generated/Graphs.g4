grammar Graphs;

// Start symbol
s
    : graph a end_graph g
    | ;

g
    : graph a end_graph g
    | ;

// Check if there is enough nodes to modify/add edge
a
    : w aa;

aa
    : k
    | ;

w
    : node w 
    | ;

k
    : node k
    | m k
    | e k 
    | ;

m
    : modify attributes 'end';

e
    : edge attributes 'end';

// Graph symbol
graph 
    : 'graph' name extend;

extend
    : 'extends' name
    | ;

// Node symbol
node
    : 'add node' name;

// Modify node symbol
modify
    : 'modify' name;

// Add edge symbol
edge
    : 'set edge' dest_node dest_node;

attributes
    : '[' (name ':' value )* ']';

value
    : number | name;  

dest_node
    : '*' | name;

end_graph
    : 'end';

name
    : ID;

number 
    : INT;

ID 
    : [a-zA-Z_] [a-zA-Z_0-9]*;

INT 
    : [0-9]+;

White_spaces 
    : [ \t\n\r]+ -> skip;