remove_duplicates([], []).
remove_duplicates([X | Xs], UniqueList) :-
    member(X, Xs),
    !,
    remove_duplicates(Xs, UniqueList).
remove_duplicates([X | Xs], [X | UniqueTail]) :-
    remove_duplicates(Xs, UniqueTail).
