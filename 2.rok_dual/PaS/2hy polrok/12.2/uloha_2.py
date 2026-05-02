
moj_list = []
moj_list.append(input("ake je tvoje meno: "))
moj_list.append(input("ake je tvoje priezvisko: "))
moj_list.append(int(input("aky je tvoj vek: ")))

print("tvoje meno je", moj_list[0], "priezvisko je", moj_list[1], "a vek", moj_list[-1])


#dorobenie neakych chujovim
if type(moj_list[-1]) == int:
    if moj_list[-1] == 1:
        print("tvoje meno je", moj_list[0], "priezvisko je", moj_list[1], "a mas", moj_list[-1], "rok.")
    elif 1 < moj_list[-1] < 5:
        print("tvoje meno je", moj_list[0], "priezvisko je", moj_list[1], "a mas", moj_list[-1], "roky.")
    else:
        print("tvoje meno je", moj_list[0], "priezvisko je", moj_list[1], "a mas", moj_list[-1], "rokov.")
else:
    print("nespravny vek")