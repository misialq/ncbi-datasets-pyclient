# V2reportsAverageNucleotideIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_check_status** | [**V2reportsAverageNucleotideIdentityTaxonomyCheckStatus**](V2reportsAverageNucleotideIdentityTaxonomyCheckStatus.md) |  | [optional] [default to V2reportsAverageNucleotideIdentityTaxonomyCheckStatus.TAXONOMY_CHECK_STATUS_UNKNOWN]
**match_status** | [**V2reportsAverageNucleotideIdentityMatchStatus**](V2reportsAverageNucleotideIdentityMatchStatus.md) |  | [optional] [default to V2reportsAverageNucleotideIdentityMatchStatus.BEST_MATCH_STATUS_UNKNOWN]
**submitted_organism** | **str** |  | [optional] 
**submitted_species** | **str** |  | [optional] 
**category** | [**V2reportsANITypeCategory**](V2reportsANITypeCategory.md) |  | [optional] [default to V2reportsANITypeCategory.ANI_CATEGORY_UNKNOWN]
**submitted_ani_match** | [**V2reportsANIMatch**](V2reportsANIMatch.md) |  | [optional] 
**best_ani_match** | [**V2reportsANIMatch**](V2reportsANIMatch.md) |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_average_nucleotide_identity import V2reportsAverageNucleotideIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsAverageNucleotideIdentity from a JSON string
v2reports_average_nucleotide_identity_instance = V2reportsAverageNucleotideIdentity.from_json(json)
# print the JSON string representation of the object
print(V2reportsAverageNucleotideIdentity.to_json())

# convert the object into a dict
v2reports_average_nucleotide_identity_dict = v2reports_average_nucleotide_identity_instance.to_dict()
# create an instance of V2reportsAverageNucleotideIdentity from a dict
v2reports_average_nucleotide_identity_from_dict = V2reportsAverageNucleotideIdentity.from_dict(v2reports_average_nucleotide_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


