# V2reportsProceedings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pmid** | **int** |  | [optional] 
**meeting** | [**V2reportsMeeting**](V2reportsMeeting.md) |  | [optional] 
**book** | [**V2reportsBook**](V2reportsBook.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_proceedings import V2reportsProceedings

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsProceedings from a JSON string
v2reports_proceedings_instance = V2reportsProceedings.from_json(json)
# print the JSON string representation of the object
print(V2reportsProceedings.to_json())

# convert the object into a dict
v2reports_proceedings_dict = v2reports_proceedings_instance.to_dict()
# create an instance of V2reportsProceedings from a dict
v2reports_proceedings_from_dict = V2reportsProceedings.from_dict(v2reports_proceedings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


