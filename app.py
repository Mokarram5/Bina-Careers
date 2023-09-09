from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title':'Data Analyst',
        'location':'Benguluru, India',
        'salary':'₹10,00,0000'
    },
    {
        'id': 2,
        'title':'Data Scientist',
        'location':'Delhi, India',
        'salary':'₹15,00,0000'
    },
    {
        'id': 3,
        'title':'Data Engineer',
        'location':'Kolkata, India',
        'salary':'₹9,00,0000'
    },
    {
        'id': 4,
        'title':'Frontend Engineer',
        'location':'Harayana, India',
        'salary':'₹6,00,0000'
    },
    {
        'id': 5,
        'title':'Backend-Engineer',
        'location':'Jaipur, India',
        'salary':'₹10,00,0000'
    }
    
]

@app.route('/')
def Welcome():
    return render_template('index.html', jobs=JOBS, company_name= 'Bina')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug= True)