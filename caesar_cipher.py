import sys
import string

alphabet = list(string.ascii_lowercase)

def caesar(string, rotations, back):
	decrypted = ''	
	for i in range(len(string)):
		if string[i].lower() not in alphabet:
			decrypted += string[i]
			continue
		if back:
			decrypted += alphabet[(alphabet.index(string[i].lower()) - rotations) % 26]
		else:
			decrypted += alphabet[(alphabet.index(string[i].lower()) + rotations) % 26]
	print(f'{string} ---> {decrypted}')

def print_usage():
    print('Usage: python3 caesar_cipher.py [message] [rotations] [back=False]')
		

if __name__ == "__main__":
	try:
		encrypter_message = sys.argv[1]
		rotations = int(sys.argv[2])
	except IndexError:
		print_usage()
		exit(0)
	try:
		back = eval(sys.argv[3])
		caesar(encrypter_message, rotations, back)
	except NameError:
		print('3rd parameter must be [True/False]')
		print_usage()
		exit(0)
	except IndexError:
		print('"back" parameter set to [False] by default')
		caesar(encrypter_message, rotations, False)
