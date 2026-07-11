# V2reportsInfraspecificModifers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strain** | **str** |  | [optional] 
**substrain** | **str** |  | [optional] 
**variety** | **str** |  | [optional] 
**serotype** | **str** |  | [optional] 
**serogroup** | **str** |  | [optional] 
**biotype** | **str** |  | [optional] 
**isolate** | **str** |  | [optional] 
**forma** | **str** |  | [optional] 
**forma_specialis** | **str** |  | [optional] 
**ecotype** | **str** |  | [optional] 
**breed** | **str** |  | [optional] 
**specimen_voucher** | [**V2reportsSpecimenVoucher**](V2reportsSpecimenVoucher.md) |  | [optional] 
**biomaterial** | **str** |  | [optional] 
**culture_collection** | [**V2reportsCultureCollection**](V2reportsCultureCollection.md) |  | [optional] 
**type_material** | [**V2reportsSequenceTypeMaterial**](V2reportsSequenceTypeMaterial.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_infraspecific_modifers import V2reportsInfraspecificModifers

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsInfraspecificModifers from a JSON string
v2reports_infraspecific_modifers_instance = V2reportsInfraspecificModifers.from_json(json)
# print the JSON string representation of the object
print(V2reportsInfraspecificModifers.to_json())

# convert the object into a dict
v2reports_infraspecific_modifers_dict = v2reports_infraspecific_modifers_instance.to_dict()
# create an instance of V2reportsInfraspecificModifers from a dict
v2reports_infraspecific_modifers_from_dict = V2reportsInfraspecificModifers.from_dict(v2reports_infraspecific_modifers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


