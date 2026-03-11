from objects import registered_objects


class ExpansionObject:
    """A simple placeable object for FEAT_OBJECTS in NML."""

    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.numeric_id = kwargs["numeric_id"]
        self.name_string = kwargs["name_string"]
        self.class_id = kwargs["class_id"]
        self.class_name_string = kwargs["class_name_string"]
        self.size = kwargs.get("size", [1, 1])
        self.build_cost_multiplier = kwargs.get("build_cost_multiplier", 16)
        self.remove_cost_multiplier = kwargs.get("remove_cost_multiplier", 4)
        self.introduction_date = kwargs.get("introduction_date", "date(1900, 1, 1)")
        self.views = kwargs.get("views", 1)
        self.height = kwargs.get("height", 4)

    def register(self):
        registered_objects.append(self)
