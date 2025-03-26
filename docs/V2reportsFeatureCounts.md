# V2reportsFeatureCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_counts** | [**V2reportsGeneCounts**](V2reportsGeneCounts.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_feature_counts import V2reportsFeatureCounts

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsFeatureCounts from a JSON string
v2reports_feature_counts_instance = V2reportsFeatureCounts.from_json(json)
# print the JSON string representation of the object
print(V2reportsFeatureCounts.to_json())

# convert the object into a dict
v2reports_feature_counts_dict = v2reports_feature_counts_instance.to_dict()
# create an instance of V2reportsFeatureCounts from a dict
v2reports_feature_counts_from_dict = V2reportsFeatureCounts.from_dict(v2reports_feature_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


