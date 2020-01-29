def text_create(name,msg):
    desktop_path = 'C://Users/yong.zhu/Desktop'
    full_path = desktop_path + name +'.txt'
    file= open(full_path,'w')#打开文件，‘w'代表作为写入模式
    file.write(msg)
    file.close()
    print('Done')
text_create('hello','hello world')