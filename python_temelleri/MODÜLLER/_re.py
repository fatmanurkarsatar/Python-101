import re

#result = dir(re)

# regular expression
# re modülü


str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

# re.findall
# result = re.findall("Python",str)
# result = len(result)

# re.split()
# result = re.split(" ",str)
# result = re.split("R",str)

# re.sub()
# result = re.sub(" ","*",str)
# result = re.sub("\s","*",str)
# result = re.sub("\s","-",str)

# re.search()
result = re.search("Python",str)
# result = result.span() # hangi aralıkta olduğunu gösterir
# result = result.start() # hangi karakterden başladığını gösterir
# result = result.end() # hangi karakterle bittiğini söyler
# result = result.group() # bulduğu ifadeyi bize geri gönderir
#result = result.string # stringi bize geri gönderir
# print(result)


"""
    [] -köşeli parantezler arasına yazılan 
        bütün karakterler aranır.
        
        [abc] => a      : 1 match
                ac      : 2 match
                Python  : no matches
                
         [a-e]   => [abcde]
         [1-5]   => [12345]
         [0-39]  => [01239]  
         
         [^abc]  => abc dışındaki karakterler.
         [^0-9]  => rakam olmayan karakterler.

"""

result = re.findall("[abc]",str)
result = re.findall("[sat]",str)
result = re.findall("[a-e]",str)
result = re.findall("[a-z]",str)
result = re.findall("[0-5]",str)
result = re.findall("[^abc]",str)
result = re.findall("[^0-9]",str)


"""
    . - Herhangi bir tek karakteri belirtir.

        .. => a     : no match
              ab    : 1 match
              abc   : 1 match
              abcd  : 2 matches 
               
"""

result = re.findall("...",str)
result = re.findall("Py..on",str)


"""
    ^ - Belirtilen karakterle başlıyor mu ?
    
    ^a => a:    1 match
          abc:  1 match
          bac:  no match    
"""

result = re.findall("^a",str)
result = re.findall("^P",str)


"""
    $ - Belirtilen karakterle bitiyor mu?
    
    a$ => a     : 1 match
          lamba : 1 match
          Python: no match
          
"""

result = re.findall("t$",str)
result = re.findall("saat$",str)
result = re.findall("saatt$",str)


"""
    * - Bir karakterin sıfır ya da daha fazla 
        sayıda olmasını kontrol eder.
         
        ma*n => mn     : 1 match
                man    : 1 match
                maaan  : 1 match
                main   : no match (a'nın arkasına n gelmiyor)
"""

result = re.findall("sa*t",str)


"""
    + - Bir karakterin bir ya da daha fazla sayıda 
        olmasını kontrol eder.
         
        ma+n => mn      : no match
                man     : 1 match
                maaan   : 1 match
                main    : no match (a nın arkasına n gelmiyor.)
"""

result = re.findall("sa+t",str)


"""
    ? - Bir karakterin sıfır ya da bir kez 
        olmasını kontrol eder.
        
        ma?n => mn     : no match
                man    : 1 match
                maaan  : 1 match
                main   : no match (a'nın arkasına n gelmiyor)
"""

result = re.findall("sa?t",str)
print(result)


""" 
    {} - karakter sayısını kontrol eder.
    
        al{2}   => a karaterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} =>a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar
        
"""

result = re.findall("a{2,3}",str)
result = re.findall("[0-9]{2}",str)


"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.
    
        a|b => a ya da b

            cde =>    no match
            ade =>    1 match
            acdbea => 3 match  
"""

"""
    () - gruplamak için kullanılır.
    
    (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""

result = re.findall("\APython",str)
result = re.findall("saat\Z",str)
print(result)

""" 
    \ - özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karaterini arar.
            yani $ regular exp. engine tarafından yorumlanmaz
            
    \A - belirtilen karakter stringin başında mı?
        \Athe => the stringin başında mı
        
    \Z - belirtilen karakter stringin sonunda mı?
        the\Z => the string in sonunda mı
        
    \b - belirtilen karakter kelimenin başında mı ya da sonunda mı?
        \bthe => the kelimein başında mı
        the\b => the kelimenin sonunda mı  
        
    \B - belirtilen karakter kelimenin başında yada sonunda değil mi?
        \Bthe => the kelimenin başında değil mi?
        the\B => the kelimenin sonunda değil mi?
        
    \d [0-9] ile aynı anlama gelir yani rakamları arar.
        \d => 12abc34
        
    \D [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
        \D => 1ab44_50
        
    \s - boşluk karakterinin arar.
    \S - boşluk karakterleri dışındakiler.
    \w - alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W - \w nin tam tersi                            
"""
