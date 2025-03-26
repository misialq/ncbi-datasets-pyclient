# V2reportsConservedDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**range** | [**V2reportsRange**](V2reportsRange.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_conserved_domain import V2reportsConservedDomain

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsConservedDomain from a JSON string
v2reports_conserved_domain_instance = V2reportsConservedDomain.from_json(json)
# print the JSON string representation of the object
print(V2reportsConservedDomain.to_json())

# convert the object into a dict
v2reports_conserved_domain_dict = v2reports_conserved_domain_instance.to_dict()
# create an instance of V2reportsConservedDomain from a dict
v2reports_conserved_domain_from_dict = V2reportsConservedDomain.from_dict(v2reports_conserved_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


