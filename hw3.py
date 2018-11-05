p = 499
q = 547
a = -57
b = 52
my_x0 = 159201
class Blum:
	def __init__(self,m,x):
		self.X = x
		self.M = m
	def getBit(self):
		bit = self.X % 2
		self.X = pow(self.X,2,self.M)
		return bit

def encrypt(message, x0):
	blum = Blum(p* q, x0)
	new = [blum.getBit() ^ bit for bit in message]
	return new, blum.X

def decrypt(encrypted, x_l):
	r_p = pow(x_l, pow((p+1)/4,len(encrypted),p-1) ,p)
	r_q = pow(x_l, pow((q+1)/4,len(encrypted),q-1) ,q)
	x_0 = (r_q * p * a + r_p *q * b) % (p*q)
	decrypted,new_x = encrypt(encrypted,x_0)
	return decrypted


input = [1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,1,0,0]
print(input)
encrypted, x_l = encrypt(input, my_x0)
print(encrypted)
decrypted = decrypt(encrypted, x_l)
print(decrypted)