import inspect
from typing import Any, Callable, Dict, List, Tuple

TYPE_MAP = {
    str: "string",
    int: "integer",
    float: "number",
    bool: "boolean",
    list: "array",
    dict: "object",
    type(None): "null",
}


def _build_parameter_schema(func: Callable[..., Any]) -> Tuple[Dict, List[str]]:
    try:
        signature = inspect.signature(func)
    except ValueError as exc:
        raise ValueError(
            f"Failed to get signature for function {func.__name__}: {exc}"
        ) from exc

    parameters = {}
    for param in signature.parameters.values():
        param_type = TYPE_MAP.get(param.annotation, "string")
        parameters[param.name] = {"type": param_type}

    required = [
        param.name
        for param in signature.parameters.values()
        if param.default == inspect.Parameter.empty
    ]
    return parameters, required


def function_to_schema(func: Callable[..., Any]) -> dict:
    """Convert a Python function into an OpenAI tool schema."""
    parameters, required = _build_parameter_schema(func)
    return {
        "type": "function",
        "function": {
            "name": func.__name__,
            "description": (func.__doc__ or "").strip(),
            "parameters": {
                "type": "object",
                "properties": parameters,
                "required": required,
            },
        },
    }


def function_to_schema_claude(func: Callable[..., Any]) -> dict:
    """Convert a Python function into a Claude tool schema."""
    parameters, required = _build_parameter_schema(func)
    return {
        "name": func.__name__,
        "description": (func.__doc__ or "").strip(),
        "input_schema": {
            "type": "object",
            "properties": parameters,
            "required": required,
        },
    }
