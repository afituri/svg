#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import csv, codecs, os
from csv_parser import Candidates
from draw import *
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from arabic_reshaper import reshape
import string

out_put = "output"
if not os.path.exists(out_put):
    os.makedirs(out_put)

obj = Candidates
for dist in obj.w:
	dist_path="%s/%s"%(out_put,dist)
	if not os.path.exists(dist_path):
		os.makedirs(dist_path)
	for sub in obj.w[dist]:
		sub_path="%s/%s"%(dist_path,sub)
		if not os.path.exists(sub_path):
			os.makedirs(sub_path)
		for race in obj.w[dist].get(sub):
			for ballot in obj.w[dist][sub][race]:
				#print ballot
				num = obj.w[dist][sub][race][ballot].get('num')
				names = obj.w[dist][sub][race][ballot].get('names')
				voting_district = reshape(obj.w[dist][sub][race][ballot].get('voting_district'))
				constituency = reshape(obj.w[dist][sub][race][ballot].get('constituency'))
				ballot=obj.w[dist][sub][race][ballot].get('ballot_number')
				title1 = reshape('انتخاب مجلس النواب في المرحلة الانتقالية'.decode('utf-8'))
				title2 =reshape(title1)
				title3=reshape('الدائرة الانتخابية '.decode('utf-8'))
				title3+=reshape(constituency)
				dir_path="%s/%s"%(sub_path,race)
				if num <= 12:
					Draw_10(title1,title2,title3,names,1,race,dir_path,num,sub,voting_district,ballot)
				elif num <=24:
					Draw_20(title1,title2,title3,names,1,race,dir_path,num,sub,voting_district,ballot)
				elif num <=48:
					Draw_30(title1,title2,title3,names,1,race,dir_path,num,sub,voting_district,ballot)
				elif num <=66:
					Draw_20(title1,title2,title3,names[0:24],1,race,dir_path,24,sub,voting_district,ballot)
					Draw_20(title1,title2,title3,names[25:49],25,race,dir_path,24,sub,voting_district,ballot)
					Draw_20(title1,title2,title3,names[50:],49,race,dir_path,num-48,sub,voting_district,ballot)
				else :
					rem = num
					start=0
					end=48
					pos=1
					quantity= end-start
					while(rem>=1):
						# print str(len(names[start:end]))+"=>"+str(ballot)+"==>"+str(num)

						Draw_30(title1,title2,title3,names[start:end],pos,race,dir_path,quantity,sub,voting_district,ballot)
						rem = rem-48
						start=end

						if(rem<48):
							end=end+rem+1
						else :
							end=end+48
						pos = start+1
						quantity= end-start
# drawing = svg2rlg("caktus_logo.svg")
drawing = svg2rlg("output/3/Benghazi/General/49.svg")
renderPDF.drawToFile(drawing, "file.pdf")

        # print x.w[dist][sub]

# my_list[:5] # grab the first five elements
#  my_list[-5:]

# delimiter = ';'
# reader = codecs.open("cands.csv", 'r', encoding='utf-8')
# for line in reader:
#     print line
#do something with your row ...

# x=380.854
# y=265
# LEFT = 279
# DOWN = 50
# flag=True

# def draw_name(x,y,number,name):
# 	temp = 	'<rect x="'+str(x)+'" y="'+str(y)+'" fill="none" stroke="#231F20" stroke-miterlimit="10" width="254.108" height="40"/>'\
# 			'<line x1="'+str(x+228.146)+'" y1="'+str(y)+'" x2="'+str(x+228.146)+'" y2="'+str(y+40)+'"  fill="none" stroke-miterlimit="10"'\
# 			' style="stroke:rgb(0,0,0);stroke-width:1" />'\
# 			'<rect x="'+str(x+6.094)+'" y="'+str(y+6.2)+'" fill="none" stroke="#231F20" stroke-miterlimit="10" width="28.347" height="28.347"/>'\
# 			'<text direction="rtl" transform="matrix(1 0 0 1 '+str(x+246.6636)+' '+str(y+24.9663)+')" font-family="ArialMT" font-size="14">'+str(number)+'</text>'\
# 			'<text direction="rtl" transform="matrix(1 0 0 1 '+str(x+221.6636)+' '+str(y+24.9663)+')" font-family="ArialMT" font-weight = "bold" font-size="14">'+name+'</text>'
# 	return temp


# target =""
# reader = codecs.open("cands.csv", 'r', encoding='utf-8')
# pos = 1
# for line in reader:
#     if pos<11:
#     	target+=draw_name(x,y,pos,line)
#     else :
#     	if(flag):
#     		y=265
#     		flag=False
#     	target+=draw_name(x-LEFT,y,pos,line)
#     pos+=1
#     y+=DOWN


# # print(target)

# infile = open('25.svg')
# outfile = open('out.svg', 'w')
# for line in infile:
# 	line = line.replace('XXXX', target)
# 	outfile.write(line.encode('utf8'))
# infile.close()
# outfile.close()