# V2reportsMaturePeptide


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession_version** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**length** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_mature_peptide import V2reportsMaturePeptide

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsMaturePeptide from a JSON string
v2reports_mature_peptide_instance = V2reportsMaturePeptide.from_json(json)
# print the JSON string representation of the object
print(V2reportsMaturePeptide.to_json())

# convert the object into a dict
v2reports_mature_peptide_dict = v2reports_mature_peptide_instance.to_dict()
# create an instance of V2reportsMaturePeptide from a dict
v2reports_mature_peptide_from_dict = V2reportsMaturePeptide.from_dict(v2reports_mature_peptide_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


