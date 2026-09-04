class Vector:
	def __init__(self, components):
		self.components = components
		self.dim = len(self.components)

	def dot(self, onther):
		return sum(a *b for a, b in zip(self.components, onther.components))
	def magnitude(self):
		return sum(x * x for x in self.components) ** 0.5

	def normalize(self):
		msg = self.magnitude()
		return Vector([x / msg for x in self.components])

	def cosine_similarity(self, other):
		return self.dot(other) / (self.magnitude() * other.magnitude())

a = Vector([1, 2, 3])
b = Vector([4, 5, 6])
print("dot =", a.dot(b))
print("|a| =", round(a.magnitude(), 4))
print("cos =",round(a.cosine_similarity(b),4)) 
print(a.dot(a), a.magnitude()**2)
print(Vector([1,1]).dot(Vector([1,-1])))
print(a.normalize().magnitude())
