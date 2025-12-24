# utils/helpers.py

def get_all_model_data(model):
    """Get all objects with all fields"""
    fields = [field.name for field in model._meta.fields]
    result = model.objects.values(*fields)
    return list(result)


# 1. Get single item by ID
def get_single_item(model, id):
    """Get single object by ID"""
    fields = [field.name for field in model._meta.fields]
    try:
        result = model.objects.values(*fields).get(id=id)
        return result
    except model.DoesNotExist:
        return None


# 2. Get specific fields only
def get_specific_fields(model, field_list):
    """Get all objects with specific fields only"""
    # Validate fields first
    valid_fields = get_valid_fields(model, field_list)
    
    if not valid_fields:
        return []
    
    result = model.objects.values(*valid_fields)
    return list(result)


# 3. Validate fields (handle invalid field names)
def get_valid_fields(model, field_list):
    """Filter out invalid field names"""
    model_fields = [field.name for field in model._meta.fields]
    valid_fields = []
    invalid_fields = []
    
    for field in field_list:
        if field in model_fields:
            valid_fields.append(field)
        else:
            invalid_fields.append(field)
    
    # Optional: Log invalid fields
    if invalid_fields:
        print(f"Warning: Invalid fields ignored: {invalid_fields}")
    
    return valid_fields


# Combined: Single item with specific fields
def get_single_item_with_fields(model, id, field_list=None):
    """Get single object with optional specific fields"""
    try:
        if field_list:
            valid_fields = get_valid_fields(model, field_list)
            if not valid_fields:
                return {"error": "No valid fields provided"}
            result = model.objects.values(*valid_fields).get(id=id)
        else:
            fields = [field.name for field in model._meta.fields]
            result = model.objects.values(*fields).get(id=id)
        return result
    except model.DoesNotExist:
        return None


# Combined: All items with specific fields
def get_all_items_with_fields(model, field_list=None):
    """Get all objects with optional specific fields"""
    if field_list:
        valid_fields = get_valid_fields(model, field_list)
        if not valid_fields:
            return []
        result = model.objects.values(*valid_fields)
    else:
        fields = [field.name for field in model._meta.fields]
        result = model.objects.values(*fields)
    return list(result)




#  Get single item by ID
def debug_item(model):
    """Get single object by ID"""
    fields = [field.name for field in model._meta.fields]
    try:
        result = model.objects.values(*fields).all()
        return result
    except model.DoesNotExist:
        return None