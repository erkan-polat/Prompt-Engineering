import matplotlib.pyplot as plt

objects = ['Görüntü 1', 'Görüntü 2', 'Görüntü 3', 'Görüntü 4', 'Görüntü 5', 'Görüntü 6', 'Görüntü 7', 'Görüntü 8', 'Görüntü 9', 'Görüntü 10']
scores = [0, 0.95, 0.95, 0.91, 0.89, 0.83, 0.88, 0.86, 0.89, 0.83] 

plt.bar(objects, scores, color='blue')
plt.xlabel('Görüntüler')
plt.ylabel('Güven Skoru')
plt.title('Görüntülerdeki Tespit Edilen Nesnelerin Güven Skorları')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
