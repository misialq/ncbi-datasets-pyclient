# V2reportsMeeting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pmid** | **int** |  | [optional] 
**number** | **int** |  | [optional] 
**var_date** | **str** |  | [optional] 
**place** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_meeting import V2reportsMeeting

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsMeeting from a JSON string
v2reports_meeting_instance = V2reportsMeeting.from_json(json)
# print the JSON string representation of the object
print(V2reportsMeeting.to_json())

# convert the object into a dict
v2reports_meeting_dict = v2reports_meeting_instance.to_dict()
# create an instance of V2reportsMeeting from a dict
v2reports_meeting_from_dict = V2reportsMeeting.from_dict(v2reports_meeting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


