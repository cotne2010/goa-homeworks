#დაწერეთ პროგრამა სადაც შეამოწმეთ, სტუდენტმა ჩააბარა თუ არა ჩააბარა კურსი მათი გამოცდის ქულების მიხედვით. 
# სთხოვეთ მომხმარებელს შეიყვანოს ქულები შუალედური გამოცდისთვის, დასკვნითი გამოცდისთვის და პროექტისთვის. 
# დარწმუნდით, რომ მომხმარებელმა შეიყვანოს სწორი ქულები (პოზიტიური რიცხვები 0-დან 100-მდე) თითოეული კომპონენტისთვის.
#გამოიყენეთ შემდეგი შეფასების კრიტერიუმები: თუ საშუალო ქულა (20% შუალედური კურსისთვის, 40% საბოლოო და 40% პროექტისთვის) არის 70 ან მეტი, სტუდენტი გაივლის კურსს. 
# თუ საშუალო ქულა 70-ზე დაბალია, სტუდენტი ვერ ახერხებს კურსის ჩაბარებას. 
# აჩვენეთ მომხმარებლისთვის შეტყობინება, რომელშიც მითითებულია მისი გავლის/ჩავარდნის სტატუსი და გამოთვლილი საშუალო ქულა


ქულა=input("შეიყვანეთ მოსწავლის ქულა: ")


if ქულა > 70:
    print('მოსწავლემ ჩააბარა გამოცდა')

elif ქულა < 70:
    print('მოსწავლემ ვერ ჩააბარა გამოცდა')





