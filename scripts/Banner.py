import os,platform,time
import scripts.color as c
import scripts.cprint as cp


try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    cp.cprint("Unfortunately you need colorama...")
    time.sleep(1)
    cp.cprint("Dont worry I got it sorted out")
    time.sleep(.3)
    cp.cprint("Attempting to install colorama...")
    time.sleep(.5)
    cp.cprint("Please connect to the internet")
    os.system("pip install colorama")



logo1 = """
      ___           ___           ___           ___           ___   
     /  /\         /  /\         /  /\         /__/\         /  /\  
    /  /:/_       /  /::\       /  /::\        \  \:\       /  /::\ 
   /  /:/ /\     /  /:/\:\     /  /:/\:\        \  \:\     /  /:/\:\
  /  /:/_/::\   /  /:/~/:/    /  /:/  \:\   ___  \  \:\   /  /:/~/:/
 /__/:/__\/\:\ /__/:/ /:/___ /__/:/ \__\:\ /__/\  \__\:\ /__/:/ /:/ 
 \  \:\ /~~/:/ \  \:\/:::::/ \  \:\ /  /:/ \  \:\ /  /:/ \  \:\/:/  
  \  \:\  /:/   \  \::/~~~~   \  \:\  /:/   \  \:\  /:/   \  \::/   
   \  \:\/:/     \  \:\        \  \:\/:/     \  \:\/:/     \  \:\   
    \  \::/       \  \:\        \  \::/       \  \::/       \  \:\  
     \__\/         \__\/         \__\/         \__\/         \__\/  
                      ___         ___                               
                     /  /\       /  /\                              
                    /  /:/      /  /:/                              
                   /__/::\     /__/::\                              
                   \__\/\:\__  \__\/\:\__                           
                      \  \:\/\    \  \:\/\                          
                       \__\::/     \__\::/                          
               ___     /__/:/      /__/:/___                        
              /__/\    \__\/ ___   \__\//  /\                       
             |  |::\        /  /\      /  /:/_                      
             |  |:|:\      /  /:/     /  /:/ /\                     
           __|__|:|\:\    /  /:/     /  /:/ /:/_                    
          /__/::::| \:\  /  /::\    /__/:/ /:/ /\                   
          \  \:\~~\__\/ /__/:/\:\   \  \:\/:/ /:/                   
           \  \:\       \__\/  \:\   \  \::/ /:/                    
            \  \:\           \  \:\   \  \:\/:/                     
             \  \:\           \__\/    \  \::/                      
              \__\/                     \__\/                       
              
              
              
"""
    
    
logo2 = f"""

       ********  *******     *******   **     ** ******* 
      **//////**/**////**   **/////** /**    /**/**////**
     **      // /**   /**  **     //**/**    /**/**   /**
    /**         /*******  /**      /**/**    /**/******* 
    /**    *****/**///**  /**      /**/**    /**/**////  
    //**  ////**/**  //** //**     ** /**    /**/**      
     //******** /**   //** //*******  //******* /**      
      ////////  //     //   ///////    ///////  //  
  
      
            /***********   /***********  
            /***********   /***********  
            //// **////    //// ** ////
                /**            /**                                   
                /**            /**                                   
                /**            /**                                   
                /**            /**                                   
                /**            /**                                   
                /**            /**                                   
            /***********   /***********  
            /***********   /***********  
             //////////    ///////////
        
             
          ****     **** ********** ********             
          /**/**   **/**/////**/// /**/////              
          /**//** ** /**    /**    /**                   
          /** //***  /**    /**    /*******              
          /**  //*   /**    /**    /**////               
          /**   /    /**    /**    /**                   
         /**        /**    /**    /********             
          //         //     //     ////////                   
"""
def banner():
    print(c.c_b+logo2)

def clear():
    if "Windows" in platform.platform():
        os.system("cls")
    else:
        os.system("clear")
def _quit():
    clear()
    print(c.c_w)
    print("Have a nice day")
    time.sleep(1)
    print(logo1)
    time.sleep(.4)
    clear()
    quit()