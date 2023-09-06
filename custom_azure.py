from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'gilscore' # Must be replaced by your <storage_account_name>
    account_key = 'Ew7rzj3z87Rz7hhKTSkFmNqjPF0sLUsVGFvwag5xBQcGFDkp7uazP4UmaBNCoaGdxKkZCm0YMQaG+AStT2o91w==' 
    azure_container = 'media'
    expiration_secs = None

# class AzureStaticStorage(AzureStorage):
#     account_name = 'djangoaccountstorage' # Must be replaced by your storage_account_name
#     account_key = 'your_key_here' # Must be replaced by your <storage_account_key>
#     azure_container = 'static'
#     expiration_secs = None