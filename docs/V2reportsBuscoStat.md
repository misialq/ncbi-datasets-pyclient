# V2reportsBuscoStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**busco_lineage** | **str** |  | [optional] 
**busco_ver** | **str** |  | [optional] 
**complete** | **float** |  | [optional] 
**single_copy** | **float** |  | [optional] 
**duplicated** | **float** |  | [optional] 
**fragmented** | **float** |  | [optional] 
**missing** | **float** |  | [optional] 
**total_count** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_busco_stat import V2reportsBuscoStat

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsBuscoStat from a JSON string
v2reports_busco_stat_instance = V2reportsBuscoStat.from_json(json)
# print the JSON string representation of the object
print(V2reportsBuscoStat.to_json())

# convert the object into a dict
v2reports_busco_stat_dict = v2reports_busco_stat_instance.to_dict()
# create an instance of V2reportsBuscoStat from a dict
v2reports_busco_stat_from_dict = V2reportsBuscoStat.from_dict(v2reports_busco_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


