
print("Welcome to the Treasure Hunt with RXD ")
print("Your mission is to find the treasure")
print("Let Us Start the game")
print("""

                     ;`',
                `,  `,
                 ',   ;   ,,-""==..,
                  \    ','          \
          ,-""'-., ;    '    __.-="-.;
        ," ,,_    "V      _."
       ;,'   ''-,          "=--,_
              ,-''    _  _       `,
             /   ,.-+(_)(_)�--.,   ;
            ,'  /   ; (_)       `\ ,
            ; ,/    ;._.;         ;
            !,'     ;   ;
            V'      ;   ;
                    ;._.;
                    ;   ;
                    ;   ;        ~
     ~              ;._.;
               ~    ;   ;
                   .�   `.                ~
             __,.--;.___.;--.,___
       _,,-""      ;     ;       ""-,,_
   .-��            ;     ;             ``-.
  ",              �       `               ,"        ~
    "-_                                _-"
~       ``----..,_          __,,......-
                  ```''''���                  ~
                              ~
""")
print("Now you are in a strange island . You see two roads . \n One is towards the right adn the next is towards the left")
direc=input("Where you would like to go ( right or left ) : ")
if direc=="right":
    print("""

               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
            """)
    print("Ohhh No , You Just Died by falling into hole ! ")
    print("GAME OVER !")
if direc=="left":
    print("This path lead you to a watterfall ")
    print("""
                                          .___________.
                                           |   |     |
                                           | |   |  ||
                                           |  |  |   |
                                           |'. .' .`.|
___________________________________________|0oOO0oO0o|____________
                                          / '  '. ` ` \    
                                        /    '  . `   ` \   
                                      /  '                \ 
                                    /       ' ' .    ` `    \  
                                  /   '   '        `      `   \
                                 /          '    . `     `    `  \
                                /  '    '      '      `            \
                              /     '     '   '                      \

        """)
    swim=input("Would you like to swim across or wait (swim or wait): ")
    if swim=="swim":
        print("""
                                        ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      _',
               \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\
                \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `\
                -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               \
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`
   `              


        """)
        print("A monster just appeared from the water and killed you !")
        print("GAME OVER !")
    if swim=="wait":
          print("Your wait is worth it . The waterfall just stopped and three doors appeared")
          print("""     
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|       
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|
""")
          print("Now , you can see a red , yellow and blue door")
          door=input("Which door are you entering : ")
          doorf=door.lower()
          if doorf=="red":
               print("""

 
  oo`'._..---.___..-
 (_,-.        ,..'`
      `'.    ;
         : :`
        _;_;  


              """)
               print("This Door lead you to the Jurassic Park !")
               print("Oh No , you were killed by the T-Rex")
               print("GMAE OVER !")
               
          if doorf=="blue":
               print("""
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/," """)
               print("You entered the HELL's DOOR !")
               print("GAME OVER !")
          if doorf=="yellow":
               
               print("Hurray ! YOU FOUND THE TREASURE ")