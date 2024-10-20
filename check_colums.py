chars=['1', '2', '3', '4', '#', ':']

print("name: check\ninit: e0\naccept: Y")

for input in chars:
    print(f"e0, {input}")
    print(f"e1,{input}, < ")

print(f"e1, _")
print(f"q01, 1, >")

for input in chars:
    if(input != ':'):
        print(f"q01, {input}")
        print(f"q01, {input}, >\n")
    else:
        print(f"q01, {input}")
        print(f"s.0.0.0.0.i0.sk0, {input}, >\n")


    for idx in range(0, 4):
        for a1 in range(0, 2):
            for a2 in range(0, 2):
                for a3 in range(0, 2):
                    for a4 in range(0, 2):
                        for input in range(1, 5):

                            print(f"s.{a1}.{a2}.{a3}.{a4}.i{idx}.sk0, {input}")

                            if(input == 1):
                                if (a1 == 0):
                                    print(f"s.{1}.{a2}.{a3}.{a4}.i{idx+1}.sk8, {input}, >\n")
                                if(a1 == 1):
                                    print(f"N, {input}, -\n")
                            
                            if(input == 2):
                                if (a2 == 0):
                                    print(f"s.{a1}.{1}.{a3}.{a4}.i{idx+1}.sk8, {input}, >\n")
                                if(a2 == 1):
                                    print(f"N, {input}, -\n")

                            if(input == 3):
                                if (a3 == 0):
                                    print(f"s.{a1}.{a2}.{1}.{a4}.i{idx+1}.sk8, {input}, >\n")
                                if(a3 == 1):
                                    print(f"N, {input}, -\n")

                            if(input == 4):
                                if (a4 == 0):
                                    print(f"s.{a1}.{a2}.{a3}.{1}.i{idx+1}.sk8, {input}, >\n")
                                if(a4 == 1):
                                    print(f"N, {input}, -\n")
for input in chars:
    print(f"s.1.1.1.1.i4.sk8, {input}\ngoback, {input}, <")

for input in chars:
    print(f"goback, {input}\ngoback, {input}, <")

print(f"goback, _\ndavai, _, >")

for skips in range(1, 4):
    print(f"davai, {skips}")
    print(f"s.0.0.0.0.i0.sk{skips+7}, {skips+1}, >")

print(f"davai, 4")
print(f"Y, {skips+1}, >")


for input in chars:
    if(input != ':'):
        print(f"q011, {input}")
        print(f"q011, {input}, >\n")
    else:
        print(f"q011, {input}")
        print(f"zz, {input}, >\n")





for idx in range(0, 4):
    for sk in range(1, 12):
        for a1 in range(0, 2):
            for a2 in range(0, 2):
                for a3 in range(0, 2):
                    for a4 in range(0, 2):
                        for input in chars:
                            print(f"s.{a1}.{a2}.{a3}.{a4}.i{idx}.sk{sk}, {input}")
                            print(f"s.{a1}.{a2}.{a3}.{a4}.i{idx}.sk{sk-1}, {input}, >\n")
