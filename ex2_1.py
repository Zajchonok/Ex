import re

massiv = ['Kana', 'Muna', 'Pelmeen', 'Apelsin', 'Õun', 'Mandariin', 'Kakao', 'Hernes', 'Ahven']
massiv2 = ['1','2','3','4','5','6','7','8','9','10','11','567894', '489761', '908762', '167045']
massiv3 = [1,2,3,4,5,6,7,8,9,10]
mas4=['See on esimene - lause.']
pat = r'Kak?'
#for i in massiv2:
    #spisok = re.search(r'1',i)
    #print(i if spisok else'')
    #if spisok:
        #print(i)

#for i in mas4:
   # B поиск символа в конце и середине, b начало
    #otv = re.search(r'\Bna', i)
    #if otv:
        #print(i)
        #otv = re.split(pat,i)
        #if otv:
            #print(i)
#print(re.sub(pat, '000', mas4[0]))
#print(mas4[0][0:3])
#for i in massiv:
    #otv = re.search(pat, i)
    #if otv:
        #print(i)

#print(re.findall(r'\w+','Hello, мир', flags=re.ASCII))
#print(re.findall(r'\w+', 'Hello мир', flags=re.ASCII))
#print(re.findall(r'[уеыаоэяию]+', 'ОООО ааааа ррррр ЫЫЫЫ яяяя', flags=re.IGNORECASE))
