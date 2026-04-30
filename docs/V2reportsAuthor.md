# V2reportsAuthor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**affiliation** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_author import V2reportsAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsAuthor from a JSON string
v2reports_author_instance = V2reportsAuthor.from_json(json)
# print the JSON string representation of the object
print(V2reportsAuthor.to_json())

# convert the object into a dict
v2reports_author_dict = v2reports_author_instance.to_dict()
# create an instance of V2reportsAuthor from a dict
v2reports_author_from_dict = V2reportsAuthor.from_dict(v2reports_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


