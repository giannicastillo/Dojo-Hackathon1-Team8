from refugeeresourceproject_app import app
from flask import render_template, redirect, request, session
from refugeeresourceproject_app.models.users import refugeeresourceproject

@app.route('/new_PLACEHOLDER')
def new_PLACEHOLDER():
    return render_template('/new_PLACEHOLDER.html')

@app.route('/create_PLACEHOLDER', methods=['POST'])
def create_PLACEHOLDER():
    if not projectClass.validate_refugeeresourceproject(request.form):
        return redirect('/?form_route?')
    data = {
        'xx': request.form['xx'],
        'xx': request.form['xx']
    }
    projectClass.save_PLACEHOLDER(data)
    return redirect('/show')

@app.route('/show_PLACEHOLDER/<int:id>')
def show_placeholder(id):
    data = {
        'id': id
    }
    return render_template("/details.html", projectData = projectClass.show(data))

@app.route('/edit_PLACEHOLDER/<int:id>')
def edit_PLACEHOLDER(id):
    data = {
        'id': id
    }
    return render_template("edit.html", projectData = projectClass.show(data))

@app.route('/update_PLACEHOLDER/<int:id>', methods=['POST']) 
def update_PLACEHOLDER(id):
    if not PLACEHOLDER.validate_PLACEHOLDER(request.form):
        return redirect(f'/edit_PLACEHOLDER/{id}')
    data = {
        'id': id,
        "xx":request.form['xx'],
    }
    projectClass.update(data)
    return redirect(f"/show/{id}")

@app.route('/delete_PLACEHOLDER/<int:id>') 
def delete_PLACEHOLDER(id):
    data = {
        'id': id,
    }
    projectClass.delete(data)
    return redirect('/show')

# Possible routes for multijoin element
@app.route('/PLACEHOLDER', methods=['POST'])
def make_PLACEHOLDER():
    data = {
        'placeholder_id': request.form['placeholder_id'],
        'user_id': request.form['user_id'],
        'PLACEHOLDER': request.form['PLACEHOLDER']
    }
    placeholder.new_PLACEHOLDER(data)
    return redirect(f"/show_placeholder/{request.form['placeholder_id']}")

@app.route('/PLACEHOLDER_update', methods=['POST'])
def PLACEHOLDER_update():
    data = {
        'PLACEHOLDER_id': request.form['PLACEHOLDER_id'],
        'user_id': request.form['user_id'],
        'placeholder_id': request.form['placeholder_id'],
        'PLACEHOLDER': request.form['PLACEHOLDER']
    }
    placeholder.PLACEHOLDER_update(data)
    return redirect(f"/show_placeholder/{request.form['placeholder_id']}")