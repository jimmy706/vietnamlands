
class FilteringData:
    def __init__(self, data):
        self.data = data

    def filtering_by_subdivision(self, subdivision_level: int, data):
        if subdivision_level < 0 or subdivision_level > 2:
            raise ValueError("subdivision_level must be 0, 1 or 2")
        if subdivision_level == 0:
            for item in data:
                item.pop('subdivisions', None)
        if subdivision_level == 1:
            for item in data:
                if 'subdivisions' in item:
                    item['subdivisions'] = item['subdivisions']
                for subdivision in item.get('subdivisions', []):
                    subdivision.pop('subdivisions', None)
        return data

    def filtering_by_license_plates(self, licensePlates: list[int], data):
        """
        Filter the data by license plates.
        :param licensePlates: List of license plates to filter by.
        :param data: Data to filter.
        :return: Filtered data.
        """
        if not isinstance(licensePlates, list):
            raise TypeError("licensePlates must be a list")
        if len(licensePlates) == 0:
            return data

        filtered_data = []
        for item in data:
            if any(item in licensePlates for item in item['licensePlates']):
                filtered_data.append(item)
        return filtered_data

    def filtering_by_name(self, name: str, data):
        """
        Filter the data by name regex and non case sensitive.
        :param name: Name to filter by.
        :param data: Data to filter.
        :return: Filtered data.
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if name:
            return [item for item in data if name.lower() in item.get('name', '').lower()]
        return data

    def filtering_data(self, name='', licensePlates=[], subdivision_level=0):
        self.data = self.filtering_by_name(name, self.data)
        self.data = self.filtering_by_license_plates(licensePlates, self.data)
        return self.filtering_by_subdivision(subdivision_level, self.data)
