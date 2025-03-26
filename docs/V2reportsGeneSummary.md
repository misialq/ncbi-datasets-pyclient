# V2reportsGeneSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_gene_summary import V2reportsGeneSummary

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGeneSummary from a JSON string
v2reports_gene_summary_instance = V2reportsGeneSummary.from_json(json)
# print the JSON string representation of the object
print(V2reportsGeneSummary.to_json())

# convert the object into a dict
v2reports_gene_summary_dict = v2reports_gene_summary_instance.to_dict()
# create an instance of V2reportsGeneSummary from a dict
v2reports_gene_summary_from_dict = V2reportsGeneSummary.from_dict(v2reports_gene_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


