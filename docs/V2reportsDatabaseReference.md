# V2reportsDatabaseReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | **str** |  | [optional] 
**resource_id** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_database_reference import V2reportsDatabaseReference

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsDatabaseReference from a JSON string
v2reports_database_reference_instance = V2reportsDatabaseReference.from_json(json)
# print the JSON string representation of the object
print(V2reportsDatabaseReference.to_json())

# convert the object into a dict
v2reports_database_reference_dict = v2reports_database_reference_instance.to_dict()
# create an instance of V2reportsDatabaseReference from a dict
v2reports_database_reference_from_dict = V2reportsDatabaseReference.from_dict(v2reports_database_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


