import os
from ordered_set import OrderedSet as oset
from nltk.tokenize import word_tokenize


class Template():


	def __init__(self):

		self.pairs = []

		pass

	def longest_common_subsequence(self, text1, text2):

		table = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
		common_text_ix = []

		for i in range(len(text1) -1, -1, -1):
			for j in range(len(text2) -1 , -1, -1):
				if text1[i] == text2[j]:
					table[i][j] = 1 + table[i+1][j+1]
					common_text_ix.append(i)
				else:
					table[i][j] = max(table[i][j + 1], table[i + 1][j])

		common_text_ix = list(oset(common_text_ix[::-1]))

		print(common_text_ix[::-1])
		print(' '.join(list(map(lambda x: text1[x], common_text_ix))))

		return table[0][0]


	def get_template(self):

		for (file0, file1) in self.pairs:

			print(self.longest_common_subsequence(file0,file1))


if __name__ == '__main__':

	input_files = os.listdir('../data')
	data_dir = '../data'


	if len(input_files) != 0:
		template = Template()
	else:
		raise IOError('Files not found in /data. Please add files in /data')

	#print(input_files[0::2])
	#print(zip(input_files[0::2], input_files[1::2]))

	## Make even to read pairwise. 
	## Duplicates don't affect the common template
	if len(input_files) % 2 != 0: 
		input_files.append(input_files[-1]) 

	for (file0, file1) in zip(input_files[0::2], input_files[1::2]):

		#print(file0, file1)

		with open(f'{os.path.join(data_dir, file0)}', 'r+', encoding="utf-8") as f:
		#with open(f'{os.path.join(data_dir, file0)}') as f:

			text0 = f.read()
			#print(text0)
			#print(word_tokenize(text0))
			text0 = word_tokenize(text0)

		with open(f'{os.path.join(data_dir, file1)}', 'r+', encoding="utf-8") as f:
		#with open(f'{os.path.join(data_dir, file1)}') as f:

			text1 = f.read()
			#print(text1)
			#print(word_tokenize(text1))
			text1 = word_tokenize(text1)


		template.pairs.append((text0, text1))
		template.get_template()


