import bpy

dictionary = {
    "DEFAULT": {},
    "en_US": {
        "几何数据": "Geometry",
        "布尔"   :  "Boolean",
        "浮点"   :  "Float",
        "整数"   :  "Integer",
        "矢量"   :  "Vector",
        "颜色"   :  "Color",
        "旋转"   :  "Rotation",
        "菜单"   :  "Menu",
        "字符串" :  "String",
        "材质"   :  "Material",
        "物体"   :  "Object",
        "集合"   :  "Collection",
        "图像"   :  "Image",
        "纹理"   :  "Texture",
        
        "w-节点组输入助手-添加拆分合并移动": "Group input helper-Add Split Merge Move",
        "快速添加组输入节点-拆分合并移动组输入节点-快速添加组输入输出接口": "Qucik add and split merge move Group Input node-Qucik add Group Input Output socket",
        "偏好设置-标题栏-N面板": "Preferences-Editor Bar-N panel",

        "组输入": "Group input",
        "w-组输入拆分": "Group input split",
        "w-添加组输入输出接口": "Add group input output interface",
        "显示面板名字": "Show Panel name in Group input add menu",
        "添加组输入菜单里显示接口所属面板名字": "Show Panel name in Group input add menu",
        "组输入隐藏节口": "Group input hide socket",
        "组输入拆分菜单: 快捷键 1 和 Ctrl Shift Alt 1": "Group input split menu: Shortcut key 1 and Ctrl Shift Alt 1",
        "空": "Null",

        "标题栏和N面板显示组输入拆分": "Title bar and N panel display group input split",
        "添加组输入": "Add group input",
        "添加组输入-菜单": "Add group input - menu",
        "添加组输入-面板": "Add group input - panel",
        "添加组输入输出接口": "Add group input output socket",
        "添加输入输出接口": "Add input output socket",
        "输入接口": "Input socket",
        "输出接口": "Output socket",

        "组输入合并拆分移动":     "Group input merge split move",
        "组输入拆分合并移动":     "Group input split merge move",
        "合并组输入接口":        "Merge group input socket",
        "合并组输入连线":        "Merge group input links",
        "留下未隐藏的接口":      "Split group input socket, leave the unhidden socket",
        "拆分组输入接口":        "Split group input socket",
        "拆分组输入并移动":      "Split group input and move", 
        "拆分组输入并移动合并":  "Split group input and move merge", 
        "拆分组输入":            "Split group input", 
        "合并节点并拆分":        "Merge group input and split", 
        "合并组输入连线":        "Merge group input links", 
        "拆分组输入连线":        "Split group input links", 
        "完全拆分并移动":        "Completely split and move", 
        "拆分并移动合并":        "Split and move merge", 
        "完全拆分组输入":        "Completely split group input", 
        "简化<组输入合并拆分移动>菜单": "Simplify the menu of Split group input", 
        "合并组输入接口,留下未隐藏的接口": "Merge group input socket,leave the unhidden socket",
        "合并组输入连线,只留下连线的接口": "Merge group input links,only leave the linked socket",
        "拆分组输入接口,只留下连线的接口": "Split group input socket, only leave the linked socket", 
        "拆分组输入接口,留下未隐藏的接口,一连多也拆开": "Split group input socket, leave the unhidden socket, also split the one-to-many connections", 
        "拆分组输入接口,并移动到连向接口的附近,留下未隐藏的接口,一连多也拆开": "Split group input socket, and move to the vicinity of the connected socket, leave the unhidden socket, also split the one-to-many connections", 
        "完全拆分组输入接口,并移动到连向的接口(to_socket),并合并连到一个节点上的和距离近的组输入节点": "Completely split group input socket, and move to the connected socket (to_socket), and merge the group input nodes that are connected to one node and close in distance", 
        "隐藏组输入接口": "hide group input sockets",
        "隐藏未使用组输入节点的接口": "hide sockets of unliked group input node ",
    },
    # "zh_CN": {
    #     "Add-on Preferences View": "插件偏好设置",
    # }
}

def i18n(text: str) -> str:
    view = bpy.context.preferences.view
    language = view.language
    trans_interface = view.use_translate_interface

    if language in ["zh_CN", "zh_HANS"] and trans_interface:
        return text
    else:
        if text in dictionary["en_US"]:
            return dictionary["en_US"][text]
        else:
            return text



# # Get the language code when addon start up
# __language_code__ = bpy.context.preferences.view.language

# dictionary["zh_HANS"] = dictionary["zh_CN"]


# def i18n(content: str) -> str:
#     return i18n_d(content)

# def i18n_l(content: str) -> str:
#     global __language_code__
#     if __language_code__ not in dictionary:
#         # return content
#         return dictionary["en_US"][content]

#     if content not in dictionary[__language_code__]:
#         return content

#     return dictionary[__language_code__][content]


# # update the preferences language code and do the translation
# def i18n_d(content: str) -> str:
#     global __language_code__
#     __language_code__ = bpy.context.preferences.view.language
#     return i18n_l(content)


