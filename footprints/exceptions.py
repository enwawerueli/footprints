class AuthenticationError(Exception):
    """Exception class for authentication related errors"""


class ValidationError(Exception):
    """Exception class for invalid field inputs"""


class TransactionCodeError(Exception):
    """Execption class for transaction code errors"""


class PrinterError(Exception):
    """Execption class for printing failures"""
