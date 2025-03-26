# V2reportsMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**V2reportsError**](V2reportsError.md) |  | [optional] 
**warning** | [**V2reportsWarning**](V2reportsWarning.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_message import V2reportsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsMessage from a JSON string
v2reports_message_instance = V2reportsMessage.from_json(json)
# print the JSON string representation of the object
print(V2reportsMessage.to_json())

# convert the object into a dict
v2reports_message_dict = v2reports_message_instance.to_dict()
# create an instance of V2reportsMessage from a dict
v2reports_message_from_dict = V2reportsMessage.from_dict(v2reports_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


