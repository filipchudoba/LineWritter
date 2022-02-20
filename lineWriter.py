import PySimpleGUI as sg    
import sys  

layout = [[sg.Text('Enter name of generated texture: (file will be named as textureName.lin)')],      
                 [sg.InputText()],
                 [sg.Text('Width in meters:')],      
                 [sg.InputText()],
                 [sg.Text('Height in meters:')],      
                 [sg.InputText()],
                 [sg.Text('Texture width in pixels:')],      
                 [sg.InputText()],
                 [sg.Text('Layer group:')],      
                 [sg.InputText()],          
                 [sg.Submit(), sg.Cancel()]]   

window = sg.Window('Line Generator', layout)    

event, values = window.read()

if event is "Cancel":
    sys.exit()

print(len(values))

i = 0
while i < len(values):
    if len(values[i]) == 0:
        sg.popup("tys tam nic nenapsal, hajzle!")
        sys.exit()
    i += 1
    

window.close()

#Text input = to co se bude propisovat do souboru
textureName = values[0]

dividedName = textureName.split('.')
linName = dividedName[0] + '.lin'

textureSizeWidth = values[1]
textureSizeHeight = values[2]
textureSize = "SIZE " + textureSizeWidth + " " + textureSizeHeight
textureWidth = "TEX_WIDTH " + values[3]
textureWidthPlain = values[3]
halfWidth = int(textureWidthPlain) / int(2)
textureWidthPlainLast = int(textureWidthPlain) - 1
textureOffset = "S_OFFSET 0 0 " + str(round(halfWidth)) + " " + str(textureWidthPlainLast)
layerGroup = "LAYER_GROUP markings +" + values[4]

startBasicLine = ['A','830','LINE_PAINT','']

textureName = "TEXTURE " + textureName

linFile = startBasicLine
linProcedure = [textureName, '', textureSize, 'LOD 3000', textureWidth, textureOffset, layerGroup, 'MIRROR']

for line in linProcedure:
    linFile.append(line)

with open(linName, 'x') as f:
    for line in linFile:
        f.write(line)
        f.write('\n')