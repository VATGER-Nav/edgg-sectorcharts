import os


def main():
	for file in os.listdir():
		if 'svg' in file:
			print(file)
			os.system('cmd /c "inkscape --export-type="png" {} -D -d 300 -b WHITE"'.format(file))


if __name__ == '__main__':
	main()
