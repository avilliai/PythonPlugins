
def readConfig():
    with open('friendPath.txt', mode='r', encoding='utf-8') as ff:
        aimFriend = ff.readline()
        print('当前私聊' + aimFriend)
    with open('groupPath.txt', mode='r', encoding='utf-8') as fd:
        aimGroup = fd.readline()
        print('当前群聊' + aimGroup)
    with open('status.txt', mode='r', encoding='utf-8') as fs:
        statusPath = fs.readline()
        print('当前对象类型' + statusPath)
    with open('ModePath.txt', mode='r', encoding='utf-8') as fa:
        model = fa.readline()
        print('当前模型' + model)
        #modeSelect = int(modeSelects)
    with open('langPath.txt', mode='r', encoding='utf-8') as la:
        lang = la.readline()
        print('当前语言' + lang)

    lista=[aimFriend,aimGroup,statusPath,model,lang]
    return lista