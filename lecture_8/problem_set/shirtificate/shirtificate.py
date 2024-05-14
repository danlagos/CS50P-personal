from fpdf import FPDF

def main():
    """
    orchestrates flow of script
    call function to prompt user to input full name
    call function to create pdf, passing users name as argument
    """
    ...


def user_input():
    """
    accepts user input from cli
    returns user full name
    """
    ...


def set_up_pdf():
    """
    generates PDF
    instantiate FPDF object with
        portrait orientation and A4 format
    add page to the PDF
    return PDF
    """
    ...


def add_title():
    """
    accept PDF as argument
    accept image as arguemnt
    center image horixontally on the pdf
    position image appriately on the page
    return updated PDF with title
    """
    ...


def overlay_user_name():
    """
    accept updated PDF with title as argument
    accept user name as argument
    set font, size and color for user name
    calculate position to place name over shirt image.  Should be:
        centered horizontally
        placed vertically about 1/4 from the top of the shirt
    add users name to PDF
    return updated PDF with name and title
    """
    ...

def ouput_pdf():
    """
    accept updated PDF with name and title
    save PDF as `shirtificate.pdf`
    return `shirtificate.pdf`
    """
    ...


if __name__ == "__main__":
    main()