from fpdf import FPDF

def main():
    """
    Orchestrates the flow of the script:
    - Calls function to prompt user to input full name.
    - Calls functions to create and modify the PDF, passing the user's name as an argument.
    """
    name = user_input()
    pdf = set_up_pdf()
    pdf = add_title(pdf)
    pdf = add_shirt_image(pdf)
    pdf = overlay_user_name(pdf, name)
    output_pdf(pdf)


def user_input():
    """
    Accepts user input from CLI.

    :return: User's full name as a string.
    :rtype: str
    """
    name = input("Name: ")
    return name


def set_up_pdf():
    """
    Generates a PDF with portrait orientation and A4 format.

    :return: Initialized PDF object.
    :rtype: FPDF
    """
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    return pdf


def add_title(pdf):
    """
    Adds a centered title to the PDF.

    :param pdf: PDF object.
    :type pdf: FPDF
    :return: Updated PDF object with title added.
    :rtype: FPDF
    """
    pdf.set_font("Helvetica", "B", 24)  # Updated to use 'Helvetica'
    pdf.cell(0, 10, "CS50 Shirtificate", align='C', new_x="LMARGIN", new_y="NEXT")  # Updated parameters
    return pdf


def add_shirt_image(pdf):
    """
    Adds the shirt image to the PDF, centered horizontally.

    :param pdf: PDF object.
    :type pdf: FPDF
    :return: Updated PDF object with shirt image added.
    :rtype: FPDF
    """
    # Assuming shirt image is 150mm wide and 150mm tall for positioning
    pdf.image("shirtificate.png", x=30, y=80, w=150)
    return pdf


def overlay_user_name(pdf, name):
    """
    Overlays the user's name on the shirt image.

    :param pdf: PDF object.
    :type pdf: FPDF
    :param name: User's full name.
    :type name: str
    :return: Updated PDF object with user's name added.
    :rtype: FPDF
    """
    pdf.set_font("Helvetica", "B", 32)  # Updated to use 'Helvetica'
    pdf.set_text_color(255, 255, 255)
    
    # Calculate the width of the name to center it horizontally
    name_width = pdf.get_string_width(name)
    page_width = 210  # A4 width in mm
    x_position = (page_width - name_width) / 2

    # Place the name at the calculated x position
    pdf.text(x=x_position, y=120, text=name)  # Updated parameter
    return pdf


def output_pdf(pdf):
    """
    Saves the PDF as 'shirtificate.pdf'.

    :param pdf: Updated PDF object.
    :type pdf: FPDF
    :return: Path to saved PDF file.
    :rtype: str
    """
    pdf.output("shirtificate.pdf")
    return "shirtificate.pdf"


if __name__ == "__main__":
    main()
