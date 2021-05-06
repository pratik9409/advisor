def add_cors(get_response):
    def addHeader(request):
        res = get_response(request)
        res.__setitem__('Access-Control-Allow_Origin', '*')
        return res
    return addHeader