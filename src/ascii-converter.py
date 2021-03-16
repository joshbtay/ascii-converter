#!/bin/python3
import PIL.Image,PIL.ImageOps
import numpy as np
import random
import sys
print("\n    sour ascii converter\n")
print("                           ³r+ÎD@&Æ╬6WB&¥¥##ÆZL┐¦*                            ")
print("                 :v:)ª÷ï≡Q0╗ZUFUÔÆ╠B8#8&╣╠#╬¥╬9╣╣9#Áx(                        ")
print("            ²═øâCwysr─rfı└!;/)(=tr│┐pe1ý¼ãÓÁ5OÉ42ÛGPHM╣X>°                    ")
print("         ,═ög¬|:i\"¤.¯.`¯°¨`.-··¨¨¨·''¯'.°^²³:i)¿?äUXÅAÈPSÕæÜ+'                 ")
print("        v«j³¹¨.'      ·.'    -`__¹l┐:_°`-¨-·-'¯`\":_|aòúHKÃÌÌÌe'               ")
print("       └'³_*^ðÈEÝTÍÏPêIõw]aür_¤  ¨   ¨¯¯`°-.      -¨,'^_¦çÞõÝÜÙ]¯             ")
print("         ·.x¶B#O╗ÙÏÂKHPYYÖË£ËAÃFæÎÃ¢v¦¹`  °             ¯`·¤|;≡┼Z\"                ")
print("         ·Å#8OØ5A║Ä0ÃÚÒæÄ╚GAKÖÏ$Q4ÂPÀÜÚ2Aðey┘~ `¨            .³‗÷é®           ")
print("        ¤88ÓÒDßßAFX3┼ûõ├%Jøô╩╔æO5Í╗æ╝XZ╚╝Çûãò%ö%wn└'¨°  `       ¨':^^`        ")
print("       :¶@ÖÛÂöùóò┼½ÞãµñùLCáýèIøàþäJóþäð%â├ýôãCàûââ%ë%¾»/\"°         `¯_i‗      ")
print("      ·M╚Ü0ò¼óáä≡ò≡úëúðøþõ┼õIûù%JðIþëô½µäûû┼öâCµLáIJ¼èûðëñ7ª¡·        ·‗r~    ")
print("      8╠Â§J%≡óá¾Þùáâû½%ê≡ûIIòLäû≡ôëëâû┼úùøâÞJý├ú├ðúý├Áµÿãö½¼ý≡ü;└¯`     ·~³   ")
print("     ═&Ë├âññô¼áôÿâäpòwì©pys}>ï┬zxJúùð¾ùêãëäâLLäõI≡ûö½%òøäþñÞáá¾µåudª^-,  °¨_¨ ")
print("     ZØôýáãhîd»m®gy]>7üb«©1<é±yî©í>xá╠W9╬╠BÊñôôµãõyn7┴┤üqs<b«wq¿®═©ÿ┼nr.^°  ¯‗")
print("    \"#Tú├±sííí»as1ç}ì1xp}<}┴«zeünqì┼╠╣W#6Å÷jW7ìüb░¢dü░┤░{ngz7í░┬]güw¾¼ã¼*:^¯ ·")
print("    âÎIëx░bîsíme7{1[]hdq┴u±qzu═p┤┤y%ØÔS├-   óp7░®épk[kì[±yƒ{xkzgmwdé1h┤ø¡¹:²:°")
print("    ÕY¼┤ebbs┤k░íq71qƒsour@dude\ça┴┴dèñê┐   °─┤¢═®]ak<¿u┴xhçe[kp┤═qkx±[î7┬`³³, ")
print("    ÂH%}umdé?ku<┴u¿íx═7bqaíym┌lîbeb®┘ƒzhl└|dç┬JÜËM8YÖJq«]7k¿YÐTXkbkmí±hƒ|·`   ")
print("    ¼╔öç»®b1<1=/ı|t)¦┐g¿fl¬lj¦j┌¡¦ºlcªv;ı÷xtâÑ¶Ñ6998╬╣╬áb©CÑ96%ë╬©ì©}pzü¨     ")
print("    ²╔Lu<»s┴─¦┌|j)┌ır(│+f¡;vv|┘jrªvio¬└┐┘f¬é¶98╣@#╣¥╠W&╠ðºËÕı   gû{7g]îk      ")
print("     Vøs¿üaî¦jf└(cf┐j(c│l+=tª×º¡¬┐i¡j┌┐!¬º└╦ÉÊZÁ╝QÙ§TZ3ÉV)¼<    ²«¢kçsw©      ")
print("     ?Lx1a»k¬r;l;+¬)└o└ı/!┌tjc+fª=l!/j¬cıf+õýèã≡ýäúÿøåâûý;rh_~*)|f─7g=s¤      ")
print("      3┼ïyya└¬c┘|r└ıt(!(¦┌+ªı│=│ii┘└÷c+─÷ª└)┼ëö≡åúJê¼¼¾?┘riª└)=¡tº┌t┌i÷       ")
print("      ,½ü[n░7;┌└×)t¬f!o¦c×);c└º;/jıfl¦ªiiº×)i1b%¾b}L┤hrª│++i│º÷×!jıilx        ")
print("       ‗ån]hì!v┐ıı!;vf┘º¡=¦¬c└j|)vı)^~¹i¤‗:¹~¹^ª×º|!÷─┐┌¦c÷!=cjıc┌=/└         ")
print("        ¤þ░¢ïw×(ı│t└¬(tl(¦fo=(rº┌¹.·    .-¨¨,¨'¨‗vrı)cªcj!ıc¬┐│c×;ª(.         ")
print("         ¨L?dçqº¬¡┘/i;!¦×/oı┐¦!i` ¨            . ·||┐ı┌┘jrv¦l+f│¦i┐           ")
print("           iµ?1o)┘┌cji¦(÷ıc+│)i`      ¤┘)┐ª^-     ~)│÷vl¬|º!+─jº(°            ")
print("            °qe¿ı¡)└j¬lvv|¡+rvi.     \"i(vªcc-     *v¡(ijtªcªl|r²              ")
print("              .┴ƒ®!┐ªj─ciªc×ı│f:      ,³\"²-'     ,+;=ª/¬f│cv|¹¨               ")
print("                ,┐ü═t;¬;rr!f┌┐/;³      °¯°      ·!÷)┐×i(/(v.                  ")
print("                   \"¡çbti+v┐!o│f×o¤'         '.¦;o¬¦|!!ª²                     ")
print("                      ,³fyïfov)+c¦│rfr*‗‗\"‗)┌(fr!×ª=¹-                        ")
print("                           °:¬r7┬xí±┘v┌│¬+j¬r)f*,¯                            \n\n")

filepath = "" 
if len(sys.argv) == 1:
    filepath = input("    please enter the file you wish to convert: \n        ")
else:
    filepath = sys.argv[1]




image = PIL.Image.open(filepath)
image = PIL.ImageOps.grayscale(image)
col,row = image.size
array = np.array(image)
text = open('input.txt', encoding="utf-8")
output = ""
if len(sys.argv) > 2:
    output = sys.argv[2]
else:
    output = input("    output file (leave blank for output.txt): \n        ")
if output == "":
    output = "output.txt"

print("\n    converting...                                 \n ")

lines = [line for line in text.readlines()]
chars = []
for line in lines:
    newline = []
    for char in line:
        if char != '\n':
            newline.append(char)
    chars.append(newline)

def getChar(index: int) -> chr:
    if index == -1:
        return ' '
    return random.choice(chars[index])



squashed = []

for i,line in enumerate(array):
    newline = []
    for j,pixel in enumerate (line):
        if i%2 == 0 and i <= row-2:
            average = int((int(pixel) + int(array[i+1][j]))/2)
            newline.append(average)
    if i%2 == 0 and i <= row-2:
        squashed.append(newline)

brightest = 0
for line in array:
    for pixel in line:
        if pixel > brightest:
            brightest = pixel

def getBound(value: int) -> int:
    length = len(lines) + 1
    percent = value / brightest
    bracket = int(percent*length)
    if bracket == length:
        bracket -= 1
    return bracket - 1

text_file = open(output, "w", encoding='utf-8')
for i,line in enumerate(squashed):
    for pixel in line:
        bound = getBound(pixel)
        char = getChar(bound)
        text_file.write(char)
    text_file.write('\n')
text_file.close()
print("conversion finished ! output is in " + output)
