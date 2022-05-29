from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/api/branch')
def fun():
    q=request.form.get('q')
    limit=request.form.get('limit')
    offset=request.form.get('offset')
    x=col.find({'branch':q})
    for i in x:
        print(i)
    return 'success'
    if __name__=='__main__':
        app.run(debug=True)