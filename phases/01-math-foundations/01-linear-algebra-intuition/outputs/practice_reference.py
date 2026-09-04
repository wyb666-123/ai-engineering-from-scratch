# practice_linalg.py — 第 1 课练习参考答案（先自己敲，再对答案）
import math
import random
import numpy as np

# ---------- 练习 1: angle_between ----------
class Vector:
    def __init__(self, components):
        self.components = list(components)
        self.dim = len(self.components)
    def dot(self, other):
        return sum(a * b for a, b in zip(self.components, other.components))
    def magnitude(self):
        return sum(x ** 2 for x in self.components) ** 0.5
    def cosine_similarity(self, other):
        return self.dot(other) / (self.magnitude() * other.magnitude())
    def __sub__(self, other):                  # 练习4 需要：撕影子要减法
        return Vector([a - b for a, b in zip(self.components, other.components)])
    def angle_between(self, other):
        c = self.cosine_similarity(other)
        c = max(-1.0, min(1.0, c))          # 防浮点误差越界
        return math.degrees(math.acos(c))
    def __repr__(self):
        return f"Vector({self.components})"

print("角度 [1,0]→[0,1] =", round(Vector([1,0]).angle_between(Vector([0,1])), 2))
print("角度 [1,0]→[1,1] =", round(Vector([1,0]).angle_between(Vector([1,1])), 2))
print("角度 [1,0]→[3,0] =", round(Vector([1,0]).angle_between(Vector([3,0])), 2))

# ---------- 练习 2: 缩放矩阵 ----------
S = [[2, 0], [0, 3]]
v = [1, 1]
out = [S[0][0]*v[0] + S[0][1]*v[1], S[1][0]*v[0] + S[1][1]*v[1]]
print("练习2 [[2,0],[0,3]] @ [1,1] =", out)

# ---------- 练习 3: 5 个 50 维词向量找最像的俩 ----------
random.seed(42)
words = ["king", "queen", "apple", "banana", "dog"]
vecs = {w: [random.gauss(0, 1) for _ in range(50)] for w in words}
def cos(a, b):
    dot = sum(x*y for x, y in zip(a, b))
    return dot / (sum(x*x for x in a) ** 0.5 * sum(y*y for y in b) ** 0.5)
best = None
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        c = cos(vecs[words[i]], vecs[words[j]])
        if best is None or c > best[2]:
            best = (words[i], words[j], c)
print("练习3 最相似一对:", best[0], "vs", best[1], "cos =", round(best[2], 4))

# ---------- 练习 4: 验证 Gram-Schmidt 正交性 ----------
def project(a, b):
    s = a.dot(b) / b.dot(b)
    return Vector([s * x for x in b.components])
def normalize(v):
    m = v.magnitude()
    return Vector([x / m for x in v.components])
def gram_schmidt(vs):
    basis = []
    for v in vs:
        w = v
        for u in basis:
            w = w - project(w, u)
        if w.magnitude() < 1e-10:
            continue
        basis.append(normalize(w))
    return basis

basis = gram_schmidt([Vector([1,0,0]), Vector([1,1,0]), Vector([1,1,1])])
print("练习4 两两点积:",
      [round(basis[i].dot(basis[j]), 10) for i in range(3) for j in range(i+1, 3)])
print("练习4 模长:", [round(u.magnitude(), 10) for u in basis])

# ---------- 练习 5: 秩 2 的 3x3 矩阵 ----------
A = np.array([[1,0,1],[0,1,1],[0,0,0]])   # c3 = c1 + c2
print("练习5 rank =", np.linalg.matrix_rank(A))

# ---------- 练习 6: 投影 [1,2,3] 到 [1,1,1] ----------
a = np.array([1., 2., 3.]); b = np.array([1., 1., 1.])
proj = (a.dot(b) / b.dot(b)) * b
resid = a - proj
print("练习6 proj =", proj, " 残差 =", resid, " 残差·b =", resid.dot(b))

# ---------- NumPy 对照 + QR ----------
a1 = np.array([1., 2., 3.]); b1 = np.array([4., 5., 6.])
print("numpy: dot =", np.dot(a1, b1),
      "norm =", round(np.linalg.norm(a1), 4),
      "cos =", round(np.dot(a1, b1) / (np.linalg.norm(a1) * np.linalg.norm(b1)), 4))
rng = np.random.default_rng(0)
Q, R = np.linalg.qr(rng.standard_normal((3, 3)))
print("QR: Q@Q.T≈I =", np.allclose(Q @ Q.T, np.eye(3)),
      " R上三角 =", np.allclose(R, np.triu(R)))
