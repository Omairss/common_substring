import os
import pdb
import argparse
import collections
from ordered_set import OrderedSet as oset
from nltk.tokenize import word_tokenize


class Template():


	def __init__(self):

		self.pairs = collections.deque()
		self.pair_names = collections.deque()

		pass

	def longest_common_subsequence(self, text1, text2):

		'''This method uses the dynamic programming based
		longest common subsequence algorithm to detect common tokens. 
		Time complexity is O(len(tokens_in_text1) * len(tokens_in_text2)'''

		if len(text1) > len(text2): # Make the smaller sentnce text1
			text1, text2 = text2, text1

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

		#print(common_text_ix[::-1])
		common_tokens = ' '.join(list(map(lambda x: text1[x], common_text_ix)))

		return table[0][0], common_tokens


	def get_template(self):

		'''This method will generate common tokens for every pair. 
		The result is fed back into the queue and aggregated with another result
		and so on and so forth. This happens in log(n) time
		where n = number of files.''' 

		while len(self.pairs) > 1:

			file0 = self.pairs.popleft()
			file1 = self.pairs.popleft()
			name0 = self.pair_names.popleft()
			name1 = self.pair_names.popleft()

			_len, common_token = self.longest_common_subsequence(file0, file1)
			print(f'\n{name0, name1} \n {word_tokenize(common_token)}')
			text0 = word_tokenize(common_token)
			self.pairs.append(text0)
			self.pair_names.append(' '.join([name0, name1]))

		return self.pairs, self.pair_names


if __name__ == '__main__':


	parser = argparse.ArgumentParser(description='Get common template across files')
	parser.add_argument('input_files', metavar='<filenames>', type=str, nargs='+',
                    help='a file in /data as the input')

	args = parser.parse_args()

	input_files = args.input_files
	data_dir = '../data'

	if len(input_files) != 0:
		template = Template()
	else:
		raise IOError('Files not found in /data. Please add files in /data')

	## Make even to read pairwise. 
	## Duplicates don't affect the common template
	if len(input_files) % 2 != 0: 
		input_files.append(input_files[-1]) 

	for file0 in input_files:

		with open(f'{os.path.join(data_dir, file0)}', 'r+', encoding="utf-8") as f:

			text0 = f.read()
			text0 = word_tokenize(text0)  ## Crucial tradeoff for performance

		template.pairs.append(text0)
		template.pair_names.append(file0)
	
	final_template, template_names = template.get_template()
	final_template = ' '.join(final_template.popleft())
	
	print(f'\n\nFinal Result:\n {final_template}')

