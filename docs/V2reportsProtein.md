# V2reportsProtein


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession_version** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**length** | **int** |  | [optional] 
**isoform_name** | **str** |  | [optional] 
**ensembl_protein** | **str** |  | [optional] 
**mature_peptides** | [**List[V2reportsMaturePeptide]**](V2reportsMaturePeptide.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_protein import V2reportsProtein

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsProtein from a JSON string
v2reports_protein_instance = V2reportsProtein.from_json(json)
# print the JSON string representation of the object
print(V2reportsProtein.to_json())

# convert the object into a dict
v2reports_protein_dict = v2reports_protein_instance.to_dict()
# create an instance of V2reportsProtein from a dict
v2reports_protein_from_dict = V2reportsProtein.from_dict(v2reports_protein_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


