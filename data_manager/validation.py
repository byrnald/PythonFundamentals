class ValidationError(ValueError): pass

def validate_error(record):
    if "username" not in record:
        raise ValidationError("username NOT in record.")

