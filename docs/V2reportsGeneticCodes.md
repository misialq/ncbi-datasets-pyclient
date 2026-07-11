# V2reportsGeneticCodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | [**V2reportsGeneticCode**](V2reportsGeneticCode.md) |  | [optional] 
**mitochondrial** | [**V2reportsGeneticCode**](V2reportsGeneticCode.md) |  | [optional] 
**plastid** | [**V2reportsGeneticCode**](V2reportsGeneticCode.md) |  | [optional] 
**hydrogenosome** | [**V2reportsGeneticCode**](V2reportsGeneticCode.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_genetic_codes import V2reportsGeneticCodes

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGeneticCodes from a JSON string
v2reports_genetic_codes_instance = V2reportsGeneticCodes.from_json(json)
# print the JSON string representation of the object
print(V2reportsGeneticCodes.to_json())

# convert the object into a dict
v2reports_genetic_codes_dict = v2reports_genetic_codes_instance.to_dict()
# create an instance of V2reportsGeneticCodes from a dict
v2reports_genetic_codes_from_dict = V2reportsGeneticCodes.from_dict(v2reports_genetic_codes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


