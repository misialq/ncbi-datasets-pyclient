# V2reportsSraRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**expression_value** | **float** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sra_run import V2reportsSraRun

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSraRun from a JSON string
v2reports_sra_run_instance = V2reportsSraRun.from_json(json)
# print the JSON string representation of the object
print(V2reportsSraRun.to_json())

# convert the object into a dict
v2reports_sra_run_dict = v2reports_sra_run_instance.to_dict()
# create an instance of V2reportsSraRun from a dict
v2reports_sra_run_from_dict = V2reportsSraRun.from_dict(v2reports_sra_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


