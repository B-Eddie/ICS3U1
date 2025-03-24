# Name: Eddie Bian
# Date: March 6, 2025
# Course Code: ICS3U1
# Description: Pygame House Project

import pygame
import math
import random
import time

pygame.init() # Initialize pygame

# Setup display
SIZE = (1000, 700)
screen = pygame.display.set_mode(SIZE)

# Define colors
LIGHTPINK = (255, 182, 193)
PINK = (255, 105, 180)
BROWN = (210, 180, 140)
DARKBROWN = (255, 87, 51)
DARKDARKBROWN = (110,44,53)
LIGHTBROWN = (188, 152, 126)
TAN = (222, 184, 135)
BLUE = (173, 216, 230)
DARKBLUE = (135,206,250)
SKYBLUE = (135, 206, 235)
GRAY = (169, 169, 169)
WHITE = (255, 255, 255)
GREEN = (144, 238, 144)
DARKGREEN = (0, 100, 0)
GRASSGREEN = (120,182,84)
BUSH1 = (91,164,82)
BUSH2 = (101,182,91)
BUSH3 = (111,200,100)
BUSH4 = (120,218,108)
BUSH5 = (130,235,117)
TREE1 = (41, 124, 24)
TREE2 = (56, 139, 40) 
TREE3 = (52, 105, 42)
TREE4 = (93, 168, 78)
TREE5 = (138, 197, 127)
CLOUD1 = (240, 240, 245)
CLOUD2 = (245, 245, 250) 
CLOUD3 = (250, 250, 255)
PEACH = (255, 218, 185)
YELLOW = (255, 239, 13)
BLACK = (0, 0, 0)
SILVER = (218,222,223,255)
LIGHTSILVER = (192,255,255)
RED = (255,0,0)
PASTEL_LAVENDER = (220, 190, 255) 
PASTEL_MINT_GREEN = (190, 240, 200)
PASTEL_PINK = (255, 180, 210)
PASTEL_YELLOW = (255, 240, 140)
PASTEL_BLUE = (180, 220, 255)
PASTEL_LILAC = (210, 180, 240)
PASTEL_PEACH = (255, 230, 210)
PASTEL_CYAN = (170, 240, 240)
PASTEL_GREEN = (200, 255, 200)
PASTEL_ORANGE = (255, 192, 103)

# Decorations behind the house
# add a brawl stars character called hank
def hank(x, y, scale):
    # head - change GREEN to PASTEL_LAVENDER
    pygame.draw.polygon(screen, PASTEL_LAVENDER, [(x+94.2630328861995*scale, y+69.993871101187*scale), (x+87.3587948917011*scale, y+46.8425187115675*scale), (x+83.0826015555751*scale, y+38.6695618899461*scale), (x+76*scale, y+36*scale), (x+68.1046607606643*scale, y+33.5770620196765*scale), (x+55.0738522690918*scale, y+31.629929716338*scale), (x+41.5937055536721*scale, y+33.5770620196765*scale), (x+35.2368656869167*scale, y+35.1887997834958*scale), (x+27.2148823905576*scale, y+39.4184589296917*scale), (x+24.2913135984639*scale, y+44.9556001085768*scale), (x+21.5169931362201*scale, y+53.3743744581279*scale), (x+24.9013190210043*scale, y+56.0645009761895*scale), (x+26.6028455409043*scale, y+59.8929356459645*scale), (x+30.8566618406544*scale, y+52.4062189584045*scale), (x+37.9179968982394*scale, y+50.0240818305445*scale), (x+45.0644082818195*scale, y+52.0659136544245*scale), (x+49.4033009075645*scale, y+58.4466381040495*scale), (x+50*scale, y+65*scale), (x+48.8928429515945*scale, y+68.2304155934745*scale), (x+52.765917371783*scale, y+66.4644772558887*scale), (x+75.4395990446085*scale, y+66.6783799131795*scale),])
    
    # goggle - change YELLOW to PASTEL_YELLOW
    pygame.draw.polygon(screen, PASTEL_YELLOW, [(x+30.7960885876309*scale, y+74.2975060714954*scale), (x+35.168261871576*scale, y+75.8670041734244*scale), (x+40.8857192428888*scale, y+75.3064691370212*scale), (x+46.8273906287629*scale, y+72.5037939550051*scale), (x+48.8928429515945*scale, y+68.2304155934745*scale), (x+50*scale, y+65*scale), (x+49.4033009075645*scale, y+58.4466381040495*scale), (x+45.0644082818195*scale, y+52.0659136544245*scale), (x+37.9179968982394*scale, y+50.0240818305445*scale), (x+30.8566618406544*scale, y+52.4062189584045*scale), (x+26.6028455409043*scale, y+59.8929356459645*scale), (x+24.9013190210043*scale, y+56.0645009761895*scale), (x+21.5169931362201*scale, y+53.3743744581279*scale), (x+14.4284655246568*scale, y+52.4366396517701*scale), (x+9.8320782261504*scale, y+54.1182447609797*scale), (x+6.0204399786086*scale, y+61.2930932269409*scale), (x+5.4599049422053*scale, y+67.6831926419375*scale), (x+6.9172960368537*scale, y+72.3916869477245*scale), (x+10.9531482989569*scale, y+66.2258015472891*scale), (x+17.0069266921117*scale, y+63.5352333725537*scale), (x+24.0696681507922*scale, y+64.4320894307989*scale), (x+29.0023764711405*scale, y+68.467941692902*scale),])

    # left inner eye - change GRASSGREEN to PASTEL_MINT_GREEN
    pygame.draw.polygon(screen, PASTEL_MINT_GREEN, [(x+20.2940640731261*scale, y+63.4683182418619*scale), (x+17.0069266921117*scale, y+63.5352333725537*scale), (x+14*scale, y+64*scale), (x+10.9531482989569*scale, y+66.2258015472891*scale), (x+8.7510081905807*scale, y+68.6724756397552*scale), (x+8.3988471636556*scale, y+63.0770282119451*scale), (x+10.5900713311896*scale, y+58.4206768559353*scale), (x+14.6594876423243*scale, y+56.1903236854096*scale), (x+17.7898078816586*scale, y+57.481580784135*scale), (x+19.5897420192758*scale, y+60.4553850115026*scale),])
    pygame.draw.line(screen, DARKGREEN, (x+8.479328657659*scale, y+62.3074048977531*scale), (x+13.1228404090619*scale, y+64.4222574896601*scale), 3)
    
    # right inner eye - change GRASSGREEN to PASTEL_MINT_GREEN
    pygame.draw.polygon(screen, PASTEL_MINT_GREEN, [(x+36.4733177767461*scale, y+71.9135547604779*scale), (x+40*scale, y+70*scale), (x+42.0606868868688*scale, y+66.2368039293414*scale), (x+42.7519695586595*scale, y+61.7928438964007*scale), (x+41.0811792549664*scale, y+56.8612072649583*scale), (x+37.753279298474*scale, y+54.0964903780261*scale), (x+32.4798378289552*scale, y+55.4788488214922*scale), (x+30.0735101681068*scale, y+58.960344160592*scale), (x+29.30553325507*scale, y+64.336182551849*scale), (x+30.1247086289759*scale, y+67.7664794300796*scale), (x+32.428639368086*scale, y+70.8895855430956*scale),])
    pygame.draw.line(screen, DARKGREEN, (x+42.2290284808324*scale, y+59.331359983433*scale), (x+29.6763353848665*scale, y+66.7122395678104*scale), 3)
   
    # nose - change RED to PASTEL_PINK
    pygame.draw.polygon(screen, PASTEL_PINK, [(x+30.7960885876309*scale, y+74.2975060714954*scale), (x+30.9014094708176*scale, y+79.8649480303595*scale), (x+29.0023764711405*scale, y+84.7234577485952*scale), (x+25.4149522381599*scale, y+89.0956310325403*scale), (x+17.5674617285149*scale, y+90.1045940980661*scale), (x+11.7378973499214*scale, y+88.5350959961371*scale), (x+8.2625801242214*scale, y+83.9387086976307*scale), (x+6.4688680077311*scale, y+77.7728232971953*scale), (x+6.9172960368537*scale, y+72.3916869477245*scale), (x+10.9531482989569*scale, y+66.2258015472891*scale), (x+17.0069266921117*scale, y+63.5352333725537*scale), (x+24.0696681507922*scale, y+64.4320894307989*scale), (x+29.0023764711405*scale, y+68.467941692902*scale),])

    # inner nose - keep BLACK
    pygame.draw.polygon(screen, BLACK, [(x+16.6481233286889*scale, y+71.7034115782952*scale), (x+17.7900295352338*scale, y+73.4434591311255*scale), (x+18.4969238535712*scale, y+76.5429188346047*scale), (x+17.7900295352338*scale, y+79.1529901638502*scale), (x+15.8324760382996*scale, y+81.6543085210439*scale), (x+14.0380519994433*scale, y+79.6423785380838*scale), (x+13.5486636252097*scale, y+76.4341658625528*scale), (x+14.309934429573*scale, y+73.8784710193331*scale),])

    # body - change BROWN to PASTEL_LILAC
    pygame.draw.polygon(screen, PASTEL_LILAC, [(x+75.4395990446085*scale, y+66.6783799131795*scale), (x+94.2630328861995*scale, y+69.993871101187*scale), (x+103.5387306711942*scale, y+80.3235581974868*scale), (x+101.9473820185347*scale, y+94.2956320748747*scale), (x+92.793295961588*scale, y+106.0903198790174*scale), (x+83.2871296716819*scale, y+110.6673629074907*scale), (x+32.0594557760766*scale, y+112.6038041887679*scale), (x+14.631484244582*scale, y+104.1538785977403*scale), (x+8.470080167791*scale, y+94.8237524243139*scale), (x+6.4688680077311*scale, y+77.7728232971953*scale), (x+8.2625801242214*scale, y+83.9387086976307*scale), (x+11.7378973499214*scale, y+88.5350959961371*scale), (x+17.5674617285149*scale, y+90.1045940980661*scale), (x+25.4149522381599*scale, y+89.0956310325403*scale), (x+29.0023764711405*scale, y+84.7234577485952*scale), (x+30.9014094708176*scale, y+79.8649480303595*scale), (x+30.7960885876309*scale, y+74.2975060714954*scale), (x+35.168261871576*scale, y+75.8670041734244*scale), (x+40.8857192428888*scale, y+75.3064691370212*scale), (x+46.8273906287629*scale, y+72.5037939550051*scale), (x+48.8928429515945*scale, y+68.2304155934745*scale), (x+52.765917371783*scale, y+66.4644772558887*scale),])

    # bottom body - change PEACH to PASTEL_PEACH
    pygame.draw.polygon(screen, PASTEL_PEACH, [(x+99*scale, y+97*scale), (x+92*scale, y+106*scale), (x+83*scale, y+110*scale), (x+32*scale, y+112*scale), (x+23*scale, y+110*scale), (x+14*scale, y+104*scale), (x+8*scale, y+94*scale), (x+8*scale, y+92*scale), (x+8*scale, y+89*scale), (x+10*scale, y+87*scale), (x+11*scale, y+88*scale), (x+17*scale, y+90*scale), (x+25*scale, y+89*scale), (x+29*scale, y+84*scale), (x+36*scale, y+84*scale), (x+43*scale, y+86*scale), (x+49*scale, y+88*scale), (x+54*scale, y+91*scale), (x+58*scale, y+96*scale)])

    # right arm - change SILVER to PASTEL_BLUE
    pygame.draw.polygon(screen, PASTEL_BLUE, [ (x+87*scale, y+79*scale), (x+89*scale, y+75*scale), (x+93*scale, y+73*scale), (x+97*scale, y+72*scale), (x+111*scale, y+73*scale), (x+117*scale, y+77*scale), (x+118*scale, y+80*scale), (x+120*scale, y+84*scale), (x+116*scale, y+91*scale), (x+110*scale, y+94*scale), (x+102*scale, y+94*scale), (x+97*scale, y+94*scale), (x+92*scale, y+92*scale), (x+88*scale, y+90*scale), (x+86*scale, y+87*scale), (x+86*scale, y+84*scale) ])

    # left arm - change SILVER to PASTEL_BLUE
    pygame.draw.polygon(screen, PASTEL_BLUE, [ (x+6*scale, y+78*scale), (x+4*scale, y+78*scale), (x+2*scale, y+79*scale), (x+1*scale, y+81*scale), (x+1*scale, y+83*scale), (x+1*scale, y+85*scale), (x+2*scale, y+86*scale), (x+2*scale, y+89*scale), (x+4*scale, y+91*scale), (x+6*scale, y+93*scale), (x+9*scale, y+94*scale), (x+7*scale, y+89*scale), (x+8*scale, y+83*scale) ])
    
    # Decorations
    # patch on body - change WHITE to PASTEL_GREEN
    pygame.draw.polygon(screen, PASTEL_GREEN, [ (x+50*scale, y+85*scale), (x+55.3331514897333*scale, y+90.6643949795285*scale), (x+58*scale, y+88*scale), (x+60.3144321754961*scale, y+90.1019923214586*scale), (x+65.2957128612589*scale, y+84.5181373591923*scale), (x+63.1264454658461*scale, y+82.2685267269123*scale), (x+65.094854769091*scale, y+79.8180580024645*scale), (x+60*scale, y+75*scale), (x+57.703276977314*scale, y+77.4479325148839*scale), (x+54.5698907394955*scale, y+75.1179786457368*scale), (x+49.6287816721663*scale, y+80.0992593314995*scale), (x+52.3202801072155*scale, y+82.4292132006466*scale) ])

    # nails on body - keep DARKBROWN
    pygame.draw.circle(screen, DARKBROWN, (x+37*scale, y+90*scale), 2)
    pygame.draw.circle(screen, DARKBROWN, (x+12*scale, y+93*scale), 2)
    pygame.draw.circle(screen, DARKBROWN, (x+59*scale, y+102*scale), 2)
    pygame.draw.circle(screen, DARKBROWN, (x+84*scale, y+105*scale), 2)

    # strap - change DARKDARKBROWN to PASTEL_PINK
    pygame.draw.polygon(screen, PASTEL_PINK, [ (x+61*scale, y+55*scale), (x+64*scale, y+66*scale), (x+69*scale, y+71*scale), (x+72*scale, y+80*scale), (x+71*scale, y+89*scale), (x+69*scale, y+96*scale), (x+65*scale, y+102*scale), (x+61*scale, y+106*scale), (x+53*scale, y+110*scale), (x+50*scale, y+110*scale), (x+51*scale, y+112*scale), (x+58*scale, y+113*scale), (x+65*scale, y+111*scale), (x+71*scale, y+108*scale), (x+75*scale, y+105*scale), (x+78*scale, y+100*scale), (x+80*scale, y+94*scale), (x+82*scale, y+89*scale), (x+82*scale, y+83*scale), (x+81*scale, y+78*scale), (x+77*scale, y+68*scale), (x+75*scale, y+66*scale), (x+73*scale, y+55*scale) ])

    # helmet bottom - change BUSH2 to PASTEL_CYAN
    pygame.draw.polygon(screen, PASTEL_CYAN, [(x+19*scale, y+53*scale), (x+55*scale, y+48*scale), (x+74*scale, y+49*scale), (x+92*scale, y+53*scale), (x+93*scale, y+56*scale), (x+92*scale, y+58*scale), (x+90*scale, y+59*scale), (x+89*scale, y+58*scale), (x+73*scale, y+54*scale), (x+50*scale, y+55*scale), (x+47*scale, y+54*scale), (x+45*scale, y+52*scale), (x+38*scale, y+50*scale), (x+31*scale, y+52*scale), (x+28*scale, y+56*scale), (x+25*scale, y+56*scale), (x+22*scale, y+53*scale)])

    # right arm gleam - change LIGHTSILVER to PASTEL_YELLOW
    pygame.draw.polygon(screen, PASTEL_YELLOW, [(x+86*scale, y+82*scale), (x+89.5340231231758*scale, y+85.1891057719905*scale), (x+94.0254091521598*scale, y+87.6205327951999*scale), (x+100*scale, y+88*scale), (x+107.1956388612105*scale, y+84.3786300975874*scale), (x+117.6693250284861*scale, y+84.5056419252322*scale), (x+118.2994929394708*scale, y+79.6678436141075*scale), (x+116.7271940332902*scale, y+76.7943318200531*scale), (x+111.4139080744727*scale, y+73.1075619710778*scale), (x+97.2632179188466*scale, y+71.5352630648971*scale), (x+92.871624422273*scale, y+72.7822587491094*scale), (x+88.967985758652*scale, y+75.2762501175339*scale), (x+86.6908632048731*scale, y+78.7461511518636*scale)])

    # left arm gleam - change LIGHTSILVER to PASTEL_YELLOW
    pygame.draw.polygon(screen, PASTEL_YELLOW, [(x+6*scale, y+78*scale), (x+7.5800193439241*scale, y+82.9529550830457*scale), (x+7.4974172006182*scale, y+89.0930477354531*scale), (x+7.5266667769288*scale, y+90.2694261372661*scale), (x+5.111368713243*scale, y+89.3604429950187*scale), (x+2.7220415964784*scale, y+87.2308253474677*scale), (x+2.1247098172873*scale, y+84.9194110714673*scale), (x+0.8001915242983*scale, y+84.0623698230626*scale), (x+0.6113602796143*scale, y+82.6075998611618*scale), (x+1.2181418573158*scale, y+81.0906459169081*scale), (x+2.4923831704889*scale, y+79.4826747359992*scale), (x+4*scale, y+78*scale)])

# Add a randomized sun
def draw_sun():
    sunx = random.randint(550, 700)
    suny = random.randint(80, 100)
    pygame.draw.circle(screen, YELLOW, (sunx, suny), 40)
    pygame.draw.polygon(screen, YELLOW, [(sunx, suny-50), (sunx+10, suny-70), (sunx-10, suny-70)])
    pygame.draw.polygon(screen, YELLOW, [(sunx+50, suny), (sunx+70, suny-10), (sunx+70, suny+10)])
    pygame.draw.polygon(screen, YELLOW, [(sunx, suny+50), (sunx+10, suny+70), (sunx-10, suny+70)])
    pygame.draw.polygon(screen, YELLOW, [(sunx-50, suny), (sunx-70, suny-10), (sunx-70, suny+10)])

    pygame.draw.polygon(screen, YELLOW, [(sunx+38, suny-30), (sunx+50, suny-50), (sunx+60, suny-30)])
    pygame.draw.polygon(screen, YELLOW, [(sunx-38, suny+30), (sunx-50, suny+50), (sunx-60, suny+30)])

    pygame.draw.polygon(screen, YELLOW, [(sunx+38, suny+30), (sunx+50, suny+50), (sunx+60, suny+30)])
    pygame.draw.polygon(screen, YELLOW, [(sunx-38, suny-30), (sunx-50, suny-50), (sunx-60, suny-30)])

# Function to draw the grass shapes
def draw_grass(x, y, scale): 
    pygame.draw.polygon(screen, BLACK, [(x+2.4989124401772*scale, y+2.286680913521*scale), (x+2.5859317156191*scale, y+1.8419157279289*scale), (x+2.8373207335625*scale, y+1.4454945842489*scale), (x+2.5472564820894*scale, y+1.580857901603*scale), (x+2.3828867395879*scale, y+1.7935716860167*scale), (x+2.4486629301395*scale, y+1.4610995311108*scale), (x+2.6129924930219*scale, y+1.1697880332736*scale), (x+2.3926414882477*scale, y+1.2631571030932*scale), (x+2.232046688158*scale, y+1.4685690566963*scale), (x+2.2992724184281*scale, y+1.0278670471478*scale), (x+2.508419134824*scale, y+0.7066774469684*scale), (x+2.2955376556353*scale, y+0.8149855679591*scale), (x+2.1498819067167*scale, y+1.0091932331839*scale), (x+2.0453085485188*scale, y+1.2071356612015*scale), (x+2.1200038043745*scale, y+0.9232936889499*scale), (x+2.265659553293*scale, y+0.7029426841756*scale), (x+2.0677171252755*scale, y+0.8336593819231*scale), (x+1.9108570879785*scale, y+1.042806098319*scale), (x+1.7913446786095*scale, y+1.3341175961561*scale), (x+1.8249575437445*scale, y+1.1025623030035*scale), (x+1.955674241492*scale, y+0.8187203307519*scale), (x+1.7054451343754*scale, y+1.0913580146252*scale), (x+1.6*scale, y+1.4*scale), (x+1.5187069947362*scale, y+1.8009629452541*scale), (x+1.4514812644661*scale, y+1.1100318285891*scale), (x+1.5037679435651*scale, y+0.7739031772385*scale), (x+1.3693164830249*scale, y+0.9606413168777*scale), (x+1.3394383806826*scale, y+1.4386909543541*scale), (x+1.2124564457279*scale, y+0.8784765354365*scale), (x+1.2087216829351*scale, y+1.371465224084*scale), (x+1.089209273566*scale, y+1.786023894083*scale), (x+0.9833577083121*scale, y+1.2270921490473*scale), (x+0.62487540562*scale, y+0.9025203344477*scale), (x+0.8354548669633*scale, y+1.1934373085644*scale), (x+0.8961593103599*scale, y+1.4693099211366*scale), (x+0.5764091052231*scale, y+1.0315337074768*scale), (x+0.2131051930682*scale, y+0.8395437137045*scale), (x+0.5699329611796*scale, y+1.1481043002599*scale), (x+0.7072294481303*scale, y+1.4886873429037*scale), (x+0.4436481523312*scale, y+1.290579469217*scale), (x+0.1113737287907*scale, y+1.2513139262563*scale), (x+0.511647664788*scale, y+1.5561013750007*scale), (x+0.7875333564857*scale, y+2.2673432967561*scale)], 2)
    pygame.draw.polygon(screen, GRASSGREEN, [(x+0.8*scale, y+2*scale), (x+2.5*scale, y+2*scale),(x+2.5*scale, y+3*scale), (x+0.8*scale, y+3*scale)])

# helper function to draw the leaves of the trees
def random_tree_leaf(x, y, scale):
    pygame.draw.circle(screen, random.choice([TREE1, TREE2, TREE3, TREE4, TREE5]), (x,y), random.randint(7, 10)*scale)

# Function to draw the trees
def draw_tree(x, y, scale):
    pygame.draw.polygon(screen, BROWN, [(x+63.56356493871*scale, y+121.5732855925662*scale), (x+71.171810972502*scale, y+101.8967872293109*scale), (x+55.2994356261428*scale, y+81.9579355545456*scale), (x+46.1170697232904*scale, y+78.1538125376495*scale), (x+49.3964861171663*scale, y+76.8420459800992*scale), (x+54*scale, y+78*scale), (x+55.19419044548*scale, y+77.433420481505*scale), (x+55.5617889376529*scale, y+74.0873362092434*scale), (x+57.4296654638008*scale, y+74.1005304541903*scale), (x+61.2502954951127*scale, y+81.9856605188129*scale), (x+71.4521905787223*scale, y+90.6024005894314*scale), (x+71.2489655770568*scale, y+85.074680544129*scale), (x+65.3147955284233*scale, y+77.8805154851691*scale), (x+66.4122105374172*scale, y+77.9618054858354*scale), (x+70.8018705733926*scale, y+81.9043705181467*scale), (x+69.6231655637325*scale, y+76.1327804708456*scale), (x+74.5412106040383*scale, y+76.4579404735104*scale), (x+76.0857206166964*scale, y+82.3108205214777*scale), (x+81.9242636924999*scale, y+78.1841729595595*scale), (x+83.8655490873202*scale, y+75.6657486635764*scale), (x+86.908645111633*scale, y+74.6688723797498*scale), (x+77.0448166190328*scale, y+85.4771099833437*scale), (x+76.8349479277009*scale, y+89.831885328481*scale), (x+88.6925289879543*scale, y+81.3846705023712*scale), (x+92.6275669504277*scale, y+75.4034127994115*scale), (x+93.7818447527533*scale, y+75.4558799722445*scale), (x+91.4732891481022*scale, y+82.5389483046968*scale), (x+91.8771393675921*scale, y+83.2249408473729*scale), (x+96.5101377400682*scale, y+81.3846705023712*scale), (x+97.7168827152268*scale, y+82.119210922033*scale), (x+91.0537831743282*scale, y+84.6004482378665*scale), (x+82.6642058613663*scale, y+89.3112158706702*scale), (x+78.0011593736455*scale, y+96.5224018494031*scale), (x+76.0253472354382*scale, y+108.3244433613076*scale), (x+76.5500538584584*scale, y+116.7197493296299*scale), (x+79.6982935965792*scale, y+122.4915221828514*scale), (x+71.8276942512771*scale, y+123.9344653961568*scale)])
    pygame.draw.polygon(screen, BLACK, [(x+63.56356493871*scale, y+121.5732855925662*scale), (x+71.171810972502*scale, y+101.8967872293109*scale), (x+55.2994356261428*scale, y+81.9579355545456*scale), (x+46.1170697232904*scale, y+78.1538125376495*scale), (x+49.3964861171663*scale, y+76.8420459800992*scale), (x+54*scale, y+78*scale), (x+55.19419044548*scale, y+77.433420481505*scale), (x+55.5617889376529*scale, y+74.0873362092434*scale), (x+57.4296654638008*scale, y+74.1005304541903*scale), (x+61.2502954951127*scale, y+81.9856605188129*scale), (x+71.4521905787223*scale, y+90.6024005894314*scale), (x+71.2489655770568*scale, y+85.074680544129*scale), (x+65.3147955284233*scale, y+77.8805154851691*scale), (x+66.4122105374172*scale, y+77.9618054858354*scale), (x+70.8018705733926*scale, y+81.9043705181467*scale), (x+69.6231655637325*scale, y+76.1327804708456*scale), (x+74.5412106040383*scale, y+76.4579404735104*scale), (x+76.0857206166964*scale, y+82.3108205214777*scale), (x+81.9242636924999*scale, y+78.1841729595595*scale), (x+83.8655490873202*scale, y+75.6657486635764*scale), (x+86.908645111633*scale, y+74.6688723797498*scale), (x+77.0448166190328*scale, y+85.4771099833437*scale), (x+76.8349479277009*scale, y+89.831885328481*scale), (x+88.6925289879543*scale, y+81.3846705023712*scale), (x+92.6275669504277*scale, y+75.4034127994115*scale), (x+93.7818447527533*scale, y+75.4558799722445*scale), (x+91.4732891481022*scale, y+82.5389483046968*scale), (x+91.8771393675921*scale, y+83.2249408473729*scale), (x+96.5101377400682*scale, y+81.3846705023712*scale), (x+97.7168827152268*scale, y+82.119210922033*scale), (x+91.0537831743282*scale, y+84.6004482378665*scale), (x+82.6642058613663*scale, y+89.3112158706702*scale), (x+78.0011593736455*scale, y+96.5224018494031*scale), (x+76.0253472354382*scale, y+108.3244433613076*scale), (x+76.5500538584584*scale, y+116.7197493296299*scale), (x+79.6982935965792*scale, y+122.4915221828514*scale), (x+71.8276942512771*scale, y+123.9344653961568*scale)], 2)
    
    # using helper function to draw the tree leaves on the top of the tree
    random_tree_leaf(x+36.3997447714691*scale, y+76.65659562826*scale, scale=scale)
    random_tree_leaf(x+29*scale, y+69*scale, scale=scale)
    random_tree_leaf(x+45*scale, y+72*scale, scale=scale)
    random_tree_leaf(x+55*scale, y+68*scale, scale=scale)
    random_tree_leaf(x+65*scale, y+72*scale, scale=scale)
    random_tree_leaf(x+76*scale, y+71*scale, scale=scale)
    random_tree_leaf(x+83*scale, y+69*scale, scale=scale)
    random_tree_leaf(x+99*scale, y+77*scale, scale=scale)
    random_tree_leaf(x+110*scale, y+76*scale, scale=scale)
    random_tree_leaf(x+91*scale, y+70*scale, scale=scale)
    random_tree_leaf(x+98*scale, y+69*scale, scale=scale)
    random_tree_leaf(x+104*scale, y+64*scale, scale=scale)
    random_tree_leaf(x+112*scale, y+66*scale, scale=scale)
    random_tree_leaf(x+116*scale, y+70*scale, scale=scale)
    random_tree_leaf(x+39*scale, y+63*scale, scale=scale)
    random_tree_leaf(x+34*scale, y+59*scale, scale=scale)
    random_tree_leaf(x+50*scale, y+60*scale, scale=scale)
    random_tree_leaf(x+43*scale, y+52*scale, scale=scale)
    random_tree_leaf(x+43*scale, y+46*scale, scale=scale)
    random_tree_leaf(x+66*scale, y+62*scale, scale=scale)
    random_tree_leaf(x+71*scale, y+54*scale, scale=scale)
    random_tree_leaf(x+77*scale, y+62*scale, scale=scale)
    random_tree_leaf(x+82*scale, y+53*scale, scale=scale)
    random_tree_leaf(x+85*scale, y+60*scale, scale=scale)
    random_tree_leaf(x+58*scale, y+42*scale, scale=scale)
    random_tree_leaf(x+44*scale, y+35*scale, scale=scale)
    random_tree_leaf(x+52*scale, y+48*scale, scale=scale)
    random_tree_leaf(x+60*scale, y+50*scale, scale=scale)
    random_tree_leaf(x+58*scale, y+58*scale, scale=scale)
    random_tree_leaf(x+56*scale, y+33*scale, scale=scale)
    random_tree_leaf(x+66*scale, y+39*scale, scale=scale)
    random_tree_leaf(x+71*scale, y+27*scale, scale=scale)
    random_tree_leaf(x+67*scale, y+33*scale, scale=scale)
    random_tree_leaf(x+71*scale, y+46*scale, scale=scale)
    random_tree_leaf(x+81*scale, y+46*scale, scale=scale)
    random_tree_leaf(x+80*scale, y+30*scale, scale=scale)
    random_tree_leaf(x+80*scale, y+38*scale, scale=scale)
    random_tree_leaf(x+74*scale, y+36*scale, scale=scale)
    random_tree_leaf(x+98*scale, y+33*scale, scale=scale)
    random_tree_leaf(x+88*scale, y+31*scale, scale=scale)
    random_tree_leaf(x+96*scale, y+37*scale, scale=scale)
    random_tree_leaf(x+88*scale, y+45*scale, scale=scale)
    random_tree_leaf(x+90*scale, y+40*scale, scale=scale)
    random_tree_leaf(x+95*scale, y+50*scale, scale=scale)
    random_tree_leaf(x+94*scale, y+56*scale, scale=scale)
    random_tree_leaf(x+108*scale, y+53*scale, scale=scale)
    random_tree_leaf(x+108*scale, y+42*scale, scale=scale)
    random_tree_leaf(x+99*scale, y+43*scale, scale=scale)
    random_tree_leaf(x+104*scale, y+58*scale, scale=scale)
    random_tree_leaf(x+113*scale, y+61*scale, scale=scale)
    random_tree_leaf(x+108*scale, y+69*scale, scale=scale)

# Function to draw the bushes
def draw_bush(x,y,scale, color):
    pygame.draw.polygon(screen, color, [(x+4.1981345727697*scale, y+12.5953185732367*scale), (x+3.401314524694*scale, y+12.2920016732171*scale), (x+2.4779552627364*scale, y+11.4579997591908*scale), (x+1.9715969577919*scale, y+10.5942120625208*scale), (x+1.8822396098605*scale, y+9.3729949741252*scale), (x+2.4183836974488*scale, y+7.7943484940041*scale), (x+3.2225998288312*scale, y+7.1986328411282*scale), (x+4.562960047802*scale, y+7.1986328411282*scale), (x+5.442225069294*scale, y+7.9801441506464*scale), (x+5.426747744472*scale, y+6.6922745361837*scale), (x+6*scale, y+6*scale), (x+7.0053942245932*scale, y+5.7987010568699*scale), (x+7.8100102078403*scale, y+6.2544702361126*scale), (x+7.9585392691946*scale, y+4.9944849254874*scale), (x+8.5542549220705*scale, y+4.041339880886*scale), (x+9.7456862278223*scale, y+3.3562668800787*scale), (x+11.2051895773682*scale, y+3.2966953147911*scale), (x+12.5753355789828*scale, y+4.0115540982422*scale), (x+13.6692751269549*scale, y+5.7327548666024*scale), (x+15.1071271037053*scale, y+5.2327711866378*scale), (x+16.2092010615257*scale, y+5.4114858825005*scale), (x+17.2814892367023*scale, y+6.1561304485954*scale), (x+17.8474191069344*scale, y+7.079489710553*scale), (x+17.9543157490172*scale, y+9.4174970777327*scale), (x+18.9792788473986*scale, y+9.2240660609062*scale), (x+19.7537091961373*scale, y+9.6112812352756*scale), (x+20.4089964143008*scale, y+10.564426279877*scale), (x+20*scale, y+12*scale), (x+19.2877483370648*scale, y+12.715714427739*scale), ])
    pygame.draw.polygon(screen, BLACK, [(x+4.1981345727697*scale, y+12.5953185732367*scale), (x+3.401314524694*scale, y+12.2920016732171*scale), (x+2.4779552627364*scale, y+11.4579997591908*scale), (x+1.9715969577919*scale, y+10.5942120625208*scale), (x+1.8822396098605*scale, y+9.3729949741252*scale), (x+2.4183836974488*scale, y+7.7943484940041*scale), (x+3.2225998288312*scale, y+7.1986328411282*scale), (x+4.562960047802*scale, y+7.1986328411282*scale), (x+5.442225069294*scale, y+7.9801441506464*scale), (x+5.426747744472*scale, y+6.6922745361837*scale), (x+6*scale, y+6*scale), (x+7.0053942245932*scale, y+5.7987010568699*scale), (x+7.8100102078403*scale, y+6.2544702361126*scale), (x+7.9585392691946*scale, y+4.9944849254874*scale), (x+8.5542549220705*scale, y+4.041339880886*scale), (x+9.7456862278223*scale, y+3.3562668800787*scale), (x+11.2051895773682*scale, y+3.2966953147911*scale), (x+12.5753355789828*scale, y+4.0115540982422*scale), (x+13.6692751269549*scale, y+5.7327548666024*scale), (x+15.1071271037053*scale, y+5.2327711866378*scale), (x+16.2092010615257*scale, y+5.4114858825005*scale), (x+17.2814892367023*scale, y+6.1561304485954*scale), (x+17.8474191069344*scale, y+7.079489710553*scale), (x+17.9543157490172*scale, y+9.4174970777327*scale), (x+18.9792788473986*scale, y+9.2240660609062*scale), (x+19.7537091961373*scale, y+9.6112812352756*scale), (x+20.4089964143008*scale, y+10.564426279877*scale), (x+20*scale, y+12*scale), (x+19.2877483370648*scale, y+12.715714427739*scale), ], 2)

# Function to draw the flowers
def draw_flower(x, y, scale, type):
    if type == 1:
        # draw type 1 flower
        # Draw filled petals
        color = random.choice([RED, PINK, PASTEL_LAVENDER, PASTEL_CYAN])
        pygame.draw.circle(screen, color, (x+55+2.5*scale, y+10.84*scale), 2.5*scale) # right petal
        pygame.draw.circle(screen, color, (x+55-2.5*scale, y+10.84*scale), 2.5*scale) # left petal
        pygame.draw.circle(screen, color, (x+55, y+8.33*scale), 2.5*scale) # top petal
        pygame.draw.circle(screen, color, (x+55, y+13.34*scale), 2.5*scale) # bottom petal
        pygame.draw.circle(screen, YELLOW, (x+55, y+10.84*scale), 2.5*scale) # inner circle 
    elif type == 2:
        # draw tulip-like flower
        color = random.choice([PASTEL_LILAC, PASTEL_YELLOW, PASTEL_PINK])
        # pygame.draw.circle(screen, color, (x, y), 15*scale) # inner circle
        pygame.draw.polygon(screen, color, [(x+7.7*scale, y+3.8*scale), (x+9.4*scale, y+7.1*scale), (x+12.3*scale, y+5*scale), (x+11.9*scale, y+6.4*scale), (x+11.8*scale, y+7.9*scale), (x+12*scale, y+10*scale), (x+11*scale, y+12.7*scale), (x+9.8*scale, y+13.8*scale), (x+8.5*scale, y+14.3*scale), (x+7.2*scale, y+14.3*scale), (x+6*scale, y+14*scale), (x+4.8*scale, y+13*scale), (x+4*scale, y+12*scale), (x+3.8*scale, y+11*scale), (x+3.6*scale, y+8.6*scale), (x+3.7*scale, y+6.5*scale), (x+3.2*scale, y+5*scale), (x+6.2*scale, y+7.1*scale)])
        pygame.draw.polygon(screen, BLACK, [(x+7.7*scale, y+3.8*scale), (x+9.4*scale, y+7.1*scale), (x+12.3*scale, y+5*scale), (x+11.9*scale, y+6.4*scale), (x+11.8*scale, y+7.9*scale), (x+12*scale, y+10*scale), (x+11*scale, y+12.7*scale), (x+9.8*scale, y+13.8*scale), (x+8.5*scale, y+14.3*scale), (x+7.2*scale, y+14.3*scale), (x+6*scale, y+14*scale), (x+4.8*scale, y+13*scale), (x+4*scale, y+12*scale), (x+3.8*scale, y+11*scale), (x+3.6*scale, y+8.6*scale), (x+3.7*scale, y+6.5*scale), (x+3.2*scale, y+5*scale), (x+6.2*scale, y+7.1*scale)], 1)
    elif type == 3:
        # draw daffodil-like flower
        pygame.draw.polygon(screen, random.choice([PASTEL_BLUE, PASTEL_CYAN, PASTEL_YELLOW, PASTEL_LAVENDER, PASTEL_LILAC]), [(x+6*scale, y+1.7*scale), (x+7*scale, y+4.3*scale), (x+10*scale, y+4.7*scale), (x+8.8*scale, y+5.9*scale), (x+7.4*scale, y+6.6*scale), (x+8.2*scale, y+8.2*scale), (x+8*scale, y+10*scale), (x+7*scale, y+9.2*scale), (x+5.8*scale, y+8.3*scale), (x+5.5*scale, y+7.7*scale), (x+4.4*scale, y+9.2*scale), (x+2.8*scale, y+9.9*scale), (x+3*scale, y+8*scale), (x+3.5*scale, y+6.8*scale), (x+2.2*scale, y+5.8*scale), (x+1.4*scale, y+4.7*scale), (x+2.7*scale, y+4.4*scale), (x+4*scale, y+4.5*scale), (x+4.9*scale, y+3.1*scale)])
        pygame.draw.polygon(screen, BLACK, [(x+6*scale, y+1.7*scale), (x+7*scale, y+4.3*scale), (x+10*scale, y+4.7*scale), (x+8.8*scale, y+5.9*scale), (x+7.4*scale, y+6.6*scale), (x+8.2*scale, y+8.2*scale), (x+8*scale, y+10*scale), (x+7*scale, y+9.2*scale), (x+5.8*scale, y+8.3*scale), (x+5.5*scale, y+7.7*scale), (x+4.4*scale, y+9.2*scale), (x+2.8*scale, y+9.9*scale), (x+3*scale, y+8*scale), (x+3.5*scale, y+6.8*scale), (x+2.2*scale, y+5.8*scale), (x+1.4*scale, y+4.7*scale), (x+2.7*scale, y+4.4*scale), (x+4*scale, y+4.5*scale), (x+4.9*scale, y+3.1*scale)], 1)
        # inner dot
        pygame.draw.polygon(screen, PASTEL_ORANGE, [ (x+5.3*scale, y+4.9*scale), (x+5.7*scale, y+4.7*scale), (x+6.0*scale, y+4.9*scale), (x+6.1*scale, y+5.0*scale), (x+6.4*scale, y+5.2*scale), (x+6.5*scale, y+5.5*scale), (x+6.5*scale, y+5.9*scale), (x+6.6*scale, y+6.3*scale), (x+6.0*scale, y+6.9*scale), (x+5.7*scale, y+6.9*scale), (x+5.5*scale, y+6.8*scale), (x+5.1*scale, y+6.9*scale), (x+4.7*scale, y+6.6*scale), (x+4.7*scale, y+6.2*scale), (x+4.5*scale, y+5.9*scale), (x+4.6*scale, y+5.6*scale), (x+4.8*scale, y+5.4*scale), (x+4.9*scale, y+5.0*scale) ])

# Function to draw clouds
def draw_clouds(x, y, scale):
    # pygame.draw.circle(screen, random.choice([CLOUD1, CLOUD2, CLOUD3]), (x,y), random.randint(7, 10)*scale)
    pygame.draw.circle(screen, random.choice([CLOUD1, CLOUD2, CLOUD3]), (x+54*scale, y+37*scale), random.randint(10, 15)*scale)
    pygame.draw.circle(screen, random.choice([CLOUD1, CLOUD2, CLOUD3]), (x+36*scale, y+47*scale), random.randint(10, 15)*scale)
    pygame.draw.circle(screen, random.choice([CLOUD1, CLOUD2, CLOUD3]), (x+18*scale, y+58*scale), random.randint(10, 15)*scale)
    pygame.draw.circle(screen, random.choice([CLOUD1, CLOUD2, CLOUD3]), (x+34*scale, y+67*scale), random.randint(10, 15)*scale)
    pygame.draw.circle(screen, random.choice([CLOUD1, CLOUD2, CLOUD3]), (x+43*scale, y+54*scale), random.randint(10, 15)*scale)
    pygame.draw.circle(screen, random.choice([CLOUD1, CLOUD2, CLOUD3]), (x+58*scale, y+50*scale), random.randint(10, 15)*scale)
    pygame.draw.circle(screen, random.choice([CLOUD1, CLOUD2, CLOUD3]), (x+56*scale, y+66*scale), random.randint(10, 15)*scale)
    pygame.draw.circle(screen, random.choice([CLOUD1, CLOUD2, CLOUD3]), (x+79*scale, y+42*scale), random.randint(10, 15)*scale)
    pygame.draw.circle(screen, random.choice([CLOUD1, CLOUD2, CLOUD3]), (x+75*scale, y+52*scale), random.randint(10, 15)*scale)
    pygame.draw.circle(screen, random.choice([CLOUD1, CLOUD2, CLOUD3]), (x+77*scale, y+63*scale), random.randint(10, 15)*scale)
    pygame.draw.circle(screen, random.choice([CLOUD1, CLOUD2, CLOUD3]), (x+91*scale, y+56*scale), random.randint(10, 15)*scale)

# Function to draw the moai's
def draw_moai(x, y, scale, arms):
    if arms:
        # If arms parameter is passed as True, draw the moai with arms
        pygame.draw.polygon(screen, GRAY, [(x+9.0281179391314*scale, y+64.8287732588016*scale), (x+3.8221743164618*scale, y+66.1967745063683*scale), (x+2.2900743405351*scale, y+68.6076861117406*scale), (x+1.6580315984639*scale, y+71.9858562770129*scale), (x+1.1291555392046*scale, y+89.1558968202786*scale), (x+13*scale, y+89.5154122927963*scale), (x+14*scale, y+72.9597205001119*scale), (x+10.2604989025057*scale, y+68*scale), ])
        pygame.draw.polygon(screen, GRAY, [(x+13.127988003853*scale, y+72.9597205001119*scale), (x+12.6951594602534*scale, y+89.5154122927963*scale), (x+49.7387408205621*scale, y+89.5201791367053*scale), (x+49.5613697190954*scale, y+71.6704848153251*scale), (x+45.6495510862714*scale, y+73.4059644495384*scale), (x+30.2458397766617*scale, y+76.3947442558806*scale), (x+15.5318468839003*scale, y+73.8657767274372*scale), ])
        pygame.draw.polygon(screen, GRAY, [(x+49.5613697190954*scale, y+71.6704848153251*scale), (x+49.7387408205621*scale, y+89.5201791367053*scale), (x+60*scale, y+90*scale), (x+60.2701238980608*scale, y+70.6274561829937*scale), (x+59.1761852091886*scale, y+68.2668516438485*scale), (x+57.0458835519113*scale, y+66.7123071912407*scale), (x+53.6962659495003*scale, y+66.0489680031576*scale), ])
        
        pygame.draw.polygon(screen, BLACK, [(x+9.0281179391314*scale, y+64.8287732588016*scale), (x+3.8221743164618*scale, y+66.1967745063683*scale), (x+2.2900743405351*scale, y+68.6076861117406*scale), (x+1.6580315984639*scale, y+71.9858562770129*scale), (x+1.1291555392046*scale, y+89.1558968202786*scale), (x+13*scale, y+89.5154122927963*scale), (x+14*scale, y+72.9597205001119*scale), (x+10.2604989025057*scale, y+68*scale), ], 2)
        pygame.draw.polygon(screen, BLACK, [(x+13.127988003853*scale, y+72.9597205001119*scale), (x+12.6951594602534*scale, y+89.5154122927963*scale), (x+49.7387408205621*scale, y+89.5201791367053*scale), (x+49.5613697190954*scale, y+71.6704848153251*scale), (x+45.6495510862714*scale, y+73.4059644495384*scale), (x+30.2458397766617*scale, y+76.3947442558806*scale), (x+15.5318468839003*scale, y+73.8657767274372*scale), ], 2)
        pygame.draw.polygon(screen, BLACK, [(x+49.5613697190954*scale, y+71.6704848153251*scale), (x+49.7387408205621*scale, y+89.5201791367053*scale), (x+60*scale, y+90*scale), (x+60.2701238980608*scale, y+70.6274561829937*scale), (x+59.1761852091886*scale, y+68.2668516438485*scale), (x+57.0458835519113*scale, y+66.7123071912407*scale), (x+53.6962659495003*scale, y+66.0489680031576*scale), ], 2)

    # Drawing the head of the moai
    pygame.draw.polygon(screen, GRAY, [(x+13.2327854944063*scale, y+20.5275524911761*scale), (x+22.4290310523822*scale, y+14.7798990174411*scale), (x+32.0850888882569*scale, y+12.7107437668965*scale), (x+41.0514283072834*scale, y+14.0901806005929*scale), (x+50.7074861431581*scale, y+19.6079279353785*scale), (x+53.6962659495003*scale, y+66.0489680031576*scale), (x+45.6495510862714*scale, y+73.4059644495384*scale), (x+30.2458397766617*scale, y+76.3947442558806*scale), (x+15.5318468839003*scale, y+73.8657767274372*scale), (x+8.8645688543677*scale, y+65.12934344736*scale) ])
    pygame.draw.polygon(screen, GRAY, [(x+13.2327854944063*scale, y+20.5275524911761*scale), (x+14.0718531943396*scale, y+11.7569566122905*scale), (x+19.4993975804086*scale, y+4.5202307641983*scale), (x+31.485224766311*scale, y+2.2587539366696*scale), (x+43.6971996349663*scale, y+3.6156400331868*scale), (x+49.3508917037882*scale, y+9.9477751502674*scale), (x+50.7074861431581*scale, y+19.6079279353785*scale), (x+41.0514283072834*scale, y+14.0901806005929*scale), (x+32.0850888882569*scale, y+12.7107437668965*scale), (x+22.4290310523822*scale, y+14.7798990174411*scale) ])
    # moai left ear
    pygame.draw.polygon(screen, BLACK, [(x+13.2327854944063*scale, y+20.5275524911761*scale), (x+10.3996437989598*scale, y+20.6669547229725*scale), (x+5.9052865450517*scale, y+51.0267965810056*scale), (x+10.5830869521806*scale, y+51.5771260406678*scale) ])
    # moai right ear
    pygame.draw.polygon(screen, BLACK, [(x+50.7074861431581*scale, y+19.6079279353785*scale), (x+54.3099846233044*scale, y+21.2968906008967*scale), (x+56.9007212743859*scale, y+51.5221515301814*scale), (x+52.7747332745153*scale, y+52.9614496696711*scale), ])
    # moai nose
    pygame.draw.polygon(screen, BLACK, [(x+27.0321195599917*scale, y+13.7411531588611*scale), (x+21.8614156491231*scale, y+40.5071498739461*scale), (x+41.4289814294691*scale, y+40.7099225763331*scale), (x+36.3089706941972*scale, y+13.7918463344579*scale), ], 2)
    pygame.draw.polygon(screen, BLACK, [(x+22.9259723366549*scale, y+36.6037753529962*scale), (x+27.2855854379755*scale, y+35.4378323142709*scale), (x+31.2903463101188*scale, y+34.9309005583034*scale), (x+36.0555048162134*scale, y+35.5392186654644*scale), (x+40.3137315663405*scale, y+36.7051617041897*scale), (x+41.4289814294691*scale, y+40.7099225763331*scale), (x+21.8614156491231*scale, y+40.5071498739461*scale), ])
    # moai mouth
    pygame.draw.polygon(screen, BLACK, [(x+18.602090867399*scale, y+51.5566943948494*scale), (x+24.1786161649373*scale, y+49.4750530849447*scale), (x+30.4211915037864*scale, y+48.9564922548442*scale), (x+36.1783201396212*scale, y+49.3733606783796*scale), (x+42.5554681571441*scale, y+51.7142824033346*scale), (x+36.5201262263936*scale, y+50.7866121230277*scale), (x+30.4227819341344*scale, y+50.2683378581856*scale), (x+25.2207872237759*scale, y+50.7687543524236*scale) ])
    # eye
    pygame.draw.ellipse(screen, BLACK, (x+13.2327854944063*scale, y+20.5275524911761*scale, 14*scale, 4*scale))
    pygame.draw.ellipse(screen, BLACK, (x+38*scale, y+21.8306275177138*scale, 14*scale, 4*scale))
    # outlines
    pygame.draw.polygon(screen, BLACK, [(x+13.2327854944063*scale, y+20.5275524911761*scale), (x+22.4290310523822*scale, y+14.7798990174411*scale), (x+32.0850888882569*scale, y+12.7107437668965*scale), (x+41.0514283072834*scale, y+14.0901806005929*scale), (x+50.7074861431581*scale, y+19.6079279353785*scale), (x+53.6962659495003*scale, y+66.0489680031576*scale), (x+45.6495510862714*scale, y+73.4059644495384*scale), (x+30.2458397766617*scale, y+76.3947442558806*scale), (x+15.5318468839003*scale, y+73.8657767274372*scale), (x+8.8645688543677*scale, y+65.12934344736*scale) ], 2)
    pygame.draw.polygon(screen, BLACK, [(x+13.2327854944063*scale, y+20.5275524911761*scale), (x+14.0718531943396*scale, y+11.7569566122905*scale), (x+19.4993975804086*scale, y+4.5202307641983*scale), (x+31.485224766311*scale, y+2.2587539366696*scale), (x+43.6971996349663*scale, y+3.6156400331868*scale), (x+49.3508917037882*scale, y+9.9477751502674*scale), (x+50.7074861431581*scale, y+19.6079279353785*scale), (x+41.0514283072834*scale, y+14.0901806005929*scale), (x+32.0850888882569*scale, y+12.7107437668965*scale), (x+22.4290310523822*scale, y+14.7798990174411*scale) ], 2)

# Function to draw the house
def draw_house():
    # Draw frame of the house
    pygame.draw.polygon(screen, WHITE, [(132, 559), (136, 204), (257, 30), (580, 200), (686, 267), (693, 540), (415, 588)])  
    pygame.draw.polygon(screen, BLACK, [(132, 559), (136, 204), (257, 30), (580, 200), (686, 267), (693, 540), (415, 588)], 6) # house outline # left line of the roof

    # Front face of house 
    pygame.draw.line(screen, BLACK, (415, 588), (411, 126), 6) # Line separating front and right face of house
    pygame.draw.polygon(screen, PINK, [(148, 210), (257, 56), (391, 139), (392, 558), (146, 540)]) # Face color
    pygame.draw.polygon(screen, BLACK, [(148, 210), (257, 56), (391, 139), (392, 558), (146, 540)], 5) # Face border
    pygame.draw.line(screen, BLACK, (262, 60), (155, 212), 4)
    pygame.draw.line(screen, BLACK, (155, 212), (153, 540), 3)

    # Straight lines of the side of the house
    pygame.draw.line(screen, BLACK, (243, 87), (285, 73), 3)
    pygame.draw.line(screen, BLACK, (224, 114), (305, 86), 3)
    pygame.draw.line(screen, BLACK, (203, 143), (330, 101), 3)
    pygame.draw.line(screen, BLACK, (187, 167), (352, 115), 3)
    pygame.draw.line(screen, BLACK, (170, 190), (378, 131), 3)
    pygame.draw.line(screen, BLACK, (155, 215), (391, 152), 3)
    pygame.draw.line(screen, BLACK, (154, 234), (391, 176), 3)
    pygame.draw.line(screen, BLACK, (154, 253), (391, 200), 3)
    pygame.draw.line(screen, BLACK, (154, 273), (391, 224), 3)
    pygame.draw.line(screen, BLACK, (154, 292), (391, 248), 3)
    pygame.draw.line(screen, BLACK, (153, 423), (392, 417), 3)
    pygame.draw.line(screen, BLACK, (153, 438), (392, 433), 3)
    pygame.draw.line(screen, BLACK, (152, 458), (392, 458), 3)
    pygame.draw.line(screen, BLACK, (152, 478), (392, 483), 3)
    pygame.draw.line(screen, BLACK, (152, 499), (392, 509), 3)
    pygame.draw.line(screen, BLACK, (152, 519), (392, 534), 3)

    # Windows
    # line seperating the windows
    pygame.draw.line(screen, BLACK, (262, 272), (261, 421), 2)
    # left window
    pygame.draw.polygon(screen, BLUE, [(160, 296), (257, 278), (256, 414), (159, 418)])
    pygame.draw.polygon(screen, BLACK, [(160, 296), (257, 278), (256, 414), (159, 418)], 3)  
    # window glare
    pygame.draw.line(screen,WHITE, (184, 359), (218, 309), 5)
    pygame.draw.line(screen,WHITE, (176, 390), (213, 333), 5)
    # right window
    pygame.draw.polygon(screen, DARKBLUE, [(266, 276), (391, 253), (392, 408), (266, 414)])
    pygame.draw.polygon(screen, BLACK, [(266, 276), (391, 253), (392, 408), (266, 414)], 3)  

    # Roof
    pygame.draw.line(screen, BLACK, (257, 30), (411, 126), 5) # left border
    pygame.draw.line(screen, BLACK, (411, 126), (686, 267), 5) # bottom border

    # Right side of house
    pygame.draw.polygon(screen, LIGHTPINK, [(429, 150), (429, 586), (693, 540), (687, 274)]) # right face color
    pygame.draw.polygon(screen, LIGHTBROWN, [(428, 243), (539, 281), (543, 435), (429, 427)]) # line pattern background color
    pygame.draw.line(screen, BLACK, (412, 142), (687, 274), 5) # right face top border
    pygame.draw.line(screen, BLACK, (429, 150), (429, 586), 5) # right face left border
    # line pattern on right side
    pygame.draw.line(screen, BLACK, (428, 243), (539, 281), 6)
    pygame.draw.line(screen, BLACK, (428, 253), (540, 289), 4)
    pygame.draw.line(screen, BLACK, (428, 267), (540, 301), 4)
    pygame.draw.line(screen, BLACK, (429, 293), (541, 322), 4)
    pygame.draw.line(screen, BLACK, (429, 317), (541, 342), 4)
    pygame.draw.line(screen, BLACK, (429, 343), (541, 364), 4)
    pygame.draw.line(screen, BLACK, (429, 368), (542, 384), 4)
    pygame.draw.line(screen, BLACK, (429, 393), (542, 405), 4)
    pygame.draw.line(screen, BLACK, (429, 417), (543, 426), 4)
    pygame.draw.line(screen, BLACK, (429, 427), (543, 435), 6)


    # Right window
    pygame.draw.line(screen, BLACK, (658, 329), (658, 440), 3) # window right border
    # opened window
    pygame.draw.polygon(screen, BLUE, [(620, 313), (653, 324), (758, 311), (730, 297)])
    pygame.draw.polygon(screen, LIGHTBROWN, [(605, 325), (639, 334), (640, 429), (607, 427)]) # opened window inside
    pygame.draw.polygon(screen, WHITE, [(603, 309), (730, 291), (730, 297), (605, 316)]) # top window border
    pygame.draw.polygon(screen, BLACK, [(603, 309), (730, 291), (730, 297), (605, 316)], 3)

    pygame.draw.polygon(screen, WHITE, [(766, 309), (730, 291), (730, 297), (765, 314)])  # right window border
    pygame.draw.polygon(screen, BLACK, [(766, 309), (730, 291), (730, 297), (765, 314)], 3)  # right window border
    pygame.draw.line(screen, BLACK, (765, 314), (766, 309), 3) # bottom window border
    pygame.draw.polygon(screen, WHITE, [(758, 311), (765, 314), (652, 330), (653, 324)])
    pygame.draw.polygon(screen, BLACK, [(758, 311), (765, 314), (652, 330), (653, 324)], 3)
    pygame.draw.polygon(screen, WHITE, [(605, 316), (620, 315), (653, 324), (652, 330), (605, 316)]) # left window border
    pygame.draw.line(screen, BLACK, (620, 313), (653, 324), 3)

    # right window frame (opening under opened window)
    pygame.draw.polygon(screen, WHITE, [(591, 430), (591, 437), (658, 440), (658, 435)])
    pygame.draw.polygon(screen, WHITE, [(652, 330), (657, 330), (658, 440), (652, 441)])
    pygame.draw.line(screen, BLACK, (597, 308), (603, 308), 3)
    pygame.draw.line(screen, BLACK, (597, 308), (600, 431), 3)
    # right inner window frame
    pygame.draw.polygon(screen, BLACK, [(603, 308), (605, 316), (647, 329), (647, 429), (606, 426)], 3)
    pygame.draw.line(screen, BLACK, (638, 428), (638, 334), 3)
    pygame.draw.line(screen, BLACK, (604, 325), (638, 334), 3)
    pygame.draw.line(screen, BLACK, (647, 329), (638, 334), 3)
    pygame.draw.line(screen, BLACK, (653, 434), (591, 430), 2)
    pygame.draw.line(screen, BLACK, (653, 434), (652, 330), 3)
    pygame.draw.line(screen, BLACK, (591, 437), (658, 440), 3)
    pygame.draw.line(screen, BLACK, (604, 358), (630, 311), 4) # lines holding window up
    pygame.draw.line(screen, BLACK, (673, 327), (648, 366), 4)

    # Door
    pygame.draw.polygon(screen, WHITE, [(539, 262), (589, 281), (593, 546), (540, 552)]) # frame color
    pygame.draw.polygon(screen, BLACK, [(539, 262), (589, 281), (593, 546), (540, 552)], 4)  
    pygame.draw.line(screen, BLACK, (593, 540), (545, 546), 2) # door bottom line
    pygame.draw.polygon(screen, TAN, [(585, 530), (582, 295),  (550, 285), (551, 533)]) # inner door frame
    pygame.draw.polygon(screen, BLACK, [(585, 530), (582, 295), (550, 285), (551, 533)], 4) # inner door frame border
    pygame.draw.line(screen, BLACK, (580, 531), (577, 294), 2) # door right frame vertical line
    pygame.draw.line(screen, BLACK, (558, 408), (562, 410), 2) # door knob
    pygame.draw.line(screen, BLACK, (562, 409), (562, 423), 3)
    pygame.draw.line(screen, BLACK, (558, 422), (562, 421), 2)

    # house platform
    pygame.draw.polygon(screen, LIGHTBROWN, [(165, 585), (165, 566), (382, 588), (382, 607)]) # left rect
    pygame.draw.polygon(screen, BLACK, [(165, 585), (165, 566), (382, 588), (382, 607)], 5)
    pygame.draw.polygon(screen, LIGHTBROWN, [(660, 565), (660, 549), (381, 588), (382, 607)]) # right rect
    pygame.draw.polygon(screen, BLACK, [(660, 565), (660, 549), (382, 588), (382, 607)], 5)
    pygame.draw.polygon(screen, BROWN, [(177, 585), (190, 587), (190, 638), (184, 642), (177, 642)]) # pillar 1
    pygame.draw.polygon(screen, BLACK, [(177, 585), (190, 587), (190, 638), (184, 642), (177, 642)], 4)  
    pygame.draw.line(screen, BLACK, (184, 642), (184, 586), 3)
    pygame.draw.polygon(screen, BROWN, [(416, 583), (430, 581), (432, 674), (425, 676), (417, 674)]) # pillar 2
    pygame.draw.polygon(screen, BLACK, [(416, 583), (430, 581), (432, 674), (425, 676), (417, 674)], 4)  
    pygame.draw.line(screen, BLACK, (425, 676), (425, 582), 3)
    pygame.draw.polygon(screen, BROWN, [(660, 549), (672, 547), (673, 590), (668, 595), (661, 595)]) # pillar 3
    pygame.draw.polygon(screen, BLACK, [(660, 549), (672, 547), (673, 590), (668, 595), (661, 595)], 3)  
    pygame.draw.line(screen, BLACK, (667, 548), (668, 596), 3)

    #Wheels
    pygame.draw.polygon(screen, BLACK, [(567, 563), (561, 576), (558, 594), (561, 610), (567, 622), (589, 621), (582, 606), (581, 592), (582, 575), (592, 560)])
    pygame.draw.polygon(screen, BLACK, [(631, 551), (628, 555), (624, 563), (622, 570), (621, 580), (622, 587), (623, 594), (625, 602), (628, 608), (634, 614), (615, 613), (611, 614), (609, 611), (610, 604), (611, 598), (611, 588), (610, 579), (608, 572), (604, 565), (604, 560), (604, 556)])
    pygame.draw.ellipse(screen, SILVER, (580, 562.53, 33, 60))  #Left wheel
    pygame.draw.ellipse(screen, BLACK, (583, 571.03, 20, 46))
    pygame.draw.ellipse(screen, SILVER, (618, 553.53, 33, 60))  #Right wheel
    pygame.draw.ellipse(screen, BLACK, (621, 562.03, 20, 46))

    # draw moais, one of them is behind window, so need to draw window shine after moai
    draw_moai(random.randint(700, 900), 440, 1, True)
    draw_moai(280, 298, 1.5, False) # put moai behind window
    pygame.draw.line(screen,WHITE, (308, 329), (338, 286), 5) # window shine
    pygame.draw.line(screen,WHITE, (295, 370), (345, 299), 5)

# Function to draw the egg
def draw_egg(x, y, scale, color):
    # Base dimensions
    base_width = 50 * scale
    base_height = 60 * scale
    base_side_width = 30 * scale
    base_side_height = 50 * scale

    # black outline
    pygame.draw.ellipse(screen, BLACK, (x - 2.5*scale, y - 3*scale, 55*scale, 65*scale))
    pygame.draw.ellipse(screen, BLACK, (x + 7.5*scale, y - 26.5*scale, 35*scale, 52.5*scale))
    
    # black outline polygon
    pygame.draw.polygon(screen, BLACK, [(x + 4.2*scale, y + 20*scale), (x + 9*scale, y - 1.5*scale), (x + 16*scale, y - 15*scale), (x + 34.5*scale, y - 15*scale), (x + 39.5*scale, y - 5*scale), (x + 44.5*scale, y + 16*scale)], int(11*scale))

    # egg shape
    pygame.draw.ellipse(screen, color, (x, y, base_width, base_height))
    pygame.draw.ellipse(screen, color, (x + 10*scale, y - 25*scale, base_side_width, base_side_height))

    # polygon outline
    pygame.draw.polygon(screen, color, [(x + 4.2*scale, y + 20*scale), (x + 9*scale, y - 1.5*scale), (x + 16*scale, y - 15*scale), (x + 34.5*scale, y - 15*scale), (x + 39.5*scale, y - 5*scale), (x + 44.5*scale, y + 16*scale)], int(6*scale))
    
    # Patterns 
    pygame.draw.arc(screen, WHITE, (x + 5*scale, y - 10*scale, 20*scale, 20*scale), math.pi, math.pi*2, int(2*scale))
    pygame.draw.arc(screen, WHITE, (x + 23.5*scale, y - 10*scale, 20*scale, 20*scale), math.pi, math.pi*2, int(2*scale))
    pygame.draw.arc(screen, WHITE, (x + 15*scale, y - 22.5*scale, 20*scale, 20*scale), math.pi, math.pi*2, int(2*scale)) # top arc
    pygame.draw.arc(screen, YELLOW, (x + 1*scale, y + 5*scale, 48*scale, 20*scale), math.pi, math.pi*2, int(5*scale)) # bottom arc
    pygame.draw.arc(screen, YELLOW, (x + 1*scale, y + 25*scale, 48*scale, 20*scale), math.pi, math.pi*2, int(5*scale)) # bottom arc
    
    # circle patterns
    pygame.draw.circle(screen, BLUE, (int(x + 10*scale), int(y + 30*scale)), int(5*scale))
    pygame.draw.circle(screen, BLUE, (int(x + 25*scale), int(y + 32.5*scale)), int(5*scale))
    pygame.draw.circle(screen, BLUE, (int(x + 40*scale), int(y + 30*scale)), int(5*scale))

# Function to draw the house, the decorations, grass, sky, etc.
def draw_everything():
    # Fill background with sky color
    screen.fill(SKYBLUE)
    
    # Draw the ground
    pygame.draw.rect(screen, GRASSGREEN, (0,500,1000,294)) # ground color & ground grass
    draw_sun() # call the  function to draw the sun

    # calling the function to draw the blades of grass
    draw_grass(random.randint(730, 780), random.randint(550, 650), 20) # right side
    draw_grass(random.randint(800, 850), random.randint(550, 650), 20)
    draw_grass(random.randint(870, 930), random.randint(550, 650), 20)
    draw_grass(random.randint(200, 330), random.randint(600, 650), 20) # left side grass
    draw_grass(random.randint(10, 70), random.randint(500, 650), 20) 

    # Call functions to draw trees
    draw_tree(random.randint(600, 840), 220, 2)
    draw_tree(random.randint(-150, -80), 200, 2.4)

    # Call function to draw bushes
    random1 = random.randint(7, 9)
    draw_bush(650, 465-(8*random1), random1, random.choice([BUSH1, BUSH2, BUSH3, BUSH4, BUSH5]))
    random3 = random.randint(7, 9)
    draw_bush(880, 465-(8*random3), random3, random.choice([BUSH1, BUSH2, BUSH3, BUSH4, BUSH5]))
    random2 = random.randint(7, 9)
    draw_bush(760, 465-(8*random2), random2, random.choice([BUSH1, BUSH2, BUSH3, BUSH4, BUSH5]))
    # left side of screen
    random4 = random.randint(7, 9)
    draw_bush(-50, 465-(8*random4), random4, random.choice([BUSH1, BUSH2, BUSH3, BUSH4, BUSH5]))
    random5 = random.randint(7, 9)
    draw_bush(30, 465-(8*random5), random5, random.choice([BUSH1, BUSH2, BUSH3, BUSH4, BUSH5]))

    # Call function to draw clouds
    draw_clouds(random.randint(650, 800), random.randint(40, 100), 2)
    draw_clouds(random.randint(0,100), random.randint(-30, 100), 2)

    # Call function to draw the entire house
    draw_house() 

    # Function to draw the eggs on the grass
    draw_egg(random.randint(700, 750), random.randint(550, 650), random.uniform(0.5, 0.8), random.choice([PINK, BLUE, SKYBLUE]))
    draw_egg(random.randint(766, 820), random.randint(550, 650), random.uniform(0.5, 0.8), random.choice([PINK, BLUE, SKYBLUE]))
    draw_egg(random.randint(832, 900), random.randint(550, 650), random.uniform(0.5, 0.8), random.choice([PINK, BLUE, SKYBLUE]))
    
    # Calling the function to draw all of the flowers
    draw_flower(random.randint(400, 600), random.randint(600, 620), 5, random.randint(1,3))
    draw_flower(random.randint(0, 50), random.randint(450, 500), 5, random.randint(1,3))
    draw_flower(random.randint(0, 50), random.randint(520, 600), 5, random.randint(1,3))


# Function to draw the hank bubble popping
def water(x, y, scale):
    # draw a bunch of water droplets
    color = GREEN
    pygame.draw.line(screen, color, (x + 5.7704125510555*scale, y + 7.2265192606305*scale), (x + 20*scale, y + 20*scale), 5)
    pygame.draw.arc(screen, color, (x+18*scale, y+2*scale, 8*scale, 20*scale), math.pi/4, math.pi, 4)
    pygame.draw.line(screen, color, (x + 28*scale, y + 1*scale), (x + 29*scale, y + 16*scale), 6)
    pygame.draw.line(screen, color, (x + 36*scale, y + 18*scale), (x + 36*scale, y + 19*scale), 5)
    pygame.draw.line(screen, color, (x + 36*scale, y + 11 * scale), (x + 37*scale, y + 4*scale), 5)
    pygame.draw.polygon(screen, color, [(x + 42 * scale, y + 18 * scale), (x + 45 * scale, y + 15 * scale), (x + 52 * scale, y + 9 * scale), (x + 53 * scale, y + 6 * scale), (x + 48 * scale, y + 9 * scale), (x + 45 * scale, y + 12 * scale)], 3)
    pygame.draw.polygon(screen, color, [(x + 42 * scale, y + 23 * scale), (x + 52 * scale, y + 18 * scale), (x + 49 * scale, y + 18 * scale), (x + 46 * scale, y + 20 * scale)], 3)
    pygame.draw.arc(screen, color, (x+35*scale, y+25*scale, 20*scale, 5*scale), 3*math.pi/2, math.pi/2, 2)
    pygame.draw.line(screen, color, (x + 45 * scale, y + 39 * scale), (x + 60 * scale, y + 55 * scale), 5)
    pygame.draw.line(screen, color, (x + 36 * scale, y + 40 * scale), (x + 43 * scale, y + 51 * scale), 5)
    pygame.draw.line(screen, color, (x + 30 * scale, y + 43 * scale), (x + 30 * scale, y + 56 * scale), 5)
    pygame.draw.line(screen, color, (x + 26 * scale, y + 43 * scale), (x + 25 * scale, y + 46 * scale), 2)
    pygame.draw.polygon(screen, color, [(x + 20 * scale, y + 42 * scale), (x + 11 * scale, y + 53 * scale), (x + 9 * scale, y + 53 * scale), (x + 10 * scale, y + 51 * scale), (x + 19 * scale, y + 42 * scale)], 3)
    pygame.draw.polygon(screen, color, [(x + 18 * scale, y + 33 * scale), (x + 13 * scale, y + 37 * scale), (x + 19 * scale, y + 35 * scale)], 3)
    pygame.draw.arc(screen, color, (x+10*scale, y+25*scale, 20*scale, 6*scale), math.pi/2, 3*math.pi/2, 2)

# Function to draw the hank bubble popping and falling
def water_fall(x, y, scale):
    # draw a bunch of water droplets falling
    color = GREEN
    pygame.draw.line(screen, color, (x + 12*scale, y + 24*scale), (x + 20*scale, y + 20*scale), 10)
    pygame.draw.arc(screen, color, (x+25*scale, y-10*scale, 10*scale, 20*scale), math.pi/2, 7*math.pi/4, 5)
    pygame.draw.line(screen, color, (x + 50*scale, y - 10*scale), (x + 54*scale, y + 3*scale), 8)
    pygame.draw.line(screen, color, (x + 70*scale, y + 10 * scale), (x + 80*scale, y - 8*scale), 7)
    pygame.draw.line(screen, color, (x + 80*scale, y + 16*scale), (x + 80*scale, y + 18*scale), 7)
    pygame.draw.polygon(screen, color, [(x + 92 * scale, y + 24 * scale), (x + 96 * scale, y + 20 * scale), (x + 106 * scale, y + 12 * scale), (x + 108 * scale, y + 8 * scale), (x + 102 * scale, y + 14 * scale), (x + 98 * scale, y + 18 * scale)], 3)
    pygame.draw.polygon(screen, color, [(x + 92 * scale, y + 34 * scale), (x + 108 * scale, y + 25 * scale), (x + 104 * scale, y + 26 * scale), (x + 100 * scale, y + 30 * scale)], 2)
    pygame.draw.arc(screen, color, (x+100*scale, y+60*scale, 20*scale, 10*scale), 3*math.pi/2, math.pi/4, 2)
    pygame.draw.line(screen, color, (x + 110 * scale, y + 90 * scale), (x + 120 * scale, y + 110 * scale), 6)
    pygame.draw.line(screen, color, (x + 79 * scale, y + 100 * scale), (x + 86 * scale, y + 112 * scale), 6)
    pygame.draw.line(screen, color, (x + 60 * scale, y + 108 * scale), (x + 60 * scale, y + 120 * scale), 6)
    pygame.draw.line(screen, color, (x + 40 * scale, y + 110 * scale), (x + 42 * scale, y + 120 * scale), 2)
    pygame.draw.polygon(screen, color, [(x + 30 * scale, y + 94 * scale), (x + 16 * scale, y + 110 * scale), (x + 13 * scale, y + 110 * scale), (x + 15 * scale, y + 107 * scale), (x + 28 * scale, y + 94 * scale)], 3)
    pygame.draw.polygon(screen, color, [(x + 26 * scale, y + 76 * scale), (x + 19 * scale, y + 82 * scale), (x + 28 * scale, y + 79 * scale)], 3)
    pygame.draw.arc(screen, color, (x, y+50*scale, 25*scale, 8*scale), math.pi/2, 3*math.pi/2, 2)

draw_everything() # draw everything initially

# Ending code & hank animation 
pygame.display.flip()
running = True
hank_ran = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and hank_ran:
            hank(230, 570, 1) # draws hank
            pygame.display.flip() # updates the screen so hank shows
            # draw a bubble getting progressively bigger
            time.sleep(0.8)
            pygame.draw.circle(screen, SKYBLUE, (220, 648), 25)
            pygame.display.flip()
            
            # draw a bigger circle
            time.sleep(0.8)
            pygame.draw.circle(screen, SKYBLUE, (190, 648), 50)
            pygame.display.flip()

            # draw a even bigger circle
            time.sleep(0.8)
            pygame.draw.circle(screen, SKYBLUE, (130, 648), 100)
            pygame.display.flip()

            # draw water popping animation            
            time.sleep(0.5)
            water(70, 600, 1.5)
            pygame.display.flip()
            time.sleep(0.8)
            water_fall(40, 570, 1.5)
            pygame.display.flip()
            time.sleep(0.3)

            # remove all bubbles by redrawing everything
            draw_everything()
            hank(230, 570, 1) # draw hank again after redrawing everything
            pygame.display.flip() # update the display to show everything
            hank_ran = False # change this variable to false so that you can't click the screen again for the animation

pygame.quit()