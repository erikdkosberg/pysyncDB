import dis

def x():
	print("hi")
def main():
	n = lambda : print('\n')
	dis.dis(x)
	n()
	print(dis.code_info(n))
	n()
	B = dis.Bytecode(x)
	print(B.codeobj)
	print(B.first_line)
	print(B.current_offset)
	print(B.dis())
	
main()


