hanoi(1, Start, End, _, Moves) :-
    write('Move disk 1 from '), write(Start), write(' to '), writeln(End),
    Moves = 1.

hanoi(N, Start, End, Aux, Moves) :-
    N > 1,
    M is N - 1,
    hanoi(M, Start, Aux, End, Moves1),
    write('Move disk '), write(N), write(' from '), write(Start),
    write(' to '), writeln(End),
    hanoi(M, Aux, End, Start, Moves2),
    Moves is Moves1 + 1 + Moves2.



% ?- hanoi(3, 'A', 'C', 'B', Moves).