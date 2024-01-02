grammar Graphs;
options {  }

s
    : graph a 'end' g
    | ;

g
    : graph a 'end' g
    | ;

a
    : w aa;

aa
    : k
    | ;

w
    : vertex w 
    | ;

k
    : vertex k
    | m k
    | e k 
    | ;

m
    : modify attributes 'end';

e
    : edge attributes 'end';

ID
    : [a-zA-Z_] [a-zA-Z_0-9]*;

name
    : ID;


value
    : liczba
    | name;

graph 
    : 'graph' name;

vertex
    : 'add vertex' name;

modify
    : 'modify' name;

edge
    : 'set edge' name name;

attributes
    : '[' (name ':' choose )* ']';

choose
    : liczba | name ;   

end
    : 'end';

liczba 
    : INT;

INT : [0-9]+ ;
White_spaces : [ \t\n\r]+ -> skip;