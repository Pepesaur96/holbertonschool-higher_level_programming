#!/usr/bin/python3
class LockedClass:
    """This class prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name."""

    def __setattr__(self, name, value):
        """Overrides the default setattr() method to prevent dynamic creation
        of new instance attributes, except if the new instance attribute is
        called first_name.
        Args:
            name (str): The name of the attribute to set.
            value (any): The value to set the attribute to.
        Raises:
            AttributeError: If the attribute being set is not called first_name."""
        if name != "first_name" or not hasattr(self, "first_name"):
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name))
        self.__dict__[name] = value
