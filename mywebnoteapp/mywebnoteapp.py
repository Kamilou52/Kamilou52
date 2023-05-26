import sqlite3
from flask import Flask, session, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('static/notes.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_note(notes_id):
    conn = get_db_connection()
    note = conn.execute('SELECT * FROM notes WHERE id = ?',
                        (notes_id,)).fetchone()
    conn.close()
    if note is None:
        abort(404)
    return note

def add_notes(title , desc):
    conn = get_db_connection()
    
    data=[title, desc]
    
    note = conn.execute('insert into notes (title, content ,created ) values (?,?,datetime())', data)
    print (note)
    
    conn.commit()
    
    conn.close()
    if note is None:
        abort(404)
    return note

app = Flask("mywebnoteapp")
app.secret_key = "super secret key"

@app.route('/')
def home_page():
    conn = get_db_connection()
    notes = conn.execute('SELECT * FROM notes').fetchall()
    conn.close()
    return render_template('indexwebnoteapp.html', notes=notes)

@app.route("/username", methods=[ "GET", "POST" ])
def username():
   return render_template("username.html", user = request.args["user_name"])

@app.route("/add_Note",  methods=[ "GET", "POST" ])
def add_Note():
    if request.method=="POST":
        title = request.form["note"]
        desc = request.form["content"]
        add_notes(title,desc)
       
        return home_page()

    return render_template("add_Note.html")

@app.route('/create', methods=('GET', 'NOTE'))
def create():
    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'NOTE'))
def edit(id):
    note = get_note(id)
    if request.method == 'NOTE':
        note = request.form['note']
        content = request.form['content']

        if not note:
            flash('Note is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE notes SET note = ?, content = ?'
                         ' WHERE id = ?',
                         (note, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('indexwebnoteapp'))
    return render_template("edit.html",note=note)

@app.route("/note", methods=["GET", "POST"])
def notes():
    notes = add_Note.query.all()
    return render_template("note.html", notes=notes)

@app.route('/<int:id>/delete', methods=('GET', 'NOTE'))
def delete(id):
    note = get_note(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM notes WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(note['content']))
    return redirect(url_for("home_page"))
 
@app.route("/seenotes")
def seenotes():
    return render_template("seenotes.html")

@app.route("/search")
def search():
    return render_template("search.html")
    
@app.route("/modifynotes")
def modifynote():
    return render_template("modifynotes.html")

@app.route("/recherchedenotes")
def rechernote():
    return render_template("recherchedenotes.html")

@app.route("/create")
def createnote():
    return render_template("create.html")



if __name__ == "__main__":
    app.run(debug=True)
 
   




