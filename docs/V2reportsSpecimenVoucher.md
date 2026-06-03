# V2reportsSpecimenVoucher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**biocollection_code** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_specimen_voucher import V2reportsSpecimenVoucher

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSpecimenVoucher from a JSON string
v2reports_specimen_voucher_instance = V2reportsSpecimenVoucher.from_json(json)
# print the JSON string representation of the object
print(V2reportsSpecimenVoucher.to_json())

# convert the object into a dict
v2reports_specimen_voucher_dict = v2reports_specimen_voucher_instance.to_dict()
# create an instance of V2reportsSpecimenVoucher from a dict
v2reports_specimen_voucher_from_dict = V2reportsSpecimenVoucher.from_dict(v2reports_specimen_voucher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


