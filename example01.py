example_string = "batata"
example_list = ['a','b','c','d','e']
example_tuple = ['where', 'when', 'why']
example_group = set(example_list)
example_integer = 1
example_rational = 3.3
example_complex = 1e10
example_boolean = True


example_dictionary = {
    "string":example_string,
    "list":example_list,
    "group": example_group,
    "integer": example_integer,
    "rational": example_rational,
    "complex": example_complex,
    "boolean": example_boolean
}
for k in example_dictionary.keys():
    print(k, ":", example_dictionary[k], "-Tipo->", type(example_dictionary[k]))

print("Type of Dictionary: ", type(example_dictionary))

a = 0
b = 1
if a > b:
   print("A maior que B")
elif a == b:
   print("A igual à B")
else:
    print("A menor que B")

for i in range(0,5):
     print(i)

i=0
while i <5:
    i+=1
    print(i)

def soma(a,b):
   return a+b  
print(soma(1,1))

class cachorro:
    def __init__(self, nome, raca, tutor):
        self.nome = nome
        self.raca = raca
        self.tutor = tutor

    def latir(self):
        return "au! au!!"