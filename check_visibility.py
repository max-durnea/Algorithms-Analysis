symbols=['1','2','3','4','#',':','_']
heights=[1,2,3,4]
print("name: check_vis\ninit: q0\naccept: Y")

for i in range(1,5):
    print(f"q0,{i}")
    print(f"v{i}.s6.h0.c0.i0,_,>")
for indx in range(0,5):
    for c in range(0,5):
        for h in range(0,5):
            for i in range(1,5):
                for j in range(1,9):
                    for symbol in symbols:
                        print(f"v{i}.s{j}.h{h}.c{c}.i{indx},{symbol}")
                        if(indx==4):
                            if(i!=c):
                                print(f"N,{symbol},-")
                            else:
                                print(f"GOBACK,{symbol},<")
                        else:
                            print(f"v{i}.s{j-1}.h{h}.c{c}.i{indx},{symbol},>\n")
                        
for symbol in symbols:
    print(f"GOBACK,{symbol}")
    if(symbol=='_'):
        print(f"q0,_,>")
    else:
        print(f"GOBACK,{symbol},<")


for indx in range(0,5):
    for input in range(1,5):
        for i in range(1,5):
            for j in range(0,5):
                for n in range(0,5):
                    print(f"v{i}.s0.h{j}.c{n}.i{indx},{input}")
                    if(input>j and (n+1>i)):
                        print(f"N,{input},-\n")
                    elif(input>j):
                        print(f"v{i}.s8.h{input}.c{n+1}.i{indx+1},{input},>\n")
                    else:
                        print(f"v{i}.s8.h{j}.c{n}.i{indx+1},{input},>\n")

print("q0,#")
print("go_to_end,#,>\n")
for symbol in symbols:
    print(f"go_to_end,{symbol}")
    if(symbol=='_'):
        print("q1,_,<")
    else:
        print(f"go_to_end,{symbol},>")




for i in range(1,5):
    print(f"q1,{i}")
    print(f"bv{i}.s6.h0.c0.i0,_,<")
for indx in range(0,5):
    for c in range(0,5):
        for h in range(0,5):
            for i in range(1,5):
                for j in range(1,9):
                    for symbol in symbols:
                        print(f"bv{i}.s{j}.h{h}.c{c}.i{indx},{symbol}")
                        if(indx==4):
                            if(i!=c):
                                print(f"N,{symbol},-")
                            else:
                                print(f"GOBACK,{symbol},>")
                        else:
                            print(f"bv{i}.s{j-1}.h{h}.c{c}.i{indx},{symbol},<\n")
                        
for symbol in symbols:
    print(f"bGOBACK,{symbol}")
    if(symbol=='_'):
        print(f"q1,_,<")
    else:
        print(f"bGOBACK,{symbol},>")
print("q1,#")
print("check_rows,#,<")


for indx in range(0,5):
    for input in range(1,5):
        for i in range(1,5):
            for j in range(0,5):
                for n in range(0,5):
                    print(f"bv{i}.s0.h{j}.c{n}.i{indx},{input}")
                    if(input>j and (n+1>i)):
                        print(f"N,{input},-\n")
                    elif(input>j):
                        print(f"bv{i}.s8.h{input}.c{n+1}.i{indx+1},{input},<\n")
                    else:
                        print(f"bv{i}.s8.h{j}.c{n}.i{indx+1},{input},<\n")
for i in range(1,5):
    print(f"check_rows,{i}")
    print(f"v.{i},{i},<")
    print(f"v.{i},:")
    print(f"v.{i}.c0.h0,:,<")

for v in range(1,5):
    for c in range(0,5):
        for h in range(0,5):
            for input in range(1,5):
                print(f"v.{v}.c{c}.h{h},{input}")
                if(input>h and (c+1)>v):
                    print(f"N,{input},-\n")
                elif(input>h):
                    print(f"v.{v}.c{c+1}.h{input},{input},<\n")
                else:
                    print(f"v.{v}.c{c}.h{h},{input},<\n")
                print(f"v.{v}.c{c}.h{h},:")
                if(c!=v):
                    print(f"N,:,-\n")
                else:
                    print("go_to#,:,<")
                
for symbol in symbols:
    print(f"go_to#,{symbol}")
    if(symbol=='#'):
        print("check_rows,#,<")
    else:
        print(f"go_to#,{symbol},<")

print("check_rows,_")
print("Zgo_to#,_,>")

print("Zcheck_rows,_")
print("Y,_,-")
for symbol in symbols:
    print(f"Zgo_to#,{symbol}")
    if(symbol=='#'):
        print("Zcheck_rows,#,>")
    else:
        print(f"Zgo_to#,{symbol},>")

for i in range(1,5):
    print(f"Zcheck_rows,{i}")
    print(f"Zv.{i},{i},>")
    print(f"Zv.{i},:")
    print(f"Zv.{i}.c0.h0,:,>")

for v in range(1,5):
    for c in range(0,5):
        for h in range(0,5):
            for input in range(1,5):
                print(f"Zv.{v}.c{c}.h{h},{input}")
                if(input>h and (c+1)>v):
                    print(f"N,{input},-\n")
                elif(input>h):
                    print(f"Zv.{v}.c{c+1}.h{input},{input},>\n")
                else:
                    print(f"Zv.{v}.c{c}.h{h},{input},>\n")
                print(f"Zv.{v}.c{c}.h{h},:")
                if(c!=v):
                    print(f"N,:,-\n")
                else:
                    print("Zgo_to#,:,>")






                
                
                


    
