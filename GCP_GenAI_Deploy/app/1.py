class UploadForm(FlaskForm):
    """A basic form to upload a file and take a text prompt."""
    pdf_file = FileField(
        validators=[FileRequired(),
FileAllowed(['pdf'], 'Please select a PDF.')],
        label="Select a PDF",
    )
    text_input = TextAreaField(label="Instructions", default="Summarize the PDF.")
    submit = SubmitField()