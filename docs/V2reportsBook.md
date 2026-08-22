# V2reportsBook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pmid** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**authors** | [**List[V2reportsAuthor]**](V2reportsAuthor.md) |  | [optional] 
**pages** | **str** |  | [optional] 
**publisher** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_book import V2reportsBook

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsBook from a JSON string
v2reports_book_instance = V2reportsBook.from_json(json)
# print the JSON string representation of the object
print(V2reportsBook.to_json())

# convert the object into a dict
v2reports_book_dict = v2reports_book_instance.to_dict()
# create an instance of V2reportsBook from a dict
v2reports_book_from_dict = V2reportsBook.from_dict(v2reports_book_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


