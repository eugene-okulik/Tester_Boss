my_dict = {'tuple': (1, 2, 3, 4, 5),
           'list': [False, True, 3.14, "John", 1],
           'dict': {"js": "frontend",
                    "django": "backend",
                    "c#": "unity",
                    "c++": "gamedev",
                    "html/css": "websites"},
           'set': {256, "Windows", True, 3.14, 666}
           }

print(my_dict['tuple'][-1])
my_dict['list'].pop(1)
my_dict['list'].append(256)

my_dict['dict'][("i am a tuple",)] = "это не кортеж"
my_dict['dict'].pop("c++")

my_dict['set'].add("байт")
my_dict['set'].pop()
print(my_dict)
