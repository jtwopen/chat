def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
        return lines

def convert(lines):
	a = []
	count_allen = 0
	count_viki = 0
	sticker_allen = 0
	sticker_viki = 0
	image_allen = 0
	image_viki = 0
	for line in lines:
		a = line.split(' ')
		time = a[0]
		name = a[1]
		if name == 'Allen':
			if a[2] == '貼圖':
				sticker_allen += 1
			elif a[2] == '圖片':
				image_allen += 1
			else:
				for s in a[2:]:
					count_allen += len(s)
		elif name == 'Viki':
			if a[2] == '貼圖':
				sticker_viki += 1
			elif a[2] == '圖片':
				image_viki += 1
			else:
				for s in a[2:]:
					count_viki += len(s)
	print('Allen傳了', image_allen, '張圖片')
	print('Viki傳了', image_viki, '張圖片')
	print('Allen傳了', sticker_allen, '張貼圖')
	print('Viki傳了', sticker_viki, '張貼圖')			
	print('Allen說了', count_allen, '個字')
	print('Viki說了', count_viki, '個字')


def main():
    lines = read_file('line_viki.txt')
    convert(lines)

main()