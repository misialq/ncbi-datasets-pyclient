# V2reportsArticle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pmid** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**authors** | [**List[V2reportsAuthor]**](V2reportsAuthor.md) |  | [optional] 
**journal** | [**V2reportsJournal**](V2reportsJournal.md) |  | [optional] 
**book** | [**V2reportsBook**](V2reportsBook.md) |  | [optional] 
**proceedings** | [**V2reportsProceedings**](V2reportsProceedings.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_article import V2reportsArticle

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsArticle from a JSON string
v2reports_article_instance = V2reportsArticle.from_json(json)
# print the JSON string representation of the object
print(V2reportsArticle.to_json())

# convert the object into a dict
v2reports_article_dict = v2reports_article_instance.to_dict()
# create an instance of V2reportsArticle from a dict
v2reports_article_from_dict = V2reportsArticle.from_dict(v2reports_article_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


