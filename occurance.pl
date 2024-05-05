occur(_, [], 0).
occur(X, [X | Tail], N) :-
    occur(X, Tail, N1),
    N is N1 + 1.
occur(X, [Y | Tail], N) :-
    X \= Y,
    occur(X, Tail, N).

% Example usage:
% occurrences(a, [a, b, c, a, d, a, e], N).
