import sys  # sys module is used to access the exception information
import logging
import logger

# Now we want to give separate message for every error
def error_message_detail(error, error_detail:sys): # error_detail is the object of sys module
    _, _, exc_tb = error_detail.exc_info() #we  are not interested in first two thing. third thing i.e. exc_tb will give all info: which file error has occured, which line it has occured etc
    file_name = exc_tb.tb_frame.f_code.co_filename # file name where error has occured
    error_message = "Error occured in python script name [{0}] line number [{1}] error messge [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# so whenever an error has occured, we will call this function and it will give us the detailed error message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message 
    
# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Checking exception handling")
#         raise CustomException(e, sys) 