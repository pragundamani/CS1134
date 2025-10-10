### Q1
a) The highest power in $5n^3+2n^2+3n$ is $n^3$ therefore $O(n)$ is $O(n^3)$
b) since $\Omega (n) = \sqrt{ 7n^2+2n-8 }\geq \sqrt{ 7n^2 }=$
and $O(n) = \sqrt{ 7n^2 +2n-8}=O(3n)=O(n)$
$\Omega(n)\leq \Theta(n)\leq O(n)$
therefore $f(n)=\Theta(n)$
c) $d(n)e(n)=O(f(n)g(n))$ 

### Q2
1. Outer loop would run $n$ iterations and inner loop would run $n$ times thus  run time would be $\Theta(n^2)$
2. Since the loop runs only one time $\Theta(n^2)$
3. Loop runs till $n^2$ but loop doubles every time therefore time is $\log(n^{2)}$ 
	- $\therefore \Theta(\log (n))$
4. Outer Loop reduces by half but inner loop increases $\therefore \Theta(n)$
