
class MyDict:
    """
    This data structure implements basic dict methods -
    adding a value by key, finding a value by key, .keys(), .values(), .items().
    Deleting from dict is not implemented.

    Unlike python dict, it doesn't perform size change when the dict gets full.
    Also, it doesn't keep insertion order.
    """
    def __init__(self, array_size=8):
        self.__array_size = array_size
        self.__array = [None] * array_size

    def __hash__(self, key):
        char_sum = sum(ord(i) for i in str(key))
        return char_sum % self.__array_size

    def __eq__(self, other):
        """
        When A.__eq__(B) returns NotImplemented constraint, python tries B.__eq__(A)
        """
        if isinstance(other, self.__class__):
            return self.items() == other.items()
        else:
            return NotImplemented

    def __ne__(self, other):
        """
        When A.__ne__(B) returns NotImplemented constraint, python tries B.__ne__(A)
        """
        if isinstance(other, self.__class__):
            return self.items() != other.items()
        else:
            return NotImplemented

    def __getitem__(self, key):
        """
        This method returns value for a given key, even if there was a collision.
        If there is nothing for a given key, KeyError is raised.
        """
        key_hash = self.__hash__(key)
        list_item = self.__array[key_hash]

        if not list_item:
            raise KeyError

        collision = len(list_item) != 1

        if collision:
            for i_key, i_value in list_item:
                if i_key == key:
                    return i_value
            raise KeyError
        else:
            i_key, i_value = list_item[0]
            if i_key == key:
                return i_value
            else:
                raise KeyError

    def __setitem__(self, new_key, new_value):
        """
        This method adds a new item, updates value by key, and handles collisions.
        """
        key_hash = self.__hash__(new_key)

        if not self.__array[key_hash]:
            # Add a new key-value pair
            self.__array[key_hash] = [(new_key, new_value)]
            return True
        else:
            # Update value by key
            for i, pair in enumerate(self.__array[key_hash]):
                key, value = pair
                if key == new_key:
                    self.__array[key_hash][i] = (new_key, new_value)
                    return True

            # Collision
            self.__array[key_hash].append((new_key, new_value))
            return True

    def __repr__(self):
        all_items = self.__get_data(data_ident='repr')
        str_item = '{' + ', '.join(all_items) + '}'
        return str_item

    def __get_data(self, data_ident='keys'):
        data = []
        for list_item in self.__array:
            if not list_item:
                # we initialized __array as [None] * array_size
                continue

            for pair in list_item:
                key, value = pair

                if data_ident == 'keys':
                    data.append(key)
                elif data_ident == 'values':
                    data.append(value)
                elif data_ident == 'items':
                    data.append(pair)
                elif data_ident == 'repr':
                    data.append('%s: %s' % pair)
        return data

    def values(self):
        return self.__get_data(data_ident='values')

    def keys(self):
        return self.__get_data(data_ident='keys')

    def items(self):
        return self.__get_data(data_ident='items')
