layer_list = []
with open("C:\\Users\\Mark\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\fav_layer\\text.txt", "r") as file:
    for lines in file:
        layer_list.append(lines)
print(layer_list)