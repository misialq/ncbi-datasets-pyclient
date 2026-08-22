# V2reportsThesis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pmid** | **int** |  | [optional] 
**book** | [**V2reportsBook**](V2reportsBook.md) |  | [optional] 
**id** | **str** |  | [optional] 
**classification_type** | [**V2reportsThesisType**](V2reportsThesisType.md) |  | [optional] [default to V2reportsThesisType.UNKNOWN]

## Example

```python
from ncbi.datasets.openapi.models.v2reports_thesis import V2reportsThesis

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsThesis from a JSON string
v2reports_thesis_instance = V2reportsThesis.from_json(json)
# print the JSON string representation of the object
print(V2reportsThesis.to_json())

# convert the object into a dict
v2reports_thesis_dict = v2reports_thesis_instance.to_dict()
# create an instance of V2reportsThesis from a dict
v2reports_thesis_from_dict = V2reportsThesis.from_dict(v2reports_thesis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


