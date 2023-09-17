def add_dots(added_string):
    l = list(str(added_string))
    jl = '.'.join(l)
    print(jl)
add_dots('hello')

def remove_dots(rm_string):
    x = rm_string.replace('.', '')
    print(x)
remove_dots('h.e.l.l.o')