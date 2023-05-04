

class HttpErrors:
    """class to define errorsr in http"""

    @staticmethod
    def error_422():
        """http 422"""
        return {"status_code":422,"body":{"error":"Unprocessable Entity"}}
    
    @staticmethod
    def error_400():
        """http 400"""
        return {"status_code":400,"body":{"error":"Bad Request"}}
    
    @staticmethod
    def error_409():
        """http 409"""
        return {"status_code":409,"body":{"error":"Conflict"}}