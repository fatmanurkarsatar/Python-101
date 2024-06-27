'''
    player 1:
        id           => 1
        name         => Cristiano Ronaldo
        yearofbirth  => 1985
        nationality  => Portugal
        current_team => Portugal
        history      => Juventus,Real Madrid,Portugal
        
     player 2:
        id           => 2  
        name         => Lionel Messi
        yearofbirth  => 1987 
        nationality  => Argentina
        current_team => Barcelona
        history      => Barcelona,Argentina,Portugal
'''

players = {}

id = input('oyuncu id: ')
name = input('oyuncu ad: ')
nationality = input('ülke: ')
yearOfBirth = input('doğum yılı: ')
current_team = input('takım: ')
history = input('oynadığı yerler: ')

players.update = ({
    id: {
        "name": name,
        "yearOfBirth": yearOfBirth,
        "nationality": nationality,
        "yearOfBirth": yearOfBirth,
        "current_team": current_team,
        "history": history.split(',')
    }  
})

players = {}

id = input('oyuncu id: ')
name = input('oyuncu adı: ')
nationality = input('ülke: ')
yearOfBirth = input('doğum yılı: ')
current_team = input('takım: ')
history = input('oynadığı yerler: ')

players.update = ({
    id: {
        "name": name,
        "yearOfBirth": yearOfBirth,
        "nationality": nationality,
        "yearOfBirth": yearOfBirth,
        "current_team": current_team,
        "history": history.split(',')
    }  
})



print(players)


# 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.
# 2- id'e göre arama yapınız.
# 3- id'e göre bilgi kayıt siliniz.