from elasticsearch import Elasticsearch
from env import elastic_index, elastic_url
es = Elasticsearch([elastic_url])

class ElasticSearch:

    def add_index_product(self, id, product_name, description):
        document = {"id": id, "product_name": product_name, "description": description}
        es.index(index=elastic_index, id=id, document=document)

    def search_product(self, txt):
        result = []
        search_results = es.search(index=elastic_index, body={
            "query": {
                "multi_match": {
                    "query": txt,
                    "fields": ["product_name", "description"],
                    "fuzziness": "AUTO"
                }
            }
        })
        for hit in search_results["hits"]["hits"]:
            result.append({"id": hit['_id'], "product_name": hit['_source']['product_name'], "description": hit['_source']['description']})
        return result
