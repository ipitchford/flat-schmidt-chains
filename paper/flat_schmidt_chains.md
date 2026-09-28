<div class="center">

Version DOI: <https://doi.org/10.5281/zenodo.23024569>

</div>

**Status.** AI-assisted, unrefereed research candidate. Version 1.0.1
addresses a supplied version-1.0 review: the executable classifier now
rejects unspecialised symbolic parameters; antecedent locators and the
full Gram decomposition are explicit. The review’s external independence
has not been authenticated. No proof-assistant formalisation, external
endorsement, historical-priority guarantee or official REF rating is
claimed.

# Model, scope and contribution

For a normalised vector $`\psi\in\mathbb C^d\otimes\mathbb C^d`$, let
$`P=\lvert \psi\rangle\langle \psi\rvert`$ and
``` math
\begin{equation}
\label{eq:HN}
 H_N(P)=\sum_{i=1}^{N-1}P_{i,i+1},\qquad
 \gamma_N(P)=\min\bigl(\operatorname{spec}H_N(P)\setminus\{0\}\bigr),\quad N\ge2.
\end{equation}
```
The boundary is open and there are no additional boundary terms. The
same ordered interaction acts on every bond. The normalisation is
$`P^2=P`$. A uniform gap means $`\inf_{N\ge2}\gamma_N>0`$; the gapless
cases established here satisfy $`\gamma_N\to0`$. This is a
classification by the open-chain spectral gap, not a classification of
phases by symmetry or spectral-flow equivalence. Local projector rank
and the Schmidt rank of its forbidden vector are different quantities.

The main result classifies *all* rank-one interactions whose forbidden
vector has two equal nonzero Schmidt probabilities. It applies in every
finite local dimension. The new case is the three-dimensional span of
two distinct, intersecting Schmidt supports. A four-site argument
distinguishes a propagating extremal overlap mode from an obstruction to
its propagation. The result also classifies the complete qutrit fibre
with Schmidt probabilities $`(1/2,1/2,0)`$ and the specified two- and
three-site spectra. That fibre has a one-parameter normal form, is
uniformly gapped except at its marker endpoint, and has a quantitative
lower bound throughout its gapped part.

Bravyi and Gosset classified arbitrary frustration-free qubit chains and
proposed rank-one and rank-two qutrit interactions as a next case . Our
theorem does not classify arbitrary qutrit interactions: unequal Schmidt
probabilities and general rank-two projectors remain outside its
principal scope. Lemm already supplied deterministic three-site criteria
and deterministic neighbourhoods ; Hunter-Jones and Lemm extend low-rank
methods to bounded-degree graphs . The hierarchy of Rai et al. includes
established finite-size positive decompositions . We use that general
method, with an explicitly proved open-boundary decomposition, and do
not claim a new semidefinite hierarchy.

The previous version supplied examples and bounds but left the
isospectral interpolation unresolved. The supplied review correctly
identified a weaker locally-isospectral obstruction obtainable from the
qubit classification and missing Motzkin comparisons.
Section <a href="#sec:qubitcomparison" data-reference-type="ref"
data-reference="sec:qubitcomparison">5.3</a> includes that comparison;
Section <a href="#sec:motzkin" data-reference-type="ref"
data-reference="sec:motzkin">8.5</a> gives the actual local terms,
normalisations and boundaries. The unrestricted obstruction is not our
originality claim. The principal candidate contribution is now the
complete flat-Schmidt-rank-two classification and its quantitative
four-site proof. A targeted primary-source search did not locate this
theorem; that search is not proof of historical priority.

<div id="lem:ff" class="lemma">

**Lemma 1** (Frustration freeness). *If a two-site projector has rank
strictly below $`d`$, every open chain has a nonzero product vector in
its kernel.*

</div>

<div class="proof">

*Proof.* Choose a nonzero first-site vector. Once $`x_i`$ has been
chosen, orthogonality of $`x_i\otimes x_{i+1}`$ to the forbidden space
imposes fewer than $`d`$ homogeneous linear constraints on $`x_{i+1}`$.
A nonzero solution exists. Continue along the chain. This is the
elementary product-state argument underlying the low-rank regime
discussed in . ◻

</div>

#### Known components and candidate extensions.

The qubit dichotomy is Theorem 1 of Bravyi–Gosset . The ground-space
recurrence is equation (11), Section II, of Movassagh et al. ; our
Proposition <a href="#prop:degeneracy" data-reference-type="ref"
data-reference="prop:degeneracy">11</a> proves its exact persistence
throughout a particular nongeneric fibre, including the gapless
endpoint. The unbiased hopping gap is used in Step 1 of the Motzkin
proof ; Theorem <a href="#thm:marker" data-reference-type="ref"
data-reference="thm:marker">6</a> permits arbitrary overlap of the two
background vectors and proves a global, rather than sector-only,
equality. The principal classification and the quantitative saturation
obstruction are distinguished from these ingredients.

# Complete classification at flat Schmidt rank two

Let
``` math
\rho_L=\operatorname{Tr}_2 P,\qquad \rho_R=\operatorname{Tr}_1 P,
 \qquad L=\operatorname{ran}\rho_L,\quad R=\operatorname{ran}\rho_R.
```
Both supports are subspaces of the same on-site space, in the same
physical basis. Throughout this section the two nonzero eigenvalues of
each reduced density matrix are $`1/2`$. Thus $`\Pi_L=2\rho_L`$ and
$`\Pi_R=2\rho_R`$ are rank-two orthogonal projectors.

<div id="thm:classification" class="theorem">

**Theorem 2** (Flat-Schmidt-rank-two dichotomy). *For every finite
$`d\ge2`$, the chain <a href="#eq:HN" data-reference-type="eqref"
data-reference="eq:HN">[eq:HN]</a> is gapless if and only if there are
unit vectors $`u,v,w\in\mathbb C^d`$, with $`w\perp u,v`$, for which, up
to an irrelevant overall phase,
``` math
\begin{equation}
\label{eq:balancedmarker}
 \psi=\frac{\lvert u,w\rangle-\lvert w,v\rangle}{\sqrt2}.
\end{equation}
```
In every gapless case the full finite-chain gap is exactly
``` math
\begin{equation}
\label{eq:diffusive}
 \gamma_N=1-\cos(\pi/N).
\end{equation}
```
Every other interaction in the specified Schmidt class is uniformly
gapped. More explicitly:*

1.  *If $`L\cap R=\{0\}`$, then
    $`\gamma_N\ge1-\left\lVert \Pi_L\Pi_R\right\rVert>0`$.*

2.  *If $`L=R`$, then
    <a href="#eq:balancedmarker" data-reference-type="eqref"
    data-reference="eq:balancedmarker">[eq:balancedmarker]</a> holds and
    <a href="#eq:diffusive" data-reference-type="eqref"
    data-reference="eq:diffusive">[eq:diffusive]</a> applies.*

3.  *If $`L\cap R=\mathbb Cw`$, choose unit $`u\in L\ominus\mathbb Cw`$
    and $`v\in R\ominus\mathbb Cw`$, and define
    ``` math
    \begin{equation}
    \label{eq:invariants}
     t=|\langle u,v\rangle|=\sqrt{\operatorname{tr}(\Pi_L\Pi_R)-1}<1,
     \qquad \tau=2|\langle w,w|\psi\rangle|^2\in[0,1].
    \end{equation}
    ```
    The chain is gapless exactly when $`\tau=0`$. For $`\tau>0`$, every
    $`N\ge2`$ satisfies
    ``` math
    \begin{equation}
    \label{eq:generalbound}
     \gamma_N\ge \frac{3\tau(2-t)(1-t)}{1024}>0.
    \end{equation}
    ```*

</div>

The invariants do not depend on phases chosen for $`u,v,w`$. In local
dimension three, only the second and third alternatives occur. The bound
in <a href="#eq:generalbound" data-reference-type="eqref"
data-reference="eq:generalbound">[eq:generalbound]</a> is deliberately
conservative; it is not asserted to be the thermodynamic gap or to give
an optimal critical exponent.

<div id="cor:minimal" class="corollary">

**Corollary 3** (Dimension-minimal flat separation). *Every maximally
entangled two-qubit forbidden vector gives the exact gap
<a href="#eq:diffusive" data-reference-type="eqref"
data-reference="eq:diffusive">[eq:diffusive]</a>. Dimension three is
minimal for a gapped/gapless separation with flat rank-two Schmidt
probabilities, even when complete two- and three-site spectra are also
required to agree.*

</div>

The existence part is furnished by
Section <a href="#sec:isospectral" data-reference-type="ref"
data-reference="sec:isospectral">5</a>. The qubit impossibility follows
from the coincident-support alternative of
Theorem <a href="#thm:classification" data-reference-type="ref"
data-reference="thm:classification">2</a>; it also follows immediately
from Bravyi–Gosset’s transfer-matrix criterion.

<div class="remark">

*Remark 4* (Higher flat Schmidt ranks). For a rank-one projector whose
forbidden vector has $`r\ge3`$ equal nonzero Schmidt probabilities, the
elementary overlap bound gives $`\gamma_N\ge1-2/r>0`$. The threshold
case $`r=2`$ is therefore the only flat entangled Schmidt class
requiring the saturation analysis below. This observation is a
consequence of the standard overlap method, not a separate novelty
claim.

</div>

# Overlap bounds and an exactly solvable marker family

The following is the standard adjacent-projection strategy, retaining a
finite-path cosine factor. We include the proof and make no claim that
this general gap method is new; compare .

<div id="lem:overlap" class="lemma">

**Lemma 5** (Finite-path overlap bound). *Let $`P`$ be a two-site
projector and let $`c=\left\lVert P_{12}P_{23}\right\rVert`$. Whenever
the right-hand side is positive,
``` math
\begin{equation}
\label{eq:pathbound}
 \gamma_N(P)\ge1-2c\cos(\pi/N).
\end{equation}
```
For $`P=\lvert \psi\rangle\langle \psi\rvert`$, write
$`\psi=\sum_{i,j}M_{ij}\lvert ij\rangle`$ with
$`\left\lVert M\right\rVert_F=1`$. Then
``` math
\begin{equation}
\label{eq:contraction}
 c=\left\lVert \overline M M\right\rVert=\left\lVert M\overline M\right\rVert.
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Put $`p_i=P_{i,i+1}`$ and $`z_i=\left\lVert p_i x\right\rVert`$
for an arbitrary vector $`x`$. Disjoint projections commute, hence have
nonnegative anticommutator. For adjacent terms, the norm of their
product bounds the angle between their ranges, giving
``` math
\langle x,H_N^2x\rangle\ge\sum_{i=1}^{N-1}z_i^2
       -2c\sum_{i=1}^{N-2}z_i z_{i+1}.
```
The largest eigenvalue of the adjacency matrix of the $`(N-1)`$-vertex
path is $`2\cos(\pi/N)`$. Thus $`H_N^2\ge(1-2c\cos(\pi/N))H_N`$, which
implies <a href="#eq:pathbound" data-reference-type="eqref"
data-reference="eq:pathbound">[eq:pathbound]</a> by the spectral
theorem.

For <a href="#eq:contraction" data-reference-type="eqref"
data-reference="eq:contraction">[eq:contraction]</a>, use the isometries
$`Vx=\psi\otimes x`$ and $`Wy=y\otimes\psi`$ into three sites. Their
overlap has entries $`(V^*W)_{c,a}=\sum_b\overline{M_{ab}}M_{bc}`$, so
$`V^*W=(\overline M M)^T`$. As $`P_{12}P_{23}=V(V^*W)W^*`$, its norm is
the norm of this $`d\times d`$ overlap matrix. Complex conjugation gives
the second equality. ◻

</div>

The readily computable region
$`\left\lVert \overline M M\right\rVert<1/2`$ therefore has a uniform
gap. It is sufficient, not necessary. Even the largest Schmidt
probability being below $`1/2`$ is sufficient, since
$`\left\lVert \overline M M\right\rVert\le\left\lVert M\right\rVert^2`$,
but the flat rank-two case reaches the threshold and requires more
information.

<div id="thm:marker" class="theorem">

**Theorem 6** (Exact marker family). *Let $`u,v,w`$ be unit vectors with
$`w\perp u,v`$. The overlap $`\langle u,v\rangle`$ is arbitrary. For
$`a,b\ge0`$ with $`a^2+b^2=1`$, set
``` math
\begin{equation}
\label{eq:marker-family}
 \psi=a\lvert u,w\rangle-b\lvert w,v\rangle.
\end{equation}
```
Then for all $`N\ge2`$,
``` math
\begin{equation}
\label{eq:marker-exact}
 \gamma_N(\lvert \psi\rangle\langle \psi\rvert)=1-2ab\cos(\pi/N).
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Choose coordinates with $`w`$ a real basis vector. The
coefficient matrix is $`M=a u w^T-b w v^T`$, so
``` math
M\overline M=-ab\bigl(u v^*+\langle u,v\rangle w w^*\bigr).
```
The two displayed summands have orthogonal domain and range supports;
the first has norm one and the second norm at most one. Hence $`c=ab`$,
and Lemma <a href="#lem:overlap" data-reference-type="ref"
data-reference="lem:overlap">5</a> gives the lower bound.

For the matching upper bound, consider the $`N`$ orthonormal vectors
``` math
e_j=u^{\otimes(j-1)}\otimes w\otimes v^{\otimes(N-j)},\quad 1\le j\le N.
```
They are orthogonal because the unique $`w`$ occurs at different sites,
regardless of $`\langle u,v\rangle`$. Their span is reducing: away from
the marker, every bond is orthogonal to the forbidden vector, while a
bond adjoining it moves the marker by one site. The restricted
Hamiltonian is $`D^*D`$, where row $`j`$ of $`D`$ has entries $`-b`$ at
column $`j`$ and $`a`$ at column $`j+1`$. The matrix $`DD^*`$ has
diagonal one and off-diagonal entries $`-ab`$. Its eigenvalues are
$`1-2ab\cos(k\pi/N)`$, $`1\le k\le N-1`$. The least of these attains the
lower bound. The cases $`ab=0`$ also follow directly. ◻

</div>

When $`u,v`$ are independent and $`ab>0`$, their union with $`w`$ spans
three local dimensions. Thus the statement includes genuinely qutrit
forbidden states, not only a qubit interaction with an unused level.
Taking $`u=\lvert 0\rangle`$, $`w=\lvert 1\rangle`$,
$`v=\lvert 2\rangle`$, $`a=b=1/\sqrt2`$ gives the gapless endpoint in
Section <a href="#sec:isospectral" data-reference-type="ref"
data-reference="sec:isospectral">5</a>.

# Four-site saturation and proof of the dichotomy

## Schmidt-support geometry

Write $`\psi=\sum M_{ij}\lvert ij\rangle`$. A Schmidt decomposition
gives $`M=AB^T/\sqrt2`$, where $`A,B`$ are $`d\times2`$ isometries onto
$`L,R`$. The nonzero singular values of $`(\overline M M)^T`$ are one
half the singular values of $`A^*B`$. Indeed, the outer factors in
$`\overline A(B^*A)B^T/2`$ are isometries or coisometries. Therefore
``` math
\begin{equation}
\label{eq:angleoverlap}
 \left\lVert P_{12}P_{23}\right\rVert=\tfrac12\left\lVert \Pi_L\Pi_R\right\rVert.
\end{equation}
```
If $`L\cap R=\{0\}`$, compactness of unit spheres gives
$`\left\lVert \Pi_L\Pi_R\right\rVert<1`$ and
Lemma <a href="#lem:overlap" data-reference-type="ref"
data-reference="lem:overlap">5</a> proves alternative 1.

Suppose henceforth that $`L\cap R=\mathbb Cw`$. Choose phases so
$`\langle u,v\rangle=t\ge0`$. In the orthonormal left frame $`(u,w)`$
and right frame $`(w,v)`$,
``` math
\begin{equation}
\label{eq:Uframe}
 \psi=\frac{a\lvert u,w\rangle+b\lvert u,v\rangle+c\lvert w,w\rangle+d\lvert w,v\rangle}{\sqrt2},
 \qquad U=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in U(2).
\end{equation}
```
Here $`\tau=|c|^2`$. These coefficients are unrelated to the weights of
the marker or dimer families. Put
``` math
\begin{equation}
\label{eq:lr}
 \ell=\sqrt2(I\otimes\langle w\rvert)\psi=a u+c w,
 \qquad r=\sqrt2(\langle w\rvert\otimes I)\psi=c w+d v.
\end{equation}
```
Both vectors are unit. Unitarity of $`U`$ gives the useful scalar
identities
``` math
\begin{equation}
\label{eq:scalars}
 \langle\psi|\ell,\ell\rangle=\langle\psi|r,r\rangle
 =\frac c{\sqrt2}=\langle w,w|\psi\rangle.
\end{equation}
```
For example, the first contraction is
$`[c(|a|^2+|c|^2)+ta(\overline b a+\overline d c)]/\sqrt2=c/\sqrt2`$.
The second follows from $`\overline a c+\overline b d=0`$ and
$`|c|^2+|d|^2=1`$. This calculation permits arbitrary complex
coefficients; it is not restricted to real forbidden vectors.

## The extremal adjacent-pair mode

For adjacent bond projectors $`p,q`$, define
``` math
\begin{equation}
\label{eq:Adef}
 \mathcal A(p,q)=(p+q)^2-\tfrac12(p+q).
\end{equation}
```
By <a href="#eq:angleoverlap" data-reference-type="eqref"
data-reference="eq:angleoverlap">[eq:angleoverlap]</a>,
$`\left\lVert pq\right\rVert=1/2`$. The nonzero singular values of the
range overlap are $`1/2,t/2`$. The two-projection decomposition thus
gives eigenvalues $`1\pm1/2`$ and $`1\pm t/2`$, with any remaining
positive eigenvalues equal to one, for $`p+q`$. Consequently
$`\mathcal A(p,q)\ge0`$.

With $`Vx=\psi\otimes x`$ and $`Wy=y\otimes\psi`$, one has
$`V^*W\ell=r/2`$ and $`W^*Vr=\ell/2`$. Thus
``` math
\begin{equation}
\label{eq:xi}
 \xi=\psi\otimes r-\ell\otimes\psi,
 \quad \left\lVert \xi\right\rVert=1,
 \quad p\xi=\tfrac12\psi\otimes r,
 \quad q\xi=-\tfrac12\ell\otimes\psi.
\end{equation}
```
Since $`t<1`$, the eigenvalue $`1/2`$ of $`p+q`$ is simple. The kernel
of $`\mathcal A(p,q)`$ is exactly the direct sum of the common zero
space of $`p,q`$ and $`\mathbb C\xi`$. On its orthogonal complement,
``` math
\begin{equation}
\label{eq:delta}
 \mathcal A(p,q)\ge \delta I,
 \qquad \delta=(1-t/2)(1-t)/2=\frac{(2-t)(1-t)}4.
\end{equation}
```
The statement remains valid after tensoring with arbitrary exterior
sites.

## A clipped four-site criterion

<div id="lem:saturation" class="lemma">

**Lemma 7** (Four-site saturation criterion). *Let $`P`$ be a two-site
projector with $`\left\lVert P_{12}P_{23}\right\rVert\le1/2`$. On four
sites put $`p_j=P_{j,j+1}`$, $`h=p_1+p_2+p_3`$, and
``` math
\begin{equation}
\label{eq:Gdef}
 \mathcal G=\mathcal A(p_1,p_2)+\mathcal A(p_2,p_3)+2p_1p_3
 =h^2-\tfrac12(p_1+p_3)\ge0.
\end{equation}
```
If $`\mathcal G\ge\kappa h`$ for some $`0<\kappa\le(3-\sqrt5)/4`$, then
every open chain satisfies
``` math
\begin{equation}
\label{eq:saturationbound}
 H_N^2\ge\tfrac32\kappa H_N,\qquad \gamma_N\ge\tfrac32\kappa.
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Extend $`p_i=0`$ outside $`1\le i\le N-1`$ and sum
<a href="#eq:Gdef" data-reference-type="eqref"
data-reference="eq:Gdef">[eq:Gdef]</a> over all three-bond windows
meeting the chain. A clipped one-bond window gives at least $`p/2`$. A
clipped two-bond window gives $`(p+q)^2-p/2`$, or its reflected version.
For any $`x`$, writing $`u=\left\lVert px\right\rVert`$ and
$`v=\left\lVert qx\right\rVert`$ bounds this quadratic form below by
$`u^2/2+v^2-uv`$. Its least matrix eigenvalue is $`\eta=(3-\sqrt5)/4`$,
so it is at least $`\eta\langle x,(p+q)x\rangle`$. Thus every full or
clipped window obeys the same inequality with $`\kappa`$.

Every bond is counted three times on the right. Direct expansion on the
left gives
``` math
\sum_j\mathcal G_j
 =2H_N+2\sum_i\{p_i,p_{i+1}\}+2\sum_i p_i p_{i+2}
 \le2H_N^2.
```
The difference consists of positive products of disjoint commuting
projectors. Therefore $`3\kappa H_N\le2H_N^2`$. The argument includes
$`N=2,3`$ because the zero extension retains all clipped windows. ◻

</div>

This is an explicit local positive decomposition in the established
finite-size framework. Its role is to exploit *incompatible saturation*
of adjacent pairs, not to lower the generic three-site threshold by
assertion.

## Quantitative incompatibility of saturation

<div id="lem:quantitative" class="lemma">

**Lemma 8** (The overlap obstruction). *Under
<a href="#eq:Uframe" data-reference-type="eqref"
data-reference="eq:Uframe">[eq:Uframe]</a>, if $`t<1`$ and $`\tau>0`$,
then
``` math
\begin{equation}
\label{eq:Gquant}
 \mathcal G\ge\frac{\tau\delta}{128}\,h.
\end{equation}
```*

</div>

<div class="proof">

*Proof.* For arbitrary $`x`$ on four sites let
$`E=\langle x,\mathcal Gx\rangle`$ and
``` math
\epsilon^2=\frac{\langle x,\mathcal A(p_1,p_2)x\rangle}{\delta},\quad
 \zeta^2=\frac{\langle x,\mathcal A(p_2,p_3)x\rangle}{\delta},\quad
 R_0=\sqrt{E/\delta}.
```
Then $`\epsilon^2+\zeta^2\le R_0^2`$. Orthogonally project $`x`$ onto
the kernels of these two pair operators and use
<a href="#eq:xi" data-reference-type="eqref"
data-reference="eq:xi">[eq:xi]</a>. The components in the common zero
spaces disappear when the corresponding bond projectors act. Absorbing
the factor $`1/2`$ in exterior vectors $`z,y`$, we obtain
``` math
\begin{align*}
 p_1x&=\psi\otimes r\otimes z+e_1,&
 p_2x&=-\ell\otimes\psi\otimes z+e_2,\\
 p_2x&=y\otimes\psi\otimes r+f_2,&
 p_3x&=-y\otimes\ell\otimes\psi+f_3,
\end{align*}
```
where
$`\left\lVert e_1\right\rVert,\left\lVert e_2\right\rVert\le\epsilon`$
and $`\left\lVert f_2\right\rVert,\left\lVert f_3\right\rVert\le\zeta`$.
Comparing the two expressions for $`p_2x`$ gives
$`\left\lVert \ell\otimes z+y\otimes r\right\rVert\le\epsilon+\zeta`$.
Let $`\alpha=\langle r,z\rangle`$. Contracting with $`r`$ on the right
gives $`\left\lVert y+\alpha\ell\right\rVert\le\epsilon+\zeta`$;
projecting on $`r^\perp`$ gives
$`\left\lVert z-\alpha r\right\rVert\le\epsilon+\zeta`$. Consequently
``` math
\begin{align*}
 p_1x&=\alpha\psi\otimes r\otimes r+E_1,\\
 p_2x&=-\alpha\ell\otimes\psi\otimes r+E_2,\\
 p_3x&=\alpha\ell\otimes\ell\otimes\psi+E_3,
\end{align*}
```
with
$`\left\lVert E_1\right\rVert,\left\lVert E_2\right\rVert\le2\epsilon+\zeta\le\sqrt5R_0`$
and $`\left\lVert E_3\right\rVert\le\epsilon+2\zeta\le\sqrt5R_0`$. Since
$`2\left\lVert p_1p_3x\right\rVert^2\le E`$, applying $`p_1`$ to the
third expression and using
<a href="#eq:scalars" data-reference-type="eqref"
data-reference="eq:scalars">[eq:scalars]</a> yields
``` math
|\alpha|\sqrt{\tau/2}\le\sqrt{E/2}+\sqrt5R_0
 \le(1/2+\sqrt5)R_0,
```
where $`\delta\le1/2`$ was used. Thus $`|\alpha|\le4R_0/\sqrt\tau`$.
Minkowski’s inequality in the direct sum of the three projected spaces
gives
``` math
\sqrt{\langle x,hx\rangle}
 \le\sqrt3|\alpha|+\sqrt{15}R_0
 \le(4\sqrt3+\sqrt{15})R_0/\sqrt\tau.
```
Because $`(4\sqrt3+\sqrt{15})^2=63+24\sqrt5<128`$, this proves
<a href="#eq:Gquant" data-reference-type="eqref"
data-reference="eq:Gquant">[eq:Gquant]</a>. The estimates also cover
$`E=0`$ directly. ◻

</div>

## Completion of the classification

If $`\tau>0`$, apply
Lemmas <a href="#lem:quantitative" data-reference-type="ref"
data-reference="lem:quantitative">8</a> and
<a href="#lem:saturation" data-reference-type="ref"
data-reference="lem:saturation">7</a>, noting that
$`\tau\delta/128\le1/256<\eta`$. This gives exactly
<a href="#eq:generalbound" data-reference-type="eqref"
data-reference="eq:generalbound">[eq:generalbound]</a>. If $`\tau=0`$,
then $`c=0`$ in <a href="#eq:Uframe" data-reference-type="eqref"
data-reference="eq:Uframe">[eq:Uframe]</a>; unitarity forces $`b=0`$ and
$`|a|=|d|=1`$. Absorb these phases into $`u,v`$ to obtain
<a href="#eq:balancedmarker" data-reference-type="eqref"
data-reference="eq:balancedmarker">[eq:balancedmarker]</a>.
Theorem <a href="#thm:marker" data-reference-type="ref"
data-reference="thm:marker">6</a> then gives
<a href="#eq:diffusive" data-reference-type="eqref"
data-reference="eq:diffusive">[eq:diffusive]</a>.

If $`L=R`$, restrict to this common two-dimensional space. The
homogeneous complex quadratic $`\langle w,w|\psi\rangle`$ has a nonzero
zero $`w`$: this is the elementary fact that every binary complex
quadratic is isotropic, with the identically zero polynomial included.
Normalise $`w`$ and complete it by an orthogonal unit vector $`u`$. In
the frame $`(u,w)`$ on both factors, the scaled coefficient matrix is
unitary. Its $`ww`$ entry vanishes, so its $`uu`$ entry also vanishes
and the two off-diagonal entries have modulus one. The forbidden state
is a balanced marker with $`v`$ a phase multiple of $`u`$. The exact
marker theorem applies on the whole on-site space, including unused
levels.

When the intersection is one-dimensional, $`L+R`$ has dimension three,
irrespective of the ambient $`d`$. The quantitative proof was given
using only vectors and operators supported on this span. Equivalently,
orthogonal spectator levels split the chain into open active segments
and cannot lower a uniform bound. This proves every case of
Theorem <a href="#thm:classification" data-reference-type="ref"
data-reference="thm:classification">2</a>. It proves the if-and-only-if
statement without assuming that a low-energy vector in a selected sector
is orthogonal to an unspecified ground space.

# The complete two- and three-site isospectral fibre

<div id="thm:fibre" class="theorem">

**Theorem 9** (Normal form and gap classification of the fibre).
*Suppose $`d=3`$, the Schmidt probabilities are $`(1/2,1/2,0)`$, and
``` math
\begin{equation}
\label{eq:h3spec}
 \operatorname{spec}H_3=\{0^{(21)},(1/2)^{(1)},1^{(4)},(3/2)^{(1)}\}.
\end{equation}
```
Up to an identical on-site unitary and an irrelevant phase, there is a
unique $`\theta\in[0,\pi/2]`$ for which
``` math
\begin{equation}
\label{eq:isopath}
 \psi=\psi_\theta=
 \frac{\cos\theta\lvert 00\rangle+\sin\theta\lvert 01\rangle-\lvert 12\rangle}{\sqrt2}.
\end{equation}
```
Every point has <a href="#eq:h3spec" data-reference-type="eqref"
data-reference="eq:h3spec">[eq:h3spec]</a> and
$`\operatorname{spec}H_2=\{0^{(8)},1\}`$. All $`\theta<\pi/2`$ are
uniformly gapped, with
``` math
\begin{equation}
\label{eq:fibrebound}
 \gamma_N(\psi_\theta)\ge\frac{\cos^2\theta}{6}\quad(N\ge2),
\end{equation}
```
whereas $`\gamma_N(\psi_{\pi/2})=1-\cos(\pi/N)`$. The bound in
<a href="#eq:fibrebound" data-reference-type="eqref"
data-reference="eq:fibrebound">[eq:fibrebound]</a> is a lower bound, not
an exact formula away from the endpoint.*

</div>

<div class="proof">

*Normal form and short spectra.* The positive eigenvalues of $`H_3`$ are
$`1\pm s_j(V^*W)`$. Since $`s_j\le1/2`$, none disappears at zero.
Therefore <a href="#eq:h3spec" data-reference-type="eqref"
data-reference="eq:h3spec">[eq:h3spec]</a> forces overlap singular
values $`(1/2,0,0)`$ and hence $`t=0`$. The supports intersect in a line
but are not equal, and $`u,w,v`$ in
<a href="#eq:Uframe" data-reference-type="eqref"
data-reference="eq:Uframe">[eq:Uframe]</a> form an orthonormal basis.
Their independent phases, together with the phase of $`\psi`$, reduce
the unitary coefficient matrix to
``` math
\begin{pmatrix}-s&-c\\c&-s\end{pmatrix},\qquad
 c=\sqrt\tau,\quad s=\sqrt{1-\tau}.
```
For nonzero entries, the only phase constraint is the unitary identity
$`\arg a+\arg d-\arg b-\arg c=\pi\pmod{2\pi}`$, which is exactly the
constraint of this real representative. Vanishing endpoint entries cause
no obstruction. Set $`e_0=cw-su`$, $`e_1=sw+cu`$, $`e_2=v`$. This gives
<a href="#eq:isopath" data-reference-type="eqref"
data-reference="eq:isopath">[eq:isopath]</a> with $`c=\cos\theta`$,
$`s=\sin\theta`$. The invariant $`\tau`$ determines $`\theta`$ uniquely.

Conversely
``` math
M_\theta=\frac1{\sqrt2}\begin{pmatrix}c&s&0\\0&0&-1\\0&0&0\end{pmatrix},\quad
 M_\theta^2=\frac12\begin{pmatrix}c^2&cs&-s\\0&0&0\\0&0&0\end{pmatrix}.
```
The rows of $`M_\theta`$ have squared norm $`1/2`$ and are orthogonal.
The sole nonzero singular value of $`M_\theta^2`$ is $`1/2`$, using
$`c^4+c^2s^2+s^2=1`$. This proves the stated Schmidt and short-chain
spectra. Gappedness except at $`c=0`$ already follows from
Theorem <a href="#thm:classification" data-reference-type="ref"
data-reference="thm:classification">2</a>. The sharper bound is proved
next. ◻

</div>

## A three-dimensional certificate inside the four-site range

<div id="lem:gram" class="lemma">

**Lemma 10** (Full range-Gram decomposition). *For the fibre normal
form, the operator $`K-D`$ defined below is unitarily equivalent to
$`S(c)`$, the scalars $`-1/2,1/2`$, four copies of
$`\left(\begin{smallmatrix}1/2&1/2\\1/2&1\end{smallmatrix}\right)`$, ten
scalar blocks $`1/2`$, and four scalar blocks $`1`$. Its negative
eigenspace is the single direction $`(\psi,0,-\psi)`$, which lies in
$`\ker C`$. In particular the entire Gram operator is not positive: the
relevant inequality is on $`\operatorname{ran}C^*`$.*

</div>

<div class="proof">

*Proof.* Write $`\ell=e_0`$, $`r=(c^2,cs,-s)^T`$ in the computational
frame of <a href="#eq:isopath" data-reference-type="eqref"
data-reference="eq:isopath">[eq:isopath]</a>. Let
``` math
C=(V_1\;V_2\;V_3),\quad
 V_1x=\psi\otimes x,\quad V_2=I\otimes\psi\otimes I,\quad V_3x=x\otimes\psi,
```
where every $`V_i`$ has nine columns. Then $`H_4=CC^*`$ and, with
$`K=C^*C`$,
``` math
\mathcal G=C(K-D)C^*,\qquad D=\operatorname{diag}(\tfrac12 I_9,0_9,\tfrac12 I_9).
```
The off-diagonal Gram blocks are
``` math
K_{12}=\tfrac12(\lvert r\rangle\langle \ell\rvert\otimes I),\quad
 K_{23}=\tfrac12(I\otimes\lvert r\rangle\langle \ell\rvert),\quad
 K_{13}=\lvert \psi\rangle\langle \psi\rvert.
```
Set $`\alpha=c/\sqrt2`$ and $`\beta=\sqrt{1-c^2/2}`$. A reducing
five-dimensional core is spanned, in the first, middle and last column
spaces respectively, by
``` math
a=r\otimes r,\ a'=(\psi-\alpha a)/\beta;\qquad
 b=\ell\otimes r;\qquad
 d=\ell\otimes\ell,\ d'=(\psi-\alpha d)/\beta.
```
These are orthonormal within their column spaces. Reflection exchanging
$`(a,a')`$ and $`(d,d')`$ splits the core. The odd block has eigenvalues
$`-1/2,1/2`$. The negative vector is proportional to $`(\psi,0,-\psi)`$
and is killed by $`C`$. In the even basis
$`(a+d)/\sqrt2,(a'+d')/\sqrt2,b`$, the block is
``` math
\begin{equation}
\label{eq:Score}
 S(c)=\begin{pmatrix}
 (1+c^2)/2&c\sqrt{2-c^2}/2&1/\sqrt2\\
 c\sqrt{2-c^2}/2&(3-c^2)/2&0\\
 1/\sqrt2&0&1
 \end{pmatrix}.
\end{equation}
```
Outside this core, there are four two-dimensional blocks with diagonal
$`(1/2,1)`$ and off-diagonal $`1/2`$, ten scalar blocks $`1/2`$, and
four scalar blocks $`1`$. To see the four paired blocks explicitly, use
the two dimensions of $`\ell\otimes r^\perp`$ in the middle space and
their first-space partners $`r\otimes r^\perp`$, and the two dimensions
of $`\ell^\perp\otimes r`$ and their last-space partners
$`\ell^\perp\otimes\ell`$. The remaining spaces have no overlap
coupling. Appendix <a href="#app:basis" data-reference-type="ref"
data-reference="app:basis">10</a> specifies the complementary bases and
the transformation without excluding either endpoint. ◻

</div>

<div class="proof">

*Completion of the fibre bound.* For $`c>0`$, the leading principal
minors of $`S(c)`$ are $`(1+c^2)/2`$, $`3/4`$, and $`c^2/4`$, so
$`S(c)>0`$. Its characteristic polynomial is
``` math
\begin{equation}
\label{eq:Scubic}
 \det(xI-S(c))=x(x-3/2)^2-c^2/4.
\end{equation}
```
If $`\lambda_1\le\lambda_2\le\lambda_3`$ are its eigenvalues, the sum of
their pairwise products is $`9/4`$. Hence
$`\lambda_1=(c^2/4)/(\lambda_2\lambda_3)\ge c^2/9`$. The other
nonnegative blocks have least eigenvalue at least $`(3-\sqrt5)/4>1/9`$.
Since $`\operatorname{ran}C^*`$ is orthogonal to the negative vector, we
have
``` math
\mathcal G\ge(c^2/9)H_4.
```
Lemma <a href="#lem:saturation" data-reference-type="ref"
data-reference="lem:saturation">7</a> proves
<a href="#eq:fibrebound" data-reference-type="eqref"
data-reference="eq:fibrebound">[eq:fibrebound]</a>. At $`c=0`$ the
marker theorem gives the exact endpoint gap. This completes
Theorem <a href="#thm:fibre" data-reference-type="ref"
data-reference="thm:fibre">9</a>. ◻

</div>

## Constant degeneracy and a dimension-minimal separation

The recurrence itself is the $`d=3,r=1`$ case of equation (11) in
Section II of Movassagh et al. . What is proved here is its exact
validity at every point of this specified fibre, not just at generic
interactions, together with its failure to determine gappedness.

<div id="prop:degeneracy" class="proposition">

**Proposition 11** (The ground-space dimension stays fixed along the
fibre). *For every $`\theta\in[0,\pi/2]`$, let
$`D_N=\dim\ker H_N(\psi_\theta)`$ and $`D_0=1`$. Then
``` math
D_1=3,\qquad D_N=3D_{N-1}-D_{N-2}=F_{2N+2},
```
where $`F_0=0,F_1=1`$ are the Fibonacci numbers.*

</div>

<div class="proof">

*Proof.* The orthogonal complement of the ground space is the
degree-$`N`$ part of the two-sided tensor ideal generated by
$`c\,00+s\,01-12`$. Orient its sole linear rewriting rule as
$`12\mapsto c\,00+s\,01`$. Degree-lexicographic order with $`1>0`$ makes
every replacement decrease the word. The leading word $`12`$ has no
proper self-overlap. Disjoint replacements commute, so induction in this
finite order makes the normal form well-defined and unique. Thus words
avoiding $`12`$ form a basis of the quotient: a linear combination of
such words cannot reduce to zero unless all coefficients vanish. There
are $`3D_{N-1}`$ extensions of admissible words, and exactly $`D_{N-2}`$
forbidden extensions ending in $`12`$, because every admissible prefix
can be followed by $`1`$. This gives the recurrence and its stated
solution. ◻

</div>

The gapped and gapless endpoints therefore have the same ground-space
dimension at every length, as well as the same specified short-chain
spectra and Schmidt probabilities. No assertion is made that their full
spectra agree beyond length three.

Put $`\psi_{\mathrm d}=\psi_0`$, $`\psi_{\mathrm m}=\psi_{\pi/2}`$ and
$`P_{\mathrm d,\mathrm m}=\lvert \psi_{\mathrm d,\mathrm m}\rangle\langle \psi_{\mathrm d,\mathrm m}\rvert`$.
The sharper dimer estimate in
Section <a href="#sec:dimer" data-reference-type="ref"
data-reference="sec:dimer">6</a> gives
``` math
\begin{equation}
\label{eq:mainbounds}
 \gamma_N(P_{\mathrm d})\ge1/4,\qquad
 \gamma_N(P_{\mathrm m})=1-\cos(\pi/N).
\end{equation}
```
The union of the left and right supports spans all three local levels at
either endpoint. Together with the qubit part of
Theorem <a href="#thm:classification" data-reference-type="ref"
data-reference="thm:classification">2</a>, this proves
Corollary <a href="#cor:minimal" data-reference-type="ref"
data-reference="cor:minimal">3</a>.

## The weaker qubit obstruction from the supplied review

The unrestricted statement that Schmidt data and two short spectra
cannot classify gaps is already a short consequence of Bravyi–Gosset.
The following explicit pair was derived in the supplied review, rather
than quoted as a pair printed in :
``` math
\chi_c=\frac{\lvert 00\rangle}{\sqrt2}+\frac{\lvert 01\rangle-\lvert 10\rangle}2,
 \qquad
 \chi_g=\frac{\lvert 00\rangle}2+\frac{1+\sqrt5}{4}\lvert 01\rangle
       +i\frac{\sqrt5-1}{4}\lvert 10\rangle.
```
Their Schmidt probabilities are $`(2\pm\sqrt3)/4`$, and their common
three-site characteristic polynomial is
``` math
x^4\bigl((x-1)^4-\tfrac38(x-1)^2+1/256\bigr).
```
For
$`T_\chi=\left(\begin{smallmatrix}\overline{\chi_{01}}&\overline{\chi_{11}}\\-\overline{\chi_{00}}&-\overline{\chi_{10}}\end{smallmatrix}\right)`$,
the first state has eigenvalue moduli $`1/2,1/2`$ and the second has
$`(\sqrt5+1)/4,(\sqrt5-1)/4`$. Theorem 1 of makes the first gapless and
the second gapped. Adding a spectator level yields a qutrit comparison.
This does not have flat Schmidt probabilities. We retain the supplied
exact verifier and its derivation in the evidence bundle and do not
claim this weaker obstruction as an independent new theorem.

# The dimer family is uniformly gapped

<div id="thm:dimer" class="theorem">

**Theorem 12** (All positive dimer weights). *For $`a,b>0`$,
$`a^2+b^2=1`$, and
``` math
\begin{equation}
\label{eq:dimer-family}
 \psi=a\lvert 00\rangle-b\lvert 12\rangle,
\end{equation}
```
one has $`\gamma_N(\lvert \psi\rangle\langle \psi\rvert)\ge b^4`$ for
every $`N\ge2`$. At either endpoint $`a=0`$ or $`b=0`$ the
commuting-projector chain has gap one.*

</div>

## Reducing sectors as hard-core configurations

The only off-diagonal move is $`00\leftrightarrow12`$. Any symbol $`1`$
or $`2`$ not belonging to an adjacent $`12`$ pair is fixed under all
moves: no move can act on it or produce a new $`12`$ pair across it.
These frozen symbols split the chain into intervals. Each remaining
interval is tiled by monomers $`0`$ and oriented dimers $`12`$. All such
tilings of the interval lie in one connected component: delete all
dimers and then insert the desired ones. Conversely no move leaves this
component.

On an interval of $`\ell`$ physical sites, a tiling is an independent
set $`\eta`$ on the path of $`m=\ell-1`$ possible dimer edges. Dimers
cannot occupy adjacent edges. The positive ground amplitude is
``` math
g(\eta)=\left(\frac ab\right)^{|\eta|}.
```
Conjugating the sector Hamiltonian by $`G=\operatorname{diag}g`$ gives
the positive generator $`\mathcal L=G^{-1}H G`$ with insertion rate
$`p=a^2`$ and deletion rate $`d=b^2`$. These are exactly rate-one
single-site heat-bath updates for the hard-core law
``` math
\pi(\eta)=Z^{-1}\lambda^{|\eta|},\qquad \lambda=a^2/b^2,
 \qquad p=\lambda/(1+\lambda),\quad d=1/(1+\lambda).
```
Insertion is allowed only when the neighbouring hard-core sites are
empty. In particular $`\mathcal L`$ is reversible in $`L^2(\pi)`$ and
has the same spectrum as the quantum sector Hamiltonian. The full chain
is a direct sum of tensor sums of these interval Hamiltonians and zero
one-dimensional sectors. It remains to bound every finite hard-core path
uniformly, including arbitrary fugacity.

## A two-site heat-bath comparison

<div id="lem:hardcore" class="lemma">

**Lemma 13** (Hard-core path bound). *For every path length $`m\ge1`$
and every fugacity $`\lambda>0`$, the rate-one single-site heat-bath
generator satisfies
``` math
\begin{equation}
\label{eq:hardcore-gap}
 \operatorname{gap}(\mathcal L)\ge(1+\lambda)^{-2}=d^2.
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Let $`E_i`$ denote conditional expectation resampling site
$`i`$, so $`\mathcal L=\sum_i(I-E_i)`$. Consider the block heat-bath
generator
``` math
\mathcal B=(I-E_{\{1\}})+\sum_{i=1}^{m-1}(I-E_{\{i,i+1\}})
                 +(I-E_{\{m\}}).
```
For $`m=1`$, retain both copies of the singleton. Every site belongs to
exactly two blocks.

First we show $`\operatorname{gap}(\mathcal B)\ge2d`$. Equip independent
sets with Hamming distance. This distance is geodesic for single-site
admissible changes: remove the occupations absent from the target and
then add its missing occupations. Consider two configurations differing
only at site $`j`$. Each of the two blocks containing $`j`$ has
identical outside conditions for the two configurations and can be
resampled identically, eliminating the discrepancy. At most two other
blocks can feel the changed boundary site. Each creates expected
additional Hamming distance at most $`p`$ under a suitable coupling.

Here is the complete nontrivial two-site coupling calculation. With
neither site blocked, the conditional weights of $`00,10,01`$ are
$`1,\lambda,\lambda`$. If the exterior discrepancy blocks the first
site, the other conditional weights are $`1,\lambda`$ on $`00,01`$.
Couple the common mass at $`00`$ and $`01`$ identically. The remaining
mass comes from $`10`$: send
``` math
\frac{\lambda}{(1+\lambda)(1+2\lambda)}\ \text{to }00,
 \qquad
 \frac{\lambda^2}{(1+\lambda)(1+2\lambda)}\ \text{to }01.
```
The transport distances are one and two, so the expected new distance is
$`\lambda/(1+\lambda)=p`$. If the other site is blocked by the unchanged
exterior condition, the calculation is a single Bernoulli update, again
costing at most $`p`$. Singleton blocks have the same bound.

Synchronising the rate-one clocks therefore gives infinitesimal
expected-distance drift at most $`-2+2p=-2d`$ for neighbouring
configurations. Concatenating the couplings along geodesics extends this
bound to arbitrary configurations, and iteration gives contraction by
$`e^{-2dt}`$ for the block semigroup in the Hamming Wasserstein
distance. Equivalently it contracts the Lipschitz seminorm of functions
by this factor. Every nonconstant eigenfunction has nonzero finite
Lipschitz seminorm; applying the contraction to an eigenfunction proves
that every nonzero eigenvalue of $`\mathcal B`$ is at least $`2d`$.

Next compare block and single-site Dirichlet forms. Conditional on the
exterior of a free pair, the positive generator
$`\mathcal L_i+\mathcal L_{i+1}`$ on $`00,10,01`$ is
``` math
\begin{pmatrix}2p&-p&-p\\-d&d&0\\-d&0&d\end{pmatrix},
```
with eigenvalues $`0,d,1+p`$. If an exterior neighbour blocks a site,
the conditional nonzero gap is one, or the space is one-dimensional.
Hence in every exterior condition
``` math
I-E_{\{i,i+1\}}\ \le\ d^{-1}(\mathcal L_i+\mathcal L_{i+1})
```
as an $`L^2(\pi)`$ quadratic-form inequality. The same bound applies to
singleton blocks. Summing, using the two-fold incidence of every site,
yields $`\mathcal B\le2d^{-1}\mathcal L`$. For every mean-zero function
$`f`$,
``` math
\langle f,\mathcal Lf\rangle_\pi
 \ge\frac d2\langle f,\mathcal Bf\rangle_\pi
 \ge d^2\left\lVert f\right\rVert_\pi^2.
```
This is <a href="#eq:hardcore-gap" data-reference-type="eqref"
data-reference="eq:hardcore-gap">[eq:hardcore-gap]</a>. ◻

</div>

<div class="proof">

*Proof of Theorem <a href="#thm:dimer" data-reference-type="ref"
data-reference="thm:dimer">12</a>.* Apply
Lemma <a href="#lem:hardcore" data-reference-type="ref"
data-reference="lem:hardcore">13</a> to every nontrivial interval
factor. The positive spectrum of a tensor sum is bounded below by the
minimum factor gap, and direct sums preserve the common lower bound.
Thus every positive eigenvalue of the full quantum chain is at least
$`d^2=b^4`$. At $`a=0`$ or $`b=0`$ all local projectors are diagonal and
the smallest positive energy is one. ◻

</div>

In particular $`a=b=1/\sqrt2`$ gives the first inequality in
<a href="#eq:mainbounds" data-reference-type="eqref"
data-reference="eq:mainbounds">[eq:mainbounds]</a>.
Section <a href="#sec:certificate" data-reference-type="ref"
data-reference="sec:certificate">7</a> supplies an independent, weaker
$`1/10`$ bound at this point using only a rational four-site
calculation. The new saturation proof gives a third, independent lower
bound. The heat-bath estimate is retained because it covers every
positive dimer weight, including unequal Schmidt probabilities.

# A rational four-site certificate and perturbation stability

<div id="thm:ball" class="theorem">

**Theorem 14** (Certified open region). *For every rank-one orthogonal
projector $`Q`$ with
$`\epsilon=\left\lVert Q-P_{\mathrm d}\right\rVert<1/45`$, one has
``` math
\begin{equation}
\label{eq:ball}
 \inf_{N\ge2}\gamma_N(Q)\ge\frac1{10}-\frac92\epsilon>0.
\end{equation}
```
In particular the closed radius-$`1/90`$ ball has gap at least $`1/20`$.
The full-Schmidt-rank vector
``` math
\begin{equation}
\label{eq:star}
 \psi_* =\frac{101\lvert 00\rangle-100\lvert 12\rangle+\lvert 21\rangle}{\sqrt{20202}}
\end{equation}
```
satisfies this bound, although its three-site gap is strictly below
$`1/2`$.*

</div>

This is a neighbourhood in the full complex rank-one projector space,
not a neighbourhood confined to a chosen real slice. The local projector
rank remains one; the vector’s Schmidt rank is a different notion.

## An open-chain finite-size inequality

<div id="lem:windows" class="lemma">

**Lemma 15** (Clipped-window criterion). *Fix $`m\ge3`$ and write
$`\delta_m=\min_{2\le k\le m}\gamma_k(P)`$. For $`N\ge m`$,
``` math
\begin{equation}
\label{eq:finite-size}
 \gamma_N(P)\ge\frac{(m-1)\delta_m-1}{m-2}
\end{equation}
```
whenever the right-hand side is positive.*

</div>

<div class="proof">

*Proof.* Write $`p_i=P_{i,i+1}`$ for $`1\le i\le N-1`$, extending
$`p_i=0`$ outside this range. For each integer starting point $`t`$
whose window meets the chain, set $`B_t=\sum_{i=t}^{t+m-2}p_i`$. This
includes clipped windows at both ends, so $`\sum_tB_t=(m-1)H_N`$. Every
nonzero window is a shorter open-chain Hamiltonian on between two and
$`m`$ sites; therefore
``` math
\mathcal A:=\sum_tB_t^2\ge(m-1)\delta_m H_N.
```
Expanding exactly gives
``` math
\mathcal A=(m-1)H_N+
 \sum_{\substack{i<j\\j-i\le m-2}}(m-1-j+i)\{p_i,p_j\}.
```
The coefficient of each adjacent anticommutator is $`m-2`$. Every other
anticommutator is nonnegative, since its projectors have disjoint
support. All its coefficients are at most $`m-2`$. Hence
$`\mathcal A\le(m-2)H_N^2+H_N`$. Combining these inequalities and using
the spectral theorem proves the result. The shorter chains $`N<m`$ are
handled by their individual gaps, not by assuming periodic boundaries. ◻

</div>

## The exact five-state calculation

For $`P=P_{\mathrm d}`$, the computational-basis components under
$`00\leftrightarrow12`$ on four sites have sizes and multiplicities
``` math
1^{(36)},\quad2^{(14)},\quad3^{(4)},\quad5^{(1)}.
```
The singleton blocks vanish; the two-state blocks have spectrum $`0,1`$;
the three-state blocks have spectrum $`0,1/2,3/2`$. The only remaining
block, in the order $`0000,0120,1200,1212,0012`$, is
``` math
\begin{equation}
\label{eq:K}
 K=\frac12\begin{pmatrix}
 3&-1&-1&0&-1\\-1&1&0&0&0\\-1&0&2&-1&0\\
 0&0&-1&2&-1\\-1&0&0&-1&2
 \end{pmatrix}.
\end{equation}
```
Let $`B=K^2-\tfrac25K`$ and let $`C`$ be the leading four-by-four
principal submatrix of $`B`$. The exact identity
``` math
\begin{equation}
\label{eq:LDL}
 C=LDL^T,\qquad
 L=\begin{pmatrix}
 1&0&0&0\\-1/3&1&0&0\\-7/16&-3&1&0\\
 5/24&5&-26/109&1
 \end{pmatrix},\qquad
 D=\operatorname{diag}\left(\frac{12}5,\frac1{30},\frac{109}{320},\frac{78}{545}\right)
\end{equation}
```
has strictly positive diagonal pivots. Since $`B`$ has zero row sums,
$`B=TCT^T`$ for $`T=[I_4;-\mathbf1^T]`$, and hence $`B\ge0`$. This
proves that the nonzero spectrum of $`K`$ is at least $`2/5`$. The
finite block classification is directly checkable by the listed move
rule; the verifier also constructs the full $`81\times81`$ matrix
independently by tensor products and checks all component boundaries.

We have consequently established the exact bounds
``` math
\begin{equation}
\label{eq:localbounds}
 \gamma_2=1,\qquad\gamma_3=1/2,\qquad\gamma_4\ge2/5.
\end{equation}
```
As a cross-check, the nontrivial block’s characteristic polynomial is
``` math
\det(xI-K)=\frac14x(x-1)(4x^3-16x^2+18x-5).
```
Its least positive root is approximately $`0.4149567567`$; this decimal
is not used in the proof.
Lemma <a href="#lem:windows" data-reference-type="ref"
data-reference="lem:windows">15</a>, with $`m=4`$, gives a uniform gap
at least $`1/10`$.

## Why degeneracy cannot invalidate the perturbation bound

A gap bound at a highly degenerate frustration-free point cannot in
general be perturbed merely by applying Weyl’s inequality: new small
positive eigenvalues might emerge from its kernel. Here local rank
maxima prevent that failure.

<div id="lem:rankmax" class="lemma">

**Lemma 16** (Short-chain rank maximality). *For every rank-one qutrit
projector $`Q`$,
``` math
\begin{equation}
\label{eq:ranks}
 \operatorname{rank}H_2(Q)\le1,\qquad \operatorname{rank}H_3(Q)\le6,\qquad \operatorname{rank}H_4(Q)\le26.
\end{equation}
```
The dimer projector attains all three maxima.*

</div>

<div class="proof">

*Proof.* The first two inequalities follow from the individual range
dimensions. On four sites each bond-projector range has dimension nine.
The first and third share the one-dimensional product range of
$`Q_{12}Q_{34}`$, so their total span has dimension at most
$`9+9+9-1=26`$. The dimer block decomposition gives kernel dimensions
$`8,21,55`$, attaining the maxima. ◻

</div>

For $`\epsilon=\left\lVert Q-P_{\mathrm d}\right\rVert`$,
``` math
\left\lVert H_k(Q)-H_k(P_{\mathrm d})\right\rVert\le(k-1)\epsilon.
```
Weyl’s inequality keeps all the existing positive eigenvalues positive
at the stated small radii. The universal upper bounds
<a href="#eq:ranks" data-reference-type="eqref"
data-reference="eq:ranks">[eq:ranks]</a> prohibit any additional
positive eigenvalues. Thus the kernel dimensions stay fixed for
$`k\le4`$, and
``` math
\begin{equation}
\label{eq:pertlocal}
 \gamma_2(Q)=1,\qquad
 \gamma_3(Q)\ge\frac12-2\epsilon,\qquad
 \gamma_4(Q)\ge\frac25-3\epsilon.
\end{equation}
```
For $`\epsilon<1/45`$, the last lower bound is the smallest.
Substitution into <a href="#eq:finite-size" data-reference-type="eqref"
data-reference="eq:finite-size">[eq:finite-size]</a> proves
<a href="#eq:ball" data-reference-type="eqref"
data-reference="eq:ball">[eq:ball]</a>; the shorter chains satisfy the
same global bound directly from
<a href="#eq:pertlocal" data-reference-type="eqref"
data-reference="eq:pertlocal">[eq:pertlocal]</a>.

For <a href="#eq:star" data-reference-type="eqref"
data-reference="eq:star">[eq:star]</a>, the unnormalised coefficient
matrix is
``` math
C_* =\begin{pmatrix}101&0&0\\0&0&-100\\0&1&0\end{pmatrix},
 \qquad \det C_*=10100\ne0.
```
The exact squared distance of rank-one projectors is
``` math
\left\lVert \lvert \psi_*\rangle\langle \psi_*\rvert-P_{\mathrm d}\right\rVert^2
 =1-|\langle\psi_{\mathrm d},\psi_*\rangle|^2
 =\frac1{13468}<\frac1{90^2}.
```
On the other hand,
``` math
\left\lVert \overline M_*M_*\right\rVert=\frac{10201}{20202}>\frac12,
 \qquad \gamma_3(\lvert \psi_*\rangle\langle \psi_*\rvert)=\frac{10001}{20202}<\frac12.
```
The three-site overlap test therefore gives no positive thermodynamic
lower bound, while our four-site certificate proves
$`\inf_N\gamma_N\ge1/20`$. This completes
Theorem <a href="#thm:ball" data-reference-type="ref"
data-reference="thm:ball">14</a>.

# Rank two: conserved order and exponential bottlenecks

<div id="thm:ranktwo-main" class="theorem">

**Theorem 17** (Exponential gap upper bound for opposing species). *For
$`0<a<1<b`$, let
``` math
\begin{equation}
\label{eq:ranktwo}
 \phi_1=\frac{\lvert 10\rangle-a\lvert 01\rangle}{\sqrt{1+a^2}},\qquad
 \phi_2=\frac{\lvert 20\rangle-b\lvert 02\rangle}{\sqrt{1+b^2}},\qquad
 P(a,b)=\sum_{s=1}^2\lvert \phi_s\rangle\langle \phi_s\rvert.
\end{equation}
```
The two vectors are orthonormal, so $`P(a,b)`$ is a rank-two projector.
Put $`A=-\log a`$ and $`B=\log b`$. For every
$`N\ge 2+\lceil B/A\rceil`$,
``` math
\begin{equation}
\label{eq:ranktwo-exp}
 \gamma_N(P(a,b))\le
 \frac{1+(b/a)^2}{1+a^2}
 \exp\left[-\frac{2AB}{A+B}(N-1)\right].
\end{equation}
```
Each chain with only one of the two rank-one constituents is uniformly
gapped, with gap infimum $`1-2q/(1+q^2)>0`$, where $`q=a`$ or $`q=b`$.
For the rational projectors defined by
``` math
\begin{equation}
\label{eq:rational-two}
 \phi_1=\frac{2\lvert 10\rangle-\lvert 01\rangle}{\sqrt5},\qquad
 \phi_2=\frac{\lvert 20\rangle-2\lvert 02\rangle}{\sqrt5},
\end{equation}
```
one has the sharper simple bound
``` math
\begin{equation}
\label{eq:rational-exp}
 \gamma_{2L+1}\le\frac85\,4^{-L}\qquad(L\ge1),
\end{equation}
```
whereas both constituent families have gap infimum $`1/5`$.*

</div>

## Exact one-vacancy reduction

In <a href="#eq:ranktwo" data-reference-type="eqref"
data-reference="eq:ranktwo">[eq:ranktwo]</a>, $`0`$ is a vacancy and
$`1,2`$ are particles which never exchange with one another. The order
of the nonzero symbols is conserved. Fix any word
$`\sigma=\sigma_1\cdots\sigma_m`$ over $`\{1,2\}`$ and take $`N=m+1`$.
Its one-vacancy sector has the orthonormal basis
``` math
e_j=\lvert \sigma_1\cdots\sigma_j\,0\,\sigma_{j+1}\cdots\sigma_m\rangle,
 \qquad0\le j\le m.
```
It is a reducing subspace, and the restricted Hamiltonian is $`D^*D`$,
with row $`i`$ of $`D`$ equal to
``` math
\begin{equation}
\label{eq:vacancyD}
 \frac{-q_{\sigma_i}e_{i-1}^T+e_i^T}{\sqrt{1+q_{\sigma_i}^2}},
 \qquad q_1=a,\quad q_2=b.
\end{equation}
```
The kernel in this sector is exactly one-dimensional, spanned by the
strictly positive vector
``` math
\begin{equation}
\label{eq:g}
 g_0=1,\qquad g_j=\prod_{i=1}^j q_{\sigma_i}.
\end{equation}
```
This identifies the ground-state component explicitly. A trial vector in
this sector orthogonal to $`g`$ is therefore orthogonal to the *entire*
ground space of the full chain, not just to a selected product ground
state.

## Opposing biases produce a two-well trial state

Assume $`0<a<1<b`$ and let $`A=-\log a`$, $`B=\log b`$. For
$`m=N-1\ge1+\lceil B/A\rceil`$ choose
``` math
k=\left\lceil\frac{mB}{A+B}\right\rceil,\qquad
 \sigma=1^k2^{m-k},
```
with $`1\le k\le m-1`$. Then $`g_j=a^j`$ up to $`j=k`$, and
$`g_j=a^k b^{j-k}`$ afterwards. In particular $`g_0=1`$,
$`a/b\le g_m\le1`$, and $`g_k=a^k`$ is exponentially small. The
inhomogeneous effective potential comes from a conserved particle order;
the local quantum Hamiltonian itself remains translation invariant.

Put
``` math
W_L=\sum_{j=0}^{k-1}g_j^2,\qquad W_R=\sum_{j=k}^{m}g_j^2,
 \qquad
 f_j=\begin{cases}W_Rg_j,&j<k,\\-W_Lg_j,&j\ge k.\end{cases}
```
Then $`\langle f,g\rangle=0`$. Every row of $`Df`$ vanishes except the
row crossing the cut. Exact cancellation gives
``` math
\begin{equation}
\label{eq:rayleigh}
 \frac{\langle f,H_N f\rangle}{\langle f,f\rangle}
 =\frac{a^{2k}}{1+a^2}\left(\frac1{W_L}+\frac1{W_R}\right).
\end{equation}
```
Since $`W_L\ge1`$, $`W_R\ge(a/b)^2`$, and
$`a^{2k}\le\exp[-2ABm/(A+B)]`$, the variational principle proves
<a href="#eq:ranktwo-exp" data-reference-type="eqref"
data-reference="eq:ranktwo-exp">[eq:ranktwo-exp]</a>. Exchanging the
species proves the same conclusion in the other opposing-bias quadrant.

For $`a=1/2`$, $`b=2`$, $`m=2L`$, take $`k=L`$. Both endpoints of $`g`$
equal one, so $`W_L,W_R\ge1`$.
Equation <a href="#eq:rayleigh" data-reference-type="eqref"
data-reference="eq:rayleigh">[eq:rayleigh]</a> gives
<a href="#eq:rational-exp" data-reference-type="eqref"
data-reference="eq:rational-exp">[eq:rational-exp]</a> directly. The
verifier checks the exact rational trial norm, orthogonality, energy,
and bound for $`1\le L\le50`$; the argument above proves the formula for
every $`L`$.

## Individually gapped constituents

For the Hamiltonian with only
$`\lvert \phi_1\rangle\langle \phi_1\rvert`$, every occurrence of symbol
$`2`$ is a fixed spectator. Fixing its positions splits the chain into
open qubit segments on $`\{0,1\}`$. Each segment is the $`u=v`$ case of
Theorem <a href="#thm:marker" data-reference-type="ref"
data-reference="thm:marker">6</a>, with gap
``` math
1-\frac{2a}{1+a^2}\cos(\pi/\ell)
```
for segment length $`\ell\ge2`$. The active sector with no spectators
attains the full-chain gap, and its infimum is $`1-2a/(1+a^2)`$. The
same reasoning applies to the second constituent. This proves the
remaining statements of
Theorem <a href="#thm:ranktwo-main" data-reference-type="ref"
data-reference="thm:ranktwo-main">17</a>. It also shows why adding
positive, individually gapped frustration-free summands is not enough:
their common ground space can have very small principal-angle
excitations.

## A complementary certified gapped region

For completeness the same rank-two family admits an elementary gapped
region. Write $`q_- =\min(a,b)`$, $`q_+=\max(a,b)`$. A direct
six-dimensional overlap calculation gives
``` math
\begin{equation}
\label{eq:two-overlap}
 c(a,b)=\left\lVert P(a,b)_{12}P(a,b)_{23}\right\rVert
       =\frac{q_+}{\sqrt{(1+q_-^2)(1+q_+^2)}}.
\end{equation}
```
Indeed the squared singular values of the overlap of its two range
isometries are
``` math
\frac{a^2}{(1+a^2)^2}\ (\text{twice}),\quad
 \frac{b^2}{(1+b^2)^2}\ (\text{twice}),\quad
 \frac{a^2}{(1+a^2)(1+b^2)},\quad
 \frac{b^2}{(1+a^2)(1+b^2)}.
```
The largest is the square of
<a href="#eq:two-overlap" data-reference-type="eqref"
data-reference="eq:two-overlap">[eq:two-overlap]</a>. Therefore
``` math
\begin{equation}
\label{eq:rank2region}
 4q_+^2<(1+q_-^2)(1+q_+^2)
 \quad\Longrightarrow\quad
 \inf_N\gamma_N(P(a,b))\ge1-2c(a,b)>0.
\end{equation}
```
The opposing-bias region is open within this two-parameter family;
stability under arbitrary rank-two perturbations is not proved. For
equal biases $`a=b=q`$, the lower bound of
Lemma <a href="#lem:overlap" data-reference-type="ref"
data-reference="lem:overlap">5</a> and the one-species upper bound
coincide, yielding the exact formula
``` math
\gamma_N(P(q,q))=1-\frac{2q}{1+q^2}\cos(\pi/N).
```
If either bias equals one, a one-species sector instead gives
$`\gamma_N\le1-\cos(\pi/N)`$, so those lines are gapless. We do *not*
classify the remaining same-direction parameter regions outside
<a href="#eq:rank2region" data-reference-type="eqref"
data-reference="eq:rank2region">[eq:rank2region]</a>.

<div id="rem:pvbs" class="remark">

*Remark 18* (Not the full PVBS model). The hopping-only projector
<a href="#eq:ranktwo" data-reference-type="eqref"
data-reference="eq:ranktwo">[eq:ranktwo]</a> lacks both same-species
exclusion penalties and unlike-species interchange terms present in the
two-species Product Vacua and Boundary States models. The PVBS
conclusion that adding a species does not introduce a new gapless phase
therefore does not apply to it. Our exponentially small gaps do not
contradict that result.

</div>

## Definition-level Motzkin and free-Motzkin comparisons

Write $`P_{\mathrm d}=\lvert 00-12\rangle\langle 00-12\rvert/2`$. In the
notation $`u=1,d=2`$, the original Motzkin bulk projector is exactly
``` math
P_{\mathrm{Motzkin}}=P_{\mathrm d}+P(1,1).
```
Bravyi et al. add endpoint penalties
$`\lvert 2\rangle\langle 2\rvert_1+\lvert 1\rangle\langle 1\rvert_N`$ to
select the unique Motzkin ground state . In Step 1 of their proof,
immediately before equation (6), they separate the hopping and
pair-creation terms and explicitly use the ferromagnetic hopping gap
$`1-\cos(\pi/N)`$. Thus neither the unbiased hopping interaction nor
that gap formula is claimed as new here.

Salberger, Padmanabhan and Korepin study the hopping-only free-Motzkin
model with periodic boundaries . In their explicit equations (2.2) and
(2.5), each local difference-vector operator is *twice* its normalised
rank-one projector. Their bond interaction is therefore $`2P(1,1)`$,
despite their use of the word projector. Their displayed relation
$`\widehat e_j^2=2\widehat e_j`$ confirms this normalisation. It must be
divided by two before comparison with our energy units, and a periodic
result is not silently substituted for an open-chain result.

For the area-weighted model, denote the area weight by $`s>0`$ to
distinguish it from the support angle $`t`$. The forbidden vectors used
by Andrei, Lemm and Movassagh are, up to signs,
``` math
\frac{s\lvert 01\rangle-\lvert 10\rangle}{\sqrt{1+s^2}},\qquad
 \frac{\lvert 02\rangle-s\lvert 20\rangle}{\sqrt{1+s^2}},\qquad
 \frac{\lvert 12\rangle-s\lvert 00\rangle}{\sqrt{1+s^2}}.
```
Thus the normalised bulk projector is
``` math
\begin{equation}
\label{eq:motzkindecomposition}
 P(s,s^{-1})+\frac{\lvert 12-s00\rangle\langle 12-s00\rvert}{1+s^2}.
\end{equation}
```
Their gap theorem for $`0<s<1`$ concerns the full Motzkin interaction,
with pinning boundaries in its main statement; its proof also controls
the open unpinned bulk chain . Our opposing-bias theorem instead
concerns the first summand alone, without either the pair-creation term
or pinning. Removing these terms enlarges the kernel, so the full-model
theorem does not imply a hopping-only gap.

In particular the hopping-only open chain has one ground vector in each
conserved particle-word sector. For a fixed word
$`\sigma_1\cdots\sigma_m`$, any placement of its ordered particles can
be reached by hopping through vacancies. The amplitudes proportional to
$`\prod_{j=1}^m q_{\sigma_j}^{-x_j}`$, where $`x_j`$ is the position of
particle $`j`$, satisfy every local zero-energy equation. Connectivity
makes the sector kernel one-dimensional. Hence its total ground-space
dimension is $`\sum_{m=0}^N2^m=2^{N+1}-1`$. Pair creation does not
preserve those sectors. This identifies why the omitted term changes the
mathematical problem.

<div class="center">

| Model | Local interaction and boundary | What the comparison establishes |
|:---|:---|:---|
| Original Motzkin | Rank-three bulk $`P_{\mathrm d}+P(1,1)`$; pinned ends | Direct antecedent of both components; the unbiased hopping reduction and its open gap are already used. |
| Free Motzkin | $`2P(1,1)`$ in the displayed convention; periodic | Direct hopping-only antecedent; divide energies by two and retain the boundary distinction. |
| Area-weighted Motzkin | Rank-three projector <a href="#eq:motzkindecomposition" data-reference-type="eqref"
data-reference="eq:motzkindecomposition">[eq:motzkindecomposition]</a>; pinning in main theorem | Full model gapped for $`0<s<1`$; does not classify its hopping-only component. |
| Present opposing-bias result | Rank-two $`P(a,b)`$; open, unpinned | Explicit exponential upper bound for $`0<a<1<b`$, including the hopping part at $`(s,s^{-1})`$. No matching asymptotic lower bound. |

</div>

The state $`(s00-12)/\sqrt{1+s^2}`$ in the omitted term belongs to the
dimer family of Section <a href="#sec:dimer" data-reference-type="ref"
data-reference="sec:dimer">6</a>. Its independent uniform gap does not
settle the gap of a sum with a different common kernel. The distinction
from the full PVBS model in
Remark <a href="#rem:pvbs" data-reference-type="ref"
data-reference="rem:pvbs">18</a> is similarly a distinction of local
terms and ground spaces, not a contradiction of that model’s theorem.

# Evidence, reproducibility and remaining questions

## Proof dependencies and checks

The principal dichotomy follows from the geometric overlap identity, the
simple extremal pair mode, the quantitative four-site inequality, and
the clipped-window summation. The marker sector provides an exact
matching upper bound on the gapless set. The fibre normal form is a
unitary-frame calculation; its stronger bound uses the three-dimensional
matrix <a href="#eq:Score" data-reference-type="eqref"
data-reference="eq:Score">[eq:Score]</a>. These are analytic proofs for
arbitrary length and exact parameters, rather than extrapolations from
diagonalisation.

The new exact verifier checks 43 groups of finite identities. It
supplies seven positive rational/Hermitian $`LDL^*`$ certificates on the
full four-site range: four general flat-Schmidt examples, including a
genuinely complex one, and three fibre points. It checks the
extremal-vector contractions, the displayed even core, its reducing
property, the cubic polynomial and leading minors, and the
clipped-window coefficient counts at lengths 2 through 30. The analytic
proof, not this finite list, establishes parameter-uniform validity. The
exact-input utility `classify_flat.py` implements the
support/intersection decision rule and rejects floating inputs.

A separate seeded numerical programme varies complex Schmidt-frame
unitaries, nontrivial support angles and common complex on-site
rotations. It also checks the marker surface, coincident supports, fibre
points and four-dimensional embeddings. Its 146 full-Hamiltonian tests
and 24 complex four-site relative-form tests are numerical diagnostics
only; the $`10^{-9}`$ zero threshold is not used in a theorem. The
supplied version-0.1 and referee programmes are retained with their
original provenance and rerun separately. The package distinguishes
historical supplied checks from newly executed checks. None of these
programmes is a proof assistant.

## What the revised release establishes

The principal result is a complete classification of a sharply specified
Schmidt class, including a necessary and sufficient condition, an exact
gap throughout its gapless set, and a positive analytic bound on its
complement. It also gives a complete normal form and gap classification
of the entire specified short-spectrum fibre. These are stronger than an
isolated locally-isospectral pair and resolve the interpolation left
open in version 0.1.

The arbitrary-complex rank-one neighbourhood in
Section <a href="#sec:certificate" data-reference-type="ref"
data-reference="sec:certificate">7</a> leaves the flat Schmidt class and
contains full-Schmidt-rank interactions. It remains a sufficient region,
not a classification of such vectors. The rank-two construction proves
only an exponential *upper* bound in its opposing-bias family, not the
optimal exponent or the asymptotic full-chain gap. Neither the remaining
same-direction rank-two parameters nor arbitrary rank-two perturbations
are classified. Periodic gaps, infinite-volume GNS gaps, and the
complete Bravyi–Gosset qutrit problem remain outside the claims.

The most consequential next checks are an unaffiliated adversarial
reading of Lemmas <a href="#lem:saturation" data-reference-type="ref"
data-reference="lem:saturation">7</a> and
<a href="#lem:quantitative" data-reference-type="ref"
data-reference="lem:quantitative">8</a>, verification of the fibre
normal form against alternative conventions, and specialist prior-art
review of the classification. A supplied version-1.0 review covered
these arguments; its independence is not authenticated by this
publication. No REF star rating follows from an internal proof audit or
from the number of computed examples.

#### Executable domain.

The classifier accepts parameter-free exact matrices only. It rejects
every free symbol before rank or null-space computation. For example,
$`M(x)=\left(\begin{smallmatrix}(1-x^2)/(1+x^2)&0&2x/(1+x^2)\\0&-1&0\\0&0&0\end{smallmatrix}\right)/\sqrt2`$
must first be specialised: $`x=0`$ is gapless, whereas $`x=1`$ is
uniformly gapped. Generic symbolic rank cannot certify the exceptional
strata. This restriction repairs the implementation, not the analytic
theorem.

#### Declarations and availability.

The source, exact-input classifier and finite checks accompany this
manuscript. The work is theoretical and uses no human-participant or
personal data. The scholarly creator is Anonymous. AI systems
contributed mathematical development, exposition and revision; complete
originating model/run details are not available. The publication agent
performed the documented revision and producer replay. The maintainer
publishes the materials but is not thereby credited with a research
contribution. No specific research funding or conflict declaration was
supplied; neither is inferred from that absence.

# An explicit endpoint-safe Gram basis

Use the five core columns in
Lemma <a href="#lem:gram" data-reference-type="ref"
data-reference="lem:gram">10</a>. Choose orthonormal bases $`q_1,q_2`$
of $`r^\perp`$ and $`p_1,p_2`$ of $`\ell^\perp`$. In the ordered direct
sum of first, middle and last nine-dimensional spaces, the four paired
blocks have columns
``` math
(r\otimes q_j,0,0),\ (0,\ell\otimes q_j,0);\qquad
(0,0,p_j\otimes\ell),\ (0,p_j\otimes r,0),\quad j=1,2.
```
The four unit scalar blocks are $`(0,p_i\otimes q_j,0)`$. For the ten
half-unit scalar blocks, use any orthonormal bases of
``` math
(r^\perp\otimes\mathbb C^3)\cap\psi^\perp
 \quad\hbox{in the first space},\qquad
 (\mathbb C^3\otimes\ell^\perp)\cap\psi^\perp
 \quad\hbox{in the last space}.
```
Each space has dimension five because the corresponding component of
$`\psi`$ has norm $`\beta=\sqrt{1-c^2/2}\ge1/\sqrt2`$. These
prescriptions are an explicit symbolic transformation: project the
standard tensor basis onto each displayed subspace, discard zero
residuals, and apply exact Gram–Schmidt in lexicographic order. Within
the core use the even columns displayed in the proof and the odd columns
$`(a-d)/\sqrt2,(a'-d')/\sqrt2`$. The odd negative and positive
eigenvectors have coordinates $`(\alpha,\beta)`$ and $`(-\beta,\alpha)`$
respectively. All denominators used for the core are nonzero at both
endpoints. The tensor orthogonality identities and the three
off-diagonal Gram blocks give the stated block matrix by direct
multiplication. This proves the all-parameter decomposition; the
accompanying finite checks remain corroboration rather than a substitute
for this argument.

<div class="thebibliography">

99 Bravyi, S., & Gosset, D. (2015). Gapped and gapless phases of
frustration-free spin-$`1/2`$ chains. *Journal of Mathematical Physics,
56*, 061902. <https://arxiv.org/abs/1503.04035>. Lemm, M. (2019).
Gaplessness is not generic for translation-invariant spin chains.
*Physical Review B, 100*, 035113.
<https://doi.org/10.1103/PhysRevB.100.035113>. Version consulted:
<https://arxiv.org/html/1903.00108v2>. Hunter-Jones, N., & Lemm, M.
(2025). *Two classes of quantum spin systems that are gapped on any
bounded-degree graph* \[Preprint\]. <https://arxiv.org/abs/2509.22438>.
Rai, K. S., Kull, I., Emonts, P., Tura, J., Schuch, N., & Baccari, F.
(2026). A hierarchy of spectral gap certificates for frustration-free
spin systems. *Quantum, 10*, 2065.
<https://doi.org/10.22331/q-2026-04-13-2065>. Movassagh, R., Farhi, E.,
Goldstone, J., Nagaj, D., Osborne, T. J., & Shor, P. W. (2010).
Unfrustrated qudit chains and their ground states. *Physical Review A,
82*, 012318. <https://arxiv.org/abs/1001.1006>. Bravyi, S., Caha, L.,
Movassagh, R., Nagaj, D., & Shor, P. W. (2012). Criticality without
frustration for quantum spin-1 chains. *Physical Review Letters, 109*,
207202. <https://doi.org/10.1103/PhysRevLett.109.207202>.
<https://arxiv.org/abs/1203.5801>. Salberger, O., Padmanabhan, P., &
Korepin, V. (2018). *Non-interacting Motzkin chain—Periodic boundary
conditions* \[Preprint\]. <https://arxiv.org/abs/1809.00709>. Andrei,
R., Lemm, M., & Movassagh, R. (2026). *The spin-one Motzkin chain is
gapped for any area weight $`t<1`$* \[Preprint, version 2, 23 May 2026;
originally submitted 2022\]. <https://arxiv.org/abs/2204.04517>. Bishop,
M. R. (2017). *Spectral gaps for the two-species Product Vacua and
Boundary States models on the $`d`$-dimensional lattice* \[Preprint
version consulted\]. <https://arxiv.org/abs/1705.04755>.

</div>
