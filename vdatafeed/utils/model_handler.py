"""
Lightweight native Python replacement for Pydantic.
Provides BaseModel, Field, AliasChoices, and model_validator decorator.
"""

class AliasChoices:
    """Class to specify multiple validation alias choices for a Field."""
    def __init__(self, *choices):
        self.choices = choices


class FieldDef:
    """Internal class representing a field configuration definition."""
    def __init__(self, validation_alias=None, default=None):
        self.default = default
        if isinstance(validation_alias, AliasChoices):
            self.aliases = list(validation_alias.choices)
        elif isinstance(validation_alias, str):
            self.aliases = [validation_alias]
        else:
            self.aliases = []


def Field(validation_alias=None, default=None):
    """Factory function to define fields with validation aliases and defaults."""
    return FieldDef(validation_alias=validation_alias, default=default)


def model_validator(mode='before'):
    """Decorator to define class-level data pre-validators."""
    def decorator(func):
        func._is_model_validator = True
        func._validator_mode = mode
        return classmethod(func)
    return decorator


class BaseModel:
    """
    Base model class providing field parsing, aliasing,
    validation hooks, and dictionary dumping.
    """
    def __init__(self, **kwargs):
        # 1. Run all model validators (mode='before')
        validators = []
        for name in dir(self.__class__):
            attr = getattr(self.__class__, name)
            func = getattr(attr, "__func__", attr)
            if getattr(func, "_is_model_validator", False) and getattr(func, "_validator_mode", None) == 'before':
                validators.append(attr)

        for validator in validators:
            kwargs = validator(kwargs)

        # 2. Map fields based on class annotations
        annotations = getattr(self.__class__, "__annotations__", {})
        for key in annotations:
            class_val = getattr(self.__class__, key, None)

            aliases = []
            default = None
            if isinstance(class_val, FieldDef):
                aliases = class_val.aliases
                default = class_val.default
            else:
                default = class_val

            # Resolve value from kwargs using either standard key or alias list
            val = None
            found = False
            if key in kwargs:
                val = kwargs[key]
                found = True
            else:
                for alias in aliases:
                    if alias in kwargs:
                        val = kwargs[alias]
                        found = True
                        break

            if not found:
                val = default

            # Perform dynamic type coercion based on field annotations
            if found and val is not None:
                field_type = annotations[key]
                origin = getattr(field_type, "__origin__", None)
                if origin is not None:
                    args = getattr(field_type, "__args__", ())
                    non_none_types = [t for t in args if t is not type(None)]
                    if non_none_types:
                        field_type = non_none_types[0]

                origin = getattr(field_type, "__origin__", None)
                args = getattr(field_type, "__args__", ())

                if isinstance(field_type, type) and issubclass(field_type, BaseModel):
                    if isinstance(val, dict):
                        val = field_type(**val)
                elif origin is list and args:
                    sub_type = args[0]
                    if isinstance(sub_type, type) and issubclass(sub_type, BaseModel):
                        if isinstance(val, list):
                            val = [sub_type(**item) if isinstance(item, dict) else item for item in val]
                elif field_type in (float, int, str):
                    try:
                        if isinstance(val, str):
                            val_cleaned = val.strip().replace(",", "")
                            if val_cleaned in ("", "None", "null"):
                                val = default
                            else:
                                if field_type is float:
                                    f_val = float(val_cleaned)
                                    val = int(f_val) if f_val.is_integer() else f_val
                                elif field_type is int:
                                    val = int(float(val_cleaned))
                                elif field_type is str:
                                    val = val.strip()
                                    if key in ("trading_date", "last_trading_date", "from_date", "to_date") or key.endswith("_date"):
                                        if "/" in val:
                                            parts = val.split("/")
                                            if len(parts) == 3 and len(parts[2]) == 4:
                                                val = f"{parts[2]}-{parts[1]}-{parts[0]}"
                        else:
                            if field_type is float:
                                f_val = float(val)
                                val = int(f_val) if f_val.is_integer() else f_val
                            elif field_type is int:
                                val = int(float(val))
                            elif field_type is str:
                                val = str(val).strip()
                                if key in ("trading_date", "last_trading_date", "from_date", "to_date") or key.endswith("_date"):
                                    if "/" in val:
                                        parts = val.split("/")
                                        if len(parts) == 3 and len(parts[2]) == 4:
                                            val = f"{parts[2]}-{parts[1]}-{parts[0]}"
                    except (ValueError, TypeError):
                        pass

            setattr(self, key, val)

    def model_dump(self) -> dict:
        """Dump the model fields recursively to a standard dictionary."""
        annotations = getattr(self.__class__, "__annotations__", {})
        res = {}
        for key in annotations:
            val = getattr(self, key, None)
            if isinstance(val, BaseModel):
                res[key] = val.model_dump()
            elif isinstance(val, list):
                res[key] = [item.model_dump() if isinstance(item, BaseModel) else item for item in val]
            else:
                res[key] = val
        return res

    def __repr__(self) -> str:
        attrs = ", ".join(f"{k}={getattr(self, k)!r}" for k in getattr(self.__class__, "__annotations__", {}))
        return f"{self.__class__.__name__}({attrs})"
