# -*- coding:utf-8 -*-

import requests
import re

# 本程序用于抓取赶集网上海各地区二手房房价均值，默认抓取页数为50页。
# 使用python语言，requests库抓取网页，re库用于正则抓取。


print u"本程序用于计算赶集上海二手区房价，单位万/平米"
print (u'''每个区对应代码如下：
0：显示上海所有区单独的平均房价；
1：浦东新区；
2：闵行区；
3：徐汇区；
4：长宁区；
5：普陀区；
6：静安区；
7：卢湾区；
8：黄浦区；
9：闸北区；
a：虹口区；
b：杨浦区；
c：宝山区；
d：嘉定区；
e：青浦区；
f：松江区；
g：金山区；
h：奉贤区；
i：南汇区；
j：崇明区；
k：上海周边；
''')

#各地区页面代码
num_area = {
    '1':'http://wap.ganji.com/sh/fang5/pudongxinqu/o',
    '2':'http://wap.ganji.com/sh/fang5/minhang/o',
    '3':'http://wap.ganji.com/sh/fang5/xuhui/o',
    '4':'http://wap.ganji.com/sh/fang5/changning/o',
    '5':'http://wap.ganji.com/sh/fang5/putuo/o',
    '6':'http://wap.ganji.com/sh/fang5/jingan/o',
    '7':'http://wap.ganji.com/sh/fang5/luwan/o',
    '8':'http://wap.ganji.com/sh/fang5/huangpu/o',
    '9':'http://wap.ganji.com/sh/fang5/zhabei/o',
    'a':'http://wap.ganji.com/sh/fang5/hongkou/o',
    'b':'http://wap.ganji.com/sh/fang5/yangpu/o',
    'c':'http://wap.ganji.com/sh/fang5/baoshan/o',
    'd':'http://wap.ganji.com/sh/fang5/jiading/o',
    'e':'http://wap.ganji.com/sh/fang5/qingpu/o',
    'f':'http://wap.ganji.com/sh/fang5/songjiang/o',
    'g':'http://wap.ganji.com/sh/fang5/jinshan/o',
    'h':'http://wap.ganji.com/sh/fang5/fengxian/o',
    'i':'http://wap.ganji.com/sh/fang5/nanhui/o',
    'j':'http://wap.ganji.com/sh/fang5/chongming/o',
    'k':'http://wap.ganji.com/sh/fang5/shanghaizhoubian/o'
}

#各地区显示代码
area = {
    '1':u'浦东新区',
    '2':u'闵行区',
    '3':u'徐汇区',
    '4':u'长宁区',
    '5':u'普陀区',
    '6':u'静安区',
    '7':u'卢湾区',
    '8':u'黄浦区',
    '9':u'闸北区',
    'a':u'虹口区',
    'b':u'杨浦区',
    'c':u'宝山区',
    'd':u'嘉定区',
    'e':u'青浦区',
    'f':u'松江区',
    'g':u'金山区',
    'h':u'奉贤区',
    'i':u'南汇区',
    'j':u'崇明区',
    'k':u'上海周边'
}


#获得房价均值函数
def get_price(numb):
    sp_list = []
    for n in range(1,50): #抓取前50页
        url = num_area[numb]+str(n)
        urlpage = requests.get(url)
        urlpage.encoding = 'utf-8'
        urltx = urlpage.text

        size_price = re.findall(u'(\d+)\u33a1.*?(\d+)\u4e07\u5143',urltx,re.S)#从页面获取房价和面积
        for sp in size_price:
            sp_list.append(sp)

    priclist = []
    sum_pric = 0
    i = 0
    for sizepri in sp_list:#计算平均房价
        pric = round(float(sizepri[1])/float(sizepri[0]),2)      
        #print pric
        priclist.append(pric)
        sum_pric = sum_pric + pric
        i = i + 1

    if i != 0:
        print (area[numb]+u"共获取二手房数量："+str(i)+u"，平均房价为："+str(round(float(sum_pric)/float(i),2))+u"万元每平方")
    else:
        print u"获取失败！请使用浏览器检查%s是否能正常显示！" % num_area[numb]
        print urltx

#获取输入区域
def get_area():
    print('')
    area_input = raw_input("请输入需要查询的区代码，可一次输入多个代码: ")
    areanum = str(area_input)
    if str(0) in areanum:#输入有0则计算全部区域
        print u"您输入的区域为：上海所有区域"
        for numbe in ('1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k'):
            get_price(numbe)
    else:#输入无0则计算输入区域
        output = u"您输入的区域为："
        for numb in ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k'):
            if str(numb) in areanum:
                output = output+str(area[numb])+" "
        print output
        for numb in ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k'):
            if str(numb) in areanum:
                get_price(numb)

get_area()
