### Mutation vs construction

| Mutating                         | Constructing                   |
| -------------------------------- | ------------------------------ |
| Indexed assignment `lst1[i]=...` | list literals `[1,2,3],[]`     |
| append method                    | list constructor `list(...)`   |
| insert method                    | `copy.copy` function (shallow) |
| pop method                       | `copy.deepcopy` function       |
| reverse method                   | `+` operator (shallow)         |
| sort method                      | `*` operator (shallow)         |
| extend method                    | slicing `lst[__:__]` (shallow) |
| `+=` Operation                   | list comprehension (shallow)   |
>[!mark] difference between a method and a function in python
>A method belongs to an object
>A function is independent

>[!mark] Shallow copy vs Deep copy
>![[list shallow deep copy.excalidraw|400]]
>- Shallow copy only affects list if it has a mutable object in it


>[!function] `id()` function can be used as a "memory location of object"


>[!define] ***Iterable-collection***: an object that produces an iterator via the syntax `iter(iterable_collection)`

>[!define] ***Iterator***: An object that exposes a series of values, by making subsequent calls to the `next(iterator)` 

>[!define] ***Generator:*** a Generator is just an interator

list reassignment
![[list reassignment.excalidraw]]