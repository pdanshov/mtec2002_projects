"""
ascii_art.py
===
Create a program that prints out ascii art based on user input.  Continue to ask the user for input until the user types in  quit .
* Create variables named  tree ,  truck  and  heart  that contain the following patterns (note that the backslashes must be  escaped ; having two backslashes in a row is intentional):

    /\\
   /  \\
   /  \\
  /____\\
    ||
      __
 ____|  \_    
|_________|
  O     O
  __  __
 /  \/  \\
  \    /
    \/

* Create a while loop that will loop forever.
* In the while loop...
* Prompt the user for input by asking for a picture to draw; store it in a variable called user_input.
* If the input is  tree ,  truck  or  heart , print out the associated image. 
* If the input is  quit , exit the program using the exit() function.
* If the input is none of the above, print out  I don  t know how to draw that. .
* As long as the input is not quit, keep prompting the user for more input.
* (INTERMEDIATE) add a command named  help ; it will display all of the commands and pictures that are available (construct the output using the existing variables for you pictures)

Example Output:
What picture should I draw?
> anteater
I don  t know how to draw that
What picture should I draw?
> truck

      __
 ____|  \_    
|_________|
  O     O

What picture should I draw?
> quit
Bye!
"""
   

# this first variable is an example of how you would store an  image  in a variable
tree =  """
    /\\
   /  \\
   /  \\
  /____\\
    ||
"""
truck = """
      __
 ____|  \_    
|_________|
  O     O
"""
heart = """
  __  __
 /  \/  \\
  \    /
    \/
"""
rose = """
                     M,        .mM
                     IMIm    ,mIM
                     ,MI: IM,mIMm
           IMmm,    ,IM::::IM::IM,          ,m
              IMMIMMIMm::IM:::::IM  ==mm ,mIM
    __      ,mIM::::::MIM:::::::IM::::mIMIM
 ,mMIMIMIIMIMM::::::::mM::::::::IMIMIMIMMM
IMM:::::::::IMM::::::M::::::::IIM:::::::MM,
  IMM::::::::::MM:::M:::::::IM:::::::::::IM,
     IMm::::::::IMMM:::::::IM:::::::::::::IM,
       Mm:::::::::IM::::::MM::::::::::::::::IM,
       IM:::::::::IM::::::MM::::::::::::::::::IM,
        MM::::::::IM:::::::IM::::::::::::::::::IM
         IM::::::::IM:::::::IM:::::::::::::::::IM;.
          IM::::::::MM::::::::IM::::::::::mmmIMMMMMMMm,.
           IM::::::::IM:::::::IM::::mIMIMM    . ..  IMMMM
            IM::::::::IM::::::mIMIMM  . . . . . .,mM     M
            IMm:::::::IM::::IIMM  . . . . . ..,mMM 
             IMMIMIMMIMM::IMM  . . . ._.,mMMMMM 
             ,IM . . . IMIM . . . .,mMMMMMMMM 
           ,IM . . . .,IMM . . . ,mMMMMMMMMM 
          IM. . . .,mIIMM,. . ..mMMMMMMMMMM 
         ,M ..,mIMMIMMIMMIMmmmMMMMMMMMMMMM 
         IM.,IMI             IIMMMMMMMMMMM
        ;IMIM                     IMMMMMMM
                                    IMMMMM
                                      IMMM
                                       IMM,
                                        IMM
                                         MM,
                                         IMM,              ______   __
                        ______            IMM__        .mIMMIMMIMMIMMIMM,
                   .,mIMMIMMIMM, ,mIMM,   IMM        ,mIM . . . .  IM,..M,
                 ,IMMM   . . .  IMM.\  M,  IMM      ,IM . . . .  / :;IM \ M,
               .mIM   . . .  / .: IM.\ MM   MM,    ,M . . .  / .;mIMIMIM,\ M
              ,IM  . . .  / . .:;,IMIMIMMM  IMM   ,M . .  / .:mIM       IM,:M
             ,IM  . . . / . .:;,mIM   ` IMM IMM   IM. .  / .mM           IMI
            ,IM . .  / . .:;,mIM        IMMMMM   MM,.  / ,mM             M  
            IM  . .  / . .;,mIM            IIMMM ,IMIM,.,IM 
            IM . . / . .,mIM               IMMMMMMM      
            `IM,.  / ;,mIM                  IIMMM
              IMI, /,mIM                  __IMMM
                IMMMM                       IMM
                                            IMM
                                            IMM__
                                            IMM   
                                            IMM
                                            IMM
                                          __IMM
                                            IMM
                                            IMM
                                            IMM
                                            IMM__
                                            IMM   
                                            IMM
                                            IMM
"""
while True:
	print "What picture should I draw?\nType help for a list of commands"
	user_input = raw_input("> ").lower()
	if user_input == "quit":
		exit()
	elif user_input == "help":
		print "\n(tree, truck, heart, rose, quit)\n"
	elif user_input == "tree":
		print tree
	elif user_input == "truck":
		print truck
	elif user_input == "heart":
		print heart
	elif user_input == "rose":
		print rose
	else:
		print "\nI don't know how to draw that.\n"