# -*- coding: utf-8 -*-

import numpy as np

def nonlin(x, deriv = False):
    if (deriv == True):
        return x * (1 - x)
    return 1/(1+np.exp(-x))

np.random.seed(1)
X = np.array([[-100.0], 
[-99.6], 
[-99.2], 
[-98.8], 
[-98.4], 
[-98.0], 
[-97.6], 
[-97.2], 
[-96.8], 
[-96.4], 
[-96.0], 
[-95.6], 
[-95.2], 
[-94.8], 
[-94.4], 
[-94.0], 
[-93.6], 
[-93.2], 
[-92.8], 
[-92.4], 
[-92.0], 
[-91.6], 
[-91.2], 
[-90.8], 
[-90.4], 
[-90.0], 
[-89.6], 
[-89.2], 
[-88.8], 
[-88.4], 
[-88.0], 
[-87.6], 
[-87.2], 
[-86.8], 
[-86.4], 
[-86.0], 
[-85.6], 
[-85.2], 
[-84.8], 
[-84.4], 
[-84.0], 
[-83.6], 
[-83.2], 
[-82.8], 
[-82.4], 
[-82.0], 
[-81.6], 
[-81.2], 
[-80.8], 
[-80.4], 
[-80.0], 
[-79.6], 
[-79.2], 
[-78.8], 
[-78.4], 
[-78.0], 
[-77.6], 
[-77.2], 
[-76.8], 
[-76.4], 
[-76.0], 
[-75.6], 
[-75.2], 
[-74.8], 
[-74.4], 
[-74.0], 
[-73.6], 
[-73.2], 
[-72.8], 
[-72.4], 
[-72.0], 
[-71.6], 
[-71.2], 
[-70.8], 
[-70.4], 
[-70.0], 
[-69.6], 
[-69.2], 
[-68.8], 
[-68.4], 
[-68.0], 
[-67.6], 
[-67.19999999999999], 
[-66.8], 
[-66.4], 
[-66.0], 
[-65.6], 
[-65.19999999999999], 
[-64.8], 
[-64.4], 
[-64.0], 
[-63.6], 
[-63.199999999999996], 
[-62.8], 
[-62.4], 
[-62.0], 
[-61.599999999999994], 
[-61.199999999999996], 
[-60.8], 
[-60.4], 
[-60.0], 
[-59.599999999999994], 
[-59.199999999999996], 
[-58.8], 
[-58.4], 
[-58.0], 
[-57.599999999999994], 
[-57.199999999999996], 
[-56.8], 
[-56.4], 
[-56.0], 
[-55.599999999999994], 
[-55.199999999999996], 
[-54.8], 
[-54.4], 
[-54.0], 
[-53.599999999999994], 
[-53.199999999999996], 
[-52.8], 
[-52.4], 
[-52.0], 
[-51.599999999999994], 
[-51.199999999999996], 
[-50.8], 
[-50.4], 
[-50.0], 
[-49.599999999999994], 
[-49.199999999999996], 
[-48.8], 
[-48.4], 
[-48.0], 
[-47.599999999999994], 
[-47.199999999999996], 
[-46.8], 
[-46.4], 
[-46.0], 
[-45.599999999999994], 
[-45.199999999999996], 
[-44.8], 
[-44.4], 
[-44.0], 
[-43.599999999999994], 
[-43.199999999999996], 
[-42.8], 
[-42.4], 
[-42.0], 
[-41.599999999999994], 
[-41.199999999999996], 
[-40.8], 
[-40.4], 
[-40.0], 
[-39.599999999999994], 
[-39.199999999999996], 
[-38.8], 
[-38.4], 
[-38.0], 
[-37.599999999999994], 
[-37.199999999999996], 
[-36.8], 
[-36.4], 
[-36.0], 
[-35.599999999999994], 
[-35.2], 
[-34.8], 
[-34.39999999999999], 
[-34.0], 
[-33.599999999999994], 
[-33.2], 
[-32.8], 
[-32.39999999999999], 
[-32.0], 
[-31.599999999999994], 
[-31.200000000000003], 
[-30.799999999999997], 
[-30.39999999999999], 
[-30.0], 
[-29.599999999999994], 
[-29.200000000000003], 
[-28.799999999999997], 
[-28.39999999999999], 
[-28.0], 
[-27.599999999999994], 
[-27.200000000000003], 
[-26.799999999999997], 
[-26.39999999999999], 
[-26.0], 
[-25.599999999999994], 
[-25.200000000000003], 
[-24.799999999999997], 
[-24.39999999999999], 
[-24.0], 
[-23.599999999999994], 
[-23.19999999999999], 
[-22.799999999999997], 
[-22.39999999999999], 
[-22.0], 
[-21.599999999999994], 
[-21.19999999999999], 
[-20.799999999999997], 
[-20.39999999999999], 
[-20.0], 
[-19.599999999999994], 
[-19.19999999999999], 
[-18.799999999999997], 
[-18.39999999999999], 
[-18.0], 
[-17.599999999999994], 
[-17.19999999999999], 
[-16.799999999999997], 
[-16.39999999999999], 
[-16.0], 
[-15.599999999999994], 
[-15.199999999999989], 
[-14.799999999999997], 
[-14.399999999999991], 
[-14.0], 
[-13.599999999999994], 
[-13.199999999999989], 
[-12.799999999999997], 
[-12.399999999999991], 
[-12.0], 
[-11.599999999999994], 
[-11.199999999999989], 
[-10.799999999999997], 
[-10.399999999999991], 
[-10.0], 
[-9.599999999999994], 
[-9.199999999999989], 
[-8.799999999999997], 
[-8.399999999999991], 
[-8.0], 
[-7.599999999999994], 
[-7.199999999999989], 
[-6.799999999999997], 
[-6.3999999999999915], 
[-6.0], 
[-5.599999999999994], 
[-5.199999999999989], 
[-4.799999999999997], 
[-4.3999999999999915], 
[-4.0], 
[-3.5999999999999943], 
[-3.1999999999999886], 
[-2.799999999999997], 
[-2.3999999999999915], 
[-2.0], 
[-1.5999999999999943], 
[-1.1999999999999886], 
[-0.7999999999999972], 
[-0.3999999999999915], 
[0.0], 
[0.4000000000000057], 
[0.8000000000000114], 
[1.2000000000000028], 
[1.6000000000000085], 
[2.0], 
[2.4000000000000057], 
[2.8000000000000114], 
[3.200000000000003], 
[3.6000000000000085], 
[4.0], 
[4.400000000000006], 
[4.800000000000011], 
[5.200000000000003], 
[5.6000000000000085], 
[6.0], 
[6.400000000000006], 
[6.800000000000011], 
[7.200000000000003], 
[7.6000000000000085], 
[8.0], 
[8.400000000000006], 
[8.800000000000011], 
[9.200000000000003], 
[9.600000000000009], 
[10.0], 
[10.400000000000006], 
[10.800000000000011], 
[11.200000000000003], 
[11.600000000000009], 
[12.0], 
[12.400000000000006], 
[12.800000000000011], 
[13.200000000000003], 
[13.600000000000009], 
[14.0], 
[14.400000000000006], 
[14.800000000000011], 
[15.200000000000003], 
[15.600000000000009], 
[16.0], 
[16.400000000000006], 
[16.80000000000001], 
[17.200000000000003], 
[17.60000000000001], 
[18.0], 
[18.400000000000006], 
[18.80000000000001], 
[19.200000000000003], 
[19.60000000000001], 
[20.0], 
[20.400000000000006], 
[20.80000000000001], 
[21.200000000000003], 
[21.60000000000001], 
[22.0], 
[22.400000000000006], 
[22.80000000000001], 
[23.200000000000003], 
[23.60000000000001], 
[24.0], 
[24.400000000000006], 
[24.80000000000001], 
[25.200000000000003], 
[25.60000000000001], 
[26.0], 
[26.400000000000006], 
[26.80000000000001], 
[27.200000000000003], 
[27.60000000000001], 
[28.0], 
[28.400000000000006], 
[28.80000000000001], 
[29.200000000000017], 
[29.599999999999994], 
[30.0], 
[30.400000000000006], 
[30.80000000000001], 
[31.200000000000017], 
[31.599999999999994], 
[32.0], 
[32.400000000000006], 
[32.80000000000001], 
[33.20000000000002], 
[33.599999999999994], 
[34.0], 
[34.400000000000006], 
[34.80000000000001], 
[35.20000000000002], 
[35.599999999999994], 
[36.0], 
[36.400000000000006], 
[36.80000000000001], 
[37.20000000000002], 
[37.599999999999994], 
[38.0], 
[38.400000000000006], 
[38.80000000000001], 
[39.20000000000002], 
[39.599999999999994], 
[40.0], 
[40.400000000000006], 
[40.80000000000001], 
[41.20000000000002], 
[41.599999999999994], 
[42.0], 
[42.400000000000006], 
[42.80000000000001], 
[43.20000000000002], 
[43.599999999999994], 
[44.0], 
[44.400000000000006], 
[44.80000000000001], 
[45.20000000000002], 
[45.599999999999994], 
[46.0], 
[46.400000000000006], 
[46.80000000000001], 
[47.20000000000002], 
[47.599999999999994], 
[48.0], 
[48.400000000000006], 
[48.80000000000001], 
[49.20000000000002], 
[49.599999999999994], 
[50.0], 
[50.400000000000006], 
[50.80000000000001], 
[51.20000000000002], 
[51.599999999999994], 
[52.0], 
[52.400000000000006], 
[52.80000000000001], 
[53.20000000000002], 
[53.60000000000002], 
[54.0], 
[54.400000000000006], 
[54.80000000000001], 
[55.20000000000002], 
[55.60000000000002], 
[56.0], 
[56.400000000000006], 
[56.80000000000001], 
[57.20000000000002], 
[57.60000000000002], 
[58.0], 
[58.400000000000006], 
[58.80000000000001], 
[59.20000000000002], 
[59.60000000000002], 
[60.0], 
[60.400000000000006], 
[60.80000000000001], 
[61.20000000000002], 
[61.60000000000002], 
[62.0], 
[62.400000000000006], 
[62.80000000000001], 
[63.20000000000002], 
[63.60000000000002], 
[64.0], 
[64.4], 
[64.80000000000001], 
[65.20000000000002], 
[65.60000000000002], 
[66.0], 
[66.4], 
[66.80000000000001], 
[67.20000000000002], 
[67.60000000000002], 
[68.0], 
[68.4], 
[68.80000000000001], 
[69.20000000000002], 
[69.60000000000002], 
[70.0], 
[70.4], 
[70.80000000000001], 
[71.20000000000002], 
[71.60000000000002], 
[72.0], 
[72.4], 
[72.80000000000001], 
[73.20000000000002], 
[73.60000000000002], 
[74.0], 
[74.4], 
[74.80000000000001], 
[75.20000000000002], 
[75.60000000000002], 
[76.0], 
[76.4], 
[76.80000000000001], 
[77.20000000000002], 
[77.60000000000002], 
[78.0], 
[78.4], 
[78.80000000000001], 
[79.20000000000002], 
[79.60000000000002], 
[80.0], 
[80.4], 
[80.80000000000001], 
[81.20000000000002], 
[81.60000000000002], 
[82.0], 
[82.4], 
[82.80000000000001], 
[83.20000000000002], 
[83.60000000000002], 
[84.0], 
[84.4], 
[84.80000000000001], 
[85.20000000000002], 
[85.60000000000002], 
[86.0], 
[86.4], 
[86.80000000000001], 
[87.20000000000002], 
[87.60000000000002], 
[88.0], 
[88.4], 
[88.80000000000001], 
[89.20000000000002], 
[89.60000000000002], 
[90.0], 
[90.4], 
[90.80000000000001], 
[91.20000000000002], 
[91.60000000000002], 
[92.0], 
[92.4], 
[92.80000000000001], 
[93.20000000000002], 
[93.60000000000002], 
[94.0], 
[94.4], 
[94.80000000000001], 
[95.20000000000002], 
[95.60000000000002], 
[96.0], 
[96.4], 
[96.80000000000001], 
[97.20000000000002], 
[97.60000000000002], 
[98.0], 
[98.4], 
[98.80000000000001], 
[99.20000000000002], 
[99.60000000000002]])

Y = np.array([[-1.5607966601082315], 
[-1.5607565034974709], 
[-1.560716023075849], 
[-1.560675214910974], 
[-1.560634075006524], 
[-1.5605925993009424], 
[-1.5605507836661008], 
[-1.5605086239059305], 
[-1.5604661157550181], 
[-1.560423254877168], 
[-1.560380036863927], 
[-1.560336457233074], 
[-1.5602925114270703], 
[-1.5602481948114706], 
[-1.5602035026732943], 
[-1.5601584302193552], 
[-1.560112972574547], 
[-1.5600671247800872], 
[-1.5600208817917134], 
[-1.559974238477833], 
[-1.5599271896176263], 
[-1.5598797298990983], 
[-1.5598318539170788], 
[-1.5597835561711721], 
[-1.5597348310636499], 
[-1.5596856728972892], 
[-1.5596360758731513], 
[-1.5595860340883028], 
[-1.5595355415334728], 
[-1.559484592090649], 
[-1.5594331795306058], 
[-1.5593812975103665], 
[-1.5593289395705947], 
[-1.5592760991329135], 
[-1.5592227694971523], 
[-1.5591689438385128], 
[-1.5591146152046598], 
[-1.5590597765127272], 
[-1.5590044205462408], 
[-1.558948539951953], 
[-1.5588921272365868], 
[-1.5588351747634872], 
[-1.5587776747491755], 
[-1.558719619259804], 
[-1.5586610002075068], 
[-1.5586018093466447], 
[-1.55854203826994], 
[-1.558481678404495], 
[-1.5584207210076952], 
[-1.5583591571629878], 
[-1.5582969777755349], 
[-1.5582341735677356], 
[-1.5581707350746117], 
[-1.5581066526390543], 
[-1.5580419164069228], 
[-1.557976516321996], 
[-1.5579104421207641], 
[-1.5578436833270612], 
[-1.557776229246529], 
[-1.5577080689609064], 
[-1.5576391913221408], 
[-1.5575695849463091], 
[-1.5574992382073485], 
[-1.5574281392305824], 
[-1.5573562758860424], 
[-1.5572836357815685], 
[-1.557210206255688], 
[-1.5571359743702602], 
[-1.557060926902878], 
[-1.556985050339018], 
[-1.5569083308639295], 
[-1.5568307543542523], 
[-1.5567523063693498], 
[-1.5566729721423507], 
[-1.5565927365708845], 
[-1.5565115842075], 
[-1.556429499249753], 
[-1.55634646552995], 
[-1.5562624665045364], 
[-1.556177485243109], 
[-1.5560915044170451], 
[-1.5560045062877244], 
[-1.5559164726943326], 
[-1.555827385041226], 
[-1.5557372242848413], 
[-1.555645970920127], 
[-1.55555360496648], 
[-1.5554601059531672], 
[-1.5553654529042018], 
[-1.5552696243226622], 
[-1.5551725981744198], 
[-1.555074351871253], 
[-1.554974862253323], 
[-1.554874105570977], 
[-1.5547720574658543], 
[-1.5546686929512603], 
[-1.554563986391777], 
[-1.5544579114820734], 
[-1.554350441224881], 
[-1.5542415479080942], 
[-1.554131203080956], 
[-1.5540193775292834], 
[-1.553906041249692], 
[-1.5537911634227668], 
[-1.5536747123851322], 
[-1.5535566556003668], 
[-1.553436959628708], 
[-1.5533155900954843], 
[-1.5531925116582173], 
[-1.5530676879723229], 
[-1.5529410816553442], 
[-1.5528126542496417], 
[-1.552682366183463], 
[-1.5525501767303076], 
[-1.5524160439665016], 
[-1.5522799247268875], 
[-1.5521417745585324], 
[-1.5520015476723483], 
[-1.5518591968925157], 
[-1.5517146736035938], 
[-1.5515679276951895], 
[-1.5514189075040565], 
[-1.5512675597534828], 
[-1.5511138294898168], 
[-1.550957660015972], 
[-1.550798992821746], 
[-1.550637767510769], 
[-1.5504739217238912], 
[-1.5503073910588083], 
[-1.5501381089857043], 
[-1.5499660067586796], 
[-1.5497910133227197], 
[-1.549613055215937], 
[-1.549432056466805], 
[-1.5492479384860822], 
[-1.5490606199531038], 
[-1.5488700166960965], 
[-1.5486760415661411], 
[-1.5484786043043974], 
[-1.5482776114021535], 
[-1.5480729659532555], 
[-1.547864567498421], 
[-1.547652311860915], 
[-1.547436090973022], 
[-1.5472157926927095], 
[-1.5469913006098266], 
[-1.546762493841139], 
[-1.5465292468134375], 
[-1.546291429033907], 
[-1.5460489048468737], 
[-1.5458015331759765], 
[-1.5455491672507347], 
[-1.5452916543164017], 
[-1.5450288353258959], 
[-1.544760544612509], 
[-1.5444866095419745], 
[-1.544206850142363], 
[-1.5439210787101398], 
[-1.5436290993905735], 
[-1.543330707730525], 
[-1.5430256902014756], 
[-1.5427138236904574], 
[-1.542394874956336], 
[-1.542068600048667], 
[-1.5417347436860835], 
[-1.5413930385908916], 
[-1.5410432047762315], 
[-1.5406849487818142], 
[-1.5403179628538508], 
[-1.5399419240643706], 
[-1.5395564933646284], 
[-1.5391613145667842], 
[-1.5387560132474296], 
[-1.5383401955658773], 
[-1.5379134469893847], 
[-1.5374753309166493], 
[-1.5370253871899826], 
[-1.5365631304855158], 
[-1.5360880485696218], 
[-1.5355996004083983], 
[-1.5350972141155728], 
[-1.534580284722485], 
[-1.534048171751901], 
[-1.5335001965752295], 
[-1.5329356395302578], 
[-1.5323537367737086], 
[-1.5317536768397295], 
[-1.5311345968717691], 
[-1.5304955784911152], 
[-1.529835643260581], 
[-1.5291537476963082], 
[-1.5284487777743208], 
[-1.527719542871135], 
[-1.526964769069259], 
[-1.526183091748594], 
[-1.5253730473733196], 
[-1.5245330643705397], 
[-1.523661452981396], 
[-1.522756393947134], 
[-1.5218159258711694], 
[-1.5208379310729538], 
[-1.5198201197195833], 
[-1.5187600119856803], 
[-1.5176549179499612], 
[-1.5165019148865906], 
[-1.5152978215491797], 
[-1.5140391689728032], 
[-1.5127221672319426], 
[-1.5113426674862398], 
[-1.5098961185169086], 
[-1.5083775167989393], 
[-1.5067813489605526], 
[-1.5051015252424318], 
[-1.503331302272992], 
[-1.501463193106688], 
[-1.4994888620096063], 
[-1.497399000893285], 
[-1.4951831835580667], 
[-1.4928296929633542], 
[-1.4903253155294358], 
[-1.4876550949064553], 
[-1.484802035600656], 
[-1.4817467441603986], 
[-1.4784669920632976], 
[-1.4749371796848834], 
[-1.4711276743037347], 
[-1.4670039863378537], 
[-1.4625257359344404], 
[-1.457645345204412], 
[-1.4523063676367587], 
[-1.446441332248135], 
[-1.4399689307208396], 
[-1.432790303137377], 
[-1.424784069083621], 
[-1.4157995848709555], 
[-1.4056476493802699], 
[-1.3940874707248598], 
[-1.3808080388761805], 
[-1.365400937605129], 
[-1.3473197256542633], 
[-1.3258176636680326], 
[-1.2998494764564756], 
[-1.2679114584199243], 
[-1.227772386374193], 
[-1.176005207095134], 
[-1.1071487177940904], 
[-1.0121970114513326], 
[-0.8760580505981888], 
[-0.674740942223551], 
[-0.3805063771123575], 
[0.0], 
[0.3805063771123698], 
[0.6747409422235596], 
[0.8760580505981945], 
[1.0121970114513366], 
[1.1071487177940904], 
[1.176005207095136], 
[1.2277723863741945], 
[1.2679114584199254], 
[1.2998494764564767], 
[1.3258176636680326], 
[1.347319725654264], 
[1.3654009376051297], 
[1.380808038876181], 
[1.3940874707248603], 
[1.4056476493802699], 
[1.4157995848709557], 
[1.4247840690836215], 
[1.4327903031373772], 
[1.4399689307208399], 
[1.446441332248135], 
[1.452306367636759], 
[1.4576453452044122], 
[1.4625257359344406], 
[1.467003986337854], 
[1.4711276743037347], 
[1.4749371796848836], 
[1.4784669920632978], 
[1.4817467441603989], 
[1.484802035600656], 
[1.4876550949064553], 
[1.4903253155294358], 
[1.4928296929633544], 
[1.495183183558067], 
[1.497399000893285], 
[1.4994888620096063], 
[1.501463193106688], 
[1.503331302272992], 
[1.505101525242432], 
[1.5067813489605526], 
[1.5083775167989393], 
[1.5098961185169086], 
[1.5113426674862398], 
[1.5127221672319426], 
[1.5140391689728032], 
[1.5152978215491797], 
[1.5165019148865906], 
[1.5176549179499612], 
[1.5187600119856803], 
[1.5198201197195833], 
[1.5208379310729538], 
[1.5218159258711694], 
[1.522756393947134], 
[1.523661452981396], 
[1.5245330643705397], 
[1.5253730473733196], 
[1.526183091748594], 
[1.526964769069259], 
[1.527719542871135], 
[1.5284487777743208], 
[1.5291537476963082], 
[1.529835643260581], 
[1.5304955784911152], 
[1.5311345968717691], 
[1.5317536768397297], 
[1.5323537367737086], 
[1.5329356395302578], 
[1.5335001965752295], 
[1.534048171751901], 
[1.534580284722485], 
[1.5350972141155728], 
[1.5355996004083983], 
[1.5360880485696218], 
[1.5365631304855158], 
[1.5370253871899826], 
[1.5374753309166493], 
[1.5379134469893847], 
[1.5383401955658773], 
[1.5387560132474296], 
[1.5391613145667842], 
[1.5395564933646284], 
[1.5399419240643706], 
[1.5403179628538508], 
[1.5406849487818142], 
[1.5410432047762315], 
[1.5413930385908916], 
[1.5417347436860835], 
[1.542068600048667], 
[1.542394874956336], 
[1.5427138236904574], 
[1.5430256902014756], 
[1.543330707730525], 
[1.5436290993905735], 
[1.5439210787101398], 
[1.544206850142363], 
[1.5444866095419745], 
[1.544760544612509], 
[1.5450288353258959], 
[1.5452916543164017], 
[1.5455491672507347], 
[1.5458015331759765], 
[1.5460489048468737], 
[1.546291429033907], 
[1.5465292468134375], 
[1.546762493841139], 
[1.5469913006098266], 
[1.5472157926927095], 
[1.547436090973022], 
[1.547652311860915], 
[1.547864567498421], 
[1.5480729659532555], 
[1.5482776114021535], 
[1.5484786043043974], 
[1.5486760415661411], 
[1.5488700166960965], 
[1.5490606199531038], 
[1.5492479384860822], 
[1.549432056466805], 
[1.549613055215937], 
[1.5497910133227197], 
[1.5499660067586796], 
[1.5501381089857043], 
[1.5503073910588083], 
[1.5504739217238912], 
[1.550637767510769], 
[1.550798992821746], 
[1.550957660015972], 
[1.5511138294898168], 
[1.5512675597534828], 
[1.5514189075040565], 
[1.5515679276951895], 
[1.5517146736035938], 
[1.5518591968925157], 
[1.5520015476723483], 
[1.5521417745585324], 
[1.5522799247268875], 
[1.5524160439665016], 
[1.5525501767303076], 
[1.552682366183463], 
[1.5528126542496417], 
[1.5529410816553442], 
[1.5530676879723229], 
[1.5531925116582173], 
[1.5533155900954843], 
[1.553436959628708], 
[1.5535566556003668], 
[1.5536747123851322], 
[1.5537911634227668], 
[1.553906041249692], 
[1.5540193775292834], 
[1.554131203080956], 
[1.5542415479080942], 
[1.554350441224881], 
[1.5544579114820734], 
[1.554563986391777], 
[1.5546686929512603], 
[1.5547720574658543], 
[1.554874105570977], 
[1.554974862253323], 
[1.555074351871253], 
[1.5551725981744198], 
[1.5552696243226622], 
[1.5553654529042018], 
[1.5554601059531672], 
[1.5555536049664802], 
[1.555645970920127], 
[1.5557372242848413], 
[1.555827385041226], 
[1.5559164726943326], 
[1.5560045062877244], 
[1.5560915044170451], 
[1.556177485243109], 
[1.5562624665045364], 
[1.55634646552995], 
[1.556429499249753], 
[1.5565115842075], 
[1.5565927365708845], 
[1.5566729721423507], 
[1.5567523063693498], 
[1.5568307543542523], 
[1.5569083308639295], 
[1.556985050339018], 
[1.557060926902878], 
[1.5571359743702602], 
[1.557210206255688], 
[1.5572836357815685], 
[1.5573562758860424], 
[1.5574281392305824], 
[1.5574992382073485], 
[1.5575695849463094], 
[1.5576391913221408], 
[1.5577080689609064], 
[1.557776229246529], 
[1.5578436833270612], 
[1.5579104421207641], 
[1.557976516321996], 
[1.5580419164069228], 
[1.5581066526390543], 
[1.5581707350746117], 
[1.5582341735677356], 
[1.5582969777755349], 
[1.5583591571629878], 
[1.5584207210076952], 
[1.558481678404495], 
[1.55854203826994], 
[1.5586018093466447], 
[1.5586610002075068], 
[1.558719619259804], 
[1.5587776747491755], 
[1.5588351747634872], 
[1.5588921272365868], 
[1.558948539951953], 
[1.5590044205462408], 
[1.5590597765127272], 
[1.5591146152046598], 
[1.5591689438385128], 
[1.5592227694971523], 
[1.5592760991329135], 
[1.5593289395705947], 
[1.5593812975103665], 
[1.5594331795306058], 
[1.559484592090649], 
[1.5595355415334728], 
[1.5595860340883028], 
[1.5596360758731513], 
[1.5596856728972892], 
[1.5597348310636499], 
[1.5597835561711721], 
[1.5598318539170788], 
[1.5598797298990983], 
[1.5599271896176263], 
[1.559974238477833], 
[1.5600208817917134], 
[1.5600671247800872], 
[1.560112972574547], 
[1.5601584302193552], 
[1.5602035026732943], 
[1.5602481948114706], 
[1.5602925114270703], 
[1.560336457233074], 
[1.560380036863927], 
[1.560423254877168], 
[1.5604661157550181], 
[1.5605086239059305], 
[1.5605507836661008], 
[1.5605925993009424], 
[1.560634075006524], 
[1.560675214910974], 
[1.560716023075849], 
[1.5607565034974709]])

syn0 = 2 * np.random.random((1, 30)) - 1
syn1 = 2 * np.random.random((30, 1)) - 1
for iter in xrange(10000000):
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    l2_error = Y - l2
    if (iter%10000) == 0:
        print "Error:" + str(np.mean(np.abs(l2_error)))
    l2_delta = l2_error * nonlin(l2, deriv=True)
    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * nonlin(l1, deriv=True)
#    l1_delta = l1_error * .0001
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)
#    print np.sum(l1_error)
#print "Correct output"
#print "[[0.07161018169493694]]"
print "Output after training"
l0 = np.array([[191.6595610201218]])
print nonlin(np.dot(nonlin(np.dot(l0, syn0)), syn1))