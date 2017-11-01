

class MyDict:
    def __init__(self, array_size):
        self.__array_size = array_size
        self.__array = [None] * array_size

    # the object is hashable if it has __hash__ and __eq__
    def __hash__(self, key):
        char_sum = sum(ord(i) for i in str(key))
        return char_sum % self.__array_size

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.items() == other.items()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, key):
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
        key_hash = self.__hash__(new_key)

        if not self.__array[key_hash]:
            self.__array[key_hash] = [(new_key, new_value)]
            return True
        else:
            # in case we need to change the value
            for i, pair in enumerate(self.__array[key_hash]):
                key, value = pair
                if key == new_key:
                    self.__array[key_hash][i] = (new_key, new_value)
                    return True

            # in case of collision
            self.__array[key_hash].append((new_key, new_value))
            return True

    def __repr__(self):
        all_items = self.__get_data(data_ident='repr')
        str_item = '{' + ', '.join(all_items) + '}'
        return str_item

    def __get_data(self, data_ident='keys'):
        data = []
        for list_item in self.__array:
            if list_item:
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


a = MyDict(111)
print()
a[3] = 0
a[4] = 2
a[1] = 7
print(a)

a[1] = 77

print(a.items())
print(a.values())
print(a.keys())

