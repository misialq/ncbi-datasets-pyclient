# V2reportsWarning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_warning_code** | [**V2reportsWarningGeneWarningCode**](V2reportsWarningGeneWarningCode.md) |  | [optional] 
**reason** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**replaced_id** | [**V2reportsWarningReplacedId**](V2reportsWarningReplacedId.md) |  | [optional] 
**unrecognized_identifier** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_warning import V2reportsWarning

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsWarning from a JSON string
v2reports_warning_instance = V2reportsWarning.from_json(json)
# print the JSON string representation of the object
print(V2reportsWarning.to_json())

# convert the object into a dict
v2reports_warning_dict = v2reports_warning_instance.to_dict()
# create an instance of V2reportsWarning from a dict
v2reports_warning_from_dict = V2reportsWarning.from_dict(v2reports_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


