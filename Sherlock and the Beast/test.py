
class Test:

	__a = False
	__inputs = ''
	__correct_outputs = ''
	function = ''

	def __init__(function_to_test,
				 input_testcases='sample_testcase.txt',
				 output_answers='sample_testcases_answers.txt',
				 all_results=False):
		self.__a = all_results
		self.__inputs = input_testcases
		self.__correct_outputs = output_answers

	def __write_error_log():
		pass

	def run_test():
		pass

