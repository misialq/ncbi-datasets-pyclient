# V2reportsPublication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pmid** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**authors** | [**List[V2reportsAuthor]**](V2reportsAuthor.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_publication import V2reportsPublication

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsPublication from a JSON string
v2reports_publication_instance = V2reportsPublication.from_json(json)
# print the JSON string representation of the object
print(V2reportsPublication.to_json())

# convert the object into a dict
v2reports_publication_dict = v2reports_publication_instance.to_dict()
# create an instance of V2reportsPublication from a dict
v2reports_publication_from_dict = V2reportsPublication.from_dict(v2reports_publication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


