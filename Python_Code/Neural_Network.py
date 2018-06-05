# -*- coding: utf-8 -*-

import numpy as np

def nonlin(x, deriv = False):
    if (deriv == True):
        return x * (1 - x)
    return 1/(1+np.exp(-x))

np.random.seed(1)
X = np.array([[1.8818090457600445, 3.9351914689555136], 
[2.3204198927511026, 0.33270442688046065], 
[0.26348918383580827, 1.38990732387288], 
[0.652593786863392, 0.4572210710592267], 
[-0.052641989738790355, -0.20506642208081088], 
[-0.2854682764671757, -0.8960062362059411], 
[1.2469788350846425, -2.0453089913975084], 
[0.007126686495921792, -0.09024589788328376], 
[-0.7419148454810198, -3.246431130479695], 
[-0.08648754879609512, -0.03375384172186275], 
[1.5805204951408651, -0.0995090393112674], 
[-0.5575695422191981, -0.007494720084374167], 
[0.2754049648491419, -0.8739513690323898], 
[-0.14837093121737815, -2.1264136863376524], 
[0.44544425232076973, -0.20841179421027917], 
[-0.07783663871323739, 0.10643937108970923], 
[3.2757257800743473, 0.6539933493114438], 
[-0.13126899084938798, -0.3503443711583007], 
[-0.15078316395035135, -0.04013082342259041], 
[0.10881405360931506, -0.00585050836986074], 
[1.238189646702068, 1.017821800098277], 
[-1.3077514266753556, -0.683388432943612], 
[0.24430037578812464, -0.7239367005613953], 
[0.0069792066979089485, 0.15405077295098532], 
[2.061063342675976, -0.3971787815470596], 
[2.3392948987406657, 1.1990538465849416], 
[-2.0690481952824364, 2.0317688161857195], 
[-0.23233928890477093, 0.3042040222055505], 
[0.001169646898386908, -0.00360782571479764], 
[0.024098882023314082, -0.1004906084209649], 
[0.03378148523671738, -0.0726748903632783], 
[-3.198299741525995, -0.6617460460638862], 
[0.08585926391409703, -0.1216259577814519], 
[0.9227285717115833, 2.679344920861722], 
[-2.294519635937723, 0.6806313040719489], 
[3.9417461588266516, 1.3188572248963852], 
[2.628869700237629, -2.0352909747286967], 
[0.19943216725369783, -0.03545650932410642], 
[0.02466723722904276, 0.02108487871235954], 
[-0.2569332079563433, 0.007273651919014416], 
[0.26286182359626853, -2.269882551997534], 
[0.05837919868726895, -0.19731811679267527], 
[-0.03290498701890491, -0.010753303036818013], 
[0.27071800210051955, 1.0458041327514054], 
[0.1467811544191802, -0.5400671645790908], 
[0.3408875008669188, 1.445256048702446], 
[-3.250009189915027, -0.8126085671343319], 
[0.34771192164360887, -1.7726199368329871], 
[-0.2951396452489118, -0.44455276284869893], 
[1.7819439556767873, -0.009148615050219832], 
[-0.6212136480486427, 1.018219328876781], 
[-0.9557539326490709, 0.33509900159836514], 
[0.13864689881353437, -1.4916527012332004], 
[-0.2933900275791183, 0.22907327103653985], 
[-3.354350579523031, 0.4393388044720962], 
[-1.9208865953559073, -3.0359669986331657], 
[0.04864708138471446, -1.1272398798566345], 
[0.5471038176733075, 0.7357678715636509], 
[-0.5737117320838061, -0.3765970523069833], 
[-0.6554779560722742, -1.154819819200591], 
[-1.6113829826887707, -0.7238707234551163], 
[-0.015799969211302434, -0.04738908663130395], 
[8.151592259350337E-4, 0.3018372784597517], 
[0.7250456927908974, -1.1167205470502493], 
[3.227868900104951, 1.1873456818583754], 
[3.6514956250798387, -0.2801924691186589], 
[-0.8920963342184451, -2.6182724180585906], 
[-0.09601609075553888, -0.4081977696488057], 
[5.835847286270186, -0.5049549842806903], 
[-0.03149306108931042, 0.04199791529509487], 
[-0.46464494383072047, -0.7804940091854307], 
[0.7197875460387194, 0.5255741433033375], 
[0.58987423822519, -0.6937345912172597], 
[-2.267713729945115, -4.054297762504448], 
[-0.5788410822104064, 0.9454572832532997], 
[-0.7063321506099681, 0.11890173914491199], 
[4.5626369973947325, -1.9163110089133655], 
[-0.049277170198617055, 0.02214475917943612], 
[3.3736138012994803, 0.7888676098840808], 
[-0.22389618190931249, -1.9073726288995996], 
[-0.26135930798029244, -0.007946030286802191], 
[0.018707297967404272, -1.1953639778151401], 
[2.6183126537098507, 0.9858235726128274], 
[2.8628757315245474, -3.229921367009282], 
[-0.6098568247050694, 0.20005290894988684], 
[-0.43751838118200775, 1.2215365241327203], 
[-0.16471173218016844, -0.21617538519667429], 
[-0.007209500224337666, -0.003808638998318301], 
[0.8068633555158695, -0.7103008001089549], 
[0.11710793570742346, 0.17933782522210148], 
[2.3763529786927777, 1.5799705338774386], 
[0.28504489397905575, -1.1198016384887], 
[-0.8584905907305503, -1.1831100089999704], 
[0.11849241407688701, 0.0017841720224716434], 
[-1.9369016186133396, 0.3663878525596186], 
[0.2373222675740456, 0.27135810209648686], 
[-1.4246249614487292, 2.121112989342086], 
[-0.0298109085349309, -0.937007135932477], 
[-0.7698995814755893, -0.8319764554160505], 
[0.8224032141089451, -0.2643607967702738], 
[-1.6025625384442175, -0.7997091217302023], 
[-0.5644967683372204, -0.5502094257031297], 
[-1.3873920097717183, -4.162449580917944], 
[0.31382478643691897, -0.002400383361056276], 
[0.8204911699527756, 0.41757015392873165], 
[2.1569424703066713, -0.3702610775394398], 
[-1.0515000412668378, 0.7108656241958415], 
[0.8038662415106549, 1.4095767657407527], 
[-0.35718438257652674, 0.20671887950218415], 
[-1.0426445436641434, -0.3302893793050245], 
[-0.03135343910615884, 0.05480893251631327], 
[-0.6392397518032977, -0.6972749515117197], 
[1.6134608450294754, 0.5183895444032608], 
[1.9743471960037569, -3.711235076666022], 
[-0.0659838017319015, 0.20116058104821943], 
[-4.210447808985431, -1.5889899459151764], 
[-2.9563473502345063, -1.3811901590747555], 
[1.768117872419419, 0.7570896058447211], 
[0.02584362444286539, -0.021277289368476004], 
[0.049731904287387364, 0.8914210587005529], 
[0.08687301689728429, 0.19637156488770793], 
[1.8933923029705138, -0.5141896270260637], 
[-2.639469640933965, 3.124849475291749], 
[-1.246139804413564, -5.601239639294845], 
[-0.7636775712145276, -0.1601998833940735], 
[-0.6437050056538313, -1.4618803955559365], 
[1.1389536169421077, 0.09197593977751818], 
[0.01654807180539817, 0.20141712717660232], 
[0.6241945292562444, 2.6463098985520523], 
[-0.08151690038914385, -0.317878311087742], 
[-2.787883537058033, 2.706327215136643], 
[0.4435096241642191, -3.0607337404466652], 
[-0.37906347363483667, -0.145380155723716], 
[-0.116846460010746, 2.5287364920693434], 
[-0.8268195557522049, -0.004106630179078724], 
[-3.958021898200208, -1.188455440963943], 
[-1.2858312131837826, -0.01429545620638688], 
[-0.04818594800807723, -0.0027668007267954405], 
[2.2697847925739016, -0.8566445520081954], 
[2.008905834052401, -0.4309666660662263], 
[-1.45045813455761, -1.3206890355868404], 
[-0.3735435818869928, -0.669551579509596], 
[1.2826518207742459, 0.5974845312050637], 
[0.029726260113828375, -0.16698659023483323], 
[0.09798216711604382, -2.215610760195564], 
[0.33071584902627693, -2.7718176228955036], 
[-0.9656129593416314, -1.5941751640433683], 
[0.06267744466328239, 0.03805204744176049], 
[2.1873419838856365, 0.6304302706346292], 
[-0.7683919728690607, -2.268458745781708], 
[0.7968163524981433, -1.0230292585593497], 
[1.124437191255743, -0.047709667651932824], 
[-3.947622146880187, 4.037451568168466], 
[-0.9947453450082567, 5.360847989588572], 
[0.2813785712365046, -0.17117687800362802], 
[0.07102236753901413, -0.024005783001129564], 
[4.452942867846313, -1.4839442492004113], 
[-3.228615028502137, 4.1919378353841275], 
[-2.428009566378746, 0.5915185697158506], 
[-3.222617713423352, -2.0041222115643778], 
[0.13374954503578368, -0.13177953548650653], 
[0.08026832359448151, -1.4623665876597793], 
[-0.34501574905203447, 1.061045765520594], 
[-0.012348924274757776, -0.7015708576973871], 
[0.04032756694141316, 1.7804979253594704], 
[0.1391462055060581, -2.4533718237898454], 
[0.053334736366822205, 0.02815622022418189], 
[-1.333539339512339, -0.35974213289205453], 
[-1.5292178793444229, -4.014847896515144], 
[4.321044200206487, 0.42278681484875036], 
[0.12619368489574695, -2.7557494898071955], 
[0.11641239048101298, -0.03983018640210253], 
[0.7953599455304952, -0.5079129382980241], 
[-1.0938789178930326, 0.9984918446932308], 
[0.17817882827381343, -0.05791612159798184], 
[0.09516795069792078, 0.01679120440545506], 
[0.9532154019115091, 3.9708234390755237], 
[3.536907726587617, -2.356199179834304], 
[0.3310319508927695, -0.19976402404866164], 
[1.975614126385429, 0.8393537776691004], 
[0.30645200452035537, -1.68103763554819], 
[0.6177043808125575, 2.3859069126122248], 
[-0.17219709606946926, 3.1758013584752676], 
[0.25011964948373583, 0.3629744728395481], 
[0.7679057046462057, -0.7306214478841887], 
[0.5155000751951394, 0.12276280236098695], 
[1.390878749220352, 2.108357205602468], 
[-3.2264938824895375, 0.45090520885534036], 
[5.903421388280683E-4, 1.3986268612357607E-4], 
[0.2379764551982814, 0.324724871406808], 
[2.171056039407635, 3.3995574696672626], 
[-0.1542063398793024, 0.3024346276860235], 
[0.003926611563330039, -0.06795712880217582], 
[0.9286812366987802, -0.7310036544649329], 
[-0.20161800896334744, -0.06758253291102329], 
[1.5257362705952129, 2.480532578176497], 
[1.7857949374783566, 4.896681665704083], 
[-0.0197659981538891, -1.6489077728227535], 
[-0.6340286245853007, -0.19745463729094936], 
[-1.5740780784809838, 0.14234646882977808], 
[0.29473149158268475, -0.47743683433828366], 
[2.80037831491793, -3.9560435693873344], 
[-2.8451699869853084, -0.2347370548895951], 
[0.1883782533418842, -0.0690831937971664], 
[0.3696503511840127, 0.7619451222349009], 
[3.56937668035931, 0.7525813726783199], 
[0.059592832499309766, -0.13002643829230442], 
[0.0051007888500326235, 0.36231997432512175], 
[1.3577024397413677, -0.0387267828460711], 
[0.02102016575886829, 0.14056893692580494], 
[2.1221075739157156, -1.2979092522566946], 
[-0.13062082320176452, -0.3012831582478834], 
[1.8256122823814747, -1.7316141612071625], 
[0.18866591871504523, 0.05456269849504324], 
[-1.17201584129658, -1.7887056343603116], 
[-1.3520750192198847, -2.0138184171480282], 
[-1.8310834118975046, 1.428350047297672], 
[-0.931261816423352, 0.808146982520959], 
[0.951618351989188, 0.047562764942361085], 
[-1.694132511454749, -0.07331174323589112], 
[-8.465128005152877E-4, 1.1189193745610462], 
[-0.6116552787246939, 0.5871377614709223], 
[-1.9636886559427231, -3.0411831832225302], 
[0.12619856260780854, 0.08467486993731099], 
[0.024197723947476935, -2.048646953613178], 
[-1.8223882646305023, 0.12821189780853845], 
[-0.6788485515332288, 0.7191641184868829], 
[3.192550540479668, -1.17236389422474], 
[0.12671909926583097, -0.3643345688342954], 
[1.1438476496496153, -3.652990463778066], 
[-0.45068354303941055, 1.8898655556966457], 
[-1.420402401295437, -0.8812511236543631], 
[-0.10407969983917921, -0.43975725435102664], 
[-1.0011343513236357, 0.62630266318952], 
[-0.4849904250705047, -2.1172398757981195], 
[-0.44865211921833753, -0.5941398305479602], 
[0.7121328860670395, 0.5670444668256772], 
[-0.10748238917667165, -4.278285917616543], 
[-0.09910554601707183, 0.007403908133142828], 
[-4.640926494009351, -0.27418913329224204], 
[-0.1467359521051428, 0.39937729564112423], 
[1.347749124511451, -0.10383792032691366], 
[-1.1256504007569206, 4.562748759671703], 
[0.3188479220468887, 0.04383691336323038], 
[-0.09370037386914196, -0.0962324924416111], 
[-0.43515298327710655, 1.2806278501458808], 
[2.6008581241463213, -0.5560369420638798], 
[-3.7450149828448676, 1.8269921157647526], 
[0.7245222453322299, 2.0274008075817083], 
[-0.4723939609964834, -0.07714329438725778]])

Y = np.array([[0.07099203475193139], 
[0.2273346610714441], 
[0.029817676716547004], 
[0.1527336047874253], 
[0.5399926325427049], 
[0.5490886638085232], 
[0.4128618847449527], 
[0.48745761975104734], 
[0.5357579968781104], 
[0.6907794197995079], 
[0.2600071331985876], 
[0.7478608051088321], 
[0.4514138761997111], 
[0.5110870978098863], 
[0.3196490906395202], 
[0.8995079522977589], 
[0.21863733402970997], 
[0.5570562518434271], 
[0.7086007358482168], 
[0.25854891079417097], 
[0.14049713704809663], 
[0.6733608138880192], 
[0.44820130342234743], 
[0.007205521923755897], 
[0.2802986659237439], 
[0.1746157103885453], 
[0.8735532068346415], 
[0.8961911271076664], 
[0.4501040343133301], 
[0.46254010245268445], 
[0.4307488087333372], 
[0.7175281529689165], 
[0.4021684212906741], 
[0.052786068836967015], 
[0.7958947745710052], 
[0.1986122945256864], 
[0.3548536382409676], 
[0.27800313229934215], 
[0.13743634674805316], 
[0.7545043945881139], 
[0.4816509295481718], 
[0.45421790389397554], 
[0.6997296710476097], 
[0.040314101818713415], 
[0.45776456303370405], 
[0.03686553113134728], 
[0.7110055368817499], 
[0.4691720515568597], 
[0.5932785534771989], 
[0.2508171045504096], 
[0.9128130942069406], 
[0.8036702484912455], 
[0.4852491670320155], 
[0.8555056419227539], 
[0.7707274617131044], 
[0.5897831809629971], 
[0.49313578024743554], 
[0.10176064386884087], 
[0.6575506132434801], 
[0.5821647991834445], 
[0.6828035409294827], 
[0.5512190935376379], 
[4.298220069578473E-4], 
[0.40834948470432164], 
[0.19390099814927295], 
[0.26218864954398624], 
[0.5522638196226605], 
[0.5367679747414424], 
[0.2637368940333725], 
[0.8975966555726893], 
[0.5854618118419748], 
[0.14962179301872147], 
[0.38784967521372143], 
[0.5811662384272671], 
[0.9125655982049254], 
[0.7765427939234781], 
[0.3132845632539502], 
[0.8172187848709894], 
[0.21344095435917088], 
[0.5185972336905889], 
[0.745162749033839], 
[0.4975094481980725], 
[0.19268914164420403], 
[0.38457632616103765], 
[0.800447710940717], 
[0.9452610348394019], 
[0.6036251886982479], 
[0.6726482664478343], 
[0.36488395141961194], 
[0.09206836629319025], 
[0.15661438792057558], 
[0.46032969204848845], 
[0.5999040629089157], 
[0.24760374246806902], 
[0.7797544709894323], 
[0.11436678231248387], 
[0.9058697207376979], 
[0.5050618116287044], 
[0.6188354155805668], 
[0.2994998790763828], 
[0.676333147655269], 
[0.6270397991059957], 
[0.5512050533078822], 
[0.25121732075931924], 
[0.17507562673364163], 
[0.27705685549033865], 
[0.8446128416233004], 
[0.08248788926153348], 
[0.8334997846092659], 
[0.7011744935859208], 
[0.9173008152170693], 
[0.6180933867565054], 
[0.20052301284203825], 
[0.422187172048092], 
[0.9495547342542016], 
[0.6925663532442624], 
[0.6804396176950891], 
[0.18561082397051917], 
[0.35962481925878165], 
[0.008869974318929665], 
[0.06628935609915633], 
[0.2922039295542449], 
[0.8883699736857692], 
[0.5348406879216688], 
[0.7170905836115288], 
[0.5660143782718494], 
[0.23717530855396213], 
[0.013046584121998994], 
[0.03686659355588428], 
[0.5399528476021298], 
[0.8726376700646647], 
[0.47709737177157263], 
[0.6917137609276846], 
[0.9926510835585395], 
[0.7492095190377013], 
[0.7035745198094567], 
[0.7482306396340265], 
[0.7408714667808707], 
[0.30743644504476203], 
[0.2836334223865623], 
[0.6324475713581948], 
[0.5809922143752686], 
[0.18061935312924945], 
[0.4719616106041334], 
[0.49296618686162214], 
[0.4810999804320052], 
[0.5866773425475955], 
[0.16316022568970723], 
[0.2053391443942391], 
[0.551979758723363], 
[0.3946825332295243], 
[0.2567488675615087], 
[0.8767903646075997], 
[0.9707997269972588], 
[0.33698409327346707], 
[0.30187615152865177], 
[0.30119628766282813], 
[0.8955463015590637], 
[0.7880328869662072], 
[0.6614522881302283], 
[0.3738192215915729], 
[0.4912728491255748], 
[0.9499645804610368], 
[0.5028011274713937], 
[0.0036041796644401547], 
[0.4909829785437019], 
[0.17269373275619482], 
[0.7080638320717104], 
[0.5579204652280549], 
[0.23447710626996066], 
[0.49271692598485217], 
[0.30246734473014264], 
[0.3404502794155749], 
[0.8677494588366627], 
[0.30001802505607716], 
[0.22220514848143627], 
[0.037496401229159315], 
[0.34352932459051616], 
[0.3364145434775404], 
[0.18605955860920467], 
[0.4713013088759638], 
[0.04031947241247058], 
[0.9913788031873138], 
[0.09602799500767346], 
[0.37104094610931837], 
[0.21279140383897463], 
[0.09281319758650662], 
[0.77209891153413], 
[0.21297597405036647], 
[0.10065565442836222], 
[0.09045411719684594], 
[0.924954802350356], 
[0.4908141270248622], 
[0.35613265561376706], 
[0.6985244533047716], 
[0.0877639273225833], 
[0.055657377502233096], 
[0.5019077511149015], 
[0.7019497734741335], 
[0.7643536008073509], 
[0.41197811295534875], 
[0.40196204248365336], 
[0.7368988003549444], 
[0.30594249299546367], 
[0.07188860190465261], 
[0.21692754993407196], 
[0.4316038575185216], 
[0.0022404564770327484], 
[0.2545384673309639], 
[0.02362439784273551], 
[0.33736253109216174], 
[0.5651085140416409], 
[0.3707953801129627], 
[0.205194407114045], 
[0.5923168608656637], 
[0.5941037754454247], 
[0.8554340924181797], 
[0.8637538160152836], 
[0.24205190277415087], 
[0.7431170370830898], 
[0.9998795921547596], 
[0.8717454431102175], 
[0.5912507958721979], 
[0.15594376512786046], 
[0.498120218669662], 
[0.7611787320574457], 
[0.8795884018939261], 
[0.3060115929090159], 
[0.4467273034560108], 
[0.45170357129656036], 
[0.9627415947539855], 
[0.6616210013114945], 
[0.5369874548651998], 
[0.8389716945097621], 
[0.5358388872924315], 
[0.6029375165728489], 
[0.14297504744610368], 
[0.5039975719979001], 
[0.7618679903125861], 
[0.7406079339609947], 
[0.9439613044037111], 
[0.26223798546909854], 
[0.9615044669995508], 
[0.22825485595966966], 
[0.6228783276308556], 
[0.9478678167514369], 
[0.2835210778877404], 
[0.8222368556506536], 
[0.05462532003528798], 
[0.7242369480506904]])

syn0 = 2 * np.random.random((2, 40)) - 1
syn1 = 2 * np.random.random((40, 1)) - 1
l0 = X
iters = 100000000
prev_error = 0
for iter in xrange(iters):
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    l2_error = Y - l2
    prev_error += np.mean(np.abs(l2_error)) * 100
    if (iter%10000) == 0:
        print "Average Error: " + str(prev_error/(iter + 1)) + "%"
        print str((float)(iter * 100)/iters) + "% complete"

    l2_delta = l2_error * nonlin(l2, deriv=True) * ((float)(iter)/iters)
    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * nonlin(l1, deriv=True) * ((float)(iter)/iters)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print "Output after training"
l0 = np.array([[0.5133270861115978, 1.150123935283164]])
print nonlin(np.dot(nonlin(np.dot(l0, syn0)), syn1))
print "Correct output" + 0.06681199714290154