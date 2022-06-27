#程序文件ex11_4.py
import numpy as np
from sklearn.cluster import KMeans

a = np.array([[1, 3],[1.5, 3.2],[1.3, 2.8],[3, 1]])
md = KMeans(2).fit(a)  #构建2聚类模型并求解
labels = md.labels_   #提取聚类标签
centers = md.cluster_centers_   #每一行是一个聚类中心
print(labels, '\n-----------\n', centers)
