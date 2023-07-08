from Exceptions.parameterNotFoundException import ParameterNotFoundException

class FilterCreator:
    def __init__(self,dictionaryKeys):
        self.dictionaryKeys = dictionaryKeys
        self.indexes = {
            'equal': self.clauseEqual,
            'like': self.clauseIn,
            'greater': self.clauseGreater,
            'smaller': self.clauseSmaller
        }

    def clauseEqual(self, key, value):
        return " AND "+key+" = '"+value+"'"

    def clauseIn(self, key, values):
        if all(val.isdigit() for val in values.split(',')):
            return ' AND ' + key + ' IN (' + values + ')'
        else:
            quoted_values = "'" + values.replace(",", "','") + "'"
            return ' AND ' + key + ' IN (' + quoted_values + ')'

    def clauseGreater(self, key, value):
        return ' AND '+key+' >= '+value

    def clauseSmaller(self, key, value):
        return ' AND '+key+' <= '+value

    def createFilter(self, filters):
        sqlFilter = '1 = 1 '
        for key in filters.keys():
            if key not in self.dictionaryKeys:
                raise ParameterNotFoundException(key)
            sqlFilter += self.indexes[self.dictionaryKeys[key]](key,filters[key])

        return sqlFilter
