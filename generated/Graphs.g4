grammar Graphs;
options {  }

s
    : graph a end_graph g
    | ;

g
    : graph a end_graph g
    | ;

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

graph 
    : 'graph' name extend;

extend
    : 'extends' name
    | ;

node
    : 'add node' name;

modify
    : 'modify' name;

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