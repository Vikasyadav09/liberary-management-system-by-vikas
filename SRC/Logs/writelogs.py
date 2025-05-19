from Authentication.signin import signin_menu
from logs.logger import setup_logger

logger = setup_logger()

def main():
    logger.info("Application started")
    print("=== Welcome to the Restaurant Management System ===")
    
    signin_menu()

    # After login/signup, you can continue to other operations like booking, ordering, billing
    # e.g.:
    # from Domain.booking import book_table
    # book_table(user)


main()