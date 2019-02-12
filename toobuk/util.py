def replace(str, r) :
	for key in r.keys() :
		str = str.replace('#'+key+'#', r[key])

	return str;

def toBool(str) :
	return str.lower() is 'true'

typeSwitcher = {
	"int" : int,
	"float": float
}

def toConvert(str, dataType) :
	return str if dataType is None else typeSwitcher[dataType](str)
