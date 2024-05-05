like(sam,meena).
like(meena,jony).
like(sam, rachel).
like(ross, rachel).


jealous(X,Y):-
    like(X,Z),
	like(Z,Y), X\=Y.
  
  
 %path finding probelm
edge(a,c).
edge(c,d).
edge(b,d).
edge(b,a).


path_checking(X,Z):-
    edge(X,Y),
	edge(Y,Z), x\=Y.
	
  
  
  male(albert).
male(jony).
male(akbor).

female(kani).
female(kavy).

parent(albert,jony).
parent(albert,kavy).
parent(akbor,albert).

grandFather(Z,X):-
    parent(Y,X),
    parent(Z,Y),
	male(Z).
  
  
  
  
  %find the factorial value of 5 in prolog. 