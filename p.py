import requests
from time import time
from time import localtime 
from matplotlib import pyplot as plt 
import tkinter

time= time()
tm= localtime(time)

yyyy= tm.tm_year 
mm= tm.tm_mon
dd=tm.tm_mday

url1= requests.get(f"https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-day.do?stn=1086yy= {yyyy}&mm-{mm}Gobs=1")
url2= requests.get(f"https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-day.do?stn=1086y= {yyyy-10}6mm-{mm}Sobs=1")
url3= requests.get(f"https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-day.do?stn=1086yy= {yyyy-20}6mm={mm}Sobs=1")
url4= requests.get(f"https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-day.do?stn=1086yy= {yyyy-30}&mm={mm}Sobs=1")
url5= requests.get(f"https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-day.do?stn=1086yy= {yyyy-40}6mm={mm}Sobs=1")
url6= requests.get(f"https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-day.do?stn=1085yy {yyyy-50}&mm={mm}&obs=1")
url7= requests.get(f"https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-day.do?stn=1085yy {yyyy-60}&mm={mm}&obs=1")

allstr1 = url1.text
allstr2 = url2.text
allstr3 = url3.text
allstr4 = url4.text
allstr5 = url5.text
allstr6 = url6.text
allstr7 = url7.text

avgtmp1 = 0
avgtmp2 = 0
avgtmp3 = 0
avgtmp4 = 0
avgtmp5 = 0
avgtmp6 = 0
avgtmp7 = 0

for i in range(0, len(allstr1)-4):
    if(allstr1[i] == '평' and allstr1[i+1] =='균' and allstr1[i+2] =='기' and allstr1[i+3] == '온' ): 
        avgtmp1 += 1
    if(avgtmp1 == dd - 1):
        ttmp1 = allstr1[i+5]
        otmp1 = allstr1[i+6]
        ptmp1 = allstr1[i+8]

for i in range(0, len(allstr2)-4):
    if(allstr2[i] == '평' and allstr2[i+1] == '균' and allstr2[i+2] == '기' and allstr2[i+3] == '온' ): 
        avgtmp2 += 1
    if(avgtmp2 == dd - 1):
        ttmp2 = allstr2[i+5]
        otmp2 = allstr2[i+6]
        ptmp2 = allstr2[i+8]

for i in range(0, len(allstr3)-4):
    if(allstr3[i] == '평' and allstr3[i+1] =='균' and allstr3[i+2] =='기' and allstr3[i+3] == '온' ): 
        avgtmp3 += 1
    if(avgtmp3 == dd - 1):
        ttmp3 = allstr3[i+5]
        otmp3 = allstr3[i+6]
        ptmp3 = allstr3[i+8]

for i in range(0, len(allstr4)-4):
    if(allstr4[i] == '평' and allstr4[i+1] =='균' and allstr4[i+2] =='기' and allstr4[i+3] == '온' ): 
        avgtmp4 += 1
    if(avgtmp4 == dd - 1):
        ttmp4 = allstr4[i+5]
        otmp4 = allstr4[i+6]
        ptmp4 = allstr4[i+8]

for i in range(0, len(allstr5)-4):
    if(allstr5[i] == '평' and allstr5[i+1] =='균' and allstr5[i+2] =='기' and allstr5[i+3] == '온' ): 
        avgtmp5 += 1
    if(avgtmp5 == dd - 1):
        ttmp5 = allstr5[i+5]
        otmp5 = allstr5[i+6]
        ptmp5 = allstr5[i+8]

for i in range(0, len(allstr6)-4):
    if(allstr6[i] == '평' and allstr6[i+1] =='균' and allstr6[i+2] =='기' and allstr6[i+3] == '온' ): 
        avgtmp6 += 1
    if(avgtmp6 == dd - 1):
        ttmp6 = allstr6[i+5]
        otmp6 = allstr6[i+6]
        ptmp6 = allstr6[i+8]

for i in range(0, len(allstr7)-4):
    if(allstr7[i] == '평' and allstr7[i+1] =='균' and allstr7[i+2] =='기' and allstr7[i+3] == '온' ): 
        avgtmp7 += 1
    if(avgtmp7 == dd - 1):
        ttmp7 = allstr7[i+5]
        otmp7 = allstr7[i+6]
        ptmp7 = allstr7[i+8]

tmp1 = float (ttmp1) * 10 + float (otmp1) + float (ptmp1) / 10
tmp2 = float (ttmp2) * 10 + float (otmp2) + float (ptmp2) / 10
tmp3 = float (ttmp3) * 10 + float (otmp3) + float (ptmp3) / 10
tmp4 = float (ttmp4) * 10 + float (otmp4) + float (ptmp4) / 10
tmp5 = float (ttmp5) * 10 + float (otmp5) + float (ptmp5) / 10
tmp6 = float (ttmp6) * 10 + float (otmp6) + float (ptmp6) / 10
tmp7 = float (ttmp7) * 10 + float (otmp7) + float (ptmp7) / 10

mtmp = tmp7 - tmp6

x_vals = [yyyy - 60, yyyy - 50, yyyy - 40, yyyy - 30, yyyy - 20, yyyy - 10, yyyy]
y_vals = [tmp7, tmp6, tmp5, tmp4, tmp3, tmp2, tmp1]

plt.plot(x_vals, y_vals)
plt.title("오늘의 시대별 평균기온", fontsize = 17)
plt.show()

