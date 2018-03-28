import os
import os.path
l=[]
def get_py(path,l):
	filelist=os.listdir(path)
	for filename in filelist:
		pathtmp=os.path.join(path,filename)
		if os.path.isdir(pathtmp):
			get_py(pathtmp,l)
		elif filename[-3:].lower=='.py':
			l.append(pathtmp)
path = input("请输入文件路径：").strip
get_py(path,l)
#print('在%s目录及其子目录下找到%d个py文件\n分别为：\n'%(path,len(l)))
print('在%s目录下及其子目录下找到%d个py文件\n分别为：\n' %(path,len(l)))
for filepath in l:
	print (filepath+'\n')
	