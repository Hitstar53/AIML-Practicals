% Family Tree Facts
male(john).
male(bob).
male(jack).
male(oliver).
male(ali).
male(james).
male(simon).
male(harry).
female(helen).
female(sophie).
female(jess).
female(lily).
female(mary).
parent(john, mary).
parent(jack,jess).
parent(jack,lily).
parent(helen, jess).
parent(helen, lily).
parent(oliver,james).
parent(sophie, james).
parent(jess, simon).
parent(ali, simon).
parent(lily, harry).
parent(james, harry).

% Rules
sister_of(X,Y) :- female(X), parent(Z,X), parent(Z, Y), X \= Y.
brother_of(X,Y) :- male(X), parent(Z,X), parent(Z, Y), X \= Y.
father_of(X,Y) :- male(X), parent(X,Y).
mother_of(X, Y) :- female(X), parent(X, Y).
grandparent_of(X, Z) :- parent(X, Y), parent(Y, Z).
aunt_of(X,Y) :- parent(Z,Y), sister_of(Z,X).
uncle_of(X,Y) :- parent(Z,Y), brother_of(Z,X).

% Declare facts as dynamic
:- dynamic(parent/2).
:- dynamic(male/1).
:- dynamic(female/1).

% Fact Base Updating
add_parent(X, Y) :- assert(parent(X, Y)).
remove_parent(X, Y) :- retract(parent(X, Y)).
add_male(X) :- assert(male(X)).
remove_male(X) :- retract(male(X)).
add_female(X) :- assert(female(X)).
remove_female(X) :- retract(female(X)).

    
% Rule Matching    
check_rules :-
    write_list([mother_of(X, Y), father_of(X, Y), grandparent(X, Y), sister(X, Y)]).

% Utility to print a list
write_list([]).
write_list([H|T]) :- writeln(H), write_list(T).