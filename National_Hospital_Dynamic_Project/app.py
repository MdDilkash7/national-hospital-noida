from flask import Flask, render_template, request, redirect

app = Flask(__name__)

patients=[{"id":101,"name":"Aman Kumar","age":22,"disease":"Fever","status":"Admitted"}]
appointments=[]
doctors=["Dr. Sharma","Dr. Khan"]
slots=["09:00 AM","09:30 AM","10:00 AM","10:30 AM"]

@app.route('/')
def dashboard():
    return render_template('index.html',
        patients=patients,
        doctors=doctors,
        slots=slots,
        total_patients=len(patients),
        total_doctors=len(doctors),
        total_appointments=len(appointments))

@app.route('/book', methods=['POST'])
def book():
    appointments.append(dict(request.form))
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
