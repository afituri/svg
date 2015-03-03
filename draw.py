# -*- coding: utf-8 -*-
import codecs, os

class Draw_30(object):
	
	def __init__(self, title1,title2,title3,names,pos,type,dir_path,num,sub,voting_district,ballot):
		x=643
		y=249
		LEFT = 279
		DOWN = 50
		flag1=True
		flag2=True
		target =""
		count=1
		headers = draw_headers30(title1,title2,title3,num,sub,voting_district,ballot)
		rem = num%3
		rem1 = num/3+rem+1
		rem2 = num*2/3+rem+1
		if(rem == 2):
			rem1 = num/3+2
			rem2 = num*2/3+2

		for name in names:

		    if count<(rem1):
		    	target+=draw_name(x,y,pos,name)
		    elif count<(rem2) :
		    	if(flag1):
		    		y=249
		    		flag1=False
		    		x=x-LEFT
		    	target+=draw_name(x,y,pos,name)
		    else:
		    	if(flag2):
		    		y=249
		    		flag2=False
		    		x=x-LEFT
		    	target+=draw_name(x,y,pos,name)
		    pos+=1
		    count+=1
		    y+=DOWN
		if not os.path.exists(dir_path):
			os.makedirs(dir_path)
		file_path="%s/%s.svg"%(dir_path,pos)
		infile = open('60.svg')
		outfile = open(file_path, 'w')
		for line in infile:
			line = line.replace('XXXX', target)
			line = line.replace('YYYY', headers)
			outfile.write(line.encode('utf8'))
		infile.close()
		outfile.close()

class Draw_20(object):
	
	def __init__(self, title1,title2,title3,names,pos,type,dir_path,num,sub,voting_district,ballot):
		x=380.854
		y=265
		LEFT = 279
		DOWN = 50
		flag=True
		target =""
		count=1
		headers = draw_headers(title1,title2,title3,num,sub,voting_district,ballot)

		for name in names:
		    if count<=(num/2+(num%2)):
		    	target+=draw_name(x,y,pos,name)
		    else :
		    	if(flag):
		    		y=265
		    		flag=False
		    	target+=draw_name(x-LEFT,y,pos,name)
		    pos+=1
		    count+=1
		    y+=DOWN
		if not os.path.exists(dir_path):
			os.makedirs(dir_path)
		file_path="%s/%s.svg"%(dir_path,pos)
		infile = open('25.svg')
		outfile = open(file_path, 'w')
		for line in infile:
			line = line.replace('XXXX', target)
			line = line.replace('YYYY', headers)
			outfile.write(line.encode('utf8'))
		infile.close()
		outfile.close()

class Draw_10(object):
	

	def __init__(self, title1,title2,title3,names,pos,type,dir_path,num,sub,voting_district,ballot):
		x=242
		y=265
		LEFT = 279
		DOWN = 50
		flag=True
		target =""
		headers = draw_headers(title1,title2,title3,num,sub,voting_district,ballot)
		for name in names:
			#print(name)
		    target+=draw_name(x,y,pos,name)
		    pos+=1
		    y+=DOWN
		if not os.path.exists(dir_path):
			os.makedirs(dir_path)
		file_path="%s/%s.svg"%(dir_path,pos)
		infile = open('25.svg')
		outfile = open(file_path, 'w')
		for line in infile:
			line = line.replace('XXXX', target)
			line = line.replace('YYYY', headers)
			outfile.write(line.encode('utf8'))
		infile.close()
		outfile.close()

def draw_headers30(title1,title2,title3,num,sub,voting_district,ballot):
	temp = ' <text direction="rtl" transform="matrix(1 0 0 1 610 106)" style="font-family: \'Dinar\'; font-weight:normal; font-style: normal"  font-size="14">'\
	 		' '+title1+'</text> '\
			' <text direction="rtl" transform="matrix(1 0 0 1 610 151)" style="font-family: \'Dinar\'; font-weight:normal; font-style: normal"  font-size="14">'\
	 		' '+title2+'</text> '\
			' <text direction="rtl" transform="matrix(1 0 0 1 556 174)" style="font-family: \'Dinar\'; font-weight:normal; font-style: normal"  font-size="13">'\
	 		' '+title3+' </text> '\
			' <text  transform="matrix(1 0 0 1 517 195)" fill="white" font-family=\'ArialMT\' style="  font-weight:normal; font-style: normal" font-size="13">'\
	 		' ('+str(ballot)+') </text>'\
			' <text direction="rtl" transform="matrix(1 0 0 1 512 195)" fill="white" style=" font-family: \'Dinar_Light\'; font-weight:normal; font-style: normal"  font-size="13">'\
	 		' '+voting_district+' </text>  '
	return temp

def draw_headers(title1,title2,title3,num,sub,voting_district,ballot):
	temp = ' <text direction="rtl" transform="matrix(1 0 0 1 483 125)" style="font-family: \'Dinar\'; font-weight:normal; font-style: normal"  font-size="14">'\
	 		' '+title1+'</text> '\
			' <text direction="rtl" transform="matrix(1 0 0 1 483 162)" style="font-family: \'Dinar\'; font-weight:normal; font-style: normal"  font-size="14">'\
	 		' '+title2+'</text> '\
			' <text direction="rtl" transform="matrix(1 0 0 1 445 185)" style="font-family: \'Dinar\'; font-weight:normal; font-style: normal"  font-size="13">'\
	 		' '+title3+' </text> '\
			' <text  transform="matrix(1 0 0 1 390 206)" fill="white" font-family=\'ArialMT\' style="  font-weight:normal; font-style: normal" font-size="13">'\
	 		' ('+str(ballot)+') </text>'\
			' <text direction="rtl" transform="matrix(1 0 0 1 385 206)" fill="white" style=" font-family: \'Dinar_Light\'; font-weight:normal; font-style: normal"  font-size="13">'\
	 		' '+voting_district+' </text>  '
	return temp


def draw_name(x,y,number,name):
	numpos=0
	if number>=10:
		numpos=2
	if number>=100:
		numpos=6
	temp = 	' <rect x="'+str(x)+'" y="'+str(y)+'" fill="none" stroke="#231F20" stroke-miterlimit="10" width="254.108" height="40"/>'\
			' <line x1="'+str(x+228.146)+'" y1="'+str(y)+'" x2="'+str(x+228.146)+'" y2="'+str(y+40)+'"  fill="none" stroke-miterlimit="10"'\
			' style="stroke:rgb(0,0,0);stroke-width:1" />'\
			' <rect x="'+str(x+6.094)+'" y="'+str(y+6.2)+'" fill="none" stroke="#231F20" stroke-miterlimit="10" width="28.347" height="28.347"/>'\
			' <text direction="rtl" transform="matrix(1 0 0 1 '+str(x+numpos+246.6636)+' '+str(y+24.9663)+')" font-family="ArialMT" font-size="14">'+str(number)+'</text>'\
			' <text direction="rtl" transform="matrix(1 0 0 1 '+str(x+221.6636)+' '+str(y+24.9663)+')" font-family="ArialMT" font-weight = "bold" font-size="14">'+name+'</text>'
	return temp
