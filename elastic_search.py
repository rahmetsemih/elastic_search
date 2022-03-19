from elasticsearch import Elasticsearch
es =Elasticsearch([{'host':'localhost','port':9200}])
e1={"first_name":"Nihat",
    "last_name":"Doğan",
    "age":29,
    "interest":['football',"basketball"]    
    }
res=es.index(index='sirketpersonal',id=1,body=e1)
e2={"first_name":"Semih",
    "last_name":"Rahmet",
    "age":21,
    "interest":['football',"tenis"]    
    }
e3={"first_name":"Sevval",
    "last_name":"Göçer",
    "age":19,
    "interest":['trip abroad',"computer games"]    
    }
res=es.index(index='sirketpersonal',id=2,body=e2)
res=es.index(index='sirketpersonal',id=3,body=e3)
#Bir sorgulama yapalım 'get' methodu ile..

res =es.get(index='sirketpersonal',id=3)
print(res)
#documentin içindeki asıl verileri almak istersek
print(res['_source'])
#sirketpersonal ın içindeki bütün verileri yazdıralım...
res=es.search(index='sirketpersonal',body={'query':{'match_all':{}}})
print(res)
#match operator:Adı Semih olan verileri getirir..

name=es.search(index='sirketpersonal',body={'query':{'match':{'first_name:''Semih'}}})
print(name)   