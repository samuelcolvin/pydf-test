from flask import Flask, make_response


app = Flask(__name__)

@app.route('/')
def index():
    return '<div>go to <a href="/pdf">pdf</a> to view a PDF.</div>'

@app.route('/pdf')
def pdf():
    from pydf import generate_pdf
    html = '<h1>This is HTML</h1>'
    pdf_content = generate_pdf(html)
    response = make_response(pdf_content)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=test.pdf'
    return response

if __name__ == "__main__":
    app.run(debug=True)