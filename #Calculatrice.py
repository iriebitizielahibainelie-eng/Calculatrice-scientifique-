print (
'===================================\n'
'       CALCULATRICE\n'
'===================================\n'
'Bienvenue ! Cette calculatrice permet d\'effectuer différents calculs.\n '
'1 - Addition\n'
'2 - Multiplication\n'
'3 - Soustraction\n'
'4 - Division\n'
'5 - Modulo\n'
'6 - Division entière\n'
'7 - Puissance\n'
'0 - Quiter\n')
while True:
    choix = input('faites un choix:  ')
    if choix == '0':
        print('Au revoir! et merci d\'avoir essayé notre calculatrice 👍')
        break 
    elif choix not in ['1', '2', '3', '4', '5', '6','7','0']:
         print('Il semble avoir une erreur, veillez verifié que vous avez opté pour un bon choix \n')
         quitter = input('voulez-vous continuer?'.lower())
         if quitter == 'non':
                print('Au revoir')
                break  
    else:
        nombre1= int(input('entrez un nombre:  '))
        nombre2= int(input('entrez un deuxième:  '))
    
    
    if choix == '1':
        print(f'Le resultat de : {nombre1} + {nombre2} ={nombre1+ nombre2} \n')
    
    elif choix == '2':
        print(f'Le resultat est : {nombre1} * {nombre2} = {nombre1 * nombre2}\n')

    elif choix == '3' :
        print(f'Le resultat est : {nombre1} - {nombre2}= {nombre1 -nombre2}\n')     
    
    elif choix == '4' :
         if nombre2 == 0:
             print('impossible de diviserpar ZERO')
         else:
             print(f'Le resultat est:  {nombre1} / {nombre2} = {nombre1 /nombre2}\n')
 
    elif choix == '5' :
              if nombre2 == 0:
                  print('impossible de diviserpar ZERO')
              else:
                  print(f'Le resultat est : {nombre1} % {nombre2} = {nombre1 %nombre2}\n')  
    elif choix == '6' :
         if nombre2 == 0:
             print('impossible de diviserpar ZERO')
         else:
             print(f'Le resultat est : {nombre1} // {nombre2} =  {nombre1// nombre2} ')  
    elif choix == '7':
            print(f"Le resultat est : {nombre1} ** {nombre2} = {nombre1 ** nombre2}\n")                     