# V2TaxonomyTaxIdsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_ids** | **List[int]** |  | [optional] 
**next_page_token** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_tax_ids_page import V2TaxonomyTaxIdsPage

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyTaxIdsPage from a JSON string
v2_taxonomy_tax_ids_page_instance = V2TaxonomyTaxIdsPage.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyTaxIdsPage.to_json())

# convert the object into a dict
v2_taxonomy_tax_ids_page_dict = v2_taxonomy_tax_ids_page_instance.to_dict()
# create an instance of V2TaxonomyTaxIdsPage from a dict
v2_taxonomy_tax_ids_page_from_dict = V2TaxonomyTaxIdsPage.from_dict(v2_taxonomy_tax_ids_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


