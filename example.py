# def multiply(a,b):
# 	print a*b

# multiply(5,6)


urls = ["example.com", "sisiwei.com"]
another_list = ["apple", "grape"]

def create_links(list_of_links):
	r = get_remainder(11, 2)

	for url in list_of_links:
		print "<a href='" + url + "'></a>"

create_links(another_list)

def get_remainder(num1, num2):
	return num1 % num2