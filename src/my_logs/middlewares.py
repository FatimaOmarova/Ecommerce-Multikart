from loguru import logger

class DjangoLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        logger.info(f"Request URL: {request.build_absolute_uri()}")
        logger.info(f"Request METHOD: {request.method}")
        logger.info(f"Request HEADERS: {request.headers}")
        logger.info(f"Request GET data: {request.GET}")
        logger.info(f"Request POST data: {request.POST}")
        logger.info(f"Request FILES data: {request.FILES}")
        response = self.get_response(request)
        logger.info(f"Request USER: {request.user}")
        logger.info(f"Response STATUS_CODE: {response.status_code}")
        response = self.get_response(request)
        logger.info(f"Request USER: {request.user}")
        logger.info(f"Response STATUS_CODE: {response.status_code}")
    
        return response