from rest_framework.exceptions import APIException
from rest_framework import status

class InvalidParameterError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid parameter value provided.'
    default_code = 'invalid_parameter'

class MovieNotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Movie not found.'
    default_code = 'movie_not_found'

class DataImportError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'Error importing movie data.'
    default_code = 'data_import_error' 