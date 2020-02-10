For Exercise 1, please see Exercise1.py
For Exercise 2-4, please see Exercise3-4.py


Exercise 5:
Suggestions to solve the problem with such a long list that can't be saved in memory.

Suggestion 1:
- Save n elements of the generated numbers to a list
- Create list for temporary unique values
- For each element, check if occurs in list with unique values
- If occurs, remove element
- If not, add to list
- Take next n elements from numbers and repeat until the end
- Finally repeat process on list with temporary unique values until there is only one element left


Suggestion 2:
- Use a group by function (pandas or itertools) such as it groups identical numbers
- Find occurrences where group by < 2
- Add to list -> temporary unique values
- Repeat until list only contains one element



