from copy import deepcopy #to copy an object with its attributs

class Matrix(object):
	def __init__(self, *args):
	
		if len(args) == 1 and type(args[0][0]) == list:  
			args = args[0] 
		self.rows = args
		self.shape = (len(args),len(args[0]))
		self.iterator_coordinate_x=0
		self.iterator_coordinate_y=0
		pass

	def product(self, matrix):
		matrix_res=[[0]*self.shape[1]]*matrix.shape[0]
		m_res = Matrix(matrix_res)
		if self.shape[0]!=matrix.shape[1]:
			print('error')
		else:

			for x in range(0,self.shape[1]):
				for y in range(0,matrix.shape[0]):
					for z in range(0,self.shape[1]):
						print(self.rows[x][z]*matrix.rows[z][y])
						print('--')
						print(x)
						print(y)
						print('--')
						m_res.rows[x][y]+=self.rows[x][z]*matrix.rows[z][y]


		return m_res

	def indices_generator(self):
	
		list_indices = []
		for i in range(self.shape[0]):
			for j in range(self.shape[1]):
				list_indices.append((i,j))
		return list_indices
		pass

	def apply(self, fun, **kwargs):
	
		for elem in self.indices_generator():
			self.rows[elem[0]][elem[1]]=fun(self.rows[elem[0]][elem[1]],**kwargs)
		pass

	def __add__(self, m):
		
		if type(self)==type(m):	
			result = deepcopy(self)
			for tuples in self.indices_generator() :
				result.rows[tuples[0]][tuples[1]]+=m.rows[tuples[0]][tuples[1]]
			return result
		else: #if one matrix + one scalar
			try:
				result = deepcopy(self)
				def functionadd(x,a=m):
					return x+a
				result.apply(functionadd,a=m)
			except TypeError:
				print("Incompatible type for addition")
			else:
				return result
			pass

	@property
	def transpose(self):
		new_rows = [] 
		for i in range(self.shape[1]): 
			new_rows.append([0]*self.shape[0])
		for tuples in self.indices_generator() :
			new_rows[tuples[1]][tuples[0]]=self.rows[tuples[0]][tuples[1]]
		return Matrix(new_rows) 
		pass

	def __str__(self):
		i=0 
		m_string ='|'
		for tuples in self.indices_generator() :
			if tuples[0]==i:
				m_string+=str(self.rows[tuples[0]][tuples[1]])+" "
			else:
				m_string=m_string[:-1]
				m_string+="|\n|"+str(self.rows[tuples[0]][tuples[1]])+" "
				i+=1
		m_string=m_string[:-1]
		m_string+='|\n'
		return m_string
		pass
	def __iter__(self):
		return self
	def next(self):
		if self.iterator_coordinate_x<self.shape[0]:
			self.iterator_coordinate_x+=1
			return self.rows[self.iterator_coordinate_x-1]

		else:
			iterator_coordinate_x=0
			raise StopIteration

	def __next2__(self):
		if self.iterator_coordinate_y<self.shape[1]:
			if self.iterator_coordinate_x<self.shape[0]:
				return self.rows[self.iterator_coordinate_x][self.iterator_coordinate_y]
				self.iterator_coordinate_y=iterator_coordinate_y+1
			else:
				raise StopIteration
		else:
			self.iterator_coordinate_y=0;
			self.iterator_coordinate_x=self.iterator_coordinate_x+1
			return self.rows[self.iterator_coordinate_x][self.iterator_coordinate_y]




if __name__ == '__main__':
	m1 = Matrix([1,1,1],[2,2,2],[3,3,3])
	m2 = Matrix([[1,2,3],[1,2,0],[0,1,3]])
	m4 = Matrix([2, 2, 2])
	m5 = Matrix([[1],[1],[1]])
	print (m1)
	print (m2)
	print (m4)
	print (m5)
	m3 = m1+m2
	print (m3)
	print (m2)
	print (m1+0.1)
	print (m1.transpose)
	print (m4.transpose)
	print (m5.transpose)

	m6 = Matrix(['A','B'],['Hello','World'])
	m7 = Matrix(['Selam','canim'],['C','D'])
	print (m6)
	print (m6+" "+m7)
	print (m6.transpose)
	m8=Matrix([1,3,1],[3,1,3])
	print(m8.shape[1])
	print(m8)
	m9=m8.product(m1)
	print(m9)
	m8=Matrix([1,2,0],[2,1,3],[1,1,2])
	m9=m8.product(m1)
	print(m8)
	print(m1)
	print(m9)
	for v in m1:
  		print (v)

   """
Output of these lines:
m1 = Matrix([1,1,1],[2,2,2],[3,3,3])
m2 = Matrix([[1,2,3],[1,2,0],[0,1,3]])
print m1
print m2
m3= m1+m2
print m3
print m1+3
print m1.transpose
Should be following:
|1 1 1|
|2 2 2|
|3 3 3|

|1 2 3|
|1 2 0|
|0 1 3|

|2 3 4|
|3 4 2|
|3 4 6|

|4 4 4|
|5 5 5|
|6 6 6|

|1 2 3|
|1 2 3|
|1 2 3|
"""
