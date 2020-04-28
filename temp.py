import re#正则表达式的包
import pandas as pd
import matplotlib.pyplot as plt
import folium as fm

plt.style.use('ggplot')#美化

#导入文件
f=open('美食1.txt',encoding='utf-8')
#导入文件的编码不是utf-8所以有报错  需要在后面加上 encoding = "utf-8"
filelist=f.readlines()
str_file=str(filelist)
#定义空的坐标列表
x=[]
y=[]

#匹配出坐标地址
data1=re.findall(pattern="\d+\.\d{2,}",string=str_file)

#得到坐标
count=0
for i in data1:
    if(float(i)<60):
        x.append(str(i))
    else:
         y.append(str(i))
    count+=1

#x只有一列，所以columns要加中括号
df_x=pd.DataFrame(x,columns=['lat'])
df_x=df_x[:1500]
df_y=pd.DataFrame(y,columns=['lng'])
df_x=df_x[:1500]
paint=df_x.join(df_y)

paint1=paint.astype('float')

print(paint1)

#绘制图像
m = fm.Map(location=[38.0, 112.4],
               zoom_start=8)
#获取行数
num=len(paint1)
#获取列数据‘
col1= paint1['lat']
col2=paint1['lng']
#获取坐标
 
for i in range(1,num):
    x=col1.__getitem__(i)
    y=col2.__getitem__(i)
    place=[x,y]
    fm.Marker(place, popup='<i>Mt. Hood Meadows</i>').add_to(m)
m.save('beautiful_food.html')
#散点图绘制
paint1.plot.scatter('lat','lng',marker='o',alpha=0.3)
plt.show()
