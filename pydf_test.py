from flask import Flask, make_response, Response
import traceback

app = Flask(__name__)


@app.route('/')
def index():
    return '<div>go to <a href="/pdf">pdf</a> to view a PDF.</div>'


@app.route('/pdf')
def pdf():
    try:
        from pydf import generate_pdf
        html = '<h1>This is HTML</h1>'
        pdf_content = generate_pdf(html)
        response = make_response(pdf_content)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=test.pdf'
    except Exception:
        exc = traceback.format_exc()
        response = Response(exc, content_type='text/plain')
    return response

if __name__ == "__main__":
    app.run(debug=True)
