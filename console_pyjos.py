import cmd
import storage_pyjos as fw
import sys

class Console(cmd.Cmd):
    info = 'Вітаємо в PujOS'
    prompt = '(pyjos) \\'

    def do_help(self, arg):
        """help"""
        print("Command: print, burn, spawn, neo, say, quit")

    def do_print(selfs, arg):
        """print"""
        print(arg)

    def do_burn(self, arg):
        """delete file"""
        fw.burn(arg)

    def do_spawn(self, arg):
        """create file (тимчасовий)"""
        fw.spawn(arg)

    def do_neo(self, arg):
        """analog of neofetch"""

        logo = r"""
        

                                                       
,-.----.                         ,----..               
\    /  \                       /   /   \   .--.--.    
|   :    \                     /   .     : /  /    '.  
|   |  .\ :              .--. .   /   ;.  \  :  /`. /  
.   :  |: |            .--,`|.   ;   /  ` ;  |  |--`   
|   |   \ :    .--,    |  |. ;   |  ; \ ; |  :  ;_     
|   : .   /  /_ ./|    '--`_ |   :  | ; | '\  \    `.  
;   | |`-', ' , ' :    ,--,'|.   |  ' ' ' : `----.   \ 
|   | ;  /___/ \: |    |  | ''   ;  \; /  | __ \  \  | 
:   ' |   .  \  ' |    :  | | \   \  ',  / /  /`--'  / 
:   : :    \  ;   :  __|  : '  ;   :    / '--'.     /  
|   | :     \  \  ;.'__/\_: |   \   \ .'    `--'---'   
`---'.|      :  \  \   :    :    `---`                 
  `---`       \  ' ;\   \  /                           
               `--`  `--`-'                            

"""
        print(logo)
        print('Info')
        print("""
Version of OS: 0.1
OS name: PyjOS
Created by Luis
        """)


    def do_say(self, arg):
        fw.say(arg)

    def do_quit(self, arg):
        sys.exit()

