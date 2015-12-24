"""
The refstates module contains pure-element reference state data.
"""

from sympy import And, Piecewise, log
from pycalphad.variables import T
from collections import OrderedDict

# SGTE 1991 Pure Element Reference compiled by Dinsdale
SGTE91 = OrderedDict(
[('AG',
  Piecewise((-3.98587e-7*T**3 - 0.001790585*T**2 - 23.8463314*T*log(T) + 118.202013*T - 7209.512 - 12011/T, And(T < 1234.93, T >= 298.15)), (-33.472*T*log(T) + 190.266404*T - 15095.252 + 1.411773e+29/T**9, And(T < 3000.0, T >= 1234.93)))),
 ('AL',
  Piecewise((-8.77664e-7*T**3 - 0.001884662*T**2 - 24.3671976*T*log(T) + 137.093038*T - 7976.15 + 74092/T, And(T < 700.0, T >= 298.15)), (-5.764227e-6*T**3 + 0.018531982*T**2 - 38.5844296*T*log(T) + 223.048446*T - 11276.24 + 74092/T, And(T < 933.47, T >= 700.0)), (-31.748192*T*log(T) + 188.684153*T - 11278.378 - 1.230524e+28/T**9, And(T < 2900.0, T >= 933.47)))),
 ('AM',
  Piecewise((-5.41038e-7*T**3 - 0.00559955*T**2 - 21.1868*T*log(T) + 89.645685*T - 6639.201 - 30424/T, And(T < 1329.0, T >= 298.15)), (-41.84*T*log(T) + 241.107269*T - 21702.938, And(T < 3000.0, T >= 1329.0)))),
 ('AS',
  Piecewise((-0.00271613*T**2 - 23.3144*T*log(T) + 122.211069*T - 7270.447 + 11600/T, And(T < 1090.0, T >= 298.15)), (-29.216037*T*log(T) + 163.457433*T - 10454.913, And(T < 1200.0, T >= 1090.0)))),
 ('AU',
  Piecewise((3.79625e-7*T**3 - 0.00385924*T**2 - 22.75455*T*log(T) + 106.830098*T - 6938.856 - 25097/T, And(T < 929.4, T >= 298.15)), (-1.1518713e-5*T**3 + 0.08756015*T**2 - 155.706745*T*log(T) + 1021.69543*T - 93586.481 + 10637210/T, And(T < 1337.33, T >= 929.4)), (8.923844e-6*T**3 - 0.118216828*T**2 + 263.252259*T*log(T) - 2016.37825*T + 314067.829 - 67999832/T, And(T < 1735.8, T >= 1337.33)), (-30.9616*T*log(T) + 165.272524*T - 12133.783, And(T < 3200.0, T >= 1735.8)))),
 ('BA',
  Piecewise((-9.5e-11*T**3 - 0.0018314*T**2 - 42.889*T*log(T) + 233.78606*T - 17685.226 + 705880/T, And(T < 1000.0, T >= 298.15)), (-1.051353e-6*T**3 + 0.019504772*T**2 - 94.2824199*T*log(T) + 608.188389*T - 64873.614 + 8220192/T, And(T < 2995.0, T >= 1000.0)), (-32.2*T*log(T) + 136.780042*T + 8083.889, And(T < 4000.0, T >= 2995.0)))),
 ('B',
  Piecewise((6.18878e-7*T**3 - 0.006864515*T**2 - 15.6641*T*log(T) + 107.111864*T - 7735.284 + 370843/T, And(T < 1100.0, T >= 298.15)), (-2.556e-8*T**3 - 0.00079809*T**2 - 26.6047*T*log(T) + 184.801744*T - 16649.474 + 1748270/T, And(T < 2348.0, T >= 1100.0)), (1.34719e-7*T**3 - 0.00159488*T**2 - 31.5957527*T*log(T) + 231.336244*T - 36667.582 + 11205883/T, And(T < 3000.0, T >= 2348.0)), (-31.4*T*log(T) + 222.396264*T - 21530.653, And(T < 6000.0, T >= 3000.0)))),
 ('BE',
  Piecewise((-1.60413e-7*T**3 - 0.00284715*T**2 - 21.204*T*log(T) + 137.560219*T - 8553.651 + 293690/T, And(T < 1527.0, T >= 298.15)), (-1.119065e-6*T**3 + 0.021078651*T**2 - 103.9843*T*log(T) + 772.405844*T - 121305.858 + 27251743/T, And(T < 3000.0, T >= 1527.0)))),
 ('BI',
  Piecewise((-8.381598e-6*T**3 + 0.012338888*T**2 - 28.4096529*T*log(T) + 128.418925*T - 7817.776, And(T < 544.55, T >= 298.15)), (1.3499885e-5*T**3 - 0.075311163*T**2 + 51.8556592*T*log(T) - 393.650351*T + 30208.022 - 3616168/T + 1.66145e+25/T**9, And(T < 800.0, T >= 544.55)), (-1.046e-6*T**3 + 0.0074266*T**2 - 35.9824*T*log(T) + 182.548971*T - 11045.664 + 1.66145e+25/T**9, And(T < 1200.0, T >= 800.0)), (-27.196*T*log(T) + 124.77144*T - 7581.312 + 1.66145e+25/T**9, And(T < 3000.0, T >= 1200.0)))),
 ('CA',
  Piecewise((-0.01110455*T**2 - 16.3138*T*log(T) + 72.794266*T - 4955.062 - 133574/T, And(T < 1115.0, T >= 298.15)), (-1.2438e-6*T**3 + 0.023733814*T**2 - 114.292247*T*log(T) + 799.982066*T - 107304.428 + 18245540/T, And(T < 3000.0, T >= 1115.0)))),
 ('CC',
  Piecewise((-0.0004723*T**2 - 24.3*T*log(T) + 170.73*T - 17368.441 + 2562600/T - 264300000.0/T**2 + 12000000000.0/T**3, And(T < 6000.0, T >= 298.15)))),
 ('CD',
  Piecewise((-0.006273908*T**2 - 22.0442408*T*log(T) + 99.506198*T - 7083.469 - 6966/T, And(T < 594.22, T >= 298.15)), (-8.99604e-7*T**3 + 0.008832011*T**2 - 45.1611543*T*log(T) + 256.812233*T - 20064.971 + 1241290/T, And(T < 1500.0, T >= 594.22)), (-29.7064*T*log(T) + 148.20548*T - 9027.489, And(T < 1600.0, T >= 1500.0)))),
 ('CE',
  Piecewise((-3.20773e-7*T**3 - 0.0067103*T**2 - 22.3664*T*log(T) + 84.23022*T - 7160.519 - 18117/T, And(T < 1000.0, T >= 298.15)), (-1.930297e-6*T**3 + 0.026046487*T**2 - 101.32248*T*log(T) + 659.4604*T - 79678.506 + 11531707/T, And(T < 2000.0, T >= 1000.0)), (-37.6978*T*log(T) + 190.370192*T - 14198.639, And(T < 4000.0, T >= 2000.0)))),
 ('CO',
  Piecewise((-1.7348e-7*T**3 - 0.002654739*T**2 - 25.0861*T*log(T) + 133.36601*T + 310.241 + 72527/T, And(T < 1768.0, T >= 298.15)), (-40.5*T*log(T) + 253.28374*T - 17197.666 + 9.3488e+30/T**9, And(T < 6000.0, T >= 1768.0)))),
 ('CR',
  Piecewise((-1.47721e-6*T**3 + 0.00189435*T**2 - 26.908*T*log(T) + 157.48*T - 8856.94 + 139250/T, And(T < 2180.0, T >= 298.15)), (-50*T*log(T) + 344.18*T - 34869.344 - 2.88526e+32/T**9, And(T < 6000.0, T >= 2180.0)))),
 ('CS',
  Piecewise((-0.000127907669*T**3 + 0.2029422*T**2 - 90.5212584*T*log(T) + 436.899787*T - 17373.82 + 245245/T, And(T < 301.59, T >= 200.0)), (-4.074846e-6*T**3 + 0.02043269*T**2 - 46.7273304*T*log(T) + 218.689955*T - 13553.817 + 181528/T + 7.8016e+21/T**9, And(T < 2000.0, T >= 301.59)))),
 ('CU',
  Piecewise((1.29223e-7*T**3 - 0.00265684*T**2 - 24.112392*T*log(T) + 130.485235*T - 7770.458 + 52478/T, And(T < 1357.77, T >= 298.15)), (-31.38*T*log(T) + 183.803828*T - 13542.026 + 3.64167e+29/T**9, And(T < 3200.0, T >= 1357.77)))),
 ('DY',
  Piecewise((-5.86914125e-7*T**3 - 0.000761683657*T**2 - 26.3917167*T*log(T) + 102.307412*T - 7937.16586 + 4010.90565/T, And(T < 1000.0, T >= 100.0)), (-3.49702836e-6*T**3 + 0.0166909801*T**2 - 43.8283359*T*log(T) + 214.012934*T - 13733.328 + 0.0173619874/T, And(T < 1654.15, T >= 1000.0)), (-2.76169148e-6*T**3 + 0.0578301681*T**2 - 272.123952*T*log(T) + 2032.1415*T - 404681.371 + 109616238.0/T, And(T < 3000.0, T >= 1654.15)))),
 ('ER',
  Piecewise((-9.52557e-7*T**3 + 0.000995792*T**2 - 28.3846744*T*log(T) + 116.698964*T - 8489.136 + 9581/T, And(T < 1802.0, T >= 298.15)), (-3.041405e-6*T**3 + 0.065950553*T**2 - 298.135131*T*log(T) + 2233.10212*T - 445688.206 + 123973199.0/T, And(T < 3200.0, T >= 1802.0)))),
 ('EU',
  Piecewise((-4.006564e-6*T**3 + 0.00931735*T**2 - 32.8418896*T*log(T) + 135.836737*T - 9864.965 + 102717/T, And(T < 1095.0, T >= 298.15)), (-8.809866e-6*T**3 + 0.114530917*T**2 - 309.357101*T*log(T) + 2174.73304*T - 287423.476 + 48455305/T, And(T < 1900.0, T >= 1095.0)))),
 ('FE',
  Piecewise((-5.8927e-8*T**3 - 0.00439752*T**2 - 23.5143*T*log(T) + 124.134*T + 1225.7 + 77359/T, And(T < 1811.0, T >= 298.15)), (-46*T*log(T) + 299.31255*T - 25383.581 + 2.29603e+31/T**9, And(T < 6000.0, T >= 1811.0)))),
 ('GA',
  Piecewise((-0.000118575257*T**3 + 0.227155636*T**2 - 108.228783*T*log(T) + 585.263691*T - 21312.331 + 439954/T, And(T < 302.91, T >= 200.0)), (-4.0173e-8*T**3 + 0.0001506*T**2 - 26.0692906*T*log(T) + 132.73019*T - 7055.643 - 118332/T + 1.64547e+23/T**9, And(T < 4000.0, T >= 302.91)))),
 ('GD',
  Piecewise((-3.14674076e-7*T**3 - 0.00285240521*T**2 - 24.7214131*T*log(T) + 97.13101*T - 6834.5855 - 8665.73348/T, And(T < 1000.0, T >= 200.0)), (-6.61211607e-7*T**3 - 0.00185225011*T**2 - 24.6598297*T*log(T) + 95.6919924*T - 6483.25362, And(T < 1508.15, T >= 1000.0)), (-6.39165948e-7*T**3 + 0.0150644246*T**2 - 101.800197*T*log(T) + 699.125537*T - 123124.992 + 29356890.3/T, And(T < 3600.0, T >= 1508.15)))),
 ('GE',
  Piecewise((-1.513694e-6*T**3 + 0.005568297*T**2 - 29.5337682*T*log(T) + 165.635573*T - 9486.153 + 163298/T, And(T < 900.0, T >= 298.15)), (-0.003672527*T**2 - 19.8536239*T*log(T) + 102.86087*T - 5689.239, And(T < 1211.4, T >= 900.0)), (-27.6144*T*log(T) + 156.708024*T - 9548.204 - 8.59809e+28/T**9, And(T < 3200.0, T >= 1211.4)))),
 ('HF',
  Piecewise((-4.77e-10*T**3 - 0.004146145*T**2 - 22.7075*T*log(T) + 110.744026*T - 6987.297 - 22590/T, And(T < 2506.0, T >= 298.15)), (-7.575759e-6*T**3 + 0.1735215*T**2 - 787.536383*T*log(T) + 6193.60999*T - 1446776.33 + 501742495.0/T, And(T < 3000.0, T >= 2506.0)))),
 ('HG',
  Piecewise((0.00118398213*T**3 - 2.0282337*T**2 + 618.193308*T*log(T) - 3348.19466*T + 82356.855 - 2366612/T, And(T < 234.32, T >= 200.0)), (-3.20695e-6*T**3 + 0.0097977*T**2 - 32.257*T*log(T) + 135.232291*T - 8961.207 + 6670/T, And(T < 400.0, T >= 234.32)), (-1.077802e-6*T**3 + 0.00318535*T**2 - 28.414*T*log(T) + 112.33345*T - 7970.627 - 41095/T, And(T < 700.0, T >= 400.0)), (8.737e-9*T**3 - 0.00166775*T**2 - 24.87*T*log(T) + 90.797305*T - 7161.338 - 27495/T, And(T < 2000.0, T >= 700.0)))),
 ('HO',
  Piecewise((2.375467e-6*T**3 - 0.00827315*T**2 - 23.4879*T*log(T) + 86.593171*T - 7612.429, And(T < 600.0, T >= 298.15)), (-4.829733e-6*T**3 + 0.01820065*T**2 - 39.6932*T*log(T) + 182.475691*T - 10917.688, And(T < 900.0, T >= 600.0)), (3.233133e-6*T**3 - 0.0424634*T**2 + 48.0595*T*log(T) - 421.474473*T + 46646.188 - 7185900/T, And(T < 1200.0, T >= 900.0)), (-1.112352e-6*T**3 - 0.01082725*T**2 + 8.28608*T*log(T) - 156.162846*T + 27786.061 - 6183850/T, And(T < 1703.0, T >= 1200.0)), (-6.824652e-6*T**3 + 0.139111904*T**2 - 558.950682*T*log(T) + 4248.37906*T - 825364.662 + 219952973.0/T, And(T < 3000.0, T >= 1703.0)))),
 ('IN',
  Piecewise((-2.120321e-6*T**3 - 0.00572566*T**2 - 21.8386*T*log(T) + 92.338115*T - 6978.89 - 22906/T, And(T < 429.75, T >= 298.15)), (-8.367e-8*T**3 + 0.00054607*T**2 - 27.4562*T*log(T) + 124.476588*T - 7033.516 - 211708/T + 3.53116e+22/T**9, And(T < 3800.0, T >= 429.75)))),
 ('IR',
  Piecewise((-0.003091976*T**2 - 22.7944*T*log(T) + 118.780119*T - 6936.288 - 20083/T, And(T < 1215.0, T >= 298.15)), (-4.7969e-7*T**3 - 26.085*T*log(T) + 140.066697*T - 8123.73, And(T < 2719.0, T >= 1215.0)), (1.844977e-6*T**3 - 0.047176402*T**2 + 152.498874*T*log(T) - 1258.35297*T + 290529.037 - 92987250/T, And(T < 4000.0, T >= 2719.0)))),
 ('KK',
  Piecewise((-8.4949147e-5*T**3 + 0.146211135*T**2 - 77.0571464*T*log(T) + 389.624197*T - 16112.929 + 243385/T, And(T < 336.53, T >= 200.0)), (-2.64387e-6*T**3 + 0.012167386*T**2 - 39.2885968*T*log(T) + 192.586544*T - 11122.441 + 43251/T + 1.19223e+22/T**9, And(T < 2200.0, T >= 336.53)))),
 ('LA',
  Piecewise((-0.001295165*T**2 - 26.34*T*log(T) + 120.284604*T - 7968.403, And(T < 550.0, T >= 298.15)), (6.8932e-7*T**3 - 0.008371705*T**2 - 17.1659411*T*log(T) + 59.06113*T - 3381.413 - 399448/T, And(T < 2000.0, T >= 550.0)), (-34.3088*T*log(T) + 181.390071*T - 15608.882, And(T < 4000.0, T >= 2000.0)))),
 ('LI',
  Piecewise((-1.9869816e-5*T**3 + 0.035466931*T**2 - 38.940488*T*log(T) + 217.637482*T - 10583.817 + 159994/T, And(T < 453.6, T >= 200.0)), (-0.000571066077*T**3 + 2.25832944*T**2 - 1702.88865*T*log(T) + 10547.8799*T - 559579.123 + 33885874/T, And(T < 500.0, T >= 453.6)), (-4.38058e-7*T**3 + 0.002633221*T**2 - 31.2283718*T*log(T) + 179.278285*T - 9062.994 - 102387/T, And(T < 3000.0, T >= 500.0)))),
 ('LU',
  Piecewise((-1.790717e-6*T**3 + 0.00519165*T**2 - 29.812*T*log(T) + 146.536283*T - 8788.329 + 39723/T, And(T < 700.0, T >= 298.15)), (-1.50147e-6*T**3 + 0.00371416*T**2 - 29.0095*T*log(T) + 142.327643*T - 9043.057 + 141549/T, And(T < 1700.0, T >= 700.0)), (-0.0119001*T**2 - 1.83986*T*log(T) - 46.91844*T + 6940.092, And(T < 1936.0, T >= 1700.0)), (-1.661174e-6*T**3 + 0.041800748*T**2 - 239.019502*T*log(T) + 1829.37943*T - 404023.691 + 124825465.0/T, And(T < 3700.0, T >= 1936.0)))),
 ('MG',
  Piecewise((-1.393669e-6*T**3 + 0.0004858*T**2 - 26.1849782*T*log(T) + 143.675547*T - 8367.34 + 78950/T, And(T < 923.0, T >= 298.15)), (-34.3088*T*log(T) + 204.716215*T - 14130.185 + 1.038192e+28/T**9, And(T < 3000.0, T >= 923.0)))),
 ('MN',
  Piecewise((-0.00734768*T**2 - 23.4582*T*log(T) + 130.059*T - 8115.28 + 69827/T, And(T < 1519.0, T >= 298.15)), (-48*T*log(T) + 312.2648*T - 28733.41 + 1.656847e+30/T**9, And(T < 2000.0, T >= 1519.0)))),
 ('MO',
  Piecewise((-1.30927e-10*T**4 + 5.66283e-7*T**3 - 0.003443396*T**2 - 23.56414*T*log(T) + 131.9197*T - 7746.302 + 65812/T, And(T < 2896.0, T >= 298.15)), (-42.63829*T*log(T) + 283.559746*T - 30556.41 - 4.849315e+33/T**9, And(T < 5000.0, T >= 2896.0)))),
 ('NA',
  Piecewise((-4.3638283e-5*T**3 + 0.072306633*T**2 - 51.0393608*T*log(T) + 260.548732*T - 11989.434 + 132154/T, And(T < 370.87, T >= 200.0)), (-1.70664e-6*T**3 + 0.009745854*T**2 - 38.1198801*T*log(T) + 199.619999*T - 11009.884 + 34342/T + 1.65071e+23/T**9, And(T < 2300.0, T >= 370.87)))),
 ('NB',
  Piecewise((-3.5012e-7*T**3 + 0.000203475*T**2 - 26.4711*T*log(T) + 142.045475*T - 8519.353 + 93399/T, And(T < 2750.0, T >= 298.15)), (-41.77*T*log(T) + 271.720843*T - 37669.3 + 1.528238e+32/T**9, And(T < 6000.0, T >= 2750.0)))),
 ('ND',
  Piecewise((-2.6923e-6*T**3 + 0.000556125*T**2 - 27.0858*T*log(T) + 111.10239*T - 8402.93 + 34887/T, And(T < 900.0, T >= 298.15)), (-1.802e-6*T**3 - 0.00420402*T**2 - 22.7536*T*log(T) + 83.662617*T - 6984.083, And(T < 1128.0, T >= 900.0)), (-6.048207e-6*T**3 + 0.078615997*T**2 - 238.182873*T*log(T) + 1673.04075*T - 225610.846 + 38810350/T, And(T < 1799.0, T >= 1128.0)), (-48.7854*T*log(T) + 276.257088*T - 25742.331, And(T < 1800.0, T >= 1799.0)))),
 ('NI',
  Piecewise((-0.0048407*T**2 - 22.096*T*log(T) + 117.854*T - 5179.159, And(T < 1728.0, T >= 298.15)), (-43.1*T*log(T) + 279.135*T - 27840.655 + 1.12754e+31/T**9, And(T < 3000.0, T >= 1728.0)))),
 ('N',
  Piecewise((2.681e-9*T**3 - 0.00176686*T**2 - 12.7819*T*log(T) - 9.45425*T - 3750.675 - 32374/T, And(T < 950.0, T >= 298.15)), (3.0097e-8*T**3 - 0.00065107*T**2 - 16.3699*T*log(T) + 17.2003*T - 7358.85 + 563070/T, And(T < 3350.0, T >= 950.0)), (-8.333e-9*T**3 + 0.000239754*T**2 - 20.4695*T*log(T) + 50.26*T - 16392.8 + 4596375/T, And(T < 6000.0, T >= 3350.0)))),
 ('NP',
  Piecewise((-0.04127725*T**2 + 4.0543*T*log(T) - 57.531347*T + 241.888 - 402857/T, And(T < 553.0, T >= 298.15)), (-2.483917e-6*T**3 + 0.0284592*T**2 - 102.523*T*log(T) + 664.27337*T - 57015.112 + 4796910/T, And(T < 1799.0, T >= 553.0)), (-45.3964*T*log(T) + 255.780866*T - 12092.736, And(T < 4000.0, T >= 1799.0)))),
 ('O',
  Piecewise((6.61845833e-7*T**3 - 0.005098875*T**2 - 11.1355*T*log(T) - 25.503038*T - 3480.87 - 38365/T, And(T < 1000.0, T >= 298.15)), (6.781e-9*T**3 - 0.0005957975*T**2 - 16.8138*T*log(T) + 12.659879*T - 6568.763 + 262905/T, And(T < 3300.0, T >= 1000.0)), (1.0721e-8*T**3 - 0.000425243*T**2 - 18.9536*T*log(T) + 31.259624*T - 13986.728 + 4383200/T, And(T < 6000.0, T >= 3300.0)))),
 ('OS',
  Piecewise((-0.00190427*T**2 - 23.5710242*T*log(T) + 126.369531*T - 7196.978, And(T < 3306.0, T >= 298.15)), (1.173861e-6*T**3 - 0.042489827*T**2 + 224.998034*T*log(T) - 1935.2137*T + 644910.07 - 312569031.0/T, And(T < 5500.0, T >= 3306.0)))),
 ('PA',
  Piecewise((-0.00621325*T**2 - 23.9116*T*log(T) + 111.973215*T - 7681.561, And(T < 1443.0, T >= 298.15)), (1.884933e-6*T**3 - 0.0263416*T**2 + 16.305*T*log(T) - 177.320253*T + 27955.763 - 5908900/T, And(T < 2176.0, T >= 1443.0)), (-47.2792*T*log(T) + 288.308639*T - 29949.683, And(T < 4000.0, T >= 2176.0)))),
 ('PB',
  Piecewise((-2.4395e-7*T**3 - 0.00365895*T**2 - 24.5242231*T*log(T) + 101.700244*T - 7650.085, And(T < 600.61, T >= 298.15)), (0.00154613*T**2 - 32.4913959*T*log(T) + 154.243182*T - 10531.095 + 8.05448e+25/T**9, And(T < 1200.0, T >= 600.61)), (9.8144e-8*T**3 - 0.002882943*T**2 - 18.9640637*T*log(T) + 53.139072*T + 4157.616 - 2696755/T + 8.05448e+25/T**9, And(T < 2100.0, T >= 1200.0)))),
 ('PD',
  Piecewise((-1.919875e-6*T**3 + 0.007120975*T**2 - 32.211*T*log(T) + 176.076315*T - 10204.027 + 168687/T, And(T < 900.0, T >= 298.15)), (1.91115e-7*T**3 - 0.00717522*T**2 - 13.5708*T*log(T) + 49.659892*T + 917.062 - 1112465/T, And(T < 1828.0, T >= 900.0)), (-6.2811e-8*T**3 + 0.002091396*T**2 - 54.2067086*T*log(T) + 370.102147*T - 67161.018 + 18683526/T, And(T < 4000.0, T >= 1828.0)))),
 ('P',
  Piecewise((-0.000104022667*T**3 + 0.290708*T**2 - 178.426*T*log(T) + 1026.69389*T - 43821.799 + 1632695/T, And(T < 317.3, T >= 250.0)), (-2.2829e-7*T**3 + 0.001715669*T**2 - 28.7335301*T*log(T) + 152.341487*T - 9587.448 + 172966/T, And(T < 1000.0, T >= 317.3)), (-26.326*T*log(T) + 135.876831*T - 8093.075, And(T < 3000.0, T >= 1000.0)))),
 ('PR',
  Piecewise((-2.5184333e-5*T**3 + 0.072929*T**2 - 68.9176*T*log(T) + 356.587384*T - 18803.379 + 507385/T, And(T < 500.0, T >= 298.15)), (-1.22951e-6*T**3 - 0.00497126*T**2 - 22.8909*T*log(T) + 82.427384*T - 7246.848, And(T < 800.0, T >= 500.0)), (1.5592233e-5*T**3 - 0.1288205*T**2 + 146.764*T*log(T) - 1073.55111*T + 95411.023 - 11588800/T, And(T < 1068.0, T >= 800.0)), (-3.0994702e-5*T**3 + 0.305181506*T**2 - 606.120311*T*log(T) + 4234.33311*T - 481663.131 + 70926840/T, And(T < 1204.0, T >= 1068.0)), (-42.9697*T*log(T) + 227.685155*T - 20014.678, And(T < 3800.0, T >= 1204.0)))),
 ('PT',
  Piecewise((-2.0138e-8*T**3 - 0.00248297*T**2 - 24.5526*T*log(T) + 124.388275*T - 7595.631 + 7974/T, And(T < 1300.0, T >= 298.15)), (-6.56946e-7*T**3 + 0.002321665*T**2 - 30.2527*T*log(T) + 161.529615*T - 9253.174 - 272106/T, And(T < 2041.5, T >= 1300.0)), (-7.59259e-7*T**3 + 0.020454938*T**2 - 136.192996*T*log(T) + 1019.35892*T - 222048.216 + 71539020/T, And(T < 4000.0, T >= 2041.5)))),
 ('PU',
  Piecewise((-0.02241*T**2 - 18.1258*T*log(T) + 80.301382*T - 7396.309, And(T < 400.0, T >= 298.15)), (2.63443e-7*T**3 - 0.00134493*T**2 - 42.4187*T*log(T) + 236.786603*T - 16605.962 + 579325/T, And(T < 944.0, T >= 400.0)), (-42.248*T*log(T) + 232.961553*T - 14462.156, And(T < 3000.0, T >= 944.0)))),
 ('RB',
  Piecewise((-0.000152236932*T**3 + 0.26277612*T**2 - 115.282589*T*log(T) + 583.580988*T - 21669.733 + 385754/T, And(T < 312.46, T >= 200.0)), (-4.6822e-7*T**3 + 0.000412369*T**2 - 29.1775424*T*log(T) + 117.050578*T - 7823.397 - 126310/T - 5.55029e+22/T**9, And(T < 900.0, T >= 312.46)), (-4.829082e-6*T**3 + 0.033795632*T**2 - 77.7006456*T*log(T) + 450.974149*T - 39488.142 + 3778006/T - 5.55029e+22/T**9, And(T < 1600.0, T >= 900.0)), (-8.61653e-6*T**3 + 0.08161687*T**2 - 191.262774*T*log(T) + 1287.78947*T - 159742.511 + 27738456/T - 5.55029e+22/T**9, And(T < 2100.0, T >= 1600.0)))),
 ('RE',
  Piecewise((1.92818e-7*T**3 - 0.00253505*T**2 - 24.348*T*log(T) + 128.421589*T - 7695.279 + 32915/T, And(T < 1200.0, T >= 298.15)), (-2.81835e-7*T**3 + 0.00224565*T**2 - 33.586*T*log(T) + 194.667426*T - 15775.998 + 1376270/T, And(T < 2400.0, T >= 1200.0)), (-7.88955e-7*T**3 + 0.01184945*T**2 - 67.956*T*log(T) + 462.110749*T - 70882.739 + 18075200/T, And(T < 3458.0, T >= 2400.0)), (1.053726e-6*T**3 - 0.033764567*T**2 + 140.831655*T*log(T) - 1211.37186*T + 346325.888 - 134548866.0/T, And(T < 5000.0, T >= 3458.0)), (-49.519*T*log(T) + 346.997842*T - 78564.296, And(T < 6000.0, T >= 5000.0)))),
 ('RH',
  Piecewise((-1.68032e-7*T**3 - 0.003424186*T**2 - 24.0178336*T*log(T) + 132.020923*T - 7848.828 + 55846/T, And(T < 1200.0, T >= 298.15)), (-1.512774e-6*T**3 + 0.00966345*T**2 - 48.3766632*T*log(T) + 305.771019*T - 28367.852 + 3348162/T, And(T < 2237.0, T >= 1200.0)), (-5.3978814e-5*T**3 + 1.04921361*T**2 - 3874.21058*T*log(T) + 30151.6342*T - 6237470.48 + 1880362180.0/T, And(T < 2450.0, T >= 2237.0)), (-50.58456*T*log(T) + 344.889895*T - 44863.489, And(T < 2500.0, T >= 2450.0)))),
 ('RU',
  Piecewise((1.7641e-7*T**3 - 0.004062566*T**2 - 22.9143287*T*log(T) + 127.866233*T - 7561.873 + 56377/T, And(T < 1500.0, T >= 298.15)), (-1.952433e-6*T**3 + 0.018726245*T**2 - 72.3241219*T*log(T) + 489.516214*T - 59448.103 + 11063885/T, And(T < 2607.0, T >= 1500.0)), (-0.000240245985*T**3 + 5.221639*T**2 - 21329.705*T*log(T) + 168610.517*T - 38588773 + 13082992600.0/T, And(T < 2740.0, T >= 2607.0)), (-51.8816*T*log(T) + 364.482314*T - 55768.304, And(T < 4500.0, T >= 2740.0)))),
 ('SB',
  Piecewise((-3.003415e-6*T**3 + 0.007748768*T**2 - 30.5130752*T*log(T) + 156.154689*T - 9242.858 + 100625/T, And(T < 903.78, T >= 298.15)), (-31.38*T*log(T) + 169.485872*T - 11738.83 + 1.616849e+27/T**9, And(T < 2000.0, T >= 903.78)))),
 ('SC',
  Piecewise((-1.64531e-6*T**3 + 0.00321892*T**2 - 28.1882*T*log(T) + 153.48097*T - 8689.547 + 72177/T, And(T < 800.0, T >= 298.15)), (-8.59345e-7*T**3 - 0.000573295*T**2 - 24.9132*T*log(T) + 132.759582*T - 7511.295, And(T < 1608.0, T >= 800.0)), (8.7398e-6*T**3 - 0.117529396*T**2 + 241.441051*T*log(T) - 1817.92245*T + 261143.04 - 50607159/T, And(T < 2000.0, T >= 1608.0)), (-44.2249*T*log(T) + 286.474338*T - 30515.246, And(T < 3200.0, T >= 2000.0)))),
 ('SE',
  Piecewise((-1.5318461e-5*T**3 + 0.02424314*T**2 - 33.6527*T*log(T) + 174.205877*T - 9376.371 + 102249/T, And(T < 494.0, T >= 298.15)), (-5.611026e-6*T**3 + 0.037144892*T**2 - 81.2006585*T*log(T) + 507.111538*T - 37546.134 + 2614263/T, And(T < 800.0, T >= 494.0)), (-35.1456*T*log(T) + 197.770166*T - 12193.47, And(T < 1000.0, T >= 800.0)))),
 ('SI',
  Piecewise((-3.552e-9*T**3 - 0.001912904*T**2 - 22.8317533*T*log(T) + 137.236859*T - 8162.609 + 176667/T, And(T < 1687.0, T >= 298.15)), (-27.196*T*log(T) + 167.281367*T - 9457.642 - 4.20369e+30/T**9, And(T < 3600.0, T >= 1687.0)))),
 ('SM',
  Piecewise((1.010345e-5*T**3 - 0.050254*T**2 - 1.6485*T*log(T) - 32.10748*T - 3872.013 - 82168/T, And(T < 700.0, T >= 298.15)), (-7.538383e-6*T**3 + 0.0474522*T**2 - 102.665*T*log(T) + 627.869894*T - 50078.215 + 3861770/T, And(T < 1190.0, T >= 700.0)), (2.7512152e-5*T**3 - 0.254986338*T**2 + 381.41982*T*log(T) - 2744.50976*T + 289719.819 - 40102102/T, And(T < 1345.0, T >= 1190.0)), (-50.208*T*log(T) + 282.194375*T - 23056.079, And(T < 2100.0, T >= 1345.0)))),
 ('SN',
  Piecewise((-3.192767e-6*T**3 + 0.00051185*T**2 - 25.858*T*log(T) + 122.765451*T - 7958.517 + 18440/T, And(T < 250.0, T >= 100.0)), (3.121167e-6*T**3 - 0.0188702*T**2 - 15.961*T*log(T) + 65.443315*T - 5855.135 - 61960/T, And(T < 505.08, T >= 250.0)), (2.623131e-6*T**3 - 0.016814429*T**2 - 8.2590486*T*log(T) + 4.005269*T + 2524.724 - 1081244/T - 1.2307e+25/T**9, And(T < 800.0, T >= 505.08)), (-28.4512*T*log(T) + 138.99688*T - 8256.959 - 1.2307e+25/T**9, And(T < 3000.0, T >= 800.0)))),
 ('SR',
  Piecewise((-1.67477e-7*T**3 - 0.00461225*T**2 - 23.905*T*log(T) + 107.183879*T - 7532.367 - 2055/T, And(T < 820.0, T >= 298.15)), (1.84189e-7*T**3 - 0.003251266*T**2 - 30.0905432*T*log(T) + 153.196104*T - 13380.102 + 850134/T, And(T < 3000.0, T >= 820.0)))),
 ('S',
  Piecewise((7.754333e-6*T**3 - 0.026529*T**2 - 11.007*T*log(T) + 55.417762*T - 5228.956, And(T < 368.3, T >= 298.15)), (1.402558e-6*T**3 - 0.010895125*T**2 - 17.941839*T*log(T) + 94.692922*T - 6513.769 + 39910/T, And(T < 1300.0, T >= 368.3)))),
 ('TA',
  Piecewise((1.70109e-7*T**3 - 0.002623033*T**2 - 23.7592624*T*log(T) + 119.139857*T - 7285.889 - 3293/T, And(T < 1300.0, T >= 298.15)), (-6.55136e-7*T**3 + 0.006167572*T**2 - 41.137088*T*log(T) + 243.88676*T - 22389.955 + 2429586/T, And(T < 2500.0, T >= 1300.0)), (1.95033e-7*T**3 - 0.017983376*T**2 + 78.5244752*T*log(T) - 722.59722*T + 229382.886 - 93813648/T, And(T < 3290.0, T >= 2500.0)), (-1.055148e-6*T**3 + 0.043117795*T**2 - 362.159132*T*log(T) + 2985.49125*T - 1042384.01 + 554714342.0/T, And(T < 6000.0, T >= 3290.0)))),
 ('TB',
  Piecewise((-2.5672833e-5*T**3 + 0.0832265*T**2 - 77.5006*T*log(T) + 409.309555*T - 20842.158 + 562430/T, And(T < 600.0, T >= 298.15)), (-8.05838e-7*T**3 - 0.002757005*T**2 - 25.8659*T*log(T) + 102.61162*T - 8772.606 + 172355/T, And(T < 1200.0, T >= 600.0)), (-1.067632e-6*T**3 - 0.001676335*T**2 - 25.9584*T*log(T) + 101.7776*T - 7944.942, And(T < 1562.0, T >= 1200.0)), (-2.044697e-6*T**3 + 0.041615159*T**2 - 200.215695*T*log(T) + 1456.04268*T - 265240.309 + 65043790/T, And(T < 3000.0, T >= 1562.0)))),
 ('TC',
  Piecewise((-0.002954747*T**2 - 24.3394*T*log(T) + 132.5101*T - 7947.794 + 63855/T, And(T < 2430.0, T >= 298.15)), (-47*T*log(T) + 318.286*T - 47759.99 + 6.63829e+32/T**9, And(T < 4000.0, T >= 2430.0)))),
 ('TE',
  Piecewise((-5.240417e-6*T**3 + 0.01583435*T**2 - 35.6687*T*log(T) + 183.372894*T - 10544.679 + 155015/T, And(T < 722.66, T >= 298.15)), (5.006367e-6*T**3 - 0.0362361*T**2 + 13.004*T*log(T) - 129.265373*T + 9160.595 - 1286810/T, And(T < 1150.0, T >= 722.66)), (-32.5596*T*log(T) + 174.901226*T - 12781.349, And(T < 1600.0, T >= 1150.0)))),
 ('TH',
  Piecewise((-5.2883e-7*T**3 - 0.00236725*T**2 - 24.841*T*log(T) + 117.022775*T - 7732.08 + 13010/T, And(T < 1633.0, T >= 298.15)), (2.36893e-7*T**3 - 0.00358025*T**2 - 39.107*T*log(T) + 237.654918*T - 37352.871 + 7981000/T, And(T < 2900.0, T >= 1633.0)), (-46.024*T*log(T) + 283.979845*T - 33353.313, And(T < 4000.0, T >= 2900.0)))),
 ('TI',
  Piecewise((1.06716e-7*T**3 - 0.004777975*T**2 - 23.9933*T*log(T) + 133.615208*T - 8059.921 + 72636/T, And(T < 900.0, T >= 298.15)), (-9.0876e-8*T**3 - 0.0042033*T**2 - 23.9887*T*log(T) + 132.988068*T - 7811.815 + 42680/T, And(T < 1155.0, T >= 900.0)), (2.02715e-7*T**3 - 0.0081465*T**2 - 14.9466*T*log(T) + 66.976538*T + 908.837 - 1477660/T, And(T < 1941.0, T >= 1155.0)), (-3.04747e-7*T**3 + 0.008204849*T**2 - 87.2182461*T*log(T) + 638.806871*T - 124526.786 + 36699805/T, And(T < 4000.0, T >= 1941.0)))),
 ('TL',
  Piecewise((-1.21807e-7*T**3 - 0.0033063*T**2 - 25.2274*T*log(T) + 107.140405*T - 8104.038 + 42058/T, And(T < 577.0, T >= 200.0)), (-5.19136e-7*T**3 + 0.005228106*T**2 - 38.4130658*T*log(T) + 196.771926*T - 15406.859 + 729665/T, And(T < 1800.0, T >= 577.0)))),
 ('TM',
  Piecewise((-3.831156e-6*T**3 + 0.012110965*T**2 - 34.3664974*T*log(T) + 151.037648*T - 10016.715 + 95982/T, And(T < 700.0, T >= 298.15)), (-3.96694e-7*T**3 + 0.000444753*T**2 - 32.1951269*T*log(T) + 147.957496*T - 14701.965 + 1091664/T, And(T < 1600.0, T >= 700.0)), (-0.003384563*T**2 - 25.1816969*T*log(T) + 97.98144*T - 8669.227, And(T < 1818.0, T >= 1600.0)), (1.1689185e-5*T**3 - 0.19093039*T**2 + 534.082763*T*log(T) - 4147.40063*T + 727125.608 - 180382220.0/T, And(T < 2300.0, T >= 1818.0)))),
 ('U',
  Piecewise((-4.42605e-6*T**3 + 0.00125156*T**2 - 26.9182*T*log(T) + 130.955151*T - 8407.734 + 38568/T, And(T < 955.0, T >= 298.15)), (-48.66*T*log(T) + 292.121093*T - 22521.8, And(T < 3000.0, T >= 955.0)))),
 ('V',
  Piecewise((1.2175e-7*T**3 - 0.003098*T**2 - 24.134*T*log(T) + 133.346053*T - 7930.43 + 69460/T, And(T < 790.0, T >= 298.15)), (-6.8e-7*T**3 + 6.25e-5*T**2 - 25.9*T*log(T) + 143.291093*T - 7967.842, And(T < 2183.0, T >= 790.0)), (-47.43*T*log(T) + 321.140783*T - 41689.864 + 6.44389e+31/T**9, And(T < 4000.0, T >= 2183.0)))),
 ('W',
  Piecewise((-5.33e-11*T**4 + 2.07e-7*T**3 - 0.001936*T**2 - 24.1*T*log(T) + 130.4*T - 7646.311 + 44500/T, And(T < 3695.0, T >= 298.15)), (-54*T*log(T) + 389.362335*T - 82868.801 + 1.528621e+33/T**9, And(T < 6000.0, T >= 3695.0)))),
 ('YB',
  Piecewise((-2.2242e-5*T**3 + 0.04227115*T**2 - 40.0791*T*log(T) + 189.327664*T - 9370.941, And(T < 553.0, T >= 298.15)), (-0.00256065*T**2 - 26.7591*T*log(T) + 121.065655*T - 8192.154, And(T < 1033.0, T >= 553.0)), (1.421719e-6*T**3 - 0.017961331*T**2 + 2.7623966*T*log(T) - 89.478241*T + 16034.89 - 3631462/T, And(T < 2000.0, T >= 1033.0)))),
 ('Y',
  Piecewise((-4.17561786e-7*T**3 - 0.00175716414*T**2 - 25.6656992*T*log(T) + 128.572856*T - 8011.09379 + 26911.509/T, And(T < 1000.0, T >= 100.0)), (-8.2534534e-8*T**3 - 0.0038211802*T**2 - 23.4941827*T*log(T) + 114.497104*T - 7179.74574, And(T < 1795.15, T >= 1000.0)), (-7.22513088e-8*T**3 + 0.00231774379*T**2 - 56.9527111*T*log(T) + 382.124727*T - 67480.7761 + 18077162.6/T, And(T < 3700.0, T >= 1795.15)))),
 ('ZN',
  Piecewise((-1.264963e-6*T**3 - 0.001712034*T**2 - 23.701314*T*log(T) + 118.470069*T - 7285.787, And(T < 692.68, T >= 298.15)), (-31.38*T*log(T) + 172.34566*T - 11070.559 + 4.70514e+26/T**9, And(T < 1700.0, T >= 692.68)))),
 ('ZR',
  Piecewise((-0.00437791*T**2 - 24.1618*T*log(T) + 125.64905*T - 7827.595 + 34971/T, And(T < 2128.0, T >= 130.0)), (-42.144*T*log(T) + 262.724183*T - 26085.921 - 1.342896e+31/T**9, And(T < 6000.0, T >= 2128.0))))
])