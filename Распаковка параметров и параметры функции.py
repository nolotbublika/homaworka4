def print_params(a=1,b='строка',c=True):
    print("qw",a)
    print("er",b)
    print("ty",c)
print_params()
values_list = [2, 'строкач', False]
values_dict ={'a':5,'b':'отступ','c':True}
print(print_params(*values_list))
print(print_params(**values_dict))
values_list_2 = [3,'липа']
print(print_params(*values_list_2, 42))