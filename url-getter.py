"""  
                                                                      ./*       
                                                                 .(###.         
                                                             *######            
                                                         /########              
                                                     ,##########                
                                                  (###########                  URL Getter to generate URL get requst form the List
              /                                #(###########.                   List must be availible in the same folder.
             (*                             (#############(                     Thanks to https://gist.github.com/demersdesigns/4442cd84c1cc6c5ccda9b19eac1ba52b
            ,#,                          ,###############.                      For URL list  demersdesigns/craft-popular-urls 
            ##/                        (################                        
           /###                      ##################                         
           ####                    ((################(                          
          *####*                 /###################                           
          ######                ####################,                           Anton Preck
          #######             *#####################                            
         .#######/           (######################*                           
         *########/         #########################.                          
         /#########(       /###########################                         
         /###########,    .###############################.                """      
                                                                                
                 
import urllib.request
import time
import random

f = open("urls.txt", "r")
user_agent = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64)', 'Mozilla/5.0 (X11; Linux x86_64)', 'Mozilla/5.0 (X11; U; Linux i686; en-US)','Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3)', 'Opera/9.80 (X11; Linux i686; Ubuntu/14.10)', 'Opera/9.80 (Windows NT 6.0)', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en)']
for x in f:
  print("call: ", x) 
  req = urllib.request.Request(x, headers={'User-Agent': random.choice(user_agent)})
  try: urllib.request.urlopen(req, timeout=10)
  except urllib.error.URLError as e:
      print(e.reason)
  time.sleep(5)
