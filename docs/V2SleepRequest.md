# V2SleepRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sleep_msec** | **int** |  | [optional] 
**error_rate** | **float** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_sleep_request import V2SleepRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2SleepRequest from a JSON string
v2_sleep_request_instance = V2SleepRequest.from_json(json)
# print the JSON string representation of the object
print(V2SleepRequest.to_json())

# convert the object into a dict
v2_sleep_request_dict = v2_sleep_request_instance.to_dict()
# create an instance of V2SleepRequest from a dict
v2_sleep_request_from_dict = V2SleepRequest.from_dict(v2_sleep_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


