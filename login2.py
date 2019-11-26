# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Compare Passwords
        if username == 'admin' and password == '19319':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            error = "Unauthorized access denied..."
            return render_template('login.html')
    return render_template('login.html')


### Logout Route ###
@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.secret_key='mysecretkey'
    app.run(debug=True)
