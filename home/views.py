from django.shortcuts import render
from django.http import request,HttpRequest,HttpResponse
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.cluster import KMeans
# import csv
# import numpy as np
import os
# Create your models here.
def home(request):
    return render(request,'index.html')

def out(request):
    return render(request,'output.html')


    
def run(request):
    
    
    # def perform_kmeans_clustering(tfidf_matrix, num_clusters):
    #     kmeans = KMeans(n_clusters=num_clusters)
    #     clusters = kmeans.fit_predict(tfidf_matrix)
    #     return clusters

    # keyword_data = pd.read_csv(request.FILES['csv_file'])


    # keywords = keyword_data["keyword"]
    # volumes = keyword_data["volume"]

    # vectorizer = TfidfVectorizer(stop_words="english")
    # tfidf_matrix = vectorizer.fit_transform(keywords)

    # inertias = [KMeans(n_clusters=k).fit(tfidf_matrix).inertia_ for k in range(1, 31)]
    # differences = np.diff(inertias)
    # knee = np.argmax(differences) + 1

    # clusters = perform_kmeans_clustering(tfidf_matrix, knee)

    # keyword_data["cluster"] = clusters

    # cluster_dict = dict(keyword_data.groupby("cluster").apply(lambda x: {"keywords": x["keyword"].tolist(), "volumes": x["volume"].tolist()}))

    # most_frequent_keywords_in_clusters = [pd.Series(data["keywords"]).value_counts().idxmax() for data in cluster_dict.values()]

    # total_volumes = [sum(data["volumes"]) for data in cluster_dict.values()]

    # # Sort cluster_dict based on total volumes in decreasing order
    # sorted_clusters = sorted(cluster_dict.items(), key=lambda x: total_volumes[x[0]], reverse=True)

    # csv_file = 'static/output.csv'
    # with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    #     csv_writer = csv.writer(csvfile)
    #     csv_writer.writerow(["ID", "variations", "Keywords", "Volume"])
    #     for cluster, data in sorted_clusters:
    #         csv_writer.writerow([cluster, ', '.join(data["keywords"]), most_frequent_keywords_in_clusters[cluster], total_volumes[cluster]])
            
    return render(request,'show.html',{"output":1})
   