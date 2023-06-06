# A Visualisation of BFS And a Graph

Made using python and pygame.

<details>
<summary>The 2 functions in pyghelpfuls.py are made using chatgpt to calculate the positions of the nodes on the screen and to display text.</summary>
<br>

*The maths to calculate the coordinates of the nodes spaced out evenly across a circle was too complicated for me.*
  
*I was too lazy to make the text show up by myself*

</details>

# To Run
- Run Main.py
- To change the graph, change what's in the testcase.txt
- To pathfind to 2 nodes, type in the letter of the first node and then the letter of the second node. Press return.

  For example: AB FG HK EF
  
*The program has a simple check to take out inputs that wouldn't work, such as "ae" or Ae" or "A E"*

Here's the program in action:

![alt text](https://github.com/Kai-Guan/BFS-Visualisation/blob/main/BFS%20Graph%20Visualisation.gif "Demonstration of the program")


Example testcases:

<pre>
A:BCE
B:AD
C:ADG
D:BCE
E:ADH
F:
G:C
H:E

(Default testcase included in testcase.txt)


A:BEK
B:AC
C:BD
D:C
E:AFH
F:EG
G:F
H:EI
I:HJ
J:I
K:AL
L:K

(A tree)


A:BEK
B:AC
C:BD
D:CN
E:AFH
F:EG
G:F
H:EIM
I:HJ
J:I
K:AL
L:K
M:HN
N:MD

(Weird Tree)
</pre>

When creating your own graph, you must include both nodes in each other (if that makes sense).

For example:

If you wanted to make a connection from A to B, you must also make a connection from B to A.
<pre>
A:B
B:A
</pre>

This would not work:
<pre>
A:B
B:
</pre>
