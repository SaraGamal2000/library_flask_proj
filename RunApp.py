from app import my_app

if __name__=='__main__':
    # my_app.run(port=5001)
    print('my_app is created')
    app = my_app('prd')
    app.run(debug=True, port=5001)