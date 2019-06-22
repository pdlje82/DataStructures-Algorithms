### WebServer Trie

Works almost identically like the Autocomplete Trie. Instead of 
characters, now path elements are stored. Instead of the is_word
boolean, now the handler is written / used for control flow.
Also, a router class is added as wrapper and to do some handling,
like path splitting.


Time complexity: 
- look-up: O(k)
- insert: O(k)

Space complexity: 
O(k ** n)

k... average path length
n... path element count (i.e. \about, \me, \anyPathName)