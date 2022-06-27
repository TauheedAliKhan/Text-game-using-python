def restart():
     import time
     print("The Game is going to restart")
     time.sleep(1)
     
def scene1():
 import time
 print("""                             
                                     Have you ever dreamed of going to an another world? Adi did.
                        He hated his life and wanted to have an adventure somehwere far away. But as usual he needs help.
                                                        SO LETS HELP HIM
                                        
 It was a typical morning. Adi woke up ate his breakfast and got ready to go to school. On his way to school he heard a strange voice calling him to go inside an alleyway. Should he listen the voice or not.
 Type YES(all caps) to listen and NO(all caps) to ignore the voice.


 """)
 
 c=input('Type your decision:')
 time.sleep(0.5)
 ans= 'incorrect'
 while(ans=='incorrect'):
         if(c.upper()=='YES'):
              print('\n Adi goes down the alleyway')
              ans='correct'
              time.sleep(0.5)
              scene2()
         elif(c.upper()=='NO'):
              print('\n Adi gets hit by a truck because the voice in his head kept distracting him.\n  GAME OVER!')
              ans='correct'
              time.sleep(2)
              restart()
              scene1()
         else:
             print("Enter the decision in all caps")
             c=input('Type your decision:')  

def scene2():
     import time
     print("""
                    As he goes down the alleyway he sees light shimmering near the end. He realises it is a portal to another world.
                    He steps into the light and feels like he is hurled off his feet and faints. As he wakes up he hears a loud roar and sees a 
                    young girl being attacked by a monster.
                    (You have two options
                    1) Attack the monster and risk certain death(adi's death)
                    2)Run away and hope nobody sees you.
                    What do you choose?
                    Type ATTACK or RUN)
                    

     """)
     time.sleep(0.5)
     d=input('What is your decision:')
     ans='incorrect'
     while(ans=='incorrect'):
          if(d.upper()=='ATTACK'):
               print('''\n Adi attacks the monster and dies instantly.\n GAME OVER''')
               ans='correct'
               time.sleep(5)
               restart()
               scene1()
          elif(d.upper()=='RUN'):
               print('Adi runs away as fast as possible(Yep he is a coward)')
               ans='correct'
               time.sleep(0.5)
               scene3()
          else:
                print("Enter the decision in all caps")
                d=input('What is your decision:')


def scene3():
     import time
     print("""                                    As Adi was running away he heard the sound of a horn blowing. An army was was riding towards the monster. 
                                                  The Army defeated the monster. Adi was seen by one of the soldiers and called over. He was asked, if he was the one who called
                                                  the army to save the princess.
               Adi now has a choice to make. He could tell the truth or lie and take the money that was being offered.
               What do you think Adi should do? TRUTH or FALSE """)
     time.sleep(0.5)          
     d=input("What is your Decsion:")
     ans='incorrect'          
     while(ans=="incorrect"):
          if(d.upper()=="TRUTH"):
               print("Adi tells the truth and is branded a coward and executed for abandoning the princess \n GAME OVER!")
               ans="correct"
               time.sleep(2)
               restart()
               scene1()
          elif(d.upper()=="FALSE"):
               print("Adi lies and claims that he called the army to save the princess\nHe is invited to the palace and the king wants to thank him personally\nSide note:The princess was not hurt but had fainted during the battle")
               ans="correct"
               time.sleep(1)
               scene4()
          else:
               print("Enter the decision in all caps")
               d=input('What is your decision:')

def scene4():
     import time
     print(""" As adi prepares for travel he asks the general of the army about  his reward.The general says that the king wanted to reward the princess commoner friend himself.\n Adi realises that if the princess woke up he would be caught.He thought of running away but there is no way he could ever outrun an army.\nIt was now a race against time.
               Will Adi be able to  reach the king and  get the award before the princess wakes up or will he be caught? Find out in the next chapter.
               
                ===================================================================END OF CHAPTER ONE=================================================== """)
     time.sleep(10)
     restart()
     scene1()

scene1()
