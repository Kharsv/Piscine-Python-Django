# -*- coding: utf-8 -*-

from local_lib import path

def my_program():
	directory = path.Path('new_dir')
	directory.mkdir()
	file = path.Path('new_dir/new_file')
	file.touch()
	file.write_text("You are beautiful!")
	text = file.read_text()
	print(text)

if __name__ == '__main__':
	my_program()