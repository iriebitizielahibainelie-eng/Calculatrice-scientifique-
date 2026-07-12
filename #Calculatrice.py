print('Hello ici vous pourrais faire diférent calcul !. ')

while True:
    
    nombre1 =int(input('entrez un prémier nombre : ')) 
    nombre2 = int(input('entrez un deuxième nombre : '))
    
    choix = input(
    'Faite un choix: Addition, multiplication, soustration,division , modulo pour le reste d\'une division, division entière, ou puissance'.lower())
    
    if choix == 'addition':
        print(f'Le resultat est : {nombre1 + nombre2}')
    
    elif choix == 'multiplication':
        print(f'Le resultat est : {nombre1 * nombre2}')

    elif choix == 'soustration' :
        print(f'Le resultat est : {nombre1 -nombre2}')     
    
    elif choix == 'division' :
         if nombre2 == 0:
             print('impossible de diviserpar ZERO')
         else:
             print(f'Le resultat est:  {nombre1 /nombre2}')
 
    elif choix == 'modulo' :
              if nombre2 == 0:
                  print('impossible de diviserpar zero')
              else:
                  print(f'Le resultat est : {nombre1 %nombre2}')  

    elif choix == 'division entière' :
         if nombre2 == 0:
             print('impossible de diviserpar ZERRO')
         else:
             print(f'Le resultat est : {nombre1 //nombre2}')  
    elif choix == 'puissance' :
     print(f'Le resultat est :  {nombre1 **nombre2}')
    else:
         print('Il semble avoir une erreur, veillez verifié que vous avez opté pour un bon choix')                                                                
         quitter = input('voulez-vous continuer ? (oui ou non)')
         if quitter.lower()== 'non':
             print('Au  revoir!')
             break                     