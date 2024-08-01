vector_index_payload = {
  "name": "customer-index",
  "fields": [
    {
        "name": "id", 
        "type": "Edm.String", 
        "key": True
    },
    {
        "name": "question",
        "type": "Edm.String"
    },
    {
        "name": "sql_query",
        "type": "Edm.String"
    },
    {
        "name": "embedding",
        "type": "Collection(Edm.Single)",
        "searchable": True,
        "retrievable": True,
        "dimensions": 1536,
        "vectorSearchProfile": "my-vector-profile"
    }
  ],
  "vectorSearch": {
        "algorithms": [
            {
                "name": "my-hnsw-vector-config-1",
                "kind": "hnsw",
                "hnswParameters": 
                {
                    "m": 4,
                    "efConstruction": 400,
                    "efSearch": 500,
                    "metric": "cosine"
                }
            },
            {
                "name": "my-hnsw-vector-config-2",
                "kind": "hnsw",
                "hnswParameters": 
                {
                    "m": 4,
                    "metric": "euclidean"
                }
            },
            {
                "name": "my-eknn-vector-config",
                "kind": "exhaustiveKnn",
                "exhaustiveKnnParameters": 
                {
                    "metric": "cosine"
                }
            }
        ],
        "profiles": [      
            {
                "name": "my-vector-profile",
                "algorithm": "my-hnsw-vector-config-1"
            }
      ]
    },
}