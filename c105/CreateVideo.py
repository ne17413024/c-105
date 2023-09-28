import os
import cv2

path = "imagenes/"

imagenes = []

for file in os.listdir(path):
    name, extens = os.path.splitext(file)
    if extens in [".gif", ".png", ".jpeg", ".jpg", ".jfif", ".webp", ".svg"]: 
        file_name = path + file
        print(file_name); 
        imagenes.append(file_name)

print(len(imagenes));

count = len(imagenes);

frame = cv2.imread(imagenes[0])

height, width, layers = frame.shape
size = (height, width)
print(size);

out = cv2.VideoWriter("imagenes.mov", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size )
for i in range(0, count):
  #ret,frame=vid.read()
  frame = cv2.imread(imagenes[i])
  out.write(frame)
  # Mostrar el video en tiempo real
  cv2.imshow("Video", frame)
  if cv2.waitKey(30) & 0xFF == ord('q'):  # Esperar 30 ms y verificar si se presiona 'q' para salir
    break

#cv2.waitKey(0)
#out.release