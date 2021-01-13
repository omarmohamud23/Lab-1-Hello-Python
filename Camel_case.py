txt = "fOnt proCESSOR and ParsER"
txt_Split = txt.split()

List = [txt_Split[0].lower()]
new_word = ""
print(txt_Split)

for j in range(1, len(txt_Split)):
    word = txt_Split[j].capitalize()
    List.append(word)
    print("" .join(List))